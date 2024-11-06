import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class ViewPaymentScreen(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master, bg="#f5f5f5")
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
        label = tk.Label(self, text="View Payments", font=("Arial", 18), bg="#f5f5f5")
        label.pack(pady=20)

        # Create a frame for the table
        table_frame = tk.Frame(self, bg="#f5f5f5")
        table_frame.pack(fill="both", expand=True, padx=20, pady=20)

        # Table (Treeview widget) with custom style
        self.table = ttk.Treeview(
            table_frame,
            style="Custom.Treeview",
            columns=("payment_no", "invoice_no", "total_amount", "payment_method", "reference"),
            show="headings"
        )

        # Define headings and column widths
        self.table.heading("payment_no", text="Payment No.")
        self.table.heading("invoice_no", text="Invoice No.")
        self.table.heading("total_amount", text="Total Amount")
        self.table.heading("payment_method", text="Payment Method")
        self.table.heading("reference", text="Reference")

        # Set column widths
        self.table.column("payment_no", width=100, anchor="center")
        self.table.column("invoice_no", width=150)
        self.table.column("total_amount", width=120, anchor="center")
        self.table.column("payment_method", width=150)
        self.table.column("reference", width=120)

        # Add sample data to the table
        self.populate_table()

        # Add vertical scrollbar for the table
        scrollbar = ttk.Scrollbar(table_frame, orient="vertical", command=self.table.yview)
        self.table.configure(yscroll=scrollbar.set)
        scrollbar.pack(side="right", fill="y")

        # Pack the table into the frame
        self.table.pack(fill="both", expand=True)

        # Delete Payment Button
        self.delete_button = tk.Button(self, text="Delete Payment", command=self.delete_payment)
        self.delete_button.pack(pady=10)

    def populate_table(self):
        """Populates the table with sample payment data."""
        sample_payments = [
            {
                "payment_no": 1,
                "invoice_no": "INV12345",
                "total_amount": "$1000",
                "payment_method": "Credit Card",
                "reference": "REF001",
            },
            {
                "payment_no": 2,
                "invoice_no": "INV12346",
                "total_amount": "$1200",
                "payment_method": "PayPal",
                "reference": "REF002",
            },
            {
                "payment_no": 3,
                "invoice_no": "INV12347",
                "total_amount": "$300",
                "payment_method": "Bank Transfer",
                "reference": "REF003",
            },
        ]

        for payment in sample_payments:
            self.table.insert("", "end", values=(
                payment["payment_no"],
                payment["invoice_no"],
                payment["total_amount"],
                payment["payment_method"],
                payment["reference"]
            ))

    def delete_payment(self):
        """Delete the selected payment from the table."""
        selected_item = self.table.selection()  # Get the selected row
        if not selected_item:
            messagebox.showwarning("No Selection", "Please select a payment to delete.")
            return

        result = messagebox.askyesno("Delete Payment", "Are you sure you want to delete the selected payment?")
        if result:
            # Remove the selected item from the table
            self.table.delete(selected_item)
            messagebox.showinfo("Payment Deleted", "Selected payment deleted successfully.")

# Example usage
if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("1300x400")  # Set window size
    ViewPaymentScreen(root).pack(fill=tk.BOTH, expand=True)
    root.mainloop()
