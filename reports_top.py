from tkinter import *
from tkinter import ttk
# backend is the file with all functions
import report_backend


import report_menu


class All_loan_books(ttk.Frame):

    def __init__(self, parent, controller):
        ttk.Frame.__init__(self, parent)
        self.controller = controller
        # New window
        # global top

        # top.geometry("570x280")
        # top.title("All books on loan")

        # Title
        titlelabel = Label(self, text="All Books on Loan Report", font="Courier 13 bold")
        titlelabel.grid(row=0, column=0, padx=10)

        # Table
        table_frame = Frame(self)
        table_frame.grid(row=1, column=0, padx=10)

        # Table Scroll Bar
        table_scroll = Scrollbar(table_frame)
        table_scroll.pack(side=RIGHT, fill=Y)

        # Formatting tree
        table = ttk.Treeview(table_frame, yscrollcommand=table_scroll.set)
        table_scroll.config(command=table.yview)
        table = ttk.Treeview(table_frame)

        # table column names
        table['columns'] = ('accession_id', 'title', 'authors', 'isbn', 'publisher', 'publication_year')

        # formatting table
        table.column("#0", width=0,  stretch=NO)
        table.column("accession_id", anchor=CENTER, width=46)
        table.column("title", anchor=CENTER, width=130)
        table.column("authors", anchor=CENTER, width=100)
        table.column("isbn", anchor=CENTER, width=88)
        table.column("publisher", anchor=CENTER, width=130)
        table.column("publication_year", anchor=CENTER, width=48)

        # column titles
        table.heading("#0", text="", anchor=CENTER)
        table.heading("accession_id", text="Acc. ID", anchor=CENTER)
        table.heading("title", text="Title", anchor=CENTER)
        table.heading("authors", text="Authors", anchor=CENTER)
        table.heading("isbn", text="ISBN", anchor=CENTER)
        table.heading("publisher", text="Publisher", anchor=CENTER)
        table.heading("publication_year", text="Pub. Year", anchor=CENTER)

        # inserting values into table
        db = report_backend.show_books_on_loan()
        i = 0
        if db:
            for row in db:
                table.insert(parent='', index='end', iid=i, text='',
                             values=(row[0], row[1], row[5], row[2], row[3], row[4]))
                i += 1

        # pack table
        table.pack()

        # back button
        back_button = Button(self, text="Back", width=23, pady=9,
                             command=lambda: controller.show_frame(report_menu.Reporthome))
        back_button.grid(row=2, column=0)



class Book_on_Reserve(ttk.Frame):

    def __init__(self, parent, controller):
        ttk.Frame.__init__(self, parent)
        self.controller = controller
        # New window
        # global self
        # self = Toplevel()
        # self.geometry("400x280")
        # self.title("Reserved Books")

        # Title
        titlelabel = Label(self, text="All Reserved Books Report", font="Courier 13 bold")
        titlelabel.grid(row=0, column=0, padx=10)

        # Table
        table_frame = Frame(self)
        table_frame.grid(row=1, column=0, padx=10)

        # Table Scroll Bar
        table_scroll = Scrollbar(table_frame)
        table_scroll.pack(side=RIGHT, fill=Y)

        # Formatting tree
        table = ttk.Treeview(table_frame, yscrollcommand=table_scroll.set)
        table_scroll.config(command=table.yview)

        # Column names
        table['columns'] = ('accession_id', 'title', 'member_id', 'name')

        # Formatting columns
        table.column("#0", width=0,  stretch=NO)
        table.column("accession_id", anchor=CENTER, width=45)
        table.column("title", anchor=CENTER, width=130)
        table.column("member_id", anchor=CENTER, width=100)
        table.column("name", anchor=CENTER, width=85)

        # Naming columns
        table.heading("#0", text="", anchor=CENTER)
        table.heading("accession_id", text="Acc. ID", anchor=CENTER)
        table.heading("title", text="Title", anchor=CENTER)
        table.heading("member_id", text="Mem. ID", anchor=CENTER)
        table.heading("name", text="Name", anchor=CENTER)

        # Inserting values into table
        db = report_backend.show_books_on_reservation()
        i = 0
        if db:
            for row in db:
                table.insert(parent='', index='end', iid=i, text='',
                             values=(row[0], row[1], row[2], row[3]))
                i += 1
        # pack table
        table.pack()

        # back button
        back_button = Button(self, text="Back", width=23, pady=9,
                             command=lambda: controller.show_frame(report_menu.Reporthome))
        back_button.grid(row=2, column=0)


class Outstanding_Fines(ttk.Frame):

    def __init__(self, parent, controller):
        ttk.Frame.__init__(self, parent)
        self.controller = controller
        # New Window
        # global self
        # self = Toplevel()
        # self.geometry("480x270")
        # self.title("Outstanding Fines")

        # Title
        titlelabel = Label(self, text="Members with Outstanding Fines", font="Courier 13 bold")
        titlelabel.grid(row=0, column=0, padx=10)

        # Table Frame
        table_frame = Frame(self)
        table_frame.grid(row=1, column=0, padx=10)

        # Table Scroll Bar
        table_scroll = Scrollbar(table_frame)
        table_scroll.pack(side=RIGHT, fill=Y)

        # configuring table
        table = ttk.Treeview(table_frame, yscrollcommand=table_scroll.set)
        table_scroll.config(command=table.yview)

        # table column names
        table['columns'] = ('membership_id', 'name', 'faculty', 'phone_no', 'email')

        # formatting table
        table.column("#0", width=0,  stretch=NO)
        table.column("membership_id", anchor=CENTER, width=60)
        table.column("name", anchor=CENTER, width=130)
        table.column("faculty", anchor=CENTER, width=100)
        table.column("phone_no", anchor=CENTER, width=85)
        table.column("email", anchor=CENTER, width=85)

        # Naming Columns
        table.heading("#0", text="", anchor=CENTER)
        table.heading("membership_id", text="Mem. ID", anchor=CENTER)
        table.heading("name", text="Name", anchor=CENTER)
        table.heading("faculty", text="Faculty", anchor=CENTER)
        table.heading("phone_no", text="Phone No.", anchor=CENTER)
        table.heading("email", text="Email", anchor=CENTER)

        # Inserting data into table
        db = report_backend.members_with_fines()
        i = 0
        if db:
            for row in db:
                table.insert(parent='', index='end', iid=i, text='',
                             values=(row[0], row[1], row[2], row[3], row[4]))
                i += 1

        # pack table
        table.pack()

        # back button
        back_button = Button(self, text="Back", width=23, pady=9,
                             command=lambda: controller.show_frame(report_menu.Reporthome))
        back_button.grid(row=2, column=0)


class Book_Loan_by_Indiv(ttk.Frame):

    def __init__(self, parent, controller):
        ttk.Frame.__init__(self, parent)
        self.controller = controller
        # New Window
        # global self
        # self = Toplevel()
        # self.geometry("600x300")
        # self.title("Books on Loan")

        # Title
        titlelabel = Label(self, text="Books on Loan", font="Courier 13 bold")
        titlelabel.grid(row=0, column=0, columnspan=2, padx=10)

        # helper function into insert records
        def get_records():
            member_id = e.get()
            db = report_backend.books_on_loan_by_member(member_id)

            if table.get_children():
                table.delete(*table.get_children())

            i = 0
            if db:
                for row in db:
                    table.insert(parent='', index='end', iid=i, text='',
                                 values=(row[0], row[1], row[5], row[2], row[3], row[4]))
                    i += 1

        # Entry box
        e = Entry(self, font='Courier 11')
        e.grid(row=1, column=0, sticky=E)

        # Search Button
        search_button = Button(self, text="Search", width=10, command=get_records)
        search_button.grid(row=1, column=1, sticky=W, padx=2)

        # Table
        table_frame = Frame(self)
        table_frame.grid(row=2, column=0, columnspan=2, padx=10)

        # Table scroll bar
        table_scroll = Scrollbar(table_frame)
        table_scroll.pack(side=RIGHT, fill=Y)

        # Configuring tree
        table = ttk.Treeview(table_frame, yscrollcommand=table_scroll.set)
        table_scroll.config(command=table.yview)

        # Column names
        table['columns'] = ('accession_id', 'title', 'authors', 'isbn', 'publisher', 'publication_year')

        # Formatting tree
        table.column("#0", width=0,  stretch=NO)
        table.column("accession_id", anchor=CENTER, width=46)
        table.column("title", anchor=CENTER, width=130)
        table.column("authors", anchor=CENTER, width=100)
        table.column("isbn", anchor=CENTER, width=88)
        table.column("publisher", anchor=CENTER, width=130)
        table.column("publication_year", anchor=CENTER, width=70)

        # Naming Columns
        table.heading("#0", text="", anchor=CENTER)
        table.heading("accession_id", text="Acc. ID", anchor=CENTER)
        table.heading("title", text="Title", anchor=CENTER)
        table.heading("authors", text="Authors", anchor=CENTER)
        table.heading("isbn", text="ISBN", anchor=CENTER)
        table.heading("publisher", text="Publisher", anchor=CENTER)
        table.heading("publication_year", text="Pub. Year", anchor=CENTER)

        # pack table
        table.pack()

        # back button
        back_button = Button(self, text="Back", width=23, pady=9,
                             command=lambda: controller.show_frame(report_menu.Reporthome))
        back_button.grid(row=3, column=0, columnspan=2)