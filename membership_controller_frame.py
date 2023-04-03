from tkinter import *
import tkinter
import membership_page
import member_deletion_page
import member_update_page
import membership_creation_page
import membership_update_form_page

class MembershipControllerFrame(tkinter.Frame):
    def __init__(self, container):
        super().__init__(container)
        self.container = container
        self.tempdata = ()

  
        container.grid_rowconfigure(0, weight = 1)
        container.grid_columnconfigure(0, weight = 1)
  
        # initializing frames to an empty array
        self.frames = {} 
  
        # iterating through a tuple consisting
        # of the different page layouts
        for F in ((membership_page.MembershipPage, membership_creation_page.MembershipCreationPage, member_deletion_page.MemberDeletionPage, member_update_page.MembershipUpdatePage, membership_update_form_page.MembershipUpdateFormPage)):
  
            frame = F(container, self)
  
            # initializing frame of that object from
            # startpage, page1, page2 respectively with
            # for loop
            self.frames[F] = frame
  
            frame.grid(row = 0, column = 0, sticky ="nsew")
  
        self.show_frame(membership_page.MembershipPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()