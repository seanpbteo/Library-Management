import traceback
import tkinter as tk
from tkinter import ttk
from booksfunctions import *
from frames import *

class BookAcquisitionFrame(GUIFrame):
    def __init__(self, container, controller):
        super().__init__(container, controller)

        options = {'padx': 5, 'pady': 5}

        # Title of Frame
        # self.header_label = ttk.Label(self, text="Book Borrowing")
        # self.header_label.grid(column=0, row=0, sticky="n", columnspan=2, **options)

        # AccessionID label
        self.accessionid_label = ttk.Label(self, text="Accession Number:")
        self.accessionid_label.grid(column=0, row=0, sticky="w", **options)

        # AccessionID field
        self.accessionid = tk.StringVar()
        self.accessionid_field = ttk.Entry(self, textvariable=self.accessionid)
        self.accessionid_field.grid(column=1, row=0, sticky="w", **options)
        self.accessionid_field.focus()

        # Title label
        self.title_label = ttk.Label(self, text="Title:")
        self.title_label.grid(column=0, row=1, sticky="w", **options)

        # Title field
        self.title = tk.StringVar()
        self.title_field = ttk.Entry(self, textvariable=self.title)
        self.title_field.grid(column=1, row=1, sticky="w", **options)

        # Authors label
        self.authors_label = ttk.Label(self, text="Authors:")
        self.authors_label.grid(column=0, row=2, sticky="w", **options)

        # Authors field
        self.authors_field = tk.Text(self, height=5, width=30)
        self.authors_field.grid(column=1, row=2, sticky="w", **options)

        # ISBN label
        self.isbn_label = ttk.Label(self, text="ISBN:")
        self.isbn_label.grid(column=0, row=3, sticky="w", **options)

        # ISBN field
        self.isbn = tk.StringVar()
        self.isbn_field = ttk.Entry(self, textvariable=self.isbn)
        self.isbn_field.grid(column=1, row=3, sticky="w", **options)

        # Publisher label
        self.publisher_label = ttk.Label(self, text="Publisher:")
        self.publisher_label.grid(column=0, row=4, sticky="w", **options)

        # Publisher field
        self.publisher = tk.StringVar()
        self.publisher_field = ttk.Entry(self, textvariable=self.publisher)
        self.publisher_field.grid(column=1, row=4, sticky="w", **options)

        # Year label
        self.year_label = ttk.Label(self, text="Year:")
        self.year_label.grid(column=0, row=5, sticky="w", **options)

        # Year field
        self.year = tk.StringVar()
        self.year_field = ttk.Entry(self, textvariable=self.year)
        self.year_field.grid(column=1, row=5, sticky="w", **options)

        # Cancel Button
        self.cancel_button = ttk.Button(self, text="Cancel")
        self.cancel_button["command"] = self.cancel_acquisition
        self.cancel_button.grid(column=0, row=6, sticky="sw", **options)

        # Submit Button
        self.submit_button = ttk.Button(self, text="Submit")
        self.submit_button["command"] = self.submit_acquisition
        self.submit_button.grid(column=1, row=6, sticky="se", **options)

        # layout method
        self.grid(column=0, row=0, sticky="nsew", **options)

    def get_authors(self):
        return self.authors_field.get(1.0, "end-1c").splitlines()

    def reset_frame(self):
        self.accessionid_field.delete(0, "end")
        self.title_field.delete(0, "end")
        self.authors_field.delete(1.0, "end")
        self.isbn_field.delete(0, "end")
        self.publisher_field.delete(0, "end")
        self.year_field.delete(0, "end")

    def cancel_acquisition(self):
        self.reset_frame()
        self.controller.show_main()

    def submit_acquisition(self):
        try:
            book_acquisition(
                self.accessionid.get(),
                self.title.get(),
                self.get_authors(),
                self.isbn.get(),
                self.publisher.get(),
                self.year.get()
        )
            self.controller.operation_success("Book Acquisition")
        except Exception as e:
            self.reset_frame()
            self.controller.raise_error(e)

class BookWithdrawalFrame(GUIFrame):
    def __init__(self, container, controller):
        super().__init__(container, controller)

        options = {'padx': 5, 'pady': 5}

        # AcceessionID label
        self.accessionid_label = ttk.Label(self, text="Accession Number:")
        self.accessionid_label.grid(column=0, row=0, sticky="w", **options)

        # AccessionID field
        self.accessionid = tk.StringVar()
        self.accessionid_field = ttk.Entry(self, textvariable=self.accessionid)
        self.accessionid_field.grid(column=1, row=0, sticky="w", **options)
        self.accessionid_field.focus()

        # Cancel Button
        self.cancel_button = ttk.Button(self, text="Cancel")
        self.cancel_button["command"] = self.cancel_withdrawal
        self.cancel_button.grid(column=0, row=6, sticky="sw", **options)

        # Submit Button
        self.submit_button = ttk.Button(self, text="Submit")
        self.submit_button["command"] = self.confirm_withdrawal
        self.submit_button.grid(column=1, row=6, sticky="sw", **options)

        # Layout method
        self.grid(column=0, row=0, sticky="nsew", **options)

    def reset_frame(self):
        self.accessionid_field.delete(0, "end")

    def cancel_withdrawal(self):
        self.reset_frame()
        self.controller.show_main()

    def confirm_withdrawal(self):
        try:
            self.controller.raise_confirmation(
                f"SELECT Books.AccessionID, Books.Title, Books.ISBN, Books.Publisher, Books.PublishYear, \
                GROUP_CONCAT(Authors.Name) AS Authors \
                FROM AuthorBook LEFT JOIN Books ON AuthorBook.AccessionID=Books.AccessionID \
                LEFT JOIN Authors ON AuthorBook.AuthorID=Authors.AuthorID \
                WHERE AuthorBook.AccessionID='{self.accessionid.get()}' \
                GROUP BY AuthorBook.AccessionID",
                self.submit_withdrawal
            )
        except Exception as e:
            self.reset_frame()
            self.controller.raise_error(e)

    def submit_withdrawal(self):
        try:
            book_withdrawal(
                self.accessionid.get()
            )
            self.controller.operation_success("Book Withdrawal")
        except Exception as e:
            self.reset_frame()
            self.controller.raise_error(e)

class BookSearchFrame(GUIFrame):
    def __init__(self, container, controller):
        super().__init__(container, controller)

        options = {'padx': 5, 'pady': 5}

        # Title label
        self.title_label = ttk.Label(self, text="Title:")
        self.title_label.grid(column=0, row=1, sticky="w", **options)

        # Title field
        self.title = tk.StringVar()
        self.title_field = ttk.Entry(self, textvariable=self.title)
        self.title_field.grid(column=1, row=1, sticky="w", **options)

        # Authors label
        self.authors_label = ttk.Label(self, text="Authors:")
        self.authors_label.grid(column=0, row=2, sticky="w", **options)

        # Authors field
        self.authors = tk.StringVar()
        self.authors_field = ttk.Entry(self, textvariable=self.authors)
        self.authors_field.grid(column=1, row=2, sticky="w", **options)

        # ISBN label
        self.isbn_label = ttk.Label(self, text="ISBN:")
        self.isbn_label.grid(column=0, row=3, sticky="w", **options)

        # ISBN field
        self.isbn = tk.StringVar()
        self.isbn_field = ttk.Entry(self, textvariable=self.isbn)
        self.isbn_field.grid(column=1, row=3, sticky="w", **options)

        # Publisher label
        self.publisher_label = ttk.Label(self, text="Publisher:")
        self.publisher_label.grid(column=0, row=4, sticky="w", **options)

        # Publisher field
        self.publisher = tk.StringVar()
        self.publisher_field = ttk.Entry(self, textvariable=self.publisher)
        self.publisher_field.grid(column=1, row=4, sticky="w", **options)

        # Year label
        self.year_label = ttk.Label(self, text="Year:")
        self.year_label.grid(column=0, row=5, sticky="w", **options)

        # Year field
        self.year = tk.StringVar()
        self.year_field = ttk.Entry(self, textvariable=self.year)
        self.year_field.grid(column=1, row=5, sticky="w", **options)

        # Cancel Button
        self.cancel_button = ttk.Button(self, text="Cancel")
        self.cancel_button["command"] = self.cancel_search
        self.cancel_button.grid(column=0, row=6, sticky="sw", **options)

        # Submit Button
        self.submit_button = ttk.Button(self, text="Submit")
        self.submit_button["command"] = self.submit_search
        self.submit_button.grid(column=1, row=6, sticky="se", **options)

        # layout method
        self.grid(column=0, row=0, sticky="nsew", **options)

    def reset_frame(self):
        self.title_field.delete(0, "end")
        self.authors_field.delete(0, "end")
        self.isbn_field.delete(0, "end")
        self.publisher_field.delete(0, "end")
        self.year_field.delete(0, "end")

    def cancel_search(self):
        self.reset_frame()
        self.controller.show_main()

    def submit_search(self):

        """
        1. Call booksearch()
        2. Open new window with ttk.Treeview
        3. Populate results from booksearch() inside ttk.Treeview
        """

        try:
            search_res = book_search(
                self.title.get(),
                self.isbn.get(),
                self.publisher.get(),
                self.year.get(),
                self.authors.get()
            )

            print(search_res)

            # Manipulate search result dictionary
            table_headings = list(search_res[0].keys())

            table_rows = []
            for row_dict in search_res:
                row = []

                for _, value in row_dict.items():
                   row.append(value)

                table_rows.append(tuple(row))

            print("\n")
            print(table_headings)
            print(table_rows)
            print("\n")

            # Search results window
            new_window = tk.Toplevel()
            new_window.rowconfigure(1, weight=1)
            new_window.columnconfigure(0, weight=1)

            # Elements
            search_result_label = ttk.Label(new_window, text="Search Results")
            search_result_frame = tk.Frame(new_window)

            search_result_table = ttk.Treeview(search_result_frame)
            search_result_scrollbar = tk.Scrollbar(search_result_frame, orient="vertical")

            # Layout methods
            search_result_label.grid(row=0, column=0)
            search_result_frame.grid(row=1, column=0, sticky="nsew")

            search_result_scrollbar.pack(side="right", fill="y")
            search_result_table.pack(fill="both")

            # Setup scrollbar
            search_result_table["yscrollcommand"] = search_result_scrollbar.set
            search_result_scrollbar["command"] = search_result_table.yview

            # Setup table
            search_result_table["columns"] = table_headings
            search_result_table["show"] = "headings"

            for i in range(len(table_headings)):
                search_result_table.column(table_headings[i], anchor="center", stretch=True)
                search_result_table.heading(table_headings[i], text=table_headings[i])

            for i in range(len(table_rows)):
                search_result_table.insert("", "end", values=table_rows[i])

        except Exception as e:
            self.reset_frame()
            self.controller.raise_error(e)
            traceback.print_exc()


class BooksMainFrame(GUIFrame):
    def __init__(self, container, controller):
        super().__init__(container, controller)

        options = {'padx': 5, 'pady': 5}

        # Book acquisition button
        self.book_acquisition_button = ttk.Button(self, text="Book Acquisition")
        self.book_acquisition_button["command"] = self.open_book_acquisition_frame
        self.book_acquisition_button.pack(**options)

        # Book withdrawal button
        self.book_withdrawal_button = ttk.Button(self, text="Book Withdrawal")
        self.book_withdrawal_button["command"] = self.open_book_withdrawal_frame
        self.book_withdrawal_button.pack(**options)

        # Book search button
        self.book_search_button = ttk.Button(self, text="Book Search")
        self.book_search_button["command"] = self.open_book_search_frame
        self.book_search_button.pack(**options)

        # Layout method
        self.grid(column=0, row=0, sticky="nsew", **options)

    def open_book_acquisition_frame(self):
        self.controller.show_frame(BookAcquisitionFrame)

    def open_book_withdrawal_frame(self):
        self.controller.show_frame(BookWithdrawalFrame)

    def open_book_search_frame(self):
        self.controller.show_frame(BookSearchFrame)

class BooksControllerFrame(ControllerFrame):
    def __init__(self, container):
        super().__init__(
            container,
            [
                BookAcquisitionFrame,
                BookWithdrawalFrame,
                BookSearchFrame,
                BooksMainFrame
            ],
            BooksMainFrame
        )

if __name__ == "__main__":
    app = App()
    BooksControllerFrame(app)
    app.mainloop()
