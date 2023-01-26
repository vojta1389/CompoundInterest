import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import pandas as pd
from compoundInterest import calculate_compound_interest
import sys

class App:
    def __init__(self, master):
        self.master = master
        master.title("Compound Interest Calculator")

        # create labels for input
        self.principal_label = tk.Label(master, text="Principal:")
        self.principal_label.grid(row=0, column=0)

        self.rate_label = tk.Label(master, text="Annual Interest Rate (%):")
        self.rate_label.grid(row=1, column=0)

        self.periods_label = tk.Label(master, text="Periods (months):")
        self.periods_label.grid(row=2, column=0)

        self.monthly_deposit_label = tk.Label(master, text="Monthly Deposit:")
        self.monthly_deposit_label.grid(row=3, column=0)

        # create entry widgets for input
        self.principal_entry = tk.Entry(master)
        self.principal_entry.grid(row=0, column=1)

        self.rate_entry = tk.Entry(master)
        self.rate_entry.grid(row=1, column=1)

        self.periods_entry = tk.Entry(master)
        self.periods_entry.grid(row=2, column=1)

        self.monthly_deposit_entry = tk.Entry(master)
        self.monthly_deposit_entry.grid(row=3, column=1)

        # create calculate button
        self.calculate_button = tk.Button(master, text="Calculate", command=self.calculate)
        self.calculate_button.grid(row=4, column=0, columnspan=2)

        self.output_label = tk.Label(master)
        self.output_label.grid(row=5, column=0, columnspan=2)

        #create close button
        self.close_button = tk.Button(master, text="Close", command=self.close)
        self.close_button.grid(row=7, column=0, columnspan=2)

    def calculate(self):
        # get input values
        principal = float(self.principal_entry.get())
        rate = float(self.rate_entry.get()) / 100
        periods = int(self.periods_entry.get())
        monthly_deposit = float(self.monthly_deposit_entry.get())

        # calculate compound interest
        total_savings = calculate_compound_interest(principal, rate, periods, monthly_deposit)

        # create figure for plot
        self.output_label.configure(text=f"Total money put in over {periods} months: ${principal + (monthly_deposit * periods):,.2f}\nTotal savings: ${total_savings:,.2f}")
        df = pd.read_csv('compoundInterest.csv')

        self.fig = plt.figure()
        self.ax = self.fig.add_subplot(111)
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.master)
        self.canvas.draw()
        self.canvas.get_tk_widget().grid(row=6, column=0, columnspan=2)

        self.ax.set_title("Investment Growth")
        self.ax.set_xlabel("Months")
        self.ax.set_ylabel("Value")
        #self.ax.legend()
        self.ax.plot(df['Month'], df['Invested'], label='Invested')
        self.ax.plot(df['Month'], df['Current Value'], label='Current Value')

    def close(self):
        try:
            self.master.destroy()
            print("Program closed")
            sys.exit()
        except:
            print("Error closing program")
            sys.exit()
            



