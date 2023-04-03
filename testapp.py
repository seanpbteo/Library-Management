import tkinter as tk
from tkinter import ttk
from booksframes import BooksControllerFrame
from loansframes import LoansControllerFrame
from frames import *

from membership_controller_frame import *
from report_control_frame import *
from Tkinter import *

class TestAppMainFrame(tk.Frame):
    def __init__(self, container):
        super().__init__(container)

        options = {"padx": 5, "pady": 5}

        # Books button
        self.books_button = ttk.Button(self, text="Books")
        self.books_button["command"] = self.open_books
        self.books_button.pack(**options)

        # Loans button
        self.loans_button = ttk.Button(self, text="Loans")
        self.loans_button["command"] = self.open_loans
        self.loans_button.pack(**options)

        # Member button
        self.member_button = ttk.Button(self, text="Member")
        self.member_button["command"] = self.open_member
        self.member_button.pack(**options)

        # Report button
        self.report_button = ttk.Button(self, text="Report")
        self.report_button["command"] = self.open_report
        self.report_button.pack(**options)

        # reservations button
        self.reservations_button = ttk.Button(self, text="Reservations")
        self.reservations_button["command"] = self.open_reservations
        self.reservations_button.pack(**options)

        # fines button
        self.fines_button = ttk.Button(self, text="Fines")
        self.fines_button["command"] = self.open_fines
        self.fines_button.pack(**options)

        # Layout method
        self.grid(column=0, row=0, sticky="nsew", **options)

    def open_books(self):
        newWindow = tk.Toplevel()
        BooksControllerFrame(newWindow)

    def open_loans(self):
        newWindow = tk.Toplevel()
        LoansControllerFrame(newWindow)

    def open_member(self):
        newWindow = tk.Toplevel()
        MembershipControllerFrame(newWindow)

    def open_report(self):
        newWindow = tk.Toplevel()
        ReportControllerFrame(newWindow)

    def open_reservations(self):
        newWindow = tk.Toplevel()
        ReservationControllerFrame(newWindow)

    def open_fines(self):
        newWindow = tk.Toplevel()
        FinesControllerFrame(newWindow)

if __name__ == "__main__":
    app = App()
    TestAppMainFrame(app)
    app.mainloop()
