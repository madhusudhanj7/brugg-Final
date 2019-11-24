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
from reportlab.lib.pagesizes import letter,landscape
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
from reportlab.graphics import shapes
from reportlab.graphics.charts.textlabels import Label
styles=getSampleStyleSheet()
stylesN = styles['Normal']
stylesH =styles['Heading1']
c = Canvas("bruggliftsecond.pdf",pagesize=landscape(letter))
logo = "brugglifting.svg"
bg = "imag1.jpg"
product = "img8.png"
wire = "imag7.png"
l1 = 'imag5.png'
l2='imag6.png'
l3='imag4.png'
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
d.rect(-20, 6.07*inch, 1.75*inch, 0.6*inch)

# d.arc(230, 130, 5, 10,startAng=90,extent=180)

c.clipPath (d, stroke=0)
c.linearGradient(10*mm,300*mm,10*mm,10*mm, ('#B8860B',white),extend=False)
c.setFont("Helvetica", 10)
c.drawString(130,440, "VOLLSTAHSEIL MIT KUNSTSTOFFMMANTELUNG")
c.setFont("Helvetica-Bold", 20)
c.drawString(30,450, "CTP")
c.setFont("Helvetica-Bold", 7)
c.drawString(2*inch, 4.6*inch, "125,000")
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

c.showPage()
logo = "brugglifting.svg"
bg = "imag1.jpg"
product = "imag3.jpg"
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
c.linearGradient(100*mm,200*mm,100*mm,60*mm, ('#F0E68C','#8B4513'),extend=False)
c.setFont("Helvetica", 10)
c.drawString(90,450, "Anpress-Ausssengewinden")
c.setFont("Helvetica-Bold", 18)
c.drawString(30,450, "APAG")
c.setFont("Helvetica-Bold", 18)
c.drawString(400,450, "SEILSCHLOSS")
c.setFont("Helvetica", 10)
c.drawString(530,450, "symmetrisch [EN-13411-7]")





c.showPage()
c.save()
