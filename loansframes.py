from datetime import date
import tkinter as tk
from tkinter import ttk
from loansfunctions import *
from frames import *

class BookBorrowFrame(GUIFrame):
    def __init__(self, container, controller):
        super().__init__(container, controller)
        
        options = {"padx": 5, "pady": 5}

        # Title of Frame
        self.header_label = ttk.Label(self, text="Book Borrowing")
        self.header_label.grid(column=0, row=0, sticky="n", columnspan=2, **options)

        # AccessionID label
        self.accessionid_label = ttk.Label(self, text="Accession Number:")
        self.accessionid_label.grid(column=0, row=1, sticky="w", **options)

        # AccessionID field
        self.accessionid = tk.StringVar()
        self.accessionid_field = ttk.Entry(self, textvariable=self.accessionid)
        self.accessionid_field.grid(column=1, row=1, sticky="w", **options)
        self.accessionid_field.focus()

        # MemberID label
        self.memberid_label = ttk.Label(self, text="Member ID:")
        self.memberid_label.grid(column=0, row=2, sticky="w", **options)

        # MemberID field
        self.memberid = tk.StringVar()
        self.memberid_field = ttk.Entry(self, textvariable=self.memberid)
        self.memberid_field.grid(column=1, row=2, sticky="w", **options)

        # Cancel button
        self.cancel_button = ttk.Button(self, text="Cancel")
        self.cancel_button["command"] = self.cancel_borrow
        self.cancel_button.grid(column=0, row=4, sticky="w", **options)

        # Submit button
        self.submit_button = ttk.Button(self, text="Submit")
        self.submit_button["command"] = self.confirm_borrow
        self.submit_button.grid(column=1, row=4, sticky="e", **options)

        # Layout method
        self.grid(column=0, row=0, sticky="nsew", **options)

    def reset_frame(self):
        self.accessionid_field.delete(0, "end")
        self.memberid_field.delete(0, "end")

    def cancel_borrow(self):
        self.reset_frame()
        self.controller.show_main()

    def confirm_borrow(self):
        try:
            self.controller.raise_confirmation(
                f"SELECT Books.AccessionID, Books.Title,\
                Members.MemberID, Members.Name,\
                CURDATE() AS BorrowDate,\
                DATE_ADD(CURDATE(), INTERVAL 14 DAY) AS DueDate \
                FROM Books, Members \
                WHERE Members.MemberID=\"{self.memberid.get()}\" AND Books.AccessionID=\"{self.accessionid.get()}\"",
                self.submit_borrow
            )
        except Exception as e:
            self.reset_frame()
            self.controller.raise_error(e)

    def submit_borrow(self):
        try:
            book_borrowing(
                self.accessionid.get(),
                self.memberid.get(),
                date.today()
            )
            self.controller.operation_success("Book Borrowing")
        except Exception as e:
            self.reset_frame()
            self.controller.raise_error(e)

class BookReturnFrame(GUIFrame):
    def __init__(self, container, controller):
        super().__init__(container, controller)

        options = {"padx": 5, "pady": 5}

        # Title of Frame
        self.header_label = ttk.Label(self, text="Book Returning")
        self.header_label.grid(column=0, row=0, sticky="n", columnspan=2, **options)

        # AccessionID label
        self.accessionid_label = ttk.Label(self, text="Accession Number:")
        self.accessionid_label.grid(column=0, row=1, sticky="w", **options)

        # AccessionID field
        self.accessionid = tk.StringVar()
        self.accessionid_field = ttk.Entry(self, textvariable=self.accessionid)
        self.accessionid_field.grid(column=1, row=1, sticky="w", **options)
        self.accessionid_field.focus()

        # Return date label
        self.return_date_label = ttk.Label(self, text="Return Date:")
        self.return_date_label.grid(column=0, row=3, sticky="nw", **options)

        # Return date field
        self.return_year = tk.IntVar()
        self.return_month = tk.IntVar()
        self.return_day = tk.IntVar()

        self.return_date_field = ttk.Frame(self)

        # Year label
        self.year_label = ttk.Label(self.return_date_field, text="Year:")
        self.year_label.grid(column=0, row=0, sticky="w")

        # Year field
        self.spinbox_year = ttk.Spinbox(self.return_date_field, from_=0, to=9999, textvariable=self.return_year)
        self.spinbox_year.grid(column=1, row=0, sticky="w")

        # Month label
        self.month_label = ttk.Label(self.return_date_field, text="Month:")
        self.month_label.grid(column=0, row=1, sticky="w")

        # Month field
        self.spinbox_month = ttk.Spinbox(self.return_date_field, from_=1, to=12, textvariable=self.return_month)
        self.spinbox_month.grid(column=1, row=1, sticky="w")

        # Day label
        self.day_label = ttk.Label(self.return_date_field, text="Day:")
        self.day_label.grid(column=0, row=2, sticky="w")

        # Day field
        self.spinbox_day = ttk.Spinbox(self.return_date_field, from_=1, to=31, textvariable=self.return_day)
        self.spinbox_day.grid(column=1, row=2, sticky="w")

        self.return_date_field.grid(column=1, row=3, sticky="w", **options)

        # Cancel button
        self.cancel_button = ttk.Button(self, text="Cancel")
        self.cancel_button["command"] = self.cancel_return
        self.cancel_button.grid(column=0, row=4, sticky="w", **options)

        # Submit button
        self.submit_button = ttk.Button(self, text="Submit")
        self.submit_button["command"] = self.confirm_return
        self.submit_button.grid(column=1, row=4, sticky="e", **options)

        # Layout method
        self.grid(column=0, row=0, sticky="nsew", **options)

    def get_return_date(self):
        for date_field in (self.return_year.get(), self.return_month.get(), self.return_day.get()):
            if date_field == 0:
                raise Exception("Invalid Date")
        return f"{self.return_year.get()}-{self.return_month.get()}-{self.return_day.get()}"

    def reset_frame(self):
        self.accessionid_field.delete(0, "end")
        self.spinbox_year.delete(0, "end")
        self.spinbox_month.delete(0, "end")
        self.spinbox_day.delete(0, "end")

    def cancel_return(self):
        self.reset_frame()
        self.controller.show_frame(LoansMainFrame)

    def confirm_return(self):
        try:
            self.controller.raise_confirmation(
                f"SELECT BorrowBy.AccessionID, Books.Title, \
                BorrowBy.MemberID, Members.Name, \
                \"{self.get_return_date()}\" AS ReturnDate, \
                GREATEST(DATEDIFF(\"{self.get_return_date()}\", BorrowBy.DueDate), 0) AS Fine \
                FROM BorrowBy LEFT JOIN Books ON BorrowBy.AccessionID=Books.AccessionID \
                LEFT JOIN Members ON BorrowBy.MemberID=Members.MemberID \
                WHERE BorrowBy.AccessionID=\"{self.accessionid.get()}\" \
                ORDER BY BorrowBy.DueDate DESC",
                self.submit_return
            )
        except Exception as e:
            self.reset_frame()
            self.controller.raise_error(e)

    def submit_return(self):
        try:
            book_returning(
                self.accessionid.get(),
                self.get_return_date()
            )
            self.controller.operation_success("Book Return")
        except Exception as e:
            self.reset_frame()
            self.controller.raise_error(e)

class LoansMainFrame(tk.Frame):
    def __init__(self, container, controller):
        super().__init__(container)
        self.controller = controller

        options = {'padx': 5, 'pady': 5}

        # Book borrowing button
        self.book_borrowing_button = ttk.Button(self, text="Book Borrowing")
        self.book_borrowing_button["command"] = self.open_book_borrow_frame
        self.book_borrowing_button.pack(**options)

        # Book returning button
        self.book_returning_button = ttk.Button(self, text="Book Returning")
        self.book_returning_button["command"] = self.open_book_return_frame
        self.book_returning_button.pack(**options)

        # Layout method
        self.grid(column=0, row=0,sticky="nsew", **options)

    def open_book_borrow_frame(self):
        self.controller.show_frame(BookBorrowFrame)

    def open_book_return_frame(self):
        self.controller.show_frame(BookReturnFrame)

class LoansControllerFrame(ControllerFrame):
    def __init__(self, container):
        super().__init__(
            container,
            [
                LoansMainFrame,
                BookBorrowFrame,
                BookReturnFrame
            ],
            LoansMainFrame
        )

if __name__ == "__main__":
    app = App()
    LoansControllerFrame(app)
    app.mainloop()
