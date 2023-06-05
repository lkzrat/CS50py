from fpdf import FPDF
#blablabla
class Shirtificate():
    def __init__(self, name):
        self.pdf = FPDF()
        self.name = name
        self.pdf.add_page()
        self.pdf.set_font('helvetica', 'B', 45)
        self.pdf.cell(0, 60, 'CS50 Shirtificate', align='C', new_x='LMARGIN', new_y='NEXT')
        self.pdf.image(r'shirtificate.png', w=self.pdf.epw)

    def create(self):
        self.pdf.set_font('helvetica', 'b', 25)
        self.pdf.set_text_color(255, 255, 255)
        self.pdf.text(x=(self.pdf.epw - len(self.name) - 50)/2, y=140, txt=f'{self.name} took CS50')
        self.pdf.output('shirtificate.pdf')

pdf = Shirtificate(str(input('Name: ')))
pdf.create()