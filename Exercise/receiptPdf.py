from fpdf import FPDF

def generate(itemid, name, price):
    pdf = FPDF(orientation='P', unit='mm', format='a4')
    pdf.add_page()

    pdf.set_font(family='Times', style='B', size=16)
    pdf.cell(w=0, h=12, align='L', ln=1, txt=f"Receipt No: {itemid}")

    pdf.set_font(family='Times', style='B', size=16)
    pdf.cell(w=0, h=12, align='L', ln=1, txt=f"Article : {name}")

    pdf.set_font(family='Times', style='B', size=16)
    pdf.cell(w=0, h=12, align='L', ln=1, txt=f"Price : {str(price)}")

    pdf.output("Receipt.pdf")
