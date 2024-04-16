import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from tkcalendar import Calendar

# Function to handle login button click
def login():
    username = username_entry.get()
    password = password_entry.get()

    # Check if username and password are correct (dummy validation)
    if username == "admin" and password == "password":
        messagebox.showinfo("Login Successful", "Welcome, " + username + "!")
        # You can add code here to navigate to the main application window or perform other actions
    else:
        messagebox.showerror("Login Failed", "Invalid username or password")

# Function to handle register button click
def register():
    # Create registration window
    register_window = tk.Toplevel(root)
    register_window.title("Register")
    register_window.geometry("500x400")

    # Function to handle registration submission
    def submit_registration():
        # Retrieve values from entry fields
        first_name = first_name_entry.get()
        last_name = last_name_entry.get()
        username = username_entry.get()
        password = password_entry.get()
        confirm_password = confirm_password_entry.get()
        id_number = id_number_entry.get()
        phone_number = phone_number_entry.get()
        dob = dob_calendar.get_date()
        gender = gender_entry.get()

        # Perform registration validation
        if password != confirm_password:
            messagebox.showerror("Registration Error", "Passwords do not match.")
        else:
            # Show successful registration message
            messagebox.showinfo("Registration Successful", "Registration successful for " + username + "!")
            # Close the registration window
            register_window.destroy()

    # Create labels and entry fields for registration
    first_name_label = tk.Label(register_window, text="First Name:")
    first_name_label.grid(row=0, column=0, padx=10, pady=5, sticky="e")
    first_name_entry = tk.Entry(register_window)
    first_name_entry.grid(row=0, column=1, padx=10, pady=5, sticky="we")

    last_name_label = tk.Label(register_window, text="Last Name:")
    last_name_label.grid(row=1, column=0, padx=10, pady=5, sticky="e")
    last_name_entry = tk.Entry(register_window)
    last_name_entry.grid(row=1, column=1, padx=10, pady=5, sticky="we")

    username_label = tk.Label(register_window, text="Username:")
    username_label.grid(row=2, column=0, padx=10, pady=5, sticky="e")
    username_entry = tk.Entry(register_window)
    username_entry.grid(row=2, column=1, padx=10, pady=5, sticky="we")

    password_label = tk.Label(register_window, text="Password:")
    password_label.grid(row=3, column=0, padx=10, pady=5, sticky="e")
    password_entry = tk.Entry(register_window, show="*")
    password_entry.grid(row=3, column=1, padx=10, pady=5, sticky="we")

    confirm_password_label = tk.Label(register_window, text="Confirm Password:")
    confirm_password_label.grid(row=4, column=0, padx=10, pady=5, sticky="e")
    confirm_password_entry = tk.Entry(register_window, show="*")
    confirm_password_entry.grid(row=4, column=1, padx=10, pady=5, sticky="we")

    id_number_label = tk.Label(register_window, text="ID Number:")
    id_number_label.grid(row=5, column=0, padx=10, pady=5, sticky="e")
    id_number_entry = tk.Entry(register_window)
    id_number_entry.grid(row=5, column=1, padx=10, pady=5, sticky="we")

    phone_number_label = tk.Label(register_window, text="Phone Number:")
    phone_number_label.grid(row=6, column=0, padx=10, pady=5, sticky="e")
    phone_number_entry = tk.Entry(register_window)
    phone_number_entry.grid(row=6, column=1, padx=10, pady=5, sticky="we")

    dob_label = tk.Label(register_window, text="Date of Birth:")
    dob_label.grid(row=7, column=0, padx=10, pady=5, sticky="e")
    dob_calendar = Calendar(register_window, selectmode="day", date_pattern="yyyy-mm-dd")
    dob_calendar.grid(row=7, column=1, padx=10, pady=5, sticky="we")

    gender_label = tk.Label(register_window, text="Gender:")
    gender_label.grid(row=8, column=0, padx=10, pady=5, sticky="e")
    gender_entry = ttk.Combobox(register_window, values=["Male", "Female"])
    gender_entry.grid(row=8, column=1, padx=10, pady=5, sticky="we")

    # Create submit and cancel buttons
    submit_button = tk.Button(register_window, text="Submit", command=submit_registration)
    submit_button.grid(row=9, column=0, padx=10, pady=10, sticky="we")

    cancel_button = tk.Button(register_window, text="Cancel", command=register_window.destroy)
    cancel_button.grid(row=9, column=1, padx=10, pady=10, sticky="we")


# Create main Tkinter window
root = tk.Tk()
root.title("Login or Register")

# Set window size and position
window_width = 400
window_height = 250
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x_coordinate = (screen_width / 2) - (window_width / 2)
y_coordinate = (screen_height / 2) - (window_height / 2)
root.geometry("%dx%d+%d+%d" % (window_width, window_height, x_coordinate, y_coordinate))

# Create username label and entry field
username_label = tk.Label(root, text="Username:")
username_label.grid(row=0, column=0, padx=10, pady=5, sticky="e")
username_entry = tk.Entry(root)
username_entry.grid(row=0, column=1, padx=10, pady=5, sticky="we")

# Create password label and entry field
password_label = tk.Label(root, text="Password:")
password_label.grid(row=1, column=0, padx=10, pady=5, sticky="e")
password_entry = tk.Entry(root, show="*")
password_entry.grid(row=1, column=1, padx=10, pady=5, sticky="we")

# Create login button
login_button = tk.Button(root, text="Login", command=login, width=10)
login_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10, sticky="e")

# Create register button
register_button = tk.Button(root, text="Register", command=register, width=10)
register_button.grid(row=3, column=0, columnspan=2, padx=10, pady=10, sticky="e")

# Run the Tkinter event loop
root.mainloop()
