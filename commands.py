from tkinter import messagebox
import csv

def check_balance(account_number):
    # open the csv file
    csv_file = open(file="accounts.csv", mode ="r")
    # read the csv content
    accounts = csv.DictReader(csv_file)
    for account in accounts:
        if account_number == account["account_number"]:
            messagebox.showinfo(
                title="Check Balance",
                message=f"Your balance is {account['balance']}"
            )
        return
    
    messagebox.showerror(
        title="Check Balance", message=f"Account number {account_number} does not exist"
    )