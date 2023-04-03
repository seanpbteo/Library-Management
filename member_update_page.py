from tkinter import *
import tkinter
from member_helper import retrieve_member
import membership_page
import membership_update_form_page


class MembershipUpdatePage(tkinter.Frame):

    def __init__(self, parent, controller):
        tkinter.Frame.__init__(self, parent)
        self.controller = controller
        top_label = tkinter.Label(self, text="To Update a Member, Please Enter Membership ID:")
        top_label.grid(row=0,column=0, columnspan=6)
        member_ID_label = tkinter.Label(self, text="Membership ID").grid(row=1, column=0, columnspan=2)
        self.member_ID_text_field = tkinter.Entry(self)
        self.member_ID_text_field.grid(row=1, column=2, columnspan=4)

        delete_member_button = tkinter.Button(self, text="Update Member", 
        command=lambda:self.update_member_form()).grid(row=2,column=0,columnspan=3)

        membership_page_button = tkinter.Button(self, text="Back to Membership Menu",
        command=lambda:controller.show_frame(membership_page.MembershipPage)).grid(row=2,column=3,columnspan=3)

    def update_member_form(self):
        id = self.member_ID_text_field.get()
        self.member_ID_text_field.delete(0,'end')
        self.controller.tempdata = retrieve_member(id)
        self.controller.frames[membership_update_form_page.MembershipUpdateFormPage].fill_info()
        self.controller.show_frame(membership_update_form_page.MembershipUpdateFormPage)
