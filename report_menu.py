import tkinter
from tkinter import *
import reports_top


class Reporthome(tkinter.Frame):

    def __init__(self, parent, controller):
        tkinter.Frame.__init__(self, parent)
        # self.geometry("452x255")
        # self.title("Reports")
        # def display_main_menu():
        #     myFrame.destroy()
        #     other_frame.destroy()
        #     Mainmenu(self)

        myFrame = LabelFrame(self, text="Select one of the Options below:", padx=5, pady=5)
        myFrame.grid(row=0, column=0)

        # creating buttons in Frame
        button_width = 23
        lbl_width = 36
        all_loan_books_button = Button(myFrame, text="12. Books on Loan", width=button_width, anchor=W, pady=9,
                                       command=lambda: controller.show_frame(reports_top.All_loan_books))
        all_loan_books_lbl = Label(myFrame, text="This function displays all the books currently\n on loan to members.",
                                   bd=2, relief=SUNKEN, pady=5, width=lbl_width)

        reserve_books_button = Button(myFrame, text="13. Books on Reservation", width=button_width, anchor=W, pady=9,
                                      command=lambda: controller.show_frame(reports_top.Book_on_Reserve))
        reserve_books_lbl = Label(myFrame, text="This function displays all the\n books that members have reserved.",
                                  bd=2, relief=SUNKEN, pady=5, width=lbl_width)

        outstanding_fines_button = Button(myFrame, text="14. Outstanding Fines", width=button_width, anchor=W, pady=9,
                                          command=lambda: controller.show_frame(reports_top.Outstanding_Fines))
        outstanding_fines_lbl = Label(myFrame, text="This function displays all\n members with outstanding fines.",
                                      bd=2, relief=SUNKEN, pady=5, width=lbl_width)

        loan_books_member_button = Button(myFrame, text="15. Books on Loan to Member", width=button_width, anchor=W, pady=9,
                                          command=lambda: controller.show_frame(reports_top.Book_Loan_by_Indiv))
        loan_books_member_lbl = Label(myFrame, text="This function displays all the books a member\n identified by the membership id has borrowed.",
                                      bd=2, relief=SUNKEN, pady=5, width=lbl_width)


        # Frame packing
        all_loan_books_button.grid(row=0, column=0)
        all_loan_books_lbl.grid(row=0, column=1, sticky=W)
        reserve_books_button.grid(row=1, column=0)
        reserve_books_lbl.grid(row=1, column=1, sticky=W)
        outstanding_fines_button.grid(row=2, column=0)
        outstanding_fines_lbl.grid(row=2, column=1, sticky=W)
        loan_books_member_button.grid(row=3, column=0)
        loan_books_member_lbl.grid(row=3, column=1, sticky=W)

        # main packing
        myFrame.grid(row=0, column=0, padx=5)




