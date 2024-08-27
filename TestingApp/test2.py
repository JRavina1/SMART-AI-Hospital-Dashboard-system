import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import os
import pandas as pd

# Creating root window
root = tk.Tk()

# Root window title and dimensions
root.title("SMART AI Hospital- Data Files")
root.geometry('650x520')

# Admin credentials
ADMIN_USERNAME = "Admin"
ADMIN_PASSWORD = "Hospital123"

# Path to the Image folder
image_folder = os.path.join(os.path.dirname(__file__), "Image2")

# Path to the Data folder
data_folder = os.path.join(os.path.dirname(__file__), "Data")

# Class for Dashboard
class Dashboard:
    def __init__(self, master):
        self.master = master
        
        # Create frame for logo
        self.logo_frame = tk.Frame(self.master)
        self.logo_frame.pack(pady=20)
        
        # Add Hospital logo
        image = Image.open("logo.jpeg")
        image = image.resize((200, 200), Image.ANTIALIAS)
        self.logo_img = ImageTk.PhotoImage(image)
        self.logo_label = tk.Label(self.logo_frame, image=self.logo_img)
        self.logo_label.pack()

        # Created login frame and adding background color 
        self.login_frame = tk.Frame(self.master, background="lightblue") 
        self.login_frame.pack(pady=20)
        
        # Create username label and entry
        self.username_label = tk.Label(self.login_frame, text="Admin Login: ")
        self.username_label.grid(row=0, column=0, padx=15, pady=15)
        self.username_entry = tk.Entry(self.login_frame)
        self.username_entry.grid(row=0, column=1, padx=15, pady=15)

        # Create password label and entry
        self.password_label = tk.Label(self.login_frame, text="Password:")
        self.password_label.grid(row=1, column=0, padx=10, pady=5)
        self.password_entry = tk.Entry(self.login_frame, show="*")
        self.password_entry.grid(row=1, column=1, padx=10, pady=5)

        # Create login button
        self.login_button = tk.Button(self.login_frame, text="Login", command=self.login)
        self.login_button.grid(row=2, columnspan=2, padx=10, pady=5)

    def login(self):
        # Retrieve entered username and password
        username = self.username_entry.get()
        password = self.password_entry.get()

        # Check if the entered credentials match the admin credentials
        if username == ADMIN_USERNAME and password == ADMIN_PASSWORD:
            # If correct, show the dashboard
            self.show_dashboard()
        else:
            # If incorrect, show an error message
            messagebox.showerror("Error", "Invalid username or password")

    def show_dashboard(self):
        # Destroy the login frame
        self.login_frame.destroy()

        # Create dashboard frame
        self.dashboard_frame = tk.Frame(self.master)
        self.dashboard_frame.pack(pady=20)

        # Add buttons
        self.upload_button = tk.Button(self.dashboard_frame, text="Upload")
        self.upload_button.pack()

        self.download_button = tk.Button(self.dashboard_frame, text="Download")
        self.download_button.pack()

        self.delete_button = tk.Button(self.dashboard_frame, text="Delete")
        self.delete_button.pack()

        # Create logout button
        self.logout_button = tk.Button(self.dashboard_frame, text="Logout", command=self.logout)
        self.logout_button.pack()
        
        # Create frame for file data display
        self.file_frame = tk.Frame(self.master)
        self.file_frame.pack(side="right", fill="both", expand=True)

        # Create list of file data with images
        files = [
            ("Staff", "medical-team.png", "staff_data.xlsx"), 
            ("Patient", "hospitalization.png", "patient_data.xlsx"),
            ("Department", "Dept.png", "Dept_data.xlsx"),
            ("Hospital", "Hospital.png", "Hospital_data.xlsx"),
            ("AI Algorithm", "AIhospital.png", "AI_data.xlsx"),
            ("Wards", "wards.png", "Wards_data.xlsx"),
            ("Doctor", "doctor.png", "Doctor_data.xlsx"),
            ("Pharmacy", "pharmacy.png", "Pharmacy_data.xlsx"),
            ("Prescription", "prescription.png", "Prescription_data.xlsx"),
            ("Appointment", "schedule.png", "Appointment_data.xlsx"),
            ("Invoice", "invoice.png", "invoice_data.xlsx")
        ]
        for file_name, image_filename, excel_filename in files:
            image_path = os.path.join(image_folder, image_filename)
            icon = Image.open(image_path)
            icon = icon.resize((50, 50), Image.ANTIALIAS)
            icon_img = ImageTk.PhotoImage(icon)
            button = tk.Button(self.file_frame, image=icon_img, text=file_name, compound="top", command=lambda excel_file=excel_filename: self.open_excel_file(excel_file))
            button.image = icon_img
            button.pack(side="left", padx=10, pady=10)
        
    def open_excel_file(self, excel_file):
        excel_path = os.path.join(data_folder, excel_file)
        if os.path.exists(excel_path):
            # Read the Excel file using pandas
            df = pd.read_excel(excel_path)
            # Display the data in a table format
            top = tk.Toplevel(self.master)
            table = ttk.Treeview(top)
            table["columns"] = tuple(df.columns)
            table["show"] = "headings"
            for col in df.columns:
                table.heading(col, text=col)
            for row in df.itertuples():
                table.insert("", "end", values=row[1:])
            table.pack(expand=True, fill="both")
        else:
            messagebox.showerror("Error", "Excel file not found.")

    def logout(self):
        # Destroy the dashboard frame
        self.dashboard_frame.destroy()

        # Recreate the login frame
        self.login_frame = tk.Frame(self.master, background="lightblue") 
        self.login_frame.pack(pady=20)
        
        # Create username label and entry
        self.username_label = tk.Label(self.login_frame, text="Admin Login: ")
        self.username_label.grid(row=0, column=0, padx=15, pady=15)
        self.username_entry = tk.Entry(self.login_frame)
        self.username_entry.grid(row=0, column=1, padx=15, pady=15)

        # Create password label and entry
        self.password_label = tk.Label(self.login_frame, text="Password:")
        self.password_label.grid(row=1, column=0, padx=10, pady=5)
        self.password_entry = tk.Entry(self.login_frame, show="*")
        self.password_entry.grid(row=1, column=1, padx=10, pady=5)

        # Create login button
        self.login_button = tk.Button(self.login_frame, text="Login", command=self.login)
        self.login_button.grid(row=2, columnspan=2, padx=10, pady=5)

# Create an instance of the Dashboard class
app = Dashboard(root)

# Run the main event loop
root.mainloop()
