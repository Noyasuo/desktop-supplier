import tkinter as tk
from tkinter import ttk, filedialog

class InsertProductScreen(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master, bg="#f5f5f5")

        # Insert Product title
        label = tk.Label(self, text="Insert Product", font=("Arial", 18), bg="#f5f5f5")
        label.pack(pady=20)

        # Frame for Product inputs
        product_frame = tk.Frame(self, bg="#f5f5f5")
        product_frame.pack(pady=10)

        # Product Title and Categories
        self.add_label_and_entry(product_frame, "Product Title:", 0)
        self.add_label_and_dropdown(product_frame, "Categories:", 1)

        # Product Image fields
        self.add_image_field(product_frame, "Product image:", 2)
        self.add_image_field(product_frame, "Product image 2:", 3)
        self.add_image_field(product_frame, "Product image 3:", 4)

        # Product Price, Keyword, and Product inputs
        self.add_label_and_entry(product_frame, "Product Price:", 5)
        self.add_label_and_entry(product_frame, "Product Keyword:", 6)
        self.add_label_and_entry(product_frame, "Product:", 7)

        # Description box
        description_label = tk.Label(product_frame, text="Description:", font=("Arial", 14), bg="#f5f5f5", anchor='w')
        description_label.grid(row=8, column=0, padx=10, pady=5, sticky='e')
        description_box = tk.Text(product_frame, height=4, width=30)
        description_box.grid(row=8, column=1, padx=10, pady=5)

        # Submit button
        submit_button = tk.Button(self, text="Insert Product", command=self.submit_product)
        submit_button.pack(pady=20)

    def add_label_and_entry(self, frame, label_text, row):
        """Helper method to add a label and entry field."""
        label = tk.Label(frame, text=label_text, font=("Arial", 14), bg="#f5f5f5", anchor='w')
        label.grid(row=row, column=0, padx=10, pady=5, sticky='e')
        entry = tk.Entry(frame, width=30)
        entry.grid(row=row, column=1, padx=10, pady=5)

    def add_label_and_dropdown(self, frame, label_text, row):
        """Helper method to add a label and dropdown."""
        label = tk.Label(frame, text=label_text, font=("Arial", 14), bg="#f5f5f5", anchor='w')
        label.grid(row=row, column=0, padx=10, pady=5, sticky='e')
        dropdown = ttk.Combobox(frame, values=["Select Categories", "Category 1", "Category 2"], state="readonly")
        dropdown.current(0)
        dropdown.grid(row=row, column=1, padx=10, pady=5)

    def add_image_field(self, frame, label_text, row):
        """Add a label and 'choose file' button for image selection."""
        image_label = tk.Label(frame, text=label_text, font=("Arial", 14), bg="#f5f5f5", anchor='w')
        image_label.grid(row=row, column=0, padx=10, pady=5, sticky='e')
        choose_button = tk.Button(frame, text="no file chosen", command=lambda: self.choose_file(choose_button), width=25)
        choose_button.grid(row=row, column=1, padx=10, pady=5)

    def choose_file(self, button):
        """Open a file dialog to choose an image and update the button text."""
        file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg;*.png;*.jpeg")])
        if file_path:
            button.config(text=file_path.split("/")[-1])  # Display only the file name

    def submit_product(self):
        print("Product submitted!")
