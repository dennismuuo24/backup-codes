import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

class InvoiceGenerator:
    def __init__(self, root):
        self.root = root
        self.root.title("Invoice Generator")

        # Invoice details
        self.invoice_number = tk.StringVar()
        self.customer_name = tk.StringVar()
        self.items = []

        # Create frame for invoice details
        self.frame = ttk.Frame(root, padding="20")
        self.frame.grid(row=0, column=0, padx=10, pady=10)

        # Invoice number
        ttk.Label(self.frame, text="Invoice Number:").grid(row=0, column=0, sticky="w")
        ttk.Entry(self.frame, textvariable=self.invoice_number).grid(row=0, column=1, sticky="w")

        # Customer name
        ttk.Label(self.frame, text="Customer Name:").grid(row=1, column=0, sticky="w")
        ttk.Entry(self.frame, textvariable=self.customer_name).grid(row=1, column=1, sticky="w")

        # Item details
        ttk.Label(self.frame, text="Items:").grid(row=2, column=0, sticky="w")
        self.item_entry = tk.Text(self.frame, height=5, width=30)
        self.item_entry.grid(row=2, column=1, sticky="w")

        # Generate and save buttons
        ttk.Button(self.frame, text="Generate Invoice", command=self.generate_invoice).grid(row=3, column=0, columnspan=2, pady=10)
        ttk.Button(self.frame, text="Save PDF", command=self.save_pdf).grid(row=4, column=0, columnspan=2)

    def generate_invoice(self):
        self.items = self.item_entry.get("1.0", tk.END).strip().split('\n')
        if self.invoice_number.get() and self.customer_name.get() and self.items:
            invoice_str = f"Invoice Number: {self.invoice_number.get()}\n"
            invoice_str += f"Customer Name: {self.customer_name.get()}\n"
            invoice_str += "-------------------------------------------\n"
            invoice_str += "Item             |  Quantity  |  Price  |  Total\n"
            invoice_str += "-------------------------------------------\n"
            total_amount = 0
            for item in self.items:
                item_data = item.split(',')
                if len(item_data) == 3:
                    quantity, description, unit_price = item_data
                    try:
                        total_price = int(quantity) * float(unit_price)
                        invoice_str += f"{description.ljust(16)} |  {str(quantity).center(9)}  |  ${str(unit_price).center(6)}  |  ${str(total_price)}\n"
                        total_amount += total_price
                    except ValueError:
                        pass  # Skip invalid items
                else:
                    messagebox.showwarning("Invalid Item", f"Invalid item: {item}. Please provide quantity, description, and unit price separated by commas.")
            invoice_str += "-------------------------------------------\n"
            invoice_str += f"Total Amount: ${total_amount}\n"
            messagebox.showinfo("Invoice Generated", "Invoice generated successfully!\nClick 'Save PDF' to save the invoice.")
            self.invoice_str = invoice_str
        else:
            messagebox.showerror("Error", "Please fill in all fields and provide at least one valid item.")

    def save_pdf(self):
        try:
            filename = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF files", "*.pdf")])
            if filename:
                c = canvas.Canvas(filename, pagesize=letter)
                c.setFont("Helvetica", 12)
                lines = self.invoice_str.split('\n')
                y = 750
                for line in lines:
                    c.drawString(100, y, line)
                    y -= 15
                c.save()
                messagebox.showinfo("PDF Saved", f"PDF saved successfully as {filename}")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred while saving PDF: {e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = InvoiceGenerator(root)
    root.mainloop()
