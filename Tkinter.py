import tkinter as tk
from tkinter import ttk
from Reservations import *
from helper import *


LARGEFONT =("Verdana", 35)

class ReservationControllerFrame(tk.Frame):

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
        for F in ((ReservationStartPage,ReserveBook,CancelReservation)):

            frame = F(container, self)

            # initializing frame of that object from
            # startpage, page1, page2 respectively with
            # for loop
            self.frames[F] = frame

            frame.grid(row = 0, column = 0, sticky ="nsew")

        self.show_frame(ReservationStartPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

class FinesControllerFrame(tk.Frame):

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
        for F in ((FinesStartPage,FinePayment)):

            frame = F(container, self)

            # initializing frame of that object from
            # startpage, page1, page2 respectively with
            # for loop
            self.frames[F] = frame

            frame.grid(row = 0, column = 0, sticky ="nsew")

        self.show_frame(FinesStartPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


class ReservationStartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # label of frame Layout 2
        label = ttk.Label(self, text ="Reservations", font = LARGEFONT)
        label.grid(row = 0, column = 4, padx = 10, pady = 10)

        ourMessage ='Select one of the options below'
        messageVar = ttk.Label(self, text = ourMessage)
        messageVar.grid(row = 1, column = 1, padx = 10, pady = 10)

        #Reservation
        button1 = ttk.Button(self, text ="Reserve a Book",
                             command = lambda : controller.show_frame(ReserveBook))
        button1.grid(row = 2, column = 1, padx = 10, pady = 10)

        ##CancelReservation
        button2 = ttk.Button(self, text ="Cancel Reservation",
                             command = lambda : controller.show_frame(CancelReservation))
        button2.grid(row = 3, column = 1, padx = 10, pady = 10)

class FinesStartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        # label of frame Layout 2
        label = ttk.Label(self, text ="Fines", font = LARGEFONT)
        label.grid(row = 0, column = 4, padx = 10, pady = 10)

        ourMessage ='Select one of the options below'
        messageVar = ttk.Label(self, text = ourMessage)
        messageVar.grid(row = 1, column = 1, padx = 10, pady = 10)

        #Reservation
        button1 = ttk.Button(self, text ="Payment",
                             command = lambda : controller.show_frame(FinePayment))
        button1.grid(row = 2, column = 1, padx = 10, pady = 10)

class FinePayment(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = ttk.Label(self, text ="Fine Payment", font = LARGEFONT)
        label.grid(row = 0, column = 1, padx = 10, pady = 10)

        ourMessage ='To pay a Fine, please enter the needed information below:'
        messageVar = ttk.Label(self, text = ourMessage)
        messageVar.grid(row = 1, column = 1, padx = 10, pady = 10)


        #Fields
        ttk.Label(self, text='Membership ID:').grid(row=3)
        ttk.Label(self, text='Payment Date:').grid(row=4)
        ttk.Label(self, text='Payment Amount:').grid(row=5)
        MemberID = ttk.Entry(self)
        PaymentDate = ttk.Entry(self)
        PaymentAmt = ttk.Entry(self)
        MemberID.grid(row=3, column=1)
        PaymentDate.grid(row=4, column=1)
        PaymentAmt.grid(row=5, column=1)

        # button to show frame 2 with text
        # layout2
        button1 = ttk.Button(self, text ="Pay Fine", command = lambda : self.PayFine(MemberID.get(), PaymentDate.get(), PaymentAmt.get()))
        button1.grid(row = 7, column = 1, padx = 10, pady = 10)

        button2 = ttk.Button(self, text ="Back to Fines Menu", command = lambda : controller.show_frame(FinesStartPage))
        button2.grid(row = 7, column = 2, padx = 10, pady = 10)

    def noFine(self):
        top = tk.Toplevel(self.controller)
        top.geometry("500x250")
        top.title("Error!")
       # top.overrideredirect(1)
        ttk.Label(top, text= "Error!", ).place(x=150,y=80)
        ttk.Label(top, text= "Member has no fine.").place(x=150,y=100)
        BackToPaymentBtn = ttk.Button(top, text ="Back to Payment Function",
                                      command = lambda : top.destroy()).place(x=150,y=120)

    def WrongPayment(self):
        top= tk.Toplevel(self.controller)
        #top.overrideredirect(1)
        top.geometry("500x250")
        top.title("Error!")
        ttk.Label(top, text= "Error!", ).place(x=150,y=80)
        ttk.Label(top, text= "Incorrect fine payment amount.").place(x=150,y=100)
        BackToPaymentBtn = ttk.Button(top, text ="Back to Payment Function",
                                      command = lambda : top.destroy()).place(x=150,y=120)

    def PayFine(self, MID, PDate, PAmt):
        CorrectPAmt = outstanding_fines(MID)
        top = tk.Toplevel(self)
        #top.overrideredirect(1)
        top.geometry("500x250")
        top.title("Confirm Payment")
        ttk.Label(top, text= "Please Confirm Details To Be Correct").place(x=150,y=80)
        ttk.Label(top, text= "Payment Due: $" + str(CorrectPAmt)).place(x=150,y=100)
        ttk.Label(top, text= "Payment Date: " + PDate ).place(x=150,y=120)
        ttk.Label(top, text= "Membership ID: " + MID ).place(x=150,y=140)


        ConfirmPaymentBtn = ttk.Button(top, text ="Confirm Payment", command = lambda : self.exePayFine(top, MID, PDate, PAmt)).place(x=60,y=160)
        BackToPaymentBtn = ttk.Button(top, text ="Back to Payment Function", command = lambda : top.destroy()).place(x=180,y=160)

    def exePayFine(self,oldTop, MID, PDate, PAmt):
        result = FinePaymentFunction(MID, PDate,PAmt)
        oldTop.destroy()
        if result == 1:
            return 

        elif result == -1:
            self.noFine()
            return 

        elif result == -2:
            self.WrongPayment()
            return 





# second window frame page1
class ReserveBook(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = ttk.Label(self, text ="Book Reservation", font = LARGEFONT)
        label.grid(row = 0, column = 1, padx = 10, pady = 10)

        ourMessage ='To reserve a Book, please enter the needed information below'
        messageVar = ttk.Label(self, text = ourMessage)
        messageVar.grid(row = 1, column = 1, padx = 10, pady = 10)


        #Fields
        ttk.Label(self, text='Accession Number').grid(row=3)
        ttk.Label(self, text='Membership ID').grid(row=4)
        ttk.Label(self, text='Reserve Date').grid(row=5)
        AccessionID = ttk.Entry(self)
        self.MemberID = ttk.Entry(self)
        ReserveDate = ttk.Entry(self)
        AccessionID.grid(row=3, column=1)
        self.MemberID.grid(row=4, column=1)
        ReserveDate.grid(row=5, column=1)

        button1 = ttk.Button(self, text ="Reserve Book",
                             command = lambda : self.confirmation(AccessionID.get(),self.MemberID.get(),ReserveDate.get()))
        button1.grid(row = 7, column = 1, padx = 10, pady = 10)


        button2 = ttk.Button(self, text ="Back to Reservations Menu", command = lambda : controller.show_frame(ReservationStartPage))
        button2.grid(row = 7, column = 2, padx = 10, pady = 10)

    def twoReservations(self):
        top= tk.Toplevel(self.controller)
        #top.overrideredirect(1)
        top.geometry("500x250")
        top.title("Error!")
        ttk.Label(top, text= "Error!", ).place(x=150,y=80)
        ttk.Label(top, text= "Member currently has 2 Books on Reservation.").place(x=150,y=100)

        BackToReserveBtn = ttk.Button(top, text ="Back to Reserve Function", command = lambda : top.destroy()).place(x=150,y=120)

    def OutstandingFine(self):
        top= tk.Toplevel(self.controller)
        #top.overrideredirect(1)
        top.geometry("500x250")
        top.title("Error!")
        ttk.Label(top, text= "Error!", ).place(x=150,y=80)
        ttk.Label(top, text= "Member currently has Outstanding Fine of: $" + str(outstanding_fines(self.MemberID.get()))).place(x=150,y=100)

        BackToReserveBtn = ttk.Button(top, text ="Back to Reserve Function", command = lambda : top.destroy()).place(x=150,y=120)

    def BookNotLoaned(self):
        top= tk.Toplevel(self.controller)
        #top.overrideredirect(1)
        top.geometry("500x250")
        top.title("Error!")
        ttk.Label(top, text= "Error!", ).place(x=150,y=80)
        ttk.Label(top, text= "Book is currently not loaned").place(x=150,y=100)

        BackToReserveBtn = ttk.Button(top, text ="Back to Reserve Function", command = lambda : top.destroy()).place(x=150,y=120)
    def confirmation(self, AID, MID, Rdate):
        top= tk.Toplevel(self.controller)
        top.geometry("500x250")
        top.title("Confirm Reservation")
        ttk.Label(top, text= "Confirm Reservation Details To Be Correct", ).place(x=150,y=80)
        ttk.Label(top, text= "Accession Number: " + AID).place(x=150,y=100)
        ttk.Label(top, text= "Book Title: " + FindBookTitle(AID) ).place(x=150,y=120)
        ttk.Label(top, text= "Membership ID: " + MID ).place(x=150,y=140)
        ttk.Label(top, text= "Member Name: " + FindMemberName(MID)).place(x=150,y=160)
        ttk.Label(top, text= "Reserve Date: " + Rdate).place(x=150,y=180)

       
        ConfirmReserveBtn = ttk.Button(top, text ="Confirm Reservation",command = lambda : self.exeReservation(top, AID, MID, Rdate)).place(x=60,y=200)
        BackToReserveBtn = ttk.Button(top, text ="Back to Reserve Function", command = lambda : top.destroy()).place(x=200,y=200)

    def exeReservation(self,oldTop, AID, MID, Rdate):
        result = ReservationFunction(AID,MID,Rdate)
        oldTop.destroy()
        if result == 1:
            return 

        elif result == -1:
            self.OutstandingFine()
            return 

        elif result == -2:
            self.twoReservations()
            return 

        elif result == -3:
            self.BookNotLoaned()
            return


# third window frame page2
class CancelReservation(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = ttk.Label(self, text ="Reservation Cancellation", font = LARGEFONT)
        label.grid(row = 0, column = 1, padx = 5, pady = 5)

        ourMessage ='To Cancel a Reservation, please enter the needed information below'
        messageVar = ttk.Label(self, text = ourMessage)
        messageVar.grid(row = 1, column = 1, padx = 5, pady = 5)

        #Fields
        ttk.Label(self, text='Accession Number').grid(row=3)
        ttk.Label(self, text='Membership ID').grid(row=4)

        self.AccessionID = ttk.Entry(self)
        MemberID = ttk.Entry(self)
        self.AccessionID.grid(row=3, column=1)
        MemberID.grid(row=4, column=1)

        # button to show frame 2 with text
        # layout2
        button1 = ttk.Button(self, text ="Cancel Reservation",
                             command = lambda : self.cancel(self.AccessionID.get(), MemberID.get()))

        # putting the button in its place
        # by using grid
        button1.grid(row = 7, column = 1, padx = 10, pady = 10)

        # button to show frame 2 with text
        # layout2
        button2 = ttk.Button(self, text ="Back to Reservations Menu",
                             command = lambda : top.destroy())

        button2.grid(row = 7, column = 2, padx = 10, pady = 10)

    def noReservation(self):
        top= tk.Toplevel(self)
        #oldTop.destroy()
        #top.overrideredirect(1)
        top.geometry("500x250")
        top.title("Error! Member has no such Reservation.")
        ttk.Label(top, text= "Error!" ).place(x=150,y=80)
        ttk.Label(top, text= "Member has no such Reservation.").place(x=150,y=100)
        BackToCancelBtn = ttk.Button(top, text ="Back to Cancellation Function", command = lambda : top.destroy()).place(x=150,y=120)

    def cancel(self, AID, MID):
        top= tk.Toplevel(self)
        top.geometry("500x250")
        #top.overrideredirect(1)
        top.title("Confirm Cancellation")
        ttk.Label(top, text= "Confirm Cancellation Details To Be Correct", ).place(x=150,y=80)
        ttk.Label(top, text= "Accession Number: " + AID).place(x=150,y=100)
        ttk.Label(top, text= "Book Title: " + FindBookTitle(AID) ).place(x=150,y=120)
        ttk.Label(top, text= "Membership ID: " + MID ).place(x=150,y=140)
        ttk.Label(top, text= "Member Name: " + FindMemberName(MID)).place(x=150,y=160)

        ConfirmCancelBtn = ttk.Button(top, text ="Confirm Cancellation",command = lambda : self.exeCancel(top,AID,MID)).place(x=60,y=180)
        BackToReserveBtn = ttk.Button(top, text ="Back to Reserve Function", command = lambda : top.destroy()).place(x=200,y=180)

    def exeCancel(self,oldTop, AID, MID):
        result = cancelReservation(AID,MID)
        oldTop.destroy()
        if result == 1:
            return 

        else:
            self.noReservation()
            return



