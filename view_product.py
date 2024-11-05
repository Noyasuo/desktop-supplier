import tkinter as tk
from tkinter import ttk

class ViewProductScreen(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master, bg="#d1e7e1")

        # Style Treeview for better visual appearance
        style = ttk.Style()
        style.configure("Treeview", rowheight=50, font=("Arial", 12), background="white", fieldbackground="white")
        style.configure("Treeview.Heading", font=("Arial", 10, "bold"), background="#999", foreground="black")  # Reduced font size

        # Title label
        label = tk.Label(self, text="View Products", font=("Arial", 18, "bold"), bg="#d1e7e1")
        label.pack(pady=20)

        # Table columns
        columns = ("Product ID", "Product Title", "Product Image", "Product Price", "Product Keyword", "Product Date", "Product Delete", "Product Edit")

        # Create Treeview
        self.tree = ttk.Treeview(self, columns=columns, show="headings", height=8)
        self.tree.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)

        # Define column settings
        self.tree.column("Product ID", width=100, anchor=tk.CENTER)
        self.tree.column("Product Title", width=150, anchor=tk.W)
        self.tree.column("Product Image", width=150, anchor=tk.CENTER)  # Product image column (left blank)
        self.tree.column("Product Price", width=120, anchor=tk.CENTER)
        self.tree.column("Product Keyword", width=150, anchor=tk.CENTER)
        self.tree.column("Product Date", width=180, anchor=tk.CENTER)
        self.tree.column("Product Delete", width=100, anchor=tk.CENTER)
        self.tree.column("Product Edit", width=100, anchor=tk.CENTER)

        # Define column headers
        for col in columns:
            self.tree.heading(col, text=col)

        # Product data (without images)
        products = [
            (1, "Projector", "", "3,599", "Home Theater", "2024-05-08 04:30:24", "Delete", "Edit"),
            (2, "Monitor", "", "2,059", "Office Equipment", "2024-04-21 04:30:24", "Delete", "Edit")
        ]

        # Insert data into treeview with action buttons
        for product in products:
            self.tree.insert("", "end", values=product)

        # Scrollbar
        scrollbar = ttk.Scrollbar(self, orient=tk.VERTICAL, command=self.tree.yview)
        self.tree.configure(yscrollcommand=scrollbar.set)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# Test the ViewProductScreen
if __name__ == "__main__":
    root = tk.Tk()
    root.title("View Products")
    root.geometry("1000x600")
    view_product_screen = ViewProductScreen(master=root)
    view_product_screen.pack(fill=tk.BOTH, expand=True)
    root.mainloop()
