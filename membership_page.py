from tkinter import *
import tkinter
import member_deletion_page 
import member_update_page 

from membership_creation_page import MembershipCreationPage
class MembershipPage(tkinter.Frame):
    def __init__(self, parent, controller):
        tkinter.Frame.__init__(self, parent)
        top_label = tkinter.Label(self, text="Select one of the Options below:")
        top_label.grid(row=0, column=0, sticky=N,columnspan=3)

        member_creation_button = tkinter.Button(self, text="1. Creation",
        command=lambda:controller.show_frame(MembershipCreationPage)).grid(row=1,column=1)
        
        member_deletion_button = tkinter.Button(self, text="2. Deletion",
        command=lambda:controller.show_frame(member_deletion_page.MemberDeletionPage)).grid(row=2,column=1)

        
        member_creation_button = tkinter.Button(self, text="3. Update",
        command=lambda:controller.show_frame(member_update_page.MembershipUpdatePage)).grid(row=3,column=1)

