import tkinter as tk
from tkinter import ttk

class RefundScreen(tk.Frame):
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
        label = tk.Label(self, text="Refunds", font=("Arial", 18), bg="#f5f5f5")
        label.pack(pady=20)

        # Create a frame for the table
        table_frame = tk.Frame(self, bg="#f5f5f5")
        table_frame.pack(fill="both", expand=True, padx=20, pady=20)

        # Table (Treeview widget) with custom style
        self.table = ttk.Treeview(
            table_frame,
            style="Custom.Treeview",
            columns=("order_no", "name", "email", "invoice_no", "product_title", "product_qty",
                     "order_date", "total_amount", "status", "refund_process"),
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
        self.table.heading("refund_process", text="Refund Process")

        # Set column widths
        self.table.column("order_no", width=100, anchor="center")
        self.table.column("name", width=150)
        self.table.column("email", width=200)
        self.table.column("invoice_no", width=150)
        self.table.column("product_title", width=150)
        self.table.column("product_qty", width=100, anchor="center")
        self.table.column("order_date", width=120)
        self.table.column("total_amount", width=120, anchor="center")
        self.table.column("status", width=100)
        self.table.column("refund_process", width=120)

        # Add sample data to the table
        self.populate_table()

        # Add vertical scrollbar for the table
        scrollbar = ttk.Scrollbar(table_frame, orient="vertical", command=self.table.yview)
        self.table.configure(yscroll=scrollbar.set)
        scrollbar.pack(side="right", fill="y")

        # Pack the table into the frame
        self.table.pack(fill="both", expand=True)

        # Action Buttons
        button_frame = tk.Frame(self, bg="#f5f5f5")
        button_frame.pack(fill="x", padx=20, pady=10)

        # Accept Refund Button
        self.accept_button = tk.Button(button_frame, text="Accept Refund", width=20, command=self.accept_refund)
        self.accept_button.pack(side="left", padx=10)

        # Decline Refund Button
        self.decline_button = tk.Button(button_frame, text="Decline Refund", width=20, command=self.decline_refund)
        self.decline_button.pack(side="left", padx=10)

    def populate_table(self):
        """Populates the table with sample refund data."""
        sample_refunds = [
            {
                "order_no": 1,
                "name": "John Doe",
                "email": "john@example.com",
                "invoice_no": "INV12345",
                "product_title": "Laptop",
                "product_qty": 1,
                "order_date": "2024-10-01",
                "total_amount": "$1000",
                "status": "Refunded",
                "refund_process": "Completed",
            },
            {
                "order_no": 2,
                "name": "Jane Smith",
                "email": "jane@example.com",
                "invoice_no": "INV12346",
                "product_title": "Smartphone",
                "product_qty": 2,
                "order_date": "2024-10-02",
                "total_amount": "$1200",
                "status": "Pending",
                "refund_process": "Pending",
            },
            {
                "order_no": 3,
                "name": "Alice Johnson",
                "email": "alice@example.com",
                "invoice_no": "INV12347",
                "product_title": "Tablet",
                "product_qty": 1,
                "order_date": "2024-10-03",
                "total_amount": "$300",
                "status": "Refunded",
                "refund_process": "Completed",
            },
        ]

        for refund in sample_refunds:
            self.table.insert("", "end", values=(
                refund["order_no"],
                refund["name"],
                refund["email"],
                refund["invoice_no"],
                refund["product_title"],
                refund["product_qty"],
                refund["order_date"],
                refund["total_amount"],
                refund["status"],
                refund["refund_process"]
            ))

    def accept_refund(self):
        """Handle the action of accepting a refund."""
        selected_item = self.table.selection()
        if selected_item:
            refund = self.table.item(selected_item)["values"]
            # Here you can add your logic to accept the refund
            print(f"Refund accepted for Order No: {refund[0]}")
            # Example: Update the status to 'Refunded'
            self.table.item(selected_item, values=(refund[0], refund[1], refund[2], refund[3], refund[4], 
                                                   refund[5], refund[6], refund[7], "Refunded", refund[9]))
        else:
            print("No row selected")

    def decline_refund(self):
        """Handle the action of declining a refund."""
        selected_item = self.table.selection()
        if selected_item:
            refund = self.table.item(selected_item)["values"]
            # Here you can add your logic to decline the refund
            print(f"Refund declined for Order No: {refund[0]}")
            # Example: Update the status to 'Declined'
            self.table.item(selected_item, values=(refund[0], refund[1], refund[2], refund[3], refund[4], 
                                                   refund[5], refund[6], refund[7], "Declined", refund[9]))
        else:
            print("No row selected")

# Example usage
if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("1200x500")  # Set window size to fit desktop screen
    RefundScreen(root).pack(fill=tk.BOTH, expand=True)
    root.mainloop()
