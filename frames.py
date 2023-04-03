import tkinter as tk
from tkinter import ttk
from helper import get_details

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("500x500")

class GUIFrame(tk.Frame):
    def __init__(self, container, controller):
        super().__init__(container)
        self.controller = controller

# frames = list of frame classes to be instantiated and included in the controller
class ControllerFrame(tk.Frame):
    def __init__(self, container, frames, mainframe):
        super().__init__(container)
        self.container = container
        self.mainframe = mainframe
        
        self.frame_dict = {}

        for frame in frames:
            self.frame_dict[frame] = frame(container, self)

        self.show_main()

    def show_frame(self, frame):
        selected_frame = self.frame_dict[frame]
        selected_frame.tkraise()

    def show_main(self):
        self.show_frame(self.mainframe)

    def raise_error(self, error_text):
        error_frame = ErrorFrame(self.container, error_text)
        error_frame.tkraise()

    def operation_success(self, operation_text):
        success_frame = SuccessFrame(self.container, operation_text)
        success_frame.tkraise()

    def raise_confirmation(self, query, button_command):
        confirm_frame = ConfirmFrame(self.container, query, button_command)
        confirm_frame.tkraise()

class PopUpFrame(tk.Frame):
    def __init__(self, container, title):
        super().__init__(container)
        self.title = title
        self.details_frame = tk.Frame(self)

        options = {"padx": 5, "pady": 5}

        # Title Label
        self.title_label = ttk.Label(self, text=self.title)
        self.title_label.pack(**options)

        # Details frame
        self.details_frame.pack(**options)

        # Return button
        self.return_button = ttk.Button(self, text="Return")
        self.return_button["command"] = self.return_to_previous_frame
        self.return_button.pack(**options)

        # Layout method
        self.grid(column=0, row=0, **options)

    def return_to_previous_frame(self):
        self.destroy()

class ErrorFrame(PopUpFrame):
    def __init__(self, container, error_text):
        super().__init__(container, "Error")

        tk.Label(self.details_frame, text=error_text).pack()

class SuccessFrame(PopUpFrame):
    def __init__(self, container, success_text):
        super().__init__(container, "Success")

        tk.Label(self.details_frame, text=success_text).pack()

class ConfirmFrame(PopUpFrame):
    def __init__(self, container, query, button_command):
        super().__init__(container, "Confirm Details")

        try:
            details = get_details(query)
        except Exception as e:
            details = {"Error": e}

        for col, value in details.items():
            tk.Label(self.details_frame, text=f"{col}: {value}").pack()

        def extended_command():
            button_command()
            self.return_to_previous_frame()

        ttk.Button(self.details_frame, text="Confirm", command=extended_command).pack()

