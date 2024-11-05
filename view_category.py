import tkinter as tk
from tkinter import ttk

class ViewCategoryScreen(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.configure(bg="#f5f5f5")

        # Add View Categories heading
        tk.Label(self, text="View Categories", font=("Arial", 18)).pack(pady=10)

        # Create a treeview for displaying categories
        self.category_tree = ttk.Treeview(self, columns=("Category ID", "Category Title", "Category Description", "Edit", "Delete"), show='headings')
        self.category_tree.pack(pady=20)

        # Define headings
        self.category_tree.heading("Category ID", text="Category ID")
        self.category_tree.heading("Category Title", text="Category Title")
        self.category_tree.heading("Category Description", text="Category Description")
        self.category_tree.heading("Edit", text="Edit Category")
        self.category_tree.heading("Delete", text="Delete Category")

        # Define column widths
        self.category_tree.column("Category ID", width=100)
        self.category_tree.column("Category Title", width=150)
        self.category_tree.column("Category Description", width=200)
        self.category_tree.column("Edit", width=100)
        self.category_tree.column("Delete", width=100)

        # Sample data (replace this with dynamic content)
        sample_categories = [
            (1, "Electronics", "Devices and gadgets"),
            (2, "Furniture", "Home furnishings"),
            (3, "Clothing", "Apparel and accessories"),
            (4, "Books", "Literature and novels"),
            (5, "Beauty Products", "Cosmetics and skincare")
        ]

        # Insert sample data into the treeview
        for category in sample_categories:
            self.category_tree.insert("", tk.END, values=category)

# Example usage if running this file directly
if __name__ == "__main__":
    root = tk.Tk()
    root.title("View Categories")
    root.geometry("600x400")
    view_category_screen = ViewCategoryScreen(master=root)
    view_category_screen.pack(fill=tk.BOTH, expand=True)
    root.mainloop()
