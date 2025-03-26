from fpdf import FPDF
from datetime import datetime
import os

class PDFReport(FPDF):
    def header(self):
        self.set_font("Arial", "B", 16)
        self.cell(0, 10, "AI-Powered Investment Report", ln=True, align="C")
        self.set_font("Arial", "", 12)
        self.cell(0, 10, f"Generated on {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}", ln=True, align="C")
        self.ln(10)

    def add_section(self, title, content):
        self.set_font("Arial", "B", 14)
        self.multi_cell(0, 10, title)
        self.set_font("Arial", "", 12)
        self.multi_cell(0, 10, content)
        self.ln()

def generate_pdf_report(ticker: str, sections: dict, output_folder="reports"):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    pdf = PDFReport()
    pdf.add_page()

    pdf.set_title(f"{ticker} Investment Report")
    pdf.add_section("📈 Ticker", ticker)

    for section_title, content in sections.items():
        pdf.add_section(section_title, content)

    filename = f"{output_folder}/{ticker}_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.pdf"
    pdf.output(filename)
    return filename
