import tkinter as tk
from tkinter import messagebox

# Initial values
correct_pin = 1010
balance = 10000

# Initialize Tkinter window
root = tk.Tk()
root.title("ATM Machine Interface")
root.geometry("400x450")
root.resizable(False, False)

# Global Variables
user_pin = tk.StringVar()
amount_var = tk.StringVar()
operation = None

# Balance (we'll modify this inside functions)
current_balance = [balance]  # Using list to allow mutable integer

# -------------------- Functions --------------------

def verify_pin():
    try:
        entered_pin = int(user_pin.get())
        if entered_pin == correct_pin:
            pin_frame.pack_forget()
            main_menu()
        else:
            messagebox.showerror("Incorrect PIN", "The PIN you entered is incorrect.")
    except:
        messagebox.showerror("Invalid", "Please enter numbers only.")

def main_menu():
    menu_frame.pack(pady=20)

def check_balance():
    messagebox.showinfo("Balance", f"Your current balance is ₹{current_balance[0]}")

def do_withdraw():
    try:
        amt = int(amount_var.get())
        if amt > current_balance[0]:
            messagebox.showerror("Error", "Insufficient Balance")
        else:
            current_balance[0] -= amt
            messagebox.showinfo("Success", f"₹{amt} withdrawn.\nNew Balance: ₹{current_balance[0]}")
            amount_var.set("")
    except:
        messagebox.showerror("Error", "Enter a valid amount")

def do_deposit():
    try:
        amt = int(amount_var.get())
        current_balance[0] += amt
        messagebox.showinfo("Success", f"₹{amt} deposited.\nNew Balance: ₹{current_balance[0]}")
        amount_var.set("")
    except:
        messagebox.showerror("Error", "Enter a valid amount")

def exit_app():
    root.destroy()

# -------------------- PIN Entry Frame --------------------

pin_frame = tk.Frame(root)
tk.Label(pin_frame, text="Enter your ATM PIN", font=("Arial", 14)).pack(pady=10)
tk.Entry(pin_frame, textvariable=user_pin, show="*", width=20, font=("Arial", 12)).pack(pady=5)
tk.Button(pin_frame, text="Submit", command=verify_pin, width=15, bg="green", fg="white").pack(pady=10)
pin_frame.pack(pady=50)

# -------------------- Main Menu Frame --------------------

menu_frame = tk.Frame(root)

tk.Label(menu_frame, text="ATM Machine Interface", font=("Arial", 16, "bold")).pack(pady=10)

tk.Button(menu_frame, text="Check Balance", command=check_balance, width=20).pack(pady=5)

tk.Label(menu_frame, text="Enter Amount", font=("Arial", 12)).pack()
tk.Entry(menu_frame, textvariable=amount_var, width=20).pack(pady=5)

tk.Button(menu_frame, text="Withdraw", command=do_withdraw, width=20).pack(pady=5)
tk.Button(menu_frame, text="Deposit", command=do_deposit, width=20).pack(pady=5)
tk.Button(menu_frame, text="Exit", command=exit_app, width=20, bg="red", fg="white").pack(pady=10)

# -------------------- Run the App --------------------
root.mainloop()
