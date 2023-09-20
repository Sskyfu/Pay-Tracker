import customtkinter
import csv
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk



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
                number = day['Hourly'].replace('$', '')
                self.pay_adv += float(number)
                self.day_count += 1
        self.pay_adv = round(self.pay_adv / self.day_count, 2)

        self.title("Pay Tracker")
        self.geometry("700x700")
        self.grid_columnconfigure(0, weight=1)
        self.app_title = customtkinter.CTkLabel(self, text="Pay Tracking App", font=('Arial', 25))
        self.app_title.grid(row=0, column=0, padx=20, pady=20, sticky="ew")
        self.adv_pay_ui = customtkinter.CTkLabel(self, text=str(self.pay_adv), font=('Arial', 25))
        self.adv_pay_ui.grid(row=1, column=0, sticky="ew")

        #graph

        dataset = {'Day': [], 'Earnings': []}
        for day in self.pay_data:
            if day['Earnings '] != '':
                dataset['Day'].append(day['Date '])
                number = day['Hourly'].replace('$', '')
                dataset['Earnings'].append(float(number))
        #print(dataset)

        days = dataset['Day']
        earnings = dataset['Earnings']

        figure = plt.Figure(figsize=(6, 4), dpi=100)

        figure_can = FigureCanvasTkAgg(figure, self)
        #NavigationToolbar2Tk(figure_can, self)

        axes = figure.add_subplot()

        axes.bar(days, earnings)
        axes.set_title('Earnings')
        axes.set_ylabel('$')

        figure_can.get_tk_widget().grid(row=2, column=0, sticky="ew")

app = App()
app.mainloop()
