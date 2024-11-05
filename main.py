import tkinter as tk
from PIL import Image, ImageTk
from login import LoginScreen
from dashboard import DashboardScreen

class Header(tk.Frame):
    """Header class to create a reusable header with an image on the left and text beside it."""
    def __init__(self, master=None):
        super().__init__(master, bg="#397D49")  # Dark green background color
        self.pack(side="top", fill="x")  # Pack the header to the top

        # Prevent the header from resizing to fit its content
        self.pack_propagate(False)

        # Set the desired height by configuring the header frame
        self.config(height=80)  # Change this value to increase or decrease height

        # Load and display the logo image
        try:
            self.logo_image = Image.open("assets/logo.png")  # Use the correct image path for your logo
            self.logo_image = self.logo_image.resize((60, 60), Image.LANCZOS)  # Resize logo to fit the header
            self.logo_photo = ImageTk.PhotoImage(self.logo_image)

            # Create a label to display the logo image
            self.logo_label = tk.Label(self, image=self.logo_photo, bg="#397D49")
            self.logo_label.pack(side="left", padx=10, pady=10)

        except FileNotFoundError:
            print("Error: Logo image file not found. Please check the image path.")

        # Add the "Colegio de Montalban" text to the right of the logo with reduced font size
        self.school_label = tk.Label(self, text="Colegio de Montalban", font=("Arial", 16), bg="#397D49", fg="white")
        self.school_label.pack(side="left", padx=10, pady=10)

        # Initialize user_frame as None
        self.user_frame = None

    def create_user_info(self, username):
        """Create and display the user information box after login."""
        # Create a frame for the user box
        self.user_frame = tk.Frame(self, bg="#FFD700")  # Yellow background for the user box
        self.user_frame.pack(side="right", padx=10)

        # Load and display the user icon image
        try:
            self.user_icon_image = Image.open("assets/user.png")  # Replace with the correct image path
            self.user_icon_image = self.user_icon_image.resize((20, 20), Image.LANCZOS)  # Resize user icon
            self.user_icon_photo = ImageTk.PhotoImage(self.user_icon_image)

            # Create a label to display the user icon image
            self.user_icon_label = tk.Label(self.user_frame, image=self.user_icon_photo, bg="#FFD700")  # Yellow background
            self.user_icon_label.pack(side="left", padx=(5, 2))  # Space between icon and user name

            # Create a user display label for the username
            self.user_box = tk.Label(self.user_frame, text=username, bg="#FFD700", fg="black", font=("Arial", 12), height=2)  # Increased height
            self.user_box.pack(side="left", padx=5)  # Space between icon and name

        except FileNotFoundError:
            print("Error: User icon image file not found. Please check the image path.")

class MainApplication(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Admin Desktop Application")
        self.geometry("800x600")  # Set the initial window size
        self.configure(bg="grey")  # Set background color to grey
        self.state('zoomed')  # Maximize the window but keep the title bar visible

        # Create the Header at the top of the application
        self.header = Header(self)
        self.header.pack(side="top", fill="x")

        # Container for dynamic content below the header
        self.content_frame = tk.Frame(self, bg="grey")
        self.content_frame.pack(expand=True, fill="both")

        # Show the Login Screen initially
        self.show_login_screen()

    def show_login_screen(self):
        """Display the login screen inside the content frame."""
        for widget in self.content_frame.winfo_children():
            widget.destroy()  # Clear previous screens
        login_screen = LoginScreen(self.content_frame, self.on_login_success)
        login_screen.pack(pady=20)  # Center the login screen within the content frame

    def on_login_success(self, username):
        """Callback function after successful login. It updates the header and shows the dashboard."""
        # Clear the content frame and show the dashboard
        for widget in self.content_frame.winfo_children():
            widget.destroy()  # Clear previous screens

        # Create and update the user info in the header
        self.header.create_user_info(username)

        # Display the dashboard
        dashboard_screen = DashboardScreen(self.content_frame)
        dashboard_screen.pack(expand=True, fill="both")

if __name__ == "__main__":
    app = MainApplication()
    app.mainloop()
