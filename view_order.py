import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class ViewOrderScreen(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master, bg="lightgrey")
        self.master = master
        self.create_style()  # Apply custom style for row selection color
        self.create_widgets()

    def create_style(self):
        """Create a custom style to change the selected row color."""
        style = ttk.Style()
        style.theme_use("default")
        
        # Configure Treeview selection color
        style.map("Custom.Treeview",
                  background=[("selected", "#397D49")],  # Selected row color
                  foreground=[("selected", "white")])    # Selected row text color

    def create_widgets(self):
        # Title label
        tk.Label(self, text="View Orders", font=("Arial", 16), bg="lightgrey").pack(pady=20)

        # Create a frame for the table
        table_frame = tk.Frame(self, bg="lightgrey")
        table_frame.pack(fill="both", expand=True, padx=20, pady=20)

        # Table (Treeview widget) with custom style
        self.table = ttk.Treeview(
            table_frame,
            style="Custom.Treeview",
            columns=("order_no", "name", "email", "invoice_no", "product_title", "product_qty", "order_date", "total_amount", "status"),
            show="headings"
        )

        # Define headings and column widths
        self.table.heading("order_no", text="Order No.")
        self.table.heading("name", text="Name")
        self.table.heading("email", text="Email")
        self.table.heading("invoice_no", text="Invoice No.")
        self.table.heading("product_title", text="Product Title")
        self.table.heading("product_qty", text="Product Qty")
        self.table.heading("order_date", text="Order Date")
        self.table.heading("total_amount", text="Total Amount")
        self.table.heading("status", text="Status")

        # Set column widths
        self.table.column("order_no", width=100, anchor="center")
        self.table.column("name", width=150)
        self.table.column("email", width=180)
        self.table.column("invoice_no", width=120)
        self.table.column("product_title", width=150)
        self.table.column("product_qty", width=100, anchor="center")
        self.table.column("order_date", width=120)
        self.table.column("total_amount", width=100, anchor="center")
        self.table.column("status", width=100, anchor="center")

        # Add sample data to the table
        self.populate_table()

        # Add vertical scrollbar for the table
        scrollbar = ttk.Scrollbar(table_frame, orient="vertical", command=self.table.yview)
        self.table.configure(yscroll=scrollbar.set)
        scrollbar.pack(side="right", fill="y")

        # Pack the table into the frame
        self.table.pack(fill="both", expand=True)

        # Button to edit order status
        self.edit_status_button = tk.Button(self, text="Edit Status", command=self.show_status_dropdown)
        self.edit_status_button.pack(pady=20)

    def populate_table(self):
        """Populates the table with sample data."""
        sample_data = [
            (1, "John Doe", "john@example.com", "INV12345", "Laptop", 1, "2024-10-01", "$1000", "Processing"),
            (2, "Jane Smith", "jane@example.com", "INV12346", "Smartphone", 2, "2024-10-02", "$1200", "Shipped"),
            (3, "Alice Johnson", "alice@example.com", "INV12347", "Tablet", 1, "2024-10-03", "$300", "Delivered"),
        ]

        for row in sample_data:
            self.table.insert("", "end", values=row)

    def show_status_dropdown(self):
        """Show a dropdown to select a new status beside the 'Edit Status' button."""
        selected_item = self.table.selection()  # Get selected item in table

        if not selected_item:
            messagebox.showwarning("No Selection", "Please select an order to edit the status.")
            return

        # Create a new window to display the dropdown for status selection
        self.status_window = tk.Toplevel(self)
        self.status_window.title("Edit Order Status")
        self.status_window.geometry("200x150+{}+{}".format(self.edit_status_button.winfo_x() + self.edit_status_button.winfo_width() + 10, self.edit_status_button.winfo_y()))

        # Dropdown for status selection
        self.status_combobox = ttk.Combobox(self.status_window, values=["Processing", "Shipped", "Delivered"], state="readonly")
        self.status_combobox.set("Select Status")
        self.status_combobox.pack(pady=10)

        # Save button to update the status
        save_button = tk.Button(self.status_window, text="Save", command=lambda: self.update_status(selected_item))
        save_button.pack(pady=10)

    def update_status(self, selected_item):
        """Update the status of the selected order."""
        new_status = self.status_combobox.get()

        if new_status == "Select Status":
            messagebox.showwarning("Invalid Selection", "Please select a valid status.")
            return

        # Update the status in the table
        self.table.item(selected_item, values=(
            self.table.item(selected_item)["values"][0],  # Order No.
            self.table.item(selected_item)["values"][1],  # Name
            self.table.item(selected_item)["values"][2],  # Email
            self.table.item(selected_item)["values"][3],  # Invoice No.
            self.table.item(selected_item)["values"][4],  # Product Title
            self.table.item(selected_item)["values"][5],  # Product Qty
            self.table.item(selected_item)["values"][6],  # Order Date
            self.table.item(selected_item)["values"][7],  # Total Amount
            new_status  # New status
        ))

        # Close the status edit window
        self.status_window.destroy()
        messagebox.showinfo("Status Updated", f"Order status updated to {new_status}.")

# To test the ViewOrderScreen independently, you can create a root window and add it to this script.
if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("800x400")
    app = ViewOrderScreen(master=root)
    app.pack(fill="both", expand=True)
    root.mainloop()
