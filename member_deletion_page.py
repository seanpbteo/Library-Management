from tkinter import *
import tkinter
from member_helper import delete_member, retrieve_member
import membership_page

class MemberDeletionPage(tkinter.Frame):
    def __init__(self, parent, controller):
        tkinter.Frame.__init__(self, parent)
        self.controller = controller
        top_label = tkinter.Label(self, text="To Delete Member, Please Enter Membership ID:")
        top_label.grid(row=0,column=0, columnspan=6)
        member_ID_label = tkinter.Label(self, text="Membership ID").grid(row=1, column=0, columnspan=2)
        self.member_ID_text_field = tkinter.Entry(self)
        self.member_ID_text_field.grid(row=1, column=2, columnspan=4)

        delete_member_button = tkinter.Button(self, text="Delete Member", 
        command=self.confirmation_message).grid(row=2,column=0,columnspan=3)

        membership_page_button = tkinter.Button(self, text="Back to Membership Menu",
        command=lambda:controller.show_frame(membership_page.MembershipPage)).grid(row=2,column=3,columnspan=3)

    def remove_member(self, top):
        status = delete_member(self.member_ID_text_field.get())
        top.destroy()
        if status == 1:
            self.member_ID_text_field.delete(0,'end')
            self.success_message()
        else:
            self.error_message()
    
    def confirmation_message(self):
        top = Toplevel(self.controller)
        top.geometry("250x500")
        top.overrideredirect(1)
        member = retrieve_member(self.member_ID_text_field.get())
        if member != None:
            Label(top, text= "Please Confirm Details to Be Correct!", wraplength=100).place(x=62,y=50)
            Label(top, text= f"Member ID: {member[0]}").place(x=62,y=100)
            Label(top, text= f"Name : {member[1]}").place(x=62,y=150)
            Label(top, text= f"Faculty : {member[2]}").place(x=62,y=200)
            Label(top, text= f"Phone Number : {member[3]}").place(x=62,y=250)
            Label(top, text= f"Email Address: {member[4]}").place(x=62,y=300)
            close = Button(top, text = "Confirm Deletion", command = lambda: self.remove_member(top), height=3, width=10, wraplength=50)
            close.place(x=10, y=400)
            confirmation = Button(top, text = "Back to Delete Function", command = lambda: top.destroy(), height=3, width=10, wraplength=50)
            confirmation.place(x=100, y=400)
        else:
            top.destroy()
            self.error_message()

    def success_message(self):
        top= Toplevel(self.controller)
        top.geometry("250x250")
        top.overrideredirect(1)
        Label(top, text= "Successfully deleted member!", wraplength=120).place(x=62,y=125)
        close = Button(top, text = "Back to Delete Function", command = lambda: top.destroy(), height=3, width=10, wraplength=50)
        close.pack(side=BOTTOM)

    def error_message(self):
        top= Toplevel(self.controller)
        top.geometry("250x250")
        top.overrideredirect(1)
        Label(top, text= "Member doesn't exist, has loans, reservations or outstanding fines!", wraplength=120).place(x=62,y=125)
        close = Button(top, text = "Back to Delete Function", command = lambda: top.destroy(), height=3, width=10, wraplength=50)
        close.pack(side=BOTTOM)
