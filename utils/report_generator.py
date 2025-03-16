import os
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

def generate_pdf_report(content, filename="report.pdf"):
    output_dir = "./reports/generated_reports"
    
    # Ensure the folder exists
    os.makedirs(output_dir, exist_ok=True)

    # Save the report inside the folder
    c = canvas.Canvas(f"{output_dir}/{filename}", pagesize=A4)
    c.setFont("Helvetica", 12)
    
    # Basic multiline text writer
    y = 800
    for line in content.split("\n"):
        c.drawString(50, y, line)
        y -= 20  # move down for next line
        if y < 50:  # simple page break logic
            c.showPage()
            y = 800
    
    c.save()
