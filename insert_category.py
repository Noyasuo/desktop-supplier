import tkinter as tk

class InsertCategoryScreen(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.configure(bg="#f5f5f5")

        # Add Insert Category Form
        tk.Label(self, text="Insert Category", font=("Arial", 18)).pack(pady=10)

        # Category name label and entry
        category_frame = tk.Frame(self)
        category_frame.pack(pady=5)
        tk.Label(category_frame, text="Category Name:", font=("Arial", 12)).pack(side=tk.LEFT)
        self.category_name_entry = tk.Entry(category_frame, width=30)
        self.category_name_entry.pack(side=tk.LEFT, padx=(5, 0))

        # Description label and text box
        description_frame = tk.Frame(self)
        description_frame.pack(pady=5)
        tk.Label(description_frame, text="Description:", font=("Arial", 12)).pack(side=tk.LEFT)
        self.description_box = tk.Text(description_frame, height=5, width=30)
        self.description_box.pack(side=tk.LEFT, padx=(5, 0))

        # Submit button
        submit_button = tk.Button(self, text="Submit", command=self.submit_category)
        submit_button.pack(pady=20)

    def submit_category(self):
        category_name = self.category_name_entry.get()
        description = self.description_box.get("1.0", tk.END).strip()
        print(f"Category '{category_name}' with description '{description}' inserted!")

# Example usage if running this file directly
if __name__ == "__main__":
    root = tk.Tk()
    root.title("Insert Category")
    root.geometry("400x300")
    insert_category_screen = InsertCategoryScreen(master=root)
    insert_category_screen.pack(fill=tk.BOTH, expand=True)
    root.mainloop()
