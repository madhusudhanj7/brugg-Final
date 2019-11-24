from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm, mm,inch
from reportlab.lib import colors, utils
from reportlab.platypus import Paragraph, Table, TableStyle, Image, Frame, Spacer, PageBreak, BaseDocTemplate, PageTemplate, SimpleDocTemplate, Flowable
from reportlab.platypus.flowables import HRFlowable
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet, TA_CENTER
from reportlab.graphics import barcode, renderPDF
from reportlab.graphics.shapes import *
from reportlab.platypus.flowables import Image as GNAA
from reportlab.lib.pagesizes import letter, landscape
from reportlab.pdfgen import canvas
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet, TA_CENTER
from reportlab.lib.colors import yellow, red, black,white,grey
from reportlab.graphics.shapes import Rect
from reportlab.lib import colors
from reportlab.graphics.shapes import *
from reportlab.graphics import renderPDF
from reportlab.graphics.shapes import Drawing
from reportlab.pdfgen.canvas import Canvas
from reportlab.graphics.shapes import *
from reportlab.graphics import renderPDF
from reportlab.pdfgen.canvas import Canvas
from reportlab.lib.colors import red, yellow, green, gray, white
from reportlab.lib.units import mm
from reportlab.lib import colors
from reportlab.graphics.shapes import *
from reportlab.platypus import Image
from reportlab.graphics import shapes
from reportlab.graphics.charts.textlabels import Label
from reportlab.graphics import renderPDF, renderPM
from reportlab.graphics.shapes import Drawing
from svglib.svglib import svg2rlg
from reportlab.graphics import renderPDF
from PIL import Image, ImageFilter
from svglib.svglib import svg2rlg
from reportlab.graphics.shapes import Drawing
from reportlab.graphics import renderSVG


c = Canvas("brugglift.pdf",pagesize=landscape(letter))

width, height = A4
styles = getSampleStyleSheet()
styleN = styles["BodyText"]
# styleN.alignment = TA_LEFT
styleBH = styles["Normal"]
# styleBH.alignment = TA_CENTER

logo = "brugglifting.svg"
logo1 = "image1.jpg"
logo2 = "image2.jpg"
logo3 = "image3.svg"
logo4 = "image4.png"
logo5 = "image5.png"
logo11 ="image11.jpg"
logo12 = "image12.png"
logo13 = "a.png"
logo14 = "b.png"
logo15 = "c.png"
logo16 = "d.png"
logo7 ="image7.png"
logo8 = "image8.png"
logo9 = "image9.png"
logo10 ="image10.png"

c.drawImage(logo1,0*inch,6*inch,width=12*inch,height=3*inch,preserveAspectRatio = True)
drawing = svg2rlg(logo)
scaleFactor = 1./0.9
drawing.width *= scaleFactor
drawing.height *= scaleFactor
drawing.scale(scaleFactor, scaleFactor)
renderPDF.draw(drawing, c, 30, 582)

textobject = c.beginText()
textobject.setTextOrigin(1.1*inch,  5*inch)
c.setFont('Helvetica-Bold', 8)
c.setFillColorRGB(0,0,0)
textobject.textLines('''
Systemlieferant''')
c.drawText(textobject)

textobject = c.beginText()
textobject.setTextOrigin(1.1*inch, 4.8*inch)
c.setFont('Helvetica', 7)
c.setFillColorRGB(0,0,0)
textobject.textLines('''
Sie finden bei uns ein umfassendes Sortiment an Aufzugseilen, Zubehor und Hilfs-
mitteln, um ihre Bedurfnisse vollstandig abzudecker. Wir beliefern Sie mit Komplett-
losungen oder individuell zusammengestellten Komponenten, als Einzelteile oder
vormontient, ganz nach ihren Wunschen.''')
c.drawText(textobject)


textobject = c.beginText()
textobject.setTextOrigin(1.1*inch, 4.2*inch)
c.setFont('Helvetica-Bold', 8)
c.setFillColorRGB(0,0,0)
textobject.textLines('''
Kundenspezifisch''')
c.drawText(textobject)


textobject = c.beginText()
textobject.setTextOrigin(1.1*inch, 4.0*inch)
c.setFont('Helvetica', 7)
c.setFillColorRGB(0,0,0)
textobject.textLines('''
Sie finden bei uns ein umfassendes Sortiment an Aufzugseilen, Zubehor und Hilfs-
mitteln, um ihre Bedurfnisse vollstandig abzudecker. Wir beliefern Sie mit Komplett-
losungen oder individuell zusammengestellten Komponenten, als Einzelteile oder
vormontient, ganz nach ihren Wunschen.''')
c.drawText(textobject)


textobject = c.beginText()
textobject.setTextOrigin(1.1*inch, 3.4*inch)
c.setFont('Helvetica-Bold', 8)
c.setFillColorRGB(0,0,0)
textobject.textLines('''
Verfugbarkeit''')
c.drawText(textobject)


textobject = c.beginText()
textobject.setTextOrigin(1.1*inch, 3.2*inch)
c.setFont('Helvetica', 7)
c.setFillColorRGB(0,0,0)
textobject.textLines('''
Sie finden bei uns ein umfassendes Sortiment an Aufzugseilen, Zubehor und Hilfs-
mitteln, um ihre Bedurfnisse vollstandig abzudecker. Wir beliefern Sie mit Komplett-
losungen oder individuell zusammengestellten Komponenten, als Einzelteile oder
vormontient, ganz nach ihren Wunschen.''')
c.drawText(textobject)


textobject = c.beginText()
textobject.setTextOrigin(1.1*inch, 2.5*inch)
c.setFont('Helvetica-Bold', 8)
c.setFillColorRGB(0,0,0)
textobject.textLines('''
Expressdient''')
c.drawText(textobject)

textobject = c.beginText()
textobject.setTextOrigin(1.1*inch, 2.3*inch)
c.setFont('Helvetica', 7)
c.setFillColorRGB(0,0,0)
textobject.textLines('''
losungen oder individuell zusammengestellten Komponenten, als Einzelteile oder
vormontient, ganz nach ihren Wunschen.
                        ''')
c.drawText(textobject)

textobject = c.beginText()
textobject.setTextOrigin(1.1*inch, 1.8*inch)
c.setFont('Helvetica-Bold', 8)
c.setFillColorRGB(0,0,0)
textobject.textLines('''
Internationale Standards''')
c.drawText(textobject)


textobject = c.beginText()
textobject.setTextOrigin(1.1*inch, 1.6*inch)
c.setFont('Helvetica', 7)
c.setFillColorRGB(0,0,0)
textobject.textLines('''
losungen oder individuell zusammengestellten Komponenten, als Einzelteile oder
                        ''')
c.drawText(textobject)

textobject = c.beginText()
textobject.setTextOrigin(1.1*inch, 1.2*inch)
c.setFont('Helvetica-Bold', 8)
c.setFillColorRGB(0,0,0)
textobject.textLines('''
Schulungen/Fachseminare''')
c.drawText(textobject)

textobject = c.beginText()
textobject.setTextOrigin(1.1*inch, 1*inch)
c.setFont('Helvetica', 7)
c.setFillColorRGB(0,0,0)
textobject.textLines('''
mitteln, um ihre Bedurfnisse vollstandig abzudecker. Wir beliefern Sie mit Komplett-
losungen oder individuell zusammengestellten Komponenten, als Einzelteile oder
vormontient, ganz nach ihren Wunschen.''')
c.drawText(textobject)


textobject = c.beginText()
textobject.setTextOrigin(5.6*inch, 4.8*inch)
c.setFont('Helvetica', 7)
c.setFillColorRGB(0,0,0)
textobject.textLines('''
Als Weltneuheit  entwickelt,  vereint CTP technologische  Innovationnen zu   einem
hochmodernen  kunststoffummantelten  Seil,  das speziell  fur  die   Aufzugsbranche
ausgelegt ist.
Zugelassen fur Treibscheiben mit einem Durchmesser von nur 115 mm, sind CTP Seile
bereits in 60.000 Aufzugen weltweit eingebaut.
CTP Seile, die mittels Simulation im Labor und unter realen Bedingungen getestet
worden sind, erfullen hochste Anspruche an Funktion und Leistungsfahigkeit.
''')
c.drawText(textobject)
# c.drawImage(logo2,4,2.5,width=750,height=425,mask='auto')
c.drawImage(logo2,5.6*inch,1.3*inch,width=5*inch,height=2.55*inch)

c.drawImage(logo4,9.8*inch,0.3*inch,width=0.78*inch,height=0.78*inch)

c.drawImage(logo5,8.8*inch,0.3*inch,width=0.78*inch,height=0.78*inch)

p = c.beginPath()
p.rect(0.3*inch,4.4*inch, 0.6*inch, 0.6*inch)
p.rect(0.3*inch,3.62*inch,0.6*inch, 0.6*inch)
p.rect(0.3*inch,2.85*inch, 0.6*inch, 0.6*inch)
p.rect(0.3*inch,2*inch, 0.6*inch, 0.6*inch)
p.rect(0.3*inch,1.3*inch, 0.6*inch, 0.6*inch)
p.rect(0.3*inch,0.6*inch, 0.6*inch, 0.6*inch)
p.rect(-20, 6.07*inch, 6.6*inch, 0.9*inch)
p.rect(455.2, 6.07*inch, 30*inch, 0.27*inch)
# p.rect(2, 3*inch, 1*inch, 1*inch)
c.clipPath(p, stroke=0)
c.linearGradient(150*mm, 100*mm, 20*mm, 10*mm, ('#996515','#DAA520'),extend=True)

# q = c.beginPath()
# q.rect(-20, 6.08*inch, 6.6*inch, 0.9*inch)
# c.clipPath(q, stroke=0)
# c.linearGradient(5*mm, 30*mm, 20*mm, 10*mm, ('#B8860B',white),extend=True)

drawing = svg2rlg(logo3)
scaleFactor = 0.1/1.4
drawing.width *= scaleFactor
drawing.height *= scaleFactor
drawing.scale(scaleFactor, scaleFactor)
renderPDF.draw(drawing, c, 26, 50)

drawing = svg2rlg(logo3)
scaleFactor = 0.1/1.4
drawing.width *= scaleFactor
drawing.height *= scaleFactor
drawing.scale(scaleFactor, scaleFactor)
renderPDF.draw(drawing, c, 26, 100)

drawing = svg2rlg(logo3)
scaleFactor = 0.1/1.4
drawing.width *= scaleFactor
drawing.height *= scaleFactor
drawing.scale(scaleFactor, scaleFactor)
renderPDF.draw(drawing, c, 26, 150)

drawing = svg2rlg(logo3)
scaleFactor = 0.1/1.4
drawing.width *= scaleFactor
drawing.height *= scaleFactor
drawing.scale(scaleFactor, scaleFactor)
renderPDF.draw(drawing, c, 26, 210)

drawing = svg2rlg(logo3)
scaleFactor = 0.1/1.4
drawing.width *= scaleFactor
drawing.height *= scaleFactor
drawing.scale(scaleFactor, scaleFactor)
renderPDF.draw(drawing, c, 26, 266)

drawing = svg2rlg(logo3)
scaleFactor = 0.1/1.4
drawing.width *= scaleFactor
drawing.height *= scaleFactor
drawing.scale(scaleFactor, scaleFactor)
renderPDF.draw(drawing, c, 26, 320)

c.setFont('Helvetica-Bold', 17)
c.drawString(40,465,"SERVICE")

c.showPage()

bg = "img1.jpg"
product = "img8.png"
wire = "img7.png"
l1 = 'img5.png'
l2='img6.png'
l3='img4.png'


c.drawImage(bg,0*inch,6*inch,width=12*inch,height=3*inch,preserveAspectRatio=True)
drawing = svg2rlg(logo)
scaleFactor = 1./0.9
drawing.width *= scaleFactor
drawing.height *= scaleFactor
drawing.scale(scaleFactor, scaleFactor)
renderPDF.draw(drawing, c, 30, 570)

c.drawImage(product,30,320,width=1*inch,height=1*inch,mask='auto')
c.drawImage(wire,50,0,width=0.5*inch,height=3.25*inch,mask='auto')
c.drawImage(l1,430,170,width=1*inch,height=1*inch,mask='auto')
c.setFont("Helvetica-Bold", 5)

c.drawString(6.10*inch, 2.25*inch, "Diagramm der festgelegten")
c.drawString(6.10*inch, 2.1*inch, "Rillen fur CTP 6.5mm")

c.drawImage(l2,560,170,width=1*inch,height=1*inch,mask='auto')
c.drawString(7.85*inch, 2.25*inch, "Diagramm der festgelegten")
c.drawString(7.85*inch, 2.1*inch, "Rillen fur CTP 8.1mm")



c.setFont("Helvetica-Bold", 20)
c.drawString(30,455, "CTP")
textobject = c.beginText()
textobject.setTextOrigin(1.95*inch, 5.5*inch)
textobject.setFont("Helvetica-Bold", 9)
textobject.setFillColorRGB(0,0,0)
textobject.textLines('''
                    Vollastahseil, 9 litzen,gensondert verseilt''')
c.drawText(textobject)
textobject = c.beginText()
textobject.setTextOrigin(1.95*inch, 5.35*inch)
textobject.setFont("Helvetica", 7)
textobject.setFillColorRGB(0,0,0)
textobject.textLines('''
                    Vollastahseil, 9 litzen,gensondert verseilt
                    ''')
c.drawText(textobject)
textobject = c.beginText()
textobject.setTextOrigin(5.75*inch, 5.5*inch)
textobject.setFont("Helvetica", 8)
textobject.setFillColorRGB(0,0,0)
textobject.textLines('''
                    For highest demandas on breaking force, elongation  elongation elongation
                    and number of trips, also under difficult instalation''')
c.drawText(textobject)

textobject = c.beginText()
textobject.setTextOrigin(5.75*inch, 5.15*inch)
textobject.setFont("Helvetica-Bold", 8)
textobject.setFillColorRGB(0,0,0)
textobject.textLines('''
                    For highest demandas on breaking force, elongation
                    ''')
c.drawText(textobject)
c.drawText(textobject)
textobject = c.beginText()
textobject.setTextOrigin(5.75*inch, 5*inch)
textobject.setFont("Helvetica", 8)
textobject.setFillColorRGB(0,0,0)
textobject.textLines('''
                    For highest demandas on breaking force, elongation elongation elongation
                    ''')
c.drawText(textobject)
textobject = c.beginText()
textobject.setTextOrigin(5.75*inch, 4.75*inch)
textobject.setFont("Helvetica-Bold", 8)
textobject.setFillColorRGB(0,0,0)
textobject.textLines('''
                    For highest demandas on breaking force, elongation
                    ''')
c.drawText(textobject)
c.drawText(textobject)
textobject = c.beginText()
textobject.setTextOrigin(5.75*inch, 4.6*inch)
textobject.setFont("Helvetica", 8)
textobject.setFillColorRGB(0,0,0)
textobject.textLines('''
                    For highest demandas on breaking force, elongation  elongation elongation
                    ''')
c.drawText(textobject)
textobject = c.beginText()
textobject.setTextOrigin(5.75*inch, 4.3*inch)
textobject.setFont("Helvetica-Bold", 8)
textobject.setFillColorRGB(0,0,0)
textobject.textLines('''
                    For highest demandas on breaking force, elongation
                    ''')
c.drawText(textobject)
c.drawText(textobject)
textobject = c.beginText()
textobject.setTextOrigin(5.75*inch, 4.15*inch)
textobject.setFont("Helvetica", 8)
textobject.setFillColorRGB(0,0,0)
textobject.textLines('''
                    For highest demandas on breaking force, elongation  elongation  elongation
                    ''')
c.drawText(textobject)
textobject = c.beginText()
textobject.setTextOrigin(5.75*inch, 3.8*inch)
textobject.setFont("Helvetica-Bold", 8)
textobject.setFillColorRGB(0,0,0)
textobject.textLines('''
                    For highest demandas on breaking force, elongation
                    ''')
c.drawText(textobject)
c.drawText(textobject)
textobject = c.beginText()
textobject.setTextOrigin(5.75*inch, 3.65*inch)
textobject.setFont("Helvetica", 8)
textobject.setFillColorRGB(0,0,0)
textobject.textLines('''
                    For highest demandas on breaking force, elongation  elongation elongation
                    ''')
c.drawText(textobject)
data = [
   ['Art.-Nr', 'Seil-@', 'BrunchKraft',  'Getwicht' , "konstruktion"],
   ['',   'mm',         'kN',         'kg/100m',     ' ',     ],
   ['73107',   '6.5',        '23.6',        '11.0',    ' ',     '6x19seal-SES(IWRC)'],
   ['10982',   '6.5',        '23.6',        '11.0',    ' ',     '6x19seal-SES(IWRC)'],


   ]

t5 =  Table(data,colWidths=[1* cm, 1* cm, 1.5 * cm,1.5* cm, 1.5* cm] ,rowHeights=5*mm)
t5.setStyle(TableStyle([
                    ('LINEABOVE',(0,2),(-1,-1),0.25,colors.black),
                    ('LINEBELOW',(0,1),(-1,-1),0.25,colors.black),
                    ('FONTSIZE', (0, 0), (-1, -1), 7),
                    ('FONTSIZE', (0, 1), (-1, -1), 6),
                    ('FONTNAME', (0, 0), (1,0), "Helvetica-Bold"),
                    ('FONTNAME', (2, 0), (3,0), "Helvetica-Bold"),
                    ('FONTNAME', (4,0), (5,0), "Helvetica-Bold"),
                    ('ALIGN', (0, 0), (-1, -1), 'CENTER'),

                    ('VALIGN', (0, 1), (-1, -1), 'MIDDLE'),
                    # ('ALIGN', (1, 0), (1, 7), 'CENTER'),
                    # ('ALIGN', (2, 0), (-1, 7), 'CENTER'),
                    # ('ALIGN', (3, 0), (-1, 7), 'LEFT'),
                    # ('ALIGN', (4, 0), (-1, 7), 'LEFT'),
                    # ('ALIGN', (5, 0), (-1, 7), 'CENTER'),
                    # ('VALIGN', (5, 0), (-1, 7), 'BOTTOM'),
                    # ('LEFTPADDING', (0, 0), (-1, 3), 0),
                    # ('LEFTPADDING', (0, 0), (-1, 3), 15),
                    #  ('LEFTPADDING', (2, 0), (-1, 3), 15),
                    ('LEFTPADDING', (4, 1), (-1,-1), -40),
                    ('ALIGN', (4, 0), (-1,-1), 'LEFT'),
                    #
                    #  ('LEFTPADDING', (5, 0), (-1, -1), -30),
                    ('BACKGROUND', (1,0), (1, 1), '#DCDCDC'),
                    ('BACKGROUND', (1,2), (1, 3), '#DCDCDC'),
                    # ('BACKGROUND', (1,4), (1, 5), '#DCDCDC'),
                    # ('BACKGROUND', (1,6), (1, 7), '#DCDCDC'),
                     ]))

t5.wrapOn(c, 150, 190)
t5.drawOn(c, 1.95*inch,3*inch)
c.drawImage(l3,150,30,width=2.25*inch,height=2.25*inch,mask='auto')

textobject1 = c.beginText()
textobject1.setTextOrigin(1.95*inch, 2.85*inch)
c.setFillColor(colors.black)
textobject1.setFont("Helvetica", 5)
textobject1.textLines('''*  Weitere Nennfestigkeiten und/oder Durchmesser (auch   imperial Masse) auf Anfrage.
                           ''')
c.drawText(textobject1)
textobject1 = c.beginText()
textobject1.setTextOrigin(2.05*inch, 2.75*inch)
c.setFillColor(colors.black)
textobject1.setFont("Helvetica", 5)
textobject1.textLines('''
                           Seildurchmesser-Toleranzen nach EN12385-5/ISO 4344.
                           Weitere Nennfestigkeiten und/oder Durchmesser (auch   imperial Masse) auf Anfrage''')
c.drawText(textobject1)
textobject = c.beginText()

textobject1 = c.beginText()
textobject1.setTextOrigin(1.95*inch, 2.6*inch)
textobject1.setFont("Helvetica", 5)
textobject1.textLines('''
                      ** Further nominal strengths and/or diameters (including imperial dimenstions) on request.
                ''')
c.drawText(textobject1)
c.setFont("Helvetica",9)

c.drawString(5.75*inch, 1.75*inch, "Ptoduckaten der Treibscheibe/Ablenkung")

data = [
    ['FUR', 'Seil-@', 'Stahlseil-@',  'Reibungs-' , "Seilgeschwindigkeit","scheiben-@","Treibscheibe","Rillenform","Abelenkscheibe"],
   ['Art.-Nr', '', '',  'Koeffzient' , "max","","Material","","Material"],
   ['',   'mm',  'mm','','m/s'   ,'mm'   '',         'hulbrund@mm',     ' ',     ],
   ['10982',   '6.5', '4,9','0,6-0,3','3,5*','>115','C45,c45 gehartet,42CrMo4','3,4-3,65','Stahl,Gusseisen,PA,PU.'],
   ['73106',   '6.5', '4,9','0,6-0,3','3,5*','>115','C45,c45 gehartet,42CrMo4','3,4-3,65','Stahl,Gusseisen,PA,PU.'],


   ]

t5 = Table(data, colWidths=[0.75* cm, 1* cm, 1 * cm,
                            1* cm, 2* cm,1* cm,2* cm,1.5* cm, ],rowHeights=5*mm)
t5.setStyle(TableStyle([
                     ('LINEABOVE',(0,2),(-1,-1),0.25,colors.black),
                     ('LINEBELOW',(0,1),(-1,-1),0.25,colors.black),
                    ('FONTSIZE', (0, 0), (-1, -1), 5),

                    ('FONTNAME', (0, 0), (1,0), "Helvetica-Bold"),
                    ('FONTNAME', (2, 0), (3,0), "Helvetica-Bold"),
                    ('FONTNAME', (4,0), (5,0), "Helvetica-Bold"),
                    ('FONTNAME', (6, 0), (7,0), "Helvetica-Bold"),
                    ('FONTNAME', (0,0),(8, 0), "Helvetica-Bold"),
                    ('FONTNAME', (0,0),(0, 1), "Helvetica-Bold"),
                    ('FONTNAME', (1,0),(3,1), "Helvetica-Bold"),
                    ('FONTNAME', (4,1),(6,1), "Helvetica-Bold"),
                    ('FONTNAME', (0,0),(8,1), "Helvetica-Bold"),
                    ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                    ('ALIGN', (0, 1), (-1, -1), 'CENTER'),
                    ('VALIGN', (0, 1), (-1, -1), 'MIDDLE'),
                    # ('ALIGN', (1, 0), (1, 7), 'CENTER'),
                    # ('ALIGN', (2, 0), (-1, 7), 'CENTER'),
                    # ('ALIGN', (3, 0), (-1, 7), 'LEFT'),
                    # ('ALIGN', (4, 0), (-1, 7), 'LEFT'),
                    # ('ALIGN', (5, 0), (-1, 7), 'CENTER'),
                    # ('VALIGN', (5, 0), (-1, 7), 'BOTTOM'),
                    # ('LEFTPADDING', (0, 0), (-1, -1), -20),
                    #  ('LEFTPADDING', (1, 0), (-1, -1),10),
                    #  ('LEFTPADDING', (2, 0), (-1, -1), -30),
                    #   ('LEFTPADDING', (3, 0), (-1, -1), -30),
                    #   ('LEFTPADDING', (5, 0), (-1, -1), -30),
                    # ('LEFTPADDING', (4, 0), (-1, 9), -30),
                    #  ('LEFTPADDING', (5, 0), (-1, 9), -70),
                    ('BACKGROUND', (1,0), (1, 1), '#DCDCDC'),
                    ('BACKGROUND', (1,2), (1, 3), '#DCDCDC'),
                    ('BACKGROUND', (1,4), (1, 5), '#DCDCDC'),
                    # ('BACKGROUND', (1,6), (1, 7), '#DCDCDC'),
                     ]))

t5.wrapOn(c, 20, 170)
t5.drawOn(c, 5.75*inch,0.6*inch)



textobject1 = c.beginText()
textobject1.setTextOrigin(5.75*inch, 0.49*inch)
c.setFillColor(colors.black)
textobject1.setFont("Helvetica", 5)
textobject1.textLines('''*  Weitere Nennfestigkeiten und/oder Durchmesser (auch   imperial Masse) auf Anfrage.
                           ''')
c.drawText(textobject1)
textobject1 = c.beginText()
textobject1.setTextOrigin(5.8*inch, 0.38*inch)
c.setFillColor(colors.black)
textobject1.setFont("Helvetica", 5)
textobject1.textLines('''
                           Seildurchmesser-Toleranzen nach EN12385-5/ISO 4344.
                           Weitere Nennfestigkeiten und/oder Durchmesser (auch   imperial Masse) auf Anfrage''')
c.drawText(textobject1)

c.setFont("Helvetica", 6)
c.drawString(2*inch, 4.1*inch, "E-Modul**")
c.drawString(2.8*inch, 4.1*inch, "elastische")
c.drawString(2.7*inch, 4*inch, "Tragseildehnung")
c.drawString(3.7*inch, 4.1*inch, "elastische")
c.drawString(3.55*inch, 4*inch, "Tragseildehnung")
c.drawString(4.45*inch,4.1*inch, "Forderhohe*")
d = c.beginPath()
d.rect(1.95*inch,4.25*inch,0.6*inch,0.6*inch)
d.rect(2.75*inch,4.25*inch,0.6*inch,0.6*inch)
d.rect(3.55*inch,4.25*inch,0.6*inch,0.6*inch)
d.rect(4.35*inch,4.25*inch,0.6*inch,0.6*inch)
d.rect(107, 6.07*inch, 12*inch, 0.2*inch)
d.rect(-20, 6.075*inch, 1.765*inch, 0.6*inch)

# d.arc(230, 130, 5, 10,startAng=90,extent=180)

c.clipPath (d, stroke=0)
c.linearGradient(100*mm,200*mm,100*mm,60*mm, ('#996515','#D4AF37','#996515'),extend=False)
c.setFont("Helvetica", 10)
c.drawString(130,440, "VOLLSTAHSEIL MIT KUNSTSTOFFMMANTELUNG")
c.setFont("Helvetica-Bold", 20)
c.drawString(30,450, "CTP")
c.setFont("Helvetica-Bold", 7)
c.drawString(2.10*inch, 4.6*inch, "125,000")
c.setFont("Helvetica", 5)
c.drawString(2.15*inch, 4.5*inch, "N/mm2")
# for box2
c.setFont("Helvetica-Bold", 7)
c.drawString(2.95*inch,4.6*inch, "0.104")
c.setFont("Helvetica", 5)
c.drawString(3.05*inch,4.5*inch, "%")
# for box3
c.setFont("Helvetica-Bold", 7)
c.setFillColor(colors.black)
c.drawString(3.75*inch,4.6*inch, "0.13")
c.setFont("Helvetica", 5)
c.drawString(3.8*inch,4.5*inch, "%")

# for box4

c.setFont("Helvetica", 9)
c.drawString(4.5*inch,4.6*inch, "<150")
c.drawString(4.6*inch,4.5*inch, "m")
c.setFont("Helvetica", 7)
r = c.beginPath()
r.circle(10*mm, 20*mm, 48*mm)
c.clipPath (r, stroke=0)
c.showPage()

bg = "image1.jpg"
product = "image3.jpg"
b = "1.png"
am = "AM.png"
j = "D.png"
c.drawImage(bg,0*inch,6*inch,width=12*inch,height=3*inch,preserveAspectRatio=True)
drawing = svg2rlg(logo)
scaleFactor = 1./0.9
drawing.width *= scaleFactor
drawing.height *= scaleFactor
drawing.scale(scaleFactor, scaleFactor)
renderPDF.draw(drawing, c, 30, 570)

c.drawImage(b,30,0,width=1*inch,height=5.8*inch,mask='auto')
c.drawImage(j,400,100,width=0.5*inch,height=3*inch,mask='auto')
c.drawImage(j,440,100,width=0.5*inch,height=3*inch,mask='auto')
c.drawImage(j,480,100,width=0.5*inch,height=3*inch,mask='auto')

textobject = c.beginText()
textobject.setTextOrigin(1.7*inch, 5.5*inch)
textobject.setFont("Helvetica-Bold", 9)
textobject.setFillColorRGB(0,0,0)
textobject.textLines('''
                    Produktdaten''')
c.drawText(textobject)
textobject = c.beginText()
textobject.setTextOrigin(1.7*inch, 5.35*inch)
textobject.setFont("Helvetica", 7)
lyrics = ['Vollastahseil, 9 litzen,gensondert verseilt',
          'Vollastahseil, 9 litzen,gensondert verseilt',

          ]
for line in lyrics:
    textobject.textLine(". %s" %(line))

c.drawText(textobject)
textobject = c.beginText()
textobject.setTextOrigin(1.7*inch, 5*inch)
textobject.setFont("Helvetica-Bold", 9)
textobject.setFillColorRGB(0,0,0)
textobject.textLines('''
                    Vorteile''')
c.drawText(textobject)
textobject = c.beginText()
textobject.setTextOrigin(1.7*inch, 4.8*inch)
textobject.setFont("Helvetica", 7)
lyrics = ['Vollastahseil, 9 litzen,gensondert verseilt ',
          'Vollastahseil, 9 litzen,gensondert verseilt',
          'Vollastahseil, 9 litzen,gensondert verseilt',
          'Vollastahseil, 9 litzen,gensondert verseilt',
          'Vollastahseil, 9 litzen,gensondert verseilt',
          'Vollastahseil, 9 litzen,gensondert verseilt',
          'Vollastahseil, 9 litzen,gensondert verseilt',
          'Vollastahseil, 9 litzen,gensondert verseilt',

          ]
for line in lyrics:
    textobject.textLine(". %s" %(line))

c.drawText(textobject)
c.setFont("Helvetica-Bold", 7)

c.drawString(1.7*inch, 3.1*inch, "Fur den Einsatz mit CTP 6.5mm")

data = [

   ['Art.-Nr', 'd1', 'd2',  'd3' , "d4","L1","L2","L3","L4"],
   ['',   '',  '','',''      'Abmessungen in mm',         '',     ' ',     ],
   ['10209',   'M 10', '13','9','7','240','150','66.0','16.6'],


   ]

t5 = Table(data, colWidths=[1* cm, 1* cm, 1 * cm,
                            1* cm, 1* cm,1* cm,1* cm,1* cm, ],rowHeights=5*mm)
t5.setStyle(TableStyle([
                     ('LINEABOVE',(0,2),(-1,-1),0.25,colors.black),
                     ('LINEABOVE',(0,1),(-1,-1),0.25,colors.black),
                     ('LINEBELOW',(0,1),(-1,-1),0.25,colors.black),
                    ('FONTSIZE', (0, 0), (-1, -1), 5),
                     ('FONTNAME', (0, 0), (1,0), "Helvetica-Bold"),
                     ('FONTNAME', (2, 0), (3,0), "Helvetica-Bold"),
                     ('FONTNAME', (4,0), (5,0), "Helvetica-Bold"),
                     ('FONTNAME', (6, 0), (7,0), "Helvetica-Bold"),
                    ('FONTNAME', (0,0),(8, 0), "Helvetica-Bold"),

                    # ('BACKGROUND', (1,2), (1, 3), '#DCDCDC'),
                    # ('BACKGROUND', (1,4), (1, 5), '#DCDCDC'),
                     ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                    ('ALIGN', (0, 1), (-1, -1), 'CENTER'),
                    ('VALIGN', (0, 1), (-1, -1), 'MIDDLE'),

                     ]))

t5.wrapOn(c, 30, 300)
t5.drawOn(c, 1.7*inch,2.25*inch)
c.setFont("Helvetica-Bold", 7)
c.drawString(1.7*inch, 1.7*inch, "Fur den Einsatz mit CTP 8.1mm")

data = [

   ['Art.-Nr', 'd1', 'd2',  'd3' , "d4","L1","L2","L3","L4"],
   ['',   '',  '','',''      'Abmessungen in mm',         '',     ' ',     ],
   ['10113',   'M 10', '13','9','7','240','150','66.0','16.6'],


   ]

t5 = Table(data, colWidths=[0.75* cm, 1* cm, 1 * cm,
                            1* cm, 1* cm,1* cm,1* cm,1* cm, ],rowHeights=5*mm)
t5.setStyle(TableStyle([
                     ('LINEABOVE',(0,2),(-1,-1),0.25,colors.black),
                     ('LINEABOVE',(0,1),(-1,-1),0.25,colors.black),
                     ('LINEBELOW',(0,1),(-1,-1),0.25,colors.black),
                    ('FONTSIZE', (0, 0), (-1, -1), 5),
                     ('FONTNAME', (0, 0), (1,0), "Helvetica-Bold"),
                     ('FONTNAME', (2, 0), (3,0), "Helvetica-Bold"),
                     ('FONTNAME', (4,0), (5,0), "Helvetica-Bold"),
                     ('FONTNAME', (6, 0), (7,0), "Helvetica-Bold"),
                    ('FONTNAME', (0,0),(8, 0), "Helvetica-Bold"),

                     ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                    ('ALIGN', (0, 1), (-1, -1), 'CENTER'),
                    ('VALIGN', (0, 1), (-1, -1), 'MIDDLE'),

                     ]))

t5.wrapOn(c, 30, 300)
t5.drawOn(c, 1.7*inch,0.9*inch)

textobject = c.beginText()
textobject.setTextOrigin(7.5*inch, 5.5*inch)
textobject.setFont("Helvetica-Bold", 9)
textobject.setFillColorRGB(0,0,0)
textobject.textLines('''
                    Produktdaten''')
c.drawText(textobject)
textobject = c.beginText()
textobject.setTextOrigin(7.5*inch, 5.35*inch)
textobject.setFont("Helvetica", 7)
lyrics = ['Vollastahseil, 9 litzen,gensondert verseilt verseilt',
          'Vollastahseil, 9 litzen,gensondert verseilt',
          'Vollastahseil, 9 litzen,gensondert verseiltverseiltverseilt',
          'Vollastahseil, 9 litzen,gensondert verseilt',
          'Vollastahseil, 9 litzen,gensondert verseiltverseiltverseilt',
          'Vollastahseil, 9 litzen,gensondert verseilt',
          'Vollastahseil, 9 litzen,gensondert verseilt',
          'Vollastahseil, 9 litzen,gensondert verseilt verseilt verseilt',

          ]
for line in lyrics:
    textobject.textLine(". %s" %(line))

c.drawText(textobject)
textobject = c.beginText()
textobject.setTextOrigin(7.5*inch, 4.25*inch)
textobject.setFont("Helvetica-Bold", 9)
textobject.setFillColorRGB(0,0,0)
textobject.textLines('''
                    Produktdaten''')
c.drawText(textobject)
textobject = c.beginText()
textobject.setTextOrigin(7.5*inch, 4.1*inch)
textobject.setFont("Helvetica", 7)
lyrics = ['Vollastahseil, 9 litzen,gensondert verseilt ',
          'Vollastahseil, 9 litzen,gensondert verseilt',
]
for line in lyrics:
    textobject.textLine(". %s" %(line))
c.drawText(textobject)

c.setFont("Helvetica-Bold", 7)
c.drawString(7.5*inch, 3.5*inch, "Fur den Einsatz mit CTP 6.5 mm")

data = [

   ['Art.-Nr','', 'Seil-@', 'd',  'd1',"L1","L2","L3"],
   ['',   '','mm',  '','',''      '',         '',     ' ',     ],
   ['64109',  'A', '5,0-6,5','M 10', '','265','180'],
   ['64140', 'AM', '5,0-6,5','M 10', '','265','180'],
   ['64115',    'D', '5,0-6,5','M 10', '23','265','180','85,5']


   ]

t5 = Table(data, colWidths=[1* cm, 1* cm, 1 * cm,
                            1* cm, 1* cm,1* cm,1* cm,1* cm, ],rowHeights=5*mm)
t5.setStyle(TableStyle([
                     ('LINEABOVE',(0,2),(-1,-1),0.25,colors.black),
                     ('LINEABOVE',(0,1),(-1,-1),0.25,colors.black),
                     ('LINEBELOW',(0,1),(-1,-1),0.25,colors.black),
                    ('FONTSIZE', (0, 0), (-1, -1), 5),
                     ('FONTNAME', (0, 0), (1,0), "Helvetica-Bold"),
                     ('FONTNAME', (2, 0), (3,0), "Helvetica-Bold"),
                     ('FONTNAME', (4,0), (5,0), "Helvetica-Bold"),
                     ('FONTNAME', (6, 0), (7,0), "Helvetica-Bold"),
                     ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                    ('ALIGN', (0, 1), (-1, -1), 'CENTER'),
                    ('VALIGN', (0, 1), (-1, -1), 'MIDDLE'),
                    ('BACKGROUND', (2,0),(2, 5), '#DCDCDC')
                     ]))

t5.wrapOn(c, 30, 300)
t5.drawOn(c, 7.5*inch,2.4*inch)
textobject1 = c.beginText()
textobject1.setTextOrigin(7.5*inch, 2.3*inch)
c.setFillColor(colors.black)
textobject1.setFont("Helvetica", 5)
textobject1.textLines(''' Weitere Nennfestigkeiten und/oder Durchmesser
                        Weitere Nennfestigkeiten und/oder Durchmesser (auch   imperial Masse) auf Anfrage   ''')
c.drawText(textobject1)
c.setFont("Helvetica-Bold", 7)

c.drawString(7.5*inch, 1.9*inch, "Fur den Einsatz mit CTP 8.1mm")

data = [

   ['Art.-Nr','', 'Seil-@', 'd',  'd1',"L1","L2","L3"],
   ['',   '','mm',  '','',''      '',         '',     ' ',     ],
   ['64109',  'A', '5,0-6,5','M 10', '','265','180'],
   ['64140', 'AM', '5,0-6,5','M 10', '','265','180'],
   ['64115',    'D', '5,0-6,5','M 10', '23','265','180','85,5']


   ]

t5 = Table(data, colWidths=[1* cm, 1* cm, 1 * cm,
                            1* cm, 1* cm,1* cm,1* cm,1* cm, ],rowHeights=5*mm)
t5.setStyle(TableStyle([
                     ('LINEABOVE',(0,2),(-1,-1),0.25,colors.black),
                     ('LINEABOVE',(0,1),(-1,-1),0.25,colors.black),
                     ('LINEBELOW',(0,1),(-1,-1),0.25,colors.black),
                    ('FONTSIZE', (0, 0), (-1, -1), 5),
                     ('FONTNAME', (0, 0), (1,0), "Helvetica-Bold"),
                     ('FONTNAME', (2, 0), (3,0), "Helvetica-Bold"),
                     ('FONTNAME', (4,0), (5,0), "Helvetica-Bold"),
                     ('FONTNAME', (6, 0), (7,0), "Helvetica-Bold"),
                     ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                    ('ALIGN', (0, 1), (-1, -1), 'CENTER'),
                    ('VALIGN', (0, 1), (-1, -1), 'MIDDLE'),
                    ('BACKGROUND', (2,0),(2, 5), '#DCDCDC'),


                     ]))

t5.wrapOn(c, 30, 300)
t5.drawOn(c, 7.5*inch,0.8*inch)

textobject1 = c.beginText()
textobject1.setTextOrigin(7.5*inch,0.7*inch)
c.setFillColor(colors.black)
textobject1.setFont("Helvetica", 5)
textobject1.textLines(''' Weitere Nennfestigkeiten und/oder Durchmesser
                        Weitere Nennfestigkeiten und/oder Durchmesser (auch   imperial Masse) auf Anfrage   ''')
c.drawText(textobject1)

d = c.beginPath()
d.rect(-20, 6.07*inch, 10*inch, 0.6*inch)
d.rect(700, 6.07*inch, 12.5*inch, 0.2*inch)
c.clipPath (d, stroke=0)
c.linearGradient(100*mm,200*mm,100*mm,60*mm, ('#996515','#DAA520','#996515'),extend=False)
c.setFont("Helvetica", 10)
c.drawString(90,450, "Anpress-Ausssengewinden")
c.setFont("Helvetica-Bold", 18)
c.drawString(30,450, "APAG")
c.setFont("Helvetica-Bold", 18)
c.drawString(400,450, "SEILSCHLOSS")
c.setFont("Helvetica", 10)
c.drawString(530,450, "symmetrisch [EN-13411-7]")





c.showPage()

logo11 ="image11.jpg"
logo12 = "image12.png"
logo13 = "a.png"
logo14 = "b.png"
logo15 = "c.png"
logo16 = "d.png"

c.drawImage(logo11,0*inch,6*inch,width=12*inch,height=3*inch,preserveAspectRatio = True)
drawing = svg2rlg(logo)
scaleFactor = 1./0.9
drawing.width *= scaleFactor
drawing.height *= scaleFactor
drawing.scale(scaleFactor, scaleFactor)
renderPDF.draw(drawing, c, 30, 582)

textobject = c.beginText()
textobject.setTextOrigin(0.25*inch, 5.5*inch)
c.setFont('Helvetica', 7)
c.setFillColorRGB(0,0,0)
textobject.textLines('''
Dieses Dokument dient als Leitfaden fur Kontrollen von
Dieses Dokument dient als Leitfaden fur Kontrollen von
Dieses Dokument dient als Leitfaden fur Kontrollen von
Dieses Dokument dient als Leitfaden fur Kontrollen von
Dieses Dokument dient als Leitfaden fur Kontrol
''')
c.drawText(textobject)

textobject = c.beginText()
textobject.setTextOrigin(0.25*inch,  4.7*inch)
c.setFont('Helvetica-Bold', 8)
c.setFillColorRGB(0,0,0)
textobject.textLines('''
1.Ablegekriterien fur CTP Seile''')
c.drawText(textobject)

textobject = c.beginText()
textobject.setTextOrigin(0.25*inch, 4.57*inch)
c.setFont('Helvetica', 7)
c.setFillColorRGB(0,0,0)
textobject.textLines('''
Dieses Dokument dient als Leitfaden fur Kontrollen von
Dieses Dokument dient als Leitfaden fur Kontrollen von
Dieses Dokument dient als Leitfaden fur Kontrollen von
Dieses Dokument dient als Leitfaden fur Kontrol
''')
c.drawText(textobject)

textobject = c.beginText()
textobject.setTextOrigin(0.25*inch, 4*inch)
c.setFont('Helvetica', 7)
c.setFillColorRGB(0,0,0)
textobject.textLines('''
Dieses Dokument dient als Leitfaden fur Kontrollen von
Dieses Dokument dient als Leitfaden fur Kontrollen von
Dieses Dokument dient als Leitfaden fur Kontrollen von
Dieses Dokument dient
''')
c.drawText(textobject)

textobject = c.beginText()
textobject.setTextOrigin(0.17*inch,  3.55*inch)
c.setFont('Helvetica-Bold', 10)
c.setFillColorRGB(0,0,0)
textobject.textLines('''
.''')
c.drawText(textobject)

textobject = c.beginText()
textobject.setTextOrigin(0.25*inch, 3.52*inch)
c.setFont('Helvetica', 7)
c.setFillColorRGB(0,0,0)
textobject.textLines('''
Dieses Dokument dient als Leitfaden fur Kontrollen von
Dieses Dokument dient als Leitfaden fur Kontrollen von
Dieses Dokument dient als
''')
c.drawText(textobject)

c.drawImage(logo12,2.85*inch,4.8*inch,width=1.2*inch,height=0.8*inch)

textobject = c.beginText()
textobject.setTextOrigin(4.10*inch, 5.3*inch)
c.setFont('Helvetica', 5.3)
c.setFillColorRGB(0,0,0)
textobject.textLines('''
Unbeschadigte Seile im Aufzugens-
Unbeschadigte Seile im Aufzugens-
Unbeschadigte Seile im Aufzugens-
Unbeschadigte Seile im Aufzugens-
Unbeschadigte Seile im Aufzugens-
Unbeschadigte Sei.
''')
c.drawText(textobject)

textobject = c.beginText()
textobject.setTextOrigin(2.85*inch, 4.6*inch)
c.setFont('Helvetica', 7)
c.setFillColorRGB(0,0,0)
textobject.textLines('''
Wahrend der Seil-Kontrolle sollte stets eine Prufung auf
Wahrend der Seil-Kontrolle sollte stets eine Prufung auf
Wahrend der Seil-Kontrolle sollte stets eine Prufung auf
Wahrend der Seil-Kontrolle sollte stets eine Pruf
''')
c.drawText(textobject)

textobject = c.beginText()
textobject.setTextOrigin(2.85*inch, 4.1*inch)
c.setFont('Helvetica', 5.3)
c.setFillColorRGB(0,0,0)
textobject.textLines('''
(1)
''')
c.drawText(textobject)

textobject = c.beginText()
textobject.setTextOrigin(3*inch, 4.1*inch)
c.setFont('Helvetica', 5.3)
c.setFillColorRGB(0,0,0)
textobject.textLines('''
Jede Richtungsanderung wird von der Aufzugssteuerung als eine Fahr
Jede Richtungsanderung wird von der Aufzugssteuerung als eine Fahr
Jede Richtungsanderung
''')
c.drawText(textobject)

textobject = c.beginText()
textobject.setTextOrigin(2.85*inch, 3.75*inch)
c.setFont('Helvetica', 5.3)
c.setFillColorRGB(0,0,0)
textobject.textLines('''
(2)
''')
c.drawText(textobject)

textobject = c.beginText()
textobject.setTextOrigin(3*inch, 3.75*inch)
c.setFont('Helvetica', 5.3)
c.setFillColorRGB(0,0,0)
textobject.textLines('''
Ubermassige Verschleiss oder Beschadigungen, wie unten dargestellt,
Ubermassige Verschleiss oder Beschadigungen, wie unten dargestellt,
Ubermassige Verschleiss oder Beschadigungen, wie unten dargestellt,
Ubermassige Verschleiss oder Beschadigungen, wie unten dargestellt,
Ubermassige Verschleiss oder Beschadigungen, wie unten dargestellt,
Ubermassige Verschleiss
''')
c.drawText(textobject)

textobject = c.beginText()
textobject.setTextOrigin(5.6*inch,  5.5*inch)
c.setFont('Helvetica-Bold', 8)
c.setFillColorRGB(0,0,0)
textobject.textLines('''
2.Spezifikationenen der Aufzugsanlage''')
c.drawText(textobject)

textobject = c.beginText()
textobject.setTextOrigin(5.6*inch, 5.35*inch)
c.setFont('Helvetica', 7)
c.setFillColorRGB(0,0,0)
textobject.textLines('''
Nur an Hand der Spezifikationenen Daten der Aufzugsanlage
Nur an Hand der Spezifikationenen Daten der Aufzugsanlage
Nur an Hand der Spezifikationenen Daten der Aufzugsanlage
Nur an Hand der Spezifikationenen Daten der
''')
c.drawText(textobject)

textobject = c.beginText()
textobject.setTextOrigin(8.4*inch,  5.5*inch)
c.setFont('Helvetica-Bold', 8)
c.setFillColorRGB(0,0,0)
textobject.textLines('''
3.Sichtprufung''')
c.drawText(textobject)

textobject = c.beginText()
textobject.setTextOrigin(8.4*inch, 5.25*inch)
c.setFont('Helvetica', 7)
c.setFillColorRGB(0,0,0)
textobject.textLines('''
Zusatzlich sind externe Faktoren , die sich auf das Seil
Zusatzlich sind externe Faktoren , die sich auf das Seil
Zusatzlich sind externe Faktoren , die sich auf das Seil
Zusatzlich sind externe Faktoren , die sich auf das Seil
Zusatzlich sind externe:
''')
c.drawText(textobject)

textobject = c.beginText()
textobject.setTextOrigin(8.35*inch, 4.55*inch)
c.setFont('Helvetica', 7)
c.setFillColorRGB(0,0,0)

dat = [
'Gebrochene Drahte die, die Ummantelung durchbohren',
'Gebrochene Drahte die, die Ummantelung durchbohren',
'Gebrochene Drahte die, die Ummantelung durchbohren',
'Gebrochene Drahte die, die Ummantelung durchbohren',
'Gebrochene Drahte die, die Ummantelung durchbohren',
'Gebrochene Drahte die, die Ummantelung durchbohren',
]

for i in dat:
    textobject.textLines(". %s"%(i))

c.drawText(textobject)

textobject = c.beginText()
textobject.setTextOrigin(8.4*inch, 3.6*inch)
c.setFont('Helvetica', 7)
c.setFillColorRGB(0,0,0)
textobject.textLines('''
Zusatzlich sind externe Faktoren , die sich auf das Seil
''')
c.drawText(textobject)

textobject = c.beginText()
textobject.setTextOrigin(8.35*inch, 3.35*inch)
c.setFont('Helvetica', 7)
c.setFillColorRGB(0,0,0)

data = [
'Kommen Seile mit Teilen des Aufzugs oder dem Schaft',
'Kommen Seile mit Teilen des Aufzugs oder dem Schaft',
'Kommen Seile mit Teilen des Aufzugs oder dem Schaft',
'Kommen Seile mit Teilen des Aufzugs oder dem Schaft',
]

for i in data:
    textobject.textLines(". %s"%(i))

c.drawText(textobject)

textobject = c.beginText()
textobject.setTextOrigin(8.4*inch, 2.7*inch)
c.setFont('Helvetica', 7)
c.setFillColorRGB(0,0,0)
textobject.textLines('''
Zusatzlich sind externe Faktoren , die sich auf das Seil
Zusatzlich sind externe Faktoren , die sich auf das Seil
Zusatzlich sind externe Faktoren , die sich auf das Seil
Zusatzlich sind externe:
''')
c.drawText(textobject)

c.setFillColor('#EEE8AA')
c.rect(405, 3.3*inch, 2.6*inch, 1.5*inch,stroke=0,fill=1)

textobject = c.beginText()
textobject.setTextOrigin(5.7*inch, 4.67*inch)
c.setFont('Helvetica-Bold', 7.5)
c.setFillColorRGB(0,0,0)
textobject.textLines('''
Sicherheitshinweise
''')
c.drawText(textobject)

textobject = c.beginText()
textobject.setTextOrigin(5.7*inch, 4.55*inch)
c.setFont('Helvetica', 6.8)
c.setFillColorRGB(0,0,0)
textobject.textLines('''
Die meisten dieser Prufungen sind bei laufendem Aufzung
Die meisten dieser Prufungen sind bei laufendem Aufzung
Die meisten dieser Prufungen sind bei laufendem Aufzung
Die meisten dieser Prufungen sind bei laufendem Aufzung
Die meisten dieser Prufungen sind bei laufendem Aufzung
Die meisten.
''')
c.drawText(textobject)

textobject = c.beginText()
textobject.setTextOrigin(5.7*inch, 3.8*inch)
c.setFont('Helvetica', 6.8)
c.setFillColorRGB(0,0,0)
textobject.textLines('''
Die meisten dieser Prufungen sind bei laufendem Aufzung
Die meisten dieser Prufungen sind bei laufendem Aufzung
Die meisten dieser Prufungen sind bei laufendem Aufzung
Die meisten dieser Prufungen sind bei laufendem Aufzung
Die meisten.
''')
c.drawText(textobject)


p1 = ['Beschreibung der Kunststoffummantelung']



c.setFillColor('#EEE8AA')
c.rect(18, 0.68*inch, 8*inch, 2.4*inch,stroke=0,fill=1)

c.drawString(30,150,'Ablegekriterien')


textobject = c.beginText()
textobject.setTextOrigin(0.4*inch,  2.9*inch)
c.setFont('Helvetica-Bold', 8)
c.setFillColorRGB(0,0,0)
textobject.textLines('''
Ablegekriterien''')
c.drawText(textobject)


# Headers
hdescrpcion = Paragraph('''<para align = "RIGHT">|</para>''', styleBH)
hpartida = Paragraph('<para fontsize=7 align = "CENTER"><b>A</b></para>', styleBH)
h1 = Paragraph('''<para align = "LEFT">|</para>''', styleBH)
hcandidad = Paragraph('<para fontsize=7 align = "CENTER" leftindent = -5 align="LEFT"><b>B</b></para>', styleBH)
h2 = Paragraph('''|''', styleBH)
hprecio_unitario = Paragraph('<para fontsize=7 leftindent = -40 align="LEFT"><b>C</b></para>', styleBH)
h3 = Paragraph('''<para  leftindent = -130 align = "CENTER">|</para>''', styleBH)
hprecio_total = Paragraph('<para fontsize=7 align="CENTER" leftindent = -140 align="CENTER"><b>D</b></para>', styleBH)
h4 = Paragraph('''<para  align = "LEFT" leftindent = -70>|</para>''', styleBH)
hprecio_empty1 = Paragraph(''+''' ''', styleBH)
hprecio_empty2 = Paragraph(''+''' ''', styleBH)


descrpcion = Paragraph('<para fontsize=5><b>Problem</b></para>', styleN)
partida = Paragraph('<para fontsize=5>Beschadigung der <br\>Kunststoffummantelung</para>', styleN)
candidad = Paragraph('<para fontsize=5>Drahbruch</para>', styleN)
precio_unitario = Paragraph('<para fontsize=4>Massive Bruche von Drahten</para>', styleN)
precio_total = Paragraph('<para fontsize=4>Litzenbrunch</para>', styleN)
precio_empty1 = Paragraph('<para fontsize=4>Seil aus der Rille</para>', styleN)
precio_empty2 = Paragraph('<para fontsize=4> Image1 </para>', styleN)
# precio_empty3 = Paragraph('<para fontsize=4> Image2 </para>', styleN)




descrpcio = Paragraph('<para fontsize=5><b>Beschreibung</b></para>', styleN)
partid = Paragraph('<para fontsize=4>Kunststoffummantelung ist so <br/>abgenutzt, dass der mettallische</para>', styleN)
candida = Paragraph('<para fontsize=4>Mehr als 10 Drahte ragen<br/>aus dem TPU-Mantel</para>', styleN)
precio_unitari = Paragraph('<para fontsize=4>Mehr als 3 Drahte ragen aus   dem</para>', styleN)
precio_tota = Paragraph('<para fontsize=4>spezifischer Seilbruch</para>', styleN)
precio_empty = Paragraph('<para fontsize=4>Seil ist aus seiner<br/>ursprunglichen Rille</para>', styleN)
# precio_empty = Paragraph('<para fontsize=4> Image1 </para>', styleN)





descrpci = Paragraph('<para fontsize=5><b>Korrektur-massnahme</b></para>', styleN)
parti = Paragraph('<para fontsize=4>Bericht an<br/>Brugg Lifting senden.</para>', styleN)
candid = Paragraph('<para fontsize=4>Bericht an<br/>Brugg Lifting senden.</para>', styleN)
precio_unitar = Paragraph('<para fontsize=4>Bericht an<br/>Brugg Lifting senden.</para>', styleN)
precio_tot = Paragraph('<para fontsize=4>Bericht anBericht an<br/>Brugg Lifting senden.</para>', styleN)
precio_empt = Paragraph('<para fontsize=4>Bericht an<br/>Brugg Lifting senden.</para>', styleN)
precio_empt = Paragraph('<para fontsize=4> Image1 </para>', styleN)




descrpc = Paragraph('<para fontsize=5><b>Zeitskala</b></para>', styleN)
part = Paragraph('<para fontsize=4>< 2 Monate</para>', styleN)
candi = Paragraph('<para fontsize=4>2 Monate</para>', styleN)
precio_unita = Paragraph('<para fontsize=4>umgehend</para>', styleN)
precio_to = Paragraph('<para fontsize=4>umgehend</para>', styleN)
precio_emp = Paragraph('<para fontsize=4>umgehend</para>', styleN)
# precio_emp = Paragraph('<para fontsize=4> Image1 </para>', styleN)


data= [[hdescrpcion, hpartida,h1,hcandidad,h2,hprecio_unitario,h3, hprecio_total,h4, hprecio_empty1,hprecio_empty2],
       [descrpcion, partida, candidad, precio_unitario, precio_total,precio_empty1],
       [descrpcio,partid,candida,precio_unitari,precio_tota,precio_empty],
       [descrpci,parti,candid,precio_unitar,precio_tot,precio_empt],
       [descrpc,part,candi,precio_unita,precio_to,precio_emp]]

table = Table(data, colWidths=[1.6 * cm, 2.5 * cm, 2 * cm,
                               2.25* cm, 2.5 * cm, 2*cm,1*cm,1.45*cm],rowHeights =12*mm)

table.setStyle(TableStyle([
                            ('LINEABOVE',(0,1),(-1,1),0.25,colors.black),
                            ('SPAN',(2,0),(2,0)),
                            ('LINEBELOW',(0,1),(5,4),0.25,colors.black),
                            ('LINEBELOW',(0,4),(-1,-1),0.25,colors.black),
                            ('FONTSIZE', (0, 1), (-1, -1), 5),
                       ]))

table.wrapOn(c, width, height)
table.drawOn(c, 17, 60, cm)

c.drawImage(logo13,6.15*inch,1.3*inch,width=0.45*inch,height=1.3*inch)
c.drawImage(logo14,6.65*inch,1.3*inch,width=0.45*inch,height=1.3*inch)
c.drawImage(logo15,7.15*inch,1.3*inch,width=0.45*inch,height=1.3*inch)
c.drawImage(logo16,7.65*inch,1.3*inch,width=0.45*inch,height=1.3*inch)

textobject = c.beginText()
textobject.setTextOrigin(6.15*inch, 1.2*inch)
c.setFont('Helvetica', 4.5)
c.setFillColorRGB(0,0,0)
textobject.textLines('''
Jede Richtungsanderung wird von der Aufzugssteuerung als eine Fahr
Jede Richtungsanderung wird von der Aufzugssteuerung als eine Fahr
Jede Richtungsanderung
''')
c.drawText(textobject)


p = c.beginPath()
p.rect(-20, 6.07*inch, 4*inch, 0.9*inch)
p.rect(268, 6.07*inch, 8*inch, 0.2*inch)

c.clipPath(p, stroke=0)
c.linearGradient(100*mm,200*mm,100*mm,60*mm, ('#996515','#DAA520','#996515'),extend=False)
c.setFont('Helvetica-Bold', 17)
c.setFillColor(colors.black)
c.drawString(20,465,"CTP PRUFHANDBUCH")

c.showPage()

logo6 = "image6.jpeg"
logo7 ="image7.png"
logo8 = "image8.png"
logo9 = "image9.png"
logo10 ="image10.png"

c.drawImage(logo6,0*inch,6*inch,width=12*inch,height=3*inch,preserveAspectRatio = True)
drawing = svg2rlg(logo)
scaleFactor = 1./0.9
drawing.width *= scaleFactor
drawing.height *= scaleFactor
drawing.scale(scaleFactor, scaleFactor)
renderPDF.draw(drawing, c, 30, 582)

textobject = c.beginText()
textobject.setTextOrigin(0.3*inch,  5.3*inch)
c.setFont('Helvetica-Bold', 8)
c.setFillColorRGB(0,0,0)
textobject.textLines('''
4.Prufung des Ablenkwinkels''')
c.drawText(textobject)

textobject = c.beginText()
textobject.setTextOrigin(0.3*inch, 5.1*inch)
c.setFont('Helvetica', 7)
c.setFillColorRGB(0,0,0)
textobject.textLines('''
Der(gemass unserer Zertifizierung) zulassige Schragzugwinkel
Der(gemass unserer Zertifizierung) zulassige Schragzugwinkel
Der(gemass unserer Zertifizierung) zulassige Schragzugwinkel
Der(gemass unserer Zertifizierung) zulassige Schragzugwinkel
Der(gemass''')
c.drawText(textobject)

textobject = c.beginText()
textobject.setTextOrigin(0.3*inch, 4.4*inch)
c.setFont('Helvetica', 7)
c.setFillColorRGB(0,0,0)
textobject.textLines('''
Der(gemass unserer Zertifizierung) zulassige Schragzugwinkel
Der(gemass unserer Zertifizierung) zulassige Schragzugwinkel
Der(gemass unserer Zertifizierung) zulassige Schragzugwinkel
Der(gemass unserer Zertifizierung) zulassige Schragzugwinkel
Der(gemass unserer Zertifizierung) zulassige Schragzugwinkel
Der(gemass unserer Zertifizierung) zulassige Schragzugwinkel
Der(gemass unserer Zertifizierung) zulassige Schragzugwinkel
Der(gemass unserer Zertifizierung) zulassige Schragzugwinkel
Der(gemass unserer Zertifizierung) zulassige Schragzugwinkel
Der(gemass unserer Zertifizierung) zulassige Schragzugwinkel
Der(gemass unserer Zertifizierung) zulassige Schragzugwinkel
Der(gemass unserer Zertifizierung)
''')
c.drawText(textobject)

textobject = c.beginText()
textobject.setTextOrigin(0.3*inch, 2.8*inch)
c.setFont('Helvetica', 7)
c.setFillColorRGB(0,0,0)
textobject.textLines('''
Der(gemass unserer Zertifizierung) zulassige Schragzugwinkel
Der(gemass unserer Zertifizierung) zulassige Schragzugwinkel
Der(gemass unserer
''')
c.drawText(textobject)


textobject = c.beginText()
textobject.setTextOrigin(0.45*inch, 2.3*inch)
c.setFont('Helvetica', 7)
c.setFillColorRGB(0,0,0)
textobject.textLines('''
Der(gemass unserer Zertifizierung) zulassige Schragzugwi
''')
c.drawText(textobject)

textobject = c.beginText()
textobject.setTextOrigin(0.3*inch, 2.2*inch)
c.setFont('Helvetica', 7)
c.setFillColorRGB(0,0,0)
textobject.textLines('''
Der(gemass unserer Zertifizierung) zulassige Schragzugwinkel
Der(gemass unserer Zertifizierung) zulassige Schragzugwinkel
Der(gemass
''')
c.drawText(textobject)

textobject = c.beginText()
textobject.setTextOrigin(0.45*inch, 1.8*inch)
c.setFont('Helvetica', 7)
c.setFillColorRGB(0,0,0)
textobject.textLines('''
Der(gemass unserer Zertifizierung) zulassige Schragzugwin

''')
c.drawText(textobject)

textobject = c.beginText()
textobject.setTextOrigin(0.3*inch, 1.7*inch)
c.setFont('Helvetica', 7)
c.setFillColorRGB(0,0,0)
textobject.textLines('''
Der(gemass unserer Zertifizierung) zulassige Schragzugwinkel
Der(gemass unserer Zertifizierung) zulassige Schragzugwinkel
Der(gemass unserer zulassige Schragzugwinkel
''')
c.drawText(textobject)

textobject = c.beginText()
textobject.setTextOrigin(0.45*inch, 1.2*inch)
c.setFont('Helvetica', 7)
c.setFillColorRGB(0,0,0)
textobject.textLines('''
Der(gemass unserer Zertifizierung) zulassige Schragzugwin
''')
c.drawText(textobject)

textobject = c.beginText()
textobject.setTextOrigin(0.3*inch, 1.1*inch)
c.setFont('Helvetica', 7)
c.setFillColorRGB(0,0,0)
textobject.textLines('''
Der(gemass unserer Zertifizierung) zulassige Schragzugwinkel
Der(gemass
''')
c.drawText(textobject)

# c.drawImage(logo2,5.8*inch,1.3*inch,width=4.4*inch,height=2.55*inch)
#
# c.drawImage(logo2,5.8*inch,1.3*inch,width=4.4*inch,height=2.55*inch)


textobject = c.beginText()
textobject.setTextOrigin(5.8*inch,  5.3*inch)
c.setFont('Helvetica-Bold', 8)
c.setFillColorRGB(0,0,0)
textobject.textLines('''
5.Prufung der Rillenform
(Treibscheiben und Umlenkrolle)''')
c.drawText(textobject)


textobject = c.beginText()
textobject.setTextOrigin(5.8*inch, 5*inch)
c.setFont('Helvetica', 7)
c.setFillColorRGB(0,0,0)
textobject.textLines('''
Selbst wenn die Rillen der Treibscheibe und der Umlenk-
Selbst wenn die Rillen der Treibscheibe und der Umlenk-
Selbst wenn die Rillen der Treibscheibe und der Umlenk-
Selbst wenn die Rillen der Treibscheibe und der Umlenk-
Selbst wenn die Rillen der Treibscheibe und der Umlenk-
Selbst wenn die Rillen der Treibscheibe und der Umlenk-
Selbst wenn die Rillen der Treibscheibe und der Umlenk-
Selbst wenn die Rillen
''')
c.drawText(textobject)

textobject = c.beginText()
textobject.setTextOrigin(5.8*inch, 4*inch)
c.setFont('Helvetica', 7)
c.setFillColorRGB(0,0,0)
textobject.textLines('''
Selbst wenn die Rillen der Treibscheibe und der Umlenk-
Selbst wenn die Rillen
''')
c.drawText(textobject)

textobject = c.beginText()
textobject.setTextOrigin(5.8*inch, 3.7*inch)
c.setFont('Helvetica', 7)
c.setFillColorRGB(0,0,0)
textobject.textLines('''
Selbst wenn die Rillen der Treibscheibe und der Umlenk-
Selbst wenn die Rillen
Selbst wenn die Ri
Selbst wenn die Rillen der Treibscheibe und der Umlenk-
Selbst wenn die Rillen der Treibscheibe und
''')
c.drawText(textobject)

textobject = c.beginText()
textobject.setTextOrigin(8.4*inch,  5.3*inch)
c.setFont('Helvetica-Bold', 8)
c.setFillColorRGB(0,0,0)
textobject.textLines('''
5.Seilspannung''')
c.drawText(textobject)

textobject = c.beginText()
textobject.setTextOrigin(8.4*inch, 4.8*inch)
c.setFont('Helvetica', 7)
c.setFillColorRGB(0,0,0)
textobject.textLines('''
Selbst wenn die Rillen der Treibscheibe und der Uml
Selbst wenn die Rillen der Treibscheibe und der Uml
Selbst wenn die Rillen der Treibscheibe und der Uml
Selbst wenn die Rillen der Treibscheibe und der Uml
Selbst wenn die Rillen der Treibscheibe und der Uml
Selbst wenn die Rillen der Treibscheibe und der Uml
Selbst wenn die Rillen der Treibscheibe und der Uml
Selbst wenn die Rillen der Treibscheibe und der Uml
Selbst wenn die Rillen der Treibscheibe und der Uml
Selbst wenn die Rillen der Treibscheibe und der Uml
Selbst wenn die Rillen der Treibscheibe und
''')
c.drawText(textobject)

c.drawImage(logo7,3.1*inch,0.8*inch,width=1.1*inch,height=3.85*inch)

c.drawImage(logo8,4.4*inch,3.2*inch,width=1*inch,height=2.3*inch)
textobject = c.beginText()
textobject.setTextOrigin(4.6*inch, 3.1*inch)
c.setFont('Helvetica', 5)
c.setFillColorRGB(0,0,0)
textobject.textLines('''
Schragzugwinkel zwischen
Scheibe und Seil
''')
c.drawText(textobject)

c.drawImage(logo9,5.8*inch,0.8*inch,width=2.4*inch,height=2.3*inch)

textobject = c.beginText()
textobject.setTextOrigin(6.8*inch, 0.7*inch)
c.setFont('Helvetica', 7)
c.setFillColorRGB(0,0,0)
textobject.textLines('''
Brugg Rillenlehre
''')
c.drawText(textobject)
c.drawImage(logo10,8.4*inch,0.8*inch,width=2*inch,height=2.8*inch)

textobject = c.beginText()
textobject.setTextOrigin(8.6*inch, 0.7*inch)
c.setFont('Helvetica', 7)
c.setFillColorRGB(0,0,0)
textobject.textLines('''
Seilspannungsmessgerat Brugg RPM
''')
c.drawText(textobject)

p = c.beginPath()
p.rect(0.3*inch,1.2*inch, 0.1*inch, 0.1*inch)
p.rect(0.3*inch,1.8*inch,0.1*inch, 0.1*inch)
p.rect(0.3*inch,2.3*inch, 0.1*inch, 0.1*inch)
p.rect(-20, 6.07*inch, 4*inch, 0.9*inch)
p.rect(268, 6.07*inch, 8*inch, 0.2*inch)

c.clipPath(p, stroke=0)
c.linearGradient(100*mm,200*mm,100*mm,60*mm, ('#996515','#DAA520','#996515'),extend=False)

c.setFont('Helvetica', 7)
c.drawString(23,87,"3")

c.setFont('Helvetica', 7)
c.drawString(23,130,"2")

c.setFont('Helvetica', 7)
c.drawString(23,167,"1")


c.setFont('Helvetica-Bold', 17)
c.drawString(20,465,"CTP PRUFHANDBUCH")

c.showPage()
c.save()