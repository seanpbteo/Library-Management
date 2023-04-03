from tkinter import *
import tkinter
from member_helper import add_new_member, id_generator
import membership_page

class MembershipCreationPage(tkinter.Frame):
    def __init__(self, parent, controller):
        tkinter.Frame.__init__(self, parent)
        self.controller = controller
        top_label = tkinter.Label(self, text="To Create Member, Please Enter Requested Information Below:")
        top_label.grid(row=0,column=0, columnspan=4)

        member_ID_label = tkinter.Label(self, text="Membership ID").grid(row=1, column=0)
        self.member_ID_text_field = tkinter.Text(self, height=1, width=5)
        self.member_ID_text_field.insert('end', id_generator())
        self.member_ID_text_field.configure(state='disabled')
        self.member_ID_text_field.grid(row=1, column=1, columnspan=3)

        name_label = tkinter.Label(self, text="Name").grid(row=2, column=0)
        self.name_text_field = tkinter.Entry(self)
        self.name_text_field.grid(row=2, column=1, columnspan=3)
        
        faculty_label = tkinter.Label(self, text="Faculty").grid(row=3, column=0)
        self.faculty_text_field = tkinter.Entry(self)
        self.faculty_text_field.grid(row=3, column=1, columnspan=3)
        
        pn_label = tkinter.Label(self, text="Phone Number").grid(row=4, column=0)
        self.pn_text_field = tkinter.Entry(self)
        self.pn_text_field.grid(row=4, column=1, columnspan=3)
        
        email_label = tkinter.Label(self, text="Email Address").grid(row=5, column=0)
        self.email_text_field = tkinter.Entry(self)
        self.email_text_field.grid(row=5, column=1, columnspan=3)

        create_new_member_button = tkinter.Button(self, text="Create Member", 
        command=self.create_member).grid(row=6,column=0,columnspan=2)
        
        main_menu = tkinter.Button(self, text="Back to Membership Page",
        command= self.return_to_membership_page).grid(row=6,column=2,columnspan=2)

    def return_to_membership_page(self):
        self.member_ID_text_field.configure(state='normal')
        self.member_ID_text_field.delete('0.0','end')
        self.member_ID_text_field.insert('end', id_generator())
        self.member_ID_text_field.configure(state='disabled')
        self.name_text_field.delete(0,'end') 
        self.faculty_text_field.delete(0,'end') 
        self.pn_text_field.delete(0,'end') 
        self.email_text_field.delete(0,'end')
        self.controller.show_frame(membership_page.MembershipPage)

    def create_member(self):
        id = self.member_ID_text_field.get("1.0",'end-1c')
        name = self.name_text_field.get()
        faculty = self.faculty_text_field.get()
        pn = self.pn_text_field.get()
        email = self.email_text_field.get()
        
        status = add_new_member(id,name,faculty, pn, email)

        if status == 1:
            self.member_ID_text_field.configure(state='normal')
            self.member_ID_text_field.delete("1.0",'end')
            self.member_ID_text_field.insert('end', id_generator())
            self.member_ID_text_field.configure(state='disabled')

            self.name_text_field.delete(0,'end') 
            self.faculty_text_field.delete(0,'end') 
            self.pn_text_field.delete(0,'end') 
            self.email_text_field.delete(0,'end')
            self.success_message()
        else:
            self.error_message()
    
    def success_message(self):
        top= Toplevel(self.controller)
        top.geometry("250x250")
        top.overrideredirect(1)
        Label(top, text= "Successfully created new member!", wraplength=120).place(x=62,y=125)
        close = Button(top, text = "Back to Create Function", command = lambda: top.destroy(), height=3, width=10, wraplength=50)
        close.pack(side=BOTTOM)

    def error_message(self):
        top= Toplevel(self.controller)
        top.geometry("250x250")
        top.overrideredirect(1)
        Label(top, text= "Member already exists; Missing or Incomplete fields!", wraplength=120).place(x=62,y=125)
        close = Button(top, text = "Back to Create Function", command = lambda: top.destroy(), height=3, width=10, wraplength=50)
        close.pack(side=BOTTOM)
