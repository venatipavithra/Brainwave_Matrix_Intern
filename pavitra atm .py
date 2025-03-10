import tkinter as tk
from tkinter import messagebox, simpledialog

# User data {PIN: Balance}
users = {1234: 5000}
current_user = None  # Track logged-in user

def authenticate():
    """Verify PIN and show main menu"""
    pin = pin_entry.get()
    if pin.isdigit() and int(pin) in users:
        global current_user
        current_user = int(pin)
        show_main_menu()
    else:
        messagebox.showerror("Error", "Invalid PIN")

def show_main_menu():
    """Display main menu"""
    clear_screen()
    tk.Label(root, text="Main Menu", font=("Arial", 14)).pack(pady=10)
    tk.Button(root, text="Check Balance", command=check_balance).pack(pady=5)
    tk.Button(root, text="Deposit", command=deposit).pack(pady=5)
    tk.Button(root, text="Withdraw", command=withdraw).pack(pady=5)
    tk.Button(root, text="Exit", command=root.quit).pack(pady=10)

def check_balance():
    """Show account balance"""
    messagebox.showinfo("Balance", f"Your balance: ${users[current_user]:.2f}")

def deposit():
    """Deposit money"""
    amount = simple_input("Enter amount to deposit:")
    if amount > 0:
        users[current_user] += amount
        messagebox.showinfo("Success", f"Deposited ${amount:.2f}")
    else:
        messagebox.showerror("Error", "Invalid deposit amount")

def withdraw():
    """Withdraw money"""
    amount = simple_input("Enter amount to withdraw:")
    if 0 < amount <= users[current_user]:
        users[current_user] -= amount
        messagebox.showinfo("Success", f"Withdrew ${amount:.2f}")
    else:
        messagebox.showerror("Error", "Invalid amount or insufficient funds")

def simple_input(prompt):
    """Get user input and validate it as a number"""
    value = simpledialog.askstring("Input", prompt)
    try:
        amount = float(value)
        if amount > 0:
            return amount
    except (ValueError, TypeError):
        pass
    return 0  # Return 0 for invalid input

def clear_screen():
    """Clear window"""
    for widget in root.winfo_children():
        widget.destroy()

# GUI Setup
root = tk.Tk()
root.title("Simple ATM")
root.geometry("300x250")

tk.Label(root, text="Enter PIN:", font=("Arial", 12)).pack(pady=10)
pin_entry = tk.Entry(root, show="*", font=("Arial", 12))
pin_entry.pack(pady=5)
tk.Button(root, text="Login", font=("Arial", 12), command=authenticate).pack(pady=10)

root.mainloop()