import string
import re
import requests
import hashlib
import tkinter as tk
from customtkinter import CTkButton
from tkinter import messagebox
import pyperclip
import random

class PasswordApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Security Checker & Generator")
        self.root.geometry("400x320")

        self.entry_label = tk.Label(root, text="Enter password to check:", font=("Helvetica", 12, "bold"))
        self.entry_label.pack(pady=10)

        self.entry = tk.Entry(root, width=40)
        self.entry.pack(pady=25)

        self.check_button = CTkButton(root, text="Check Password", command=self.check_password)
        self.check_button.pack(pady=10)

        self.generate_button = CTkButton(root, text="Generate Secure Password", command=self.generate_password)
        self.generate_button.pack(pady=10)

        self.copy_button = CTkButton(root, text="Copy to Clipboard", command=self.copy_to_clipboard)
        self.copy_button.pack(pady=40)

    def check_password(self):
        password = self.entry.get()

        if len(password) < 12:
            return messagebox.showinfo("Password Strength", "Password is too short, it should be at least 12 characters.")
        
        elif not re.search("[a-z]", password):
            return messagebox.showinfo("Password Strength", "Password should have at least one lowercase character.")
        
        elif not re.search("[A-Z]", password):
            return messagebox.showinfo("Password Strength", "Password should have at least one uppercase character.")
        
        elif not re.search("[0-9]", password):
            return messagebox.showinfo("Password Strength", "Password should have at least one numeral.")
        
        elif not re.search("[!@#$%:+-_/£^&*()=|]", password):
            return messagebox.showinfo("Password Strength", "Password should have at least one of these special characters: _@$")

        elif self.pwned_password(password):
            return messagebox.showinfo("Password Strength", "This password has been exposed in a data breach and is not considered secure.")
        
        else:
            return messagebox.showinfo("Password Strength", "Your password seems strong!")

    def pwned_password(self, password):
        sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
        first5_char, tail = sha1password[:5], sha1password[5:]
        response = requests.get('https://api.pwnedpasswords.com/range/' + first5_char)
        hashes = (line.split(':') for line in response.text.splitlines())
        return any(h for h, count in hashes if h == tail)

    def generate_password(self):
        # Generate random password
        password_characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(password_characters) for i in range(18))
        
        # Ensure at least one special character and one digit
        if not any(char in string.punctuation for char in password):
            password += random.choice(string.punctuation)
        if not any(char in string.digits for char in password):
            password += random.choice(string.digits)
    
        # Ensure the password is not in the leaked passwords list
        while self.pwned_password(password):
            password = ''.join(random.choice(password_characters) for i in range(18))
            if not any(char in string.punctuation for char in password):
                password += random.choice(string.punctuation)
            if not any(char in string.digits for char in password):
                password += random.choice(string.digits)
    
        self.entry.delete(0, tk.END)
        self.entry.insert(0, password)




    def copy_to_clipboard(self):
        password = self.entry.get()
        pyperclip.copy(password)


root = tk.Tk()
app = PasswordApp(root)
root.mainloop()
