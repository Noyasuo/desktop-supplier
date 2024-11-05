import tkinter as tk

class RefundScreen(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master, bg="#f5f5f5")
        label = tk.Label(self, text="Refunds", font=("Arial", 18), bg="#f5f5f5")
        label.pack(pady=20)

        # Table headers
        header_frame = tk.Frame(self, bg="#d9d9d9")
        header_frame.pack(fill=tk.X, padx=10)

        headers = ["Order No.", "Name", "Email", "Invoice No.", "Product Title", "Product Qty", "Order Date", "Total Amount", "Status", "Refund Process"]
        
        for index, header in enumerate(headers):
            tk.Label(header_frame, text=header, bg="#d9d9d9", width=15).grid(row=0, column=index, padx=5, pady=5)

        # Sample refund data for demonstration
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

        # Display refunds in table format
        for refund in sample_refunds:
            row_frame = tk.Frame(self)
            row_frame.pack(fill=tk.X, padx=10, pady=5)

            tk.Label(row_frame, text=refund["order_no"], width=15).grid(row=0, column=0, padx=5)
            tk.Label(row_frame, text=refund["name"], width=15).grid(row=0, column=1, padx=5)
            tk.Label(row_frame, text=refund["email"], width=15).grid(row=0, column=2, padx=5)
            tk.Label(row_frame, text=refund["invoice_no"], width=15).grid(row=0, column=3, padx=5)
            tk.Label(row_frame, text=refund["product_title"], width=15).grid(row=0, column=4, padx=5)
            tk.Label(row_frame, text=refund["product_qty"], width=15).grid(row=0, column=5, padx=5)
            tk.Label(row_frame, text=refund["order_date"], width=15).grid(row=0, column=6, padx=5)
            tk.Label(row_frame, text=refund["total_amount"], width=15).grid(row=0, column=7, padx=5)
            tk.Label(row_frame, text=refund["status"], width=15).grid(row=0, column=8, padx=5)
            tk.Label(row_frame, text=refund["refund_process"], width=15).grid(row=0, column=9, padx=5)

# Example usage
if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("1200x400")  # Set window size to fit desktop screen
    RefundScreen(root).pack(fill=tk.BOTH, expand=True)
    root.mainloop()
