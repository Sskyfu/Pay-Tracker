import customtkinter

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("Pay Tracker")
        self.geometry("400x150")
        self.grid_columnconfigure((0, 1), weight=1)
        self.title = customtkinter.CTkLabel(self, text="Pay Tracking App")
        self.title.grid(row=0, column=0, padx=20, pady=20, sticky="e")

app = App()
app.mainloop()


