import customtkinter
import csv

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # pull data from csv, will have
        # TODO: add a pop-up on start asking for file path


        self.pay_data = []
        self.pay_adv = 0
        self.day_count = 0

        with open('Hour _ pay_tracker - pay tracking.csv', 'r') as pay_doc:
            csv_reader = csv.DictReader(pay_doc)

            for line in csv_reader:
                if line['Date '] != '':
                    self.pay_data.append(line)

        for day in self.pay_data:
            if day['Earnings '] != '':
                number = day['Hourly'].replace('$','')
                self.pay_adv += float(number)
                self.day_count += 1
        self.pay_adv = round(self.pay_adv/self.day_count, 2)

        self.title("Pay Tracker")
        self.geometry("400x150")
        self.grid_columnconfigure((0), weight=1)
        self.app_title = customtkinter.CTkLabel(self, text="Pay Tracking App", font=('Arial', 25))
        self.app_title.grid(row=0, column=0, padx=20, pady=20, sticky="ew")
        self.adv_pay_ui = customtkinter.CTkLabel(self, text=str(self.pay_adv), font=('Arial', 25))
        self.adv_pay_ui.grid(row=1, column=0, sticky="ew")

app = App()
app.mainloop()


