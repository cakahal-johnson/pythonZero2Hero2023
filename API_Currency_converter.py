 # importing required modules
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import tkinter as tk
import requests  # API request
import datetime as dt

# we use OOP classs
class CurrencyConverter:

    def __init__(self, url):
        self.url = 'https://api.exchangerate.host/latest'
        self.response = requests.get(url)
        self.data = self.response.json()
        self.rates = self.data.get('rates')

    def convert(self, amount, base_currency, des_currency):
        if base_currency == 'EUR':
            amount = amount/self.rates[base_currency]

            # Limiting the result to 2 decimal places
            amount = round(amount*self.rates[des_currency], 2)

            # Add comma every 3 Numbers
            amount = '{:,}'.format(amount)
            return amount


# Creating GUI
class Main(tk.Tk):

    def __init__(self, converter):
        tk.Tk.__init__(self)
        self.title('Cakahal Currency cal')
        self.geometry('400x400')
        self.config(bg='#3A3B3C')
        self.CurrencyConverter = converter

        #Creating title label
        self.title_label = Label(self, text='Currency Converter', bg='#000', fg='white', font=('franklin gothic medium', 20), relief='sunken')
        self.title_label.place(x=200, y=35, anchor='center')

        #Creating date label
        ##
        ##

        #create version label
        self.version_label = Label(self, text='GUI_project_v1.0', bg='black', fg='#fff', font=('calibri', 10))
        self.version_label.place(x=400, y=400, anchor='se')

        # create amount label
        self.title_label = Label(self, text='Input Amount', bg='#000', fg='white',
                                 font=('franklin gothic medium', 15))
        self.title_label.place(x=200, y=80, anchor='center')

        #create amount entry box for inputs
        self.amount_entry = Entry(self)
        self.amount_entry.config(width=25)
        self.amount_entry.place(x=200, y=110, anchor='center')

        # creating a label where the currency is "from"
        self.base_currency_label = Label(self, text='Initial Amount', bg='#000', fg='white',
                                 font=('franklin gothic medium', 15))
        self.base_currency_label.place(x=200, y=140, anchor='center')

        # creating a label where the currency is "Destination"
        self.des_currency_label = Label(self, text='Des Currency', bg='#000', fg='white',
                                         font=('franklin gothic medium', 15))
        self.des_currency_label.place(x=200, y=200, anchor='center')

        # creating dropdown menu for the currency
        self.currency_variable1 = StringVar(self)
        self.currency_variable2 = StringVar(self)
        self.currency_variable1.set('NGN')
        self.currency_variable2.set('USD')

        # using a combobox to fatch the dropdown initial currency display
        self.currency_combobox1 = ttk.Combobox(self, width=20, textvariable=self.currency_variable1,
                                               values=list(self.CurrencyConverter.rates.keys()), state='readonly')
        self.currency_combobox1.place(x=200, y=170, anchor='center')

        # combobox=x2 destination currency display
        self.currency_combobox2 = ttk.Combobox(self, width=20, textvariable=self.currency_variable2,
                                               values=list(self.CurrencyConverter.rates.keys()), state='readonly')
        self.currency_combobox2.place(x=200, y=230, anchor='center')

        # creating a button for the conversion
        self.convert_button = Button(self, text='Submit', bg='#52595d', fg='#f4f4f4', command=self.process)
        self.convert_button.place(x=170, y=270, anchor='center')

        # creating a button to clear
        self.clear_button = Button(self, text='Clear', bg='red', fg='#f4f4f4', command=self.clear)
        self.clear_button.place(x=230, y=270, anchor='center')

        # creating for the result
        self.show_result = Label(self, text='', width=40, bg='#52595d', fg='white',
                                 font=('calibri', 12), relief='sunken')
        self.show_result.place(x=200, y=310, anchor='center')

    #creating clear function, to clear the amount field and show result field
    def clear(self):
        clear_entry = self.amount_entry.delete(0, END)
        clear_result = self.show_result.config(text='')
        return clear_entry, clear_result

    def process(self):
        try:
            given_amount = float(self.amount_entry.get())
            given_base_currency = self.currency_variable1.get()
            given_des_currency = self.currency_variable2.get()
            converted_amount = self.CurrencyConverter.convert(given_amount, given_base_currency, given_des_currency)

            # add comma every 3 numbers
            given_amount = '{:,}'.format(given_amount)

            self.show_result.config(text=f'{given_amount} {given_base_currency} = {converted_amount} {given_des_currency}')

            # Creating a waring message box
        except ValueError:
            convert_error = messagebox.showwarning('WARNING!', 'Please Fill the Amount Field (integer only!)')
            return convert_error


if __name__ == '__main__':
    converter = CurrencyConverter('https://api.exchangerate.host/lastest')
    Main(converter)
    mainloop()
