import tkinter as tk

class ViewPaymentScreen(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master, bg="#f5f5f5")
        label = tk.Label(self, text="View Payments", font=("Arial", 18), bg="#f5f5f5")
        label.pack(pady=20)

        # Table headers
        header_frame = tk.Frame(self, bg="#d9d9d9")
        header_frame.pack(fill=tk.X, padx=10)

        headers = ["Payment No.", "Invoice No.", "Total Amount", "Payment Method", "Reference", "Delete Payment"]
        
        for index, header in enumerate(headers):
            tk.Label(header_frame, text=header, bg="#d9d9d9", width=20).grid(row=0, column=index, padx=5, pady=5)

        # Sample payment data for demonstration
        sample_payments = [
            {
                "payment_no": 1,
                "invoice_no": "INV12345",
                "total_amount": "$1000",
                "payment_method": "Credit Card",
                "reference": "REF001",
                "delete": "Yes",
            },
            {
                "payment_no": 2,
                "invoice_no": "INV12346",
                "total_amount": "$1200",
                "payment_method": "PayPal",
                "reference": "REF002",
                "delete": "No",
            },
            {
                "payment_no": 3,
                "invoice_no": "INV12347",
                "total_amount": "$300",
                "payment_method": "Bank Transfer",
                "reference": "REF003",
                "delete": "Yes",
            },
        ]

        # Display payments in table format
        for payment in sample_payments:
            row_frame = tk.Frame(self)
            row_frame.pack(fill=tk.X, padx=10, pady=5)

            tk.Label(row_frame, text=payment["payment_no"], width=20).grid(row=0, column=0, padx=5)
            tk.Label(row_frame, text=payment["invoice_no"], width=20).grid(row=0, column=1, padx=5)
            tk.Label(row_frame, text=payment["total_amount"], width=20).grid(row=0, column=2, padx=5)
            tk.Label(row_frame, text=payment["payment_method"], width=20).grid(row=0, column=3, padx=5)
            tk.Label(row_frame, text=payment["reference"], width=20).grid(row=0, column=4, padx=5)
            tk.Label(row_frame, text=payment["delete"], width=20).grid(row=0, column=5, padx=5)

# Example usage
if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("1300x400")  # Set window size
    ViewPaymentScreen(root).pack(fill=tk.BOTH, expand=True)
    root.mainloop()
