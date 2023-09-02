import random
import string
import customtkinter as ctk
from tkinter import messagebox


class PasswordGenerator(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Password Generator")
        self.geometry("200x200")

        # Create the password entry field
        self.password_entry = ctk.CTkEntry(self)
        self.password_entry.pack(padx=20, pady=10)

        # Create the generate password button
        self.generate_password_button = ctk.CTkButton(self, text="Generate Password",
                                                      command=self.generate_password)
        self.generate_password_button.pack(padx=20, pady=10)

        # Create the show password button
        self.show_password_button = ctk.CTkButton(self, text="Show Password",
                                                  command=self.show_password)
        self.show_password_button.pack(padx=20, pady=10)

    def generate_password(self):
        # Generate a random password
        password = "".join(random.choice(string.ascii_lowercase +
                                         string.ascii_uppercase +
                                         string.digits + string.punctuation)
                           for _ in range(12))

        # Set the password in the entry field
        self.password_entry.delete(0, ctk.END)
        self.password_entry.insert(0, password)

    def show_password(self):
        # Get the password from the entry field
        password = self.password_entry.get()

        # Display the password in a messagebox
        messagebox.showinfo("The Password is:", password)

# if __name__ == "__main__":
#     password_generator = PasswordGenerator()
#     password_generator.mainloop()
