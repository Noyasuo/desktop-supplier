import tkinter as tk
from tkinter import ttk, filedialog

class InsertProductScreen(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master, bg="lightgrey")
        self.configure(bg="lightgrey")

        # Create the card frame with padding to move it down a bit
        card_frame = tk.Frame(self, bg="white", padx=20, pady=20, relief="raised", borderwidth=2)
        card_frame.pack(padx=20, pady=(40, 20))  # Add more space at the top to move the card down

        # Title for the Insert Product screen inside the card
        tk.Label(card_frame, text="Insert Product", font=("Arial", 18, "bold"), bg="white").grid(row=0, column=0, columnspan=2, pady=10)

        # Product Title
        self.add_label_and_entry(card_frame, "Product Title:", 1)

        # Categories (Dropdown)
        self.add_label_and_dropdown(card_frame, "Categories:", 2)

        # Product Image field (Only Product Image 1 remains)
        self.add_image_field(card_frame, "Product Image:", 3)

        # Product Price, Keyword, and Description
        self.add_label_and_entry(card_frame, "Product Price:", 4)
        self.add_label_and_entry(card_frame, "Product Keyword:", 5)
        self.add_label_and_entry(card_frame, "Product:", 6)

        # Description box
        description_label = tk.Label(card_frame, text="Description:", font=("Arial", 14), bg="white", anchor='w')
        description_label.grid(row=7, column=0, padx=10, pady=5, sticky='e')
        description_box = tk.Text(card_frame, height=4, width=30)
        description_box.grid(row=7, column=1, padx=10, pady=5)

        # Submit button
        submit_button = tk.Button(card_frame, text="Insert Product", command=self.submit_product)
        submit_button.grid(row=8, column=0, columnspan=2, pady=20)

    def add_label_and_entry(self, frame, label_text, row):
        """Helper method to add a label and entry field."""
        label = tk.Label(frame, text=label_text, font=("Arial", 14), bg="white", anchor='w')
        label.grid(row=row, column=0, padx=10, pady=5, sticky='e')
        entry = tk.Entry(frame, width=30)
        entry.grid(row=row, column=1, padx=10, pady=5)

    def add_label_and_dropdown(self, frame, label_text, row):
        """Helper method to add a label and dropdown with a placeholder text."""
        label = tk.Label(frame, text=label_text, font=("Arial", 14), bg="white", anchor='w')
        label.grid(row=row, column=0, padx=10, pady=5, sticky='e')
        
        # Create dropdown with actual categories
        dropdown = ttk.Combobox(frame, values=["Electronics supply", "Cleaning supply", "Office supply"], state="normal")
        dropdown.set("Select categories")  # Set the default placeholder text
        dropdown.grid(row=row, column=1, padx=10, pady=5)

        # Bind event to reset placeholder text when the user interacts
        dropdown.bind("<FocusIn>", lambda e: self.clear_placeholder(dropdown))
        dropdown.bind("<FocusOut>", lambda e: self.set_placeholder(dropdown))

    def clear_placeholder(self, dropdown):
        """Clear the placeholder text when the dropdown is focused."""
        if dropdown.get() == "Select categories":
            dropdown.set("")

    def set_placeholder(self, dropdown):
        """Restore placeholder text if the dropdown is empty."""
        if dropdown.get() == "":
            dropdown.set("Select categories")

    def add_image_field(self, frame, label_text, row):
        """Add a label and 'choose file' button for image selection."""
        image_label = tk.Label(frame, text=label_text, font=("Arial", 14), bg="white", anchor='w')
        image_label.grid(row=row, column=0, padx=10, pady=5, sticky='e')
        choose_button = tk.Button(frame, text="no file chosen", command=lambda: self.choose_file(choose_button), width=25)
        choose_button.grid(row=row, column=1, padx=10, pady=5)

    def choose_file(self, button):
        """Open a file dialog to choose an image and update the button text."""
        file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg;*.png;*.jpeg")])
        if file_path:
            button.config(text=file_path.split("/")[-1])  # Display only the file name

    def submit_product(self):
        """Handle product submission logic."""
        print("Product submitted!")

# Example of how to run this in a Tkinter window
if __name__ == "__main__":
    root = tk.Tk()
    root.title("Insert Product Screen")
    root.geometry("500x600")  # Adjust window size as needed
    app = InsertProductScreen(master=root)
    app.pack(fill="both", expand=True)
    root.mainloop()
