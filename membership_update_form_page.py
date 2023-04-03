from tkinter import *
import tkinter
from member_helper import update_member
import member_update_page
import membership_page 

class MembershipUpdateFormPage(tkinter.Frame):
    def __init__(self, parent, controller):
        tkinter.Frame.__init__(self, parent)
        top_label = tkinter.Label(self, text="Please Enter Requestd Information Below:")
        top_label.grid(row=0,column=0, columnspan=4)
        self.controller = controller
        self.ogname = StringVar()
        self.ogfaculty = StringVar()
        self.ogpn = StringVar()
        self.ogemail = StringVar()

        member_ID_label = tkinter.Label(self, text="Membership ID").grid(row=1, column=0)
        self.member_ID_text_field = tkinter.Text(self, height=1, width=5)
        self.member_ID_text_field.configure(state='disabled')
        self.member_ID_text_field.grid(row=1, column=1, columnspan=3)

        name_label = tkinter.Label(self, text="Name").grid(row=2, column=0)

        self.name_text_field = tkinter.Entry(self, textvariable=self.ogname)
        self.name_text_field.grid(row=2, column=1, columnspan=3)
        
        faculty_label = tkinter.Label(self, text="Faculty").grid(row=3, column=0)
        self.faculty_text_field = tkinter.Entry(self, textvariable=self.ogfaculty)
        self.faculty_text_field.grid(row=3, column=1, columnspan=3)
        
        pn_label = tkinter.Label(self, text="Phone Number").grid(row=4, column=0)
        self.pn_text_field = tkinter.Entry(self, textvariable=self.ogpn)
        self.pn_text_field.grid(row=4, column=1, columnspan=3)
        
        email_label = tkinter.Label(self, text="Email Address").grid(row=5, column=0)
        self.email_text_field = tkinter.Entry(self, textvariable=self.ogemail)
        self.email_text_field.grid(row=5, column=1, columnspan=3)

        create_new_member_button = tkinter.Button(self, text="Update Member", 
        command=self.confirmation_message).grid(row=6,column=0,columnspan=2)
        
        main_menu = tkinter.Button(self, text="Back to Membership Menu",
        command=lambda:controller.show_frame(membership_page.MembershipPage)).grid(row=6,column=2,columnspan=2)

    def confirmation_message(self):
        top = Toplevel(self.controller)
        top.geometry("250x500")
        top.overrideredirect(1)
        Label(top, text= "Please Confirm Details to Be Correct!", wraplength=100).place(x=62,y=50)
        Label(top, text= f"Member ID: {self.member_ID_text_field.get('1.0','1.5')}").place(x=62,y=100)
        Label(top, text= f"Name : {self.name_text_field.get()}").place(x=62,y=150)
        Label(top, text= f"Faculty : {self.faculty_text_field.get()}").place(x=62,y=200)
        Label(top, text= f"Phone Number : {self.pn_text_field.get()}").place(x=62,y=250)
        Label(top, text= f"Email Address: {self.email_text_field.get()}").place(x=62,y=300)
        close = Button(top, text = "Confirm Update", command = lambda: self.update_member_info(top), height=3, width=10, wraplength=50)
        close.place(x=10, y=400)
        confirmation = Button(top, text = "Back to Update Function", command = lambda: top.destroy(), height=3, width=10, wraplength=50)
        confirmation.place(x=100, y=400)
    
    def update_member_info(self, top):
        id = self.member_ID_text_field.get("1.0","end-1c")
        name = self.name_text_field.get()
        faculty = self.faculty_text_field.get()
        pn = self.pn_text_field.get()
        email = self.email_text_field.get()
        status = update_member(id, name, faculty, pn, email)

        if status == 1:
            self.member_ID_text_field.configure(state='normal')
            self.member_ID_text_field.delete("1.0",'end')
            self.member_ID_text_field.configure(state='disabled')

            self.name_text_field.delete(0,'end') 
            self.faculty_text_field.delete(0,'end') 
            self.pn_text_field.delete(0,'end') 
            self.email_text_field.delete(0,'end')
            top.destroy()
            self.controller.show_frame(member_update_page.MembershipUpdatePage)
            self.success_message()
        else:
            top.destroy()
            self.error_message()

    def error_message(self):
        top= Toplevel(self.controller)
        top.geometry("250x250")
        top.overrideredirect(1)
        Label(top, text= "Missing or incomplete fields.", wraplength=120).place(x=62,y=125)
        close = Button(top, text = "Back to Update Function", command = lambda: top.destroy(), height=3, width=10, wraplength=50)
        close.pack(side=BOTTOM)

    def success_message(self):
        top= Toplevel(self.controller)
        top.geometry("250x250")
        top.overrideredirect(1)
        Label(top, text= "ALS Membership updated.", wraplength=120).place(x=62,y=125)
        close = Button(top, text = "Back to Update Function", command = lambda: top.destroy(), height=3, width=10, wraplength=50)
        close.pack(side=BOTTOM)
    
    def fill_info(self):
        self.member_ID_text_field.configure(state='normal')
        self.member_ID_text_field.delete("1.0", 'end')
        self.member_ID_text_field.insert('end', self.controller.tempdata[0])
        self.ogname.set(self.controller.tempdata[1])

        self.ogfaculty.set(self.controller.tempdata[2])

        self.ogpn.set(self.controller.tempdata[3])

        self.ogemail.set(self.controller.tempdata[4])

        self.member_ID_text_field.configure(state='disabled')

