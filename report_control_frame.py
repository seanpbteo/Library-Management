import tkinter
import report_menu
import reports_top


class ReportControllerFrame(tkinter.Frame):
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
        frames = ((report_menu.Reporthome, reports_top.All_loan_books, reports_top.Book_on_Reserve, reports_top.Outstanding_Fines, reports_top.Book_Loan_by_Indiv))

        for F in frames:
            frame = F(container, self)

            # initializing frame of that object from
            # startpage, page1, page2 respectively with
            # for loop
            self.frames[F] = frame

            frame.grid(row = 0, column = 0, sticky ="nsew")

        self.show_frame(report_menu.Reporthome)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()
