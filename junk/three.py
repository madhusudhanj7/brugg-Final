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
from reportlab.lib.styles import getSampleStyleSheet



styles=getSampleStyleSheet()
stylesN = styles['Normal']
stylesH =styles['Heading1']
c = Canvas("bruggliftthird.pdf",pagesize=letter)
logo = "brugglifting.svg"
bg = "image1.jpg"
product = "image3.jpg"
b = "1.png"
am = "AM.png"
j = "D.png"
c.drawImage(bg,0*inch,6*inch,width=12*inch,height=7.25*inch,preserveAspectRatio=True)
drawing = svg2rlg(logo)
scaleFactor = 1./0.9
drawing.width *= scaleFactor
drawing.height *= scaleFactor
drawing.scale(scaleFactor, scaleFactor)
renderPDF.draw(drawing, c, 30,10.5*inch)

c.drawImage(b,30,0,width=1.5*inch,height=7.75*inch,mask='auto')


textobject1 = c.beginText()
textobject1.setTextOrigin(2.5*inch, 7.5*inch)
textobject1.setFont("Helvetica", 7)
textobject1.textLines('''
    Produktdaten
    Vollastahseil, 9 litzen,gensondert verseilt
    Vollastahseil, 9 litzen,gensondert verseilt''')




c.drawText(textobject1)

textobject1 = c.beginText()
textobject1.setTextOrigin(2.5*inch, 7*inch)
textobject1.setFont("Helvetica", 7)
textobject1.textLines('''
           Vorteile
           Vollastahseil, 9 litzen,gensondert verseilt
           Vollastahseil, 9 litzen,gensondert verseilt
           Vollastahseil, 9 litzen,gensondert verseilt
           Vollastahseil, 9 litzen,gensondert verseilt
           Vollastahseil, 9 litzen,gensondert verseilt
           Vollastahseil, 9 litzen,gensondert verseilt
           Vollastahseil, 9 litzen,gensondert verseilt
           Vollastahseil, 9 litzen,gensondert verseilt


''')

c.drawText(textobject1)
c.setFont("Helvetica-Bold", 7)

c.drawString(2.5*inch, 3.1*inch, "Fur den Einsatz mit CTP 6.5mm")

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
t5.drawOn(c, 2.5*inch,2.25*inch)
c.setFont("Helvetica-Bold", 7)
c.drawString(2.5*inch, 1.7*inch, "Fur den Einsatz mit CTP 8.1mm")

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
t5.drawOn(c, 2.5*inch,0.9*inch)
d = c.beginPath()
d.rect(-50, 8.2*inch, 10*inch, 0.6*inch)
d.rect(700, 6.07*inch, 12.5*inch, 0.2*inch)
c.clipPath (d, stroke=0)
c.linearGradient(100*mm,200*mm,10*mm,100*mm, ('#F0E68C','#8B4513','#8B4513',),extend=True)
c.setFont("Helvetica", 10)
c.drawString(90,8.4*inch, "Anpress-Ausssengewinden")
c.setFont("Helvetica-Bold", 18)
c.drawString(30,8.4*inch, "APAG")
c.setFont("Helvetica-Bold", 18)
c.showPage()


c.drawImage(bg,0*inch,6*inch,width=12*inch,height=7.25*inch,preserveAspectRatio=True)

c.drawImage(j,30,200,width=0.5*inch,height=3.25*inch,mask='auto')
c.drawImage(j,70,200,width=0.5*inch,height=3*inch,mask='auto')
c.drawImage(j,110,200,width=0.5*inch,height=3*inch,mask='auto')


textobject = c.beginText()
textobject.setTextOrigin(3.5*inch, 7.5*inch)
textobject.setFont("Helvetica", 7)
textobject.textLines('''
            Produktdaten
            Vollastahseil, 9 litzen,gensondert verseilt verseilt',
            Vollastahseil, 9 litzen,gensondert verseilt',
            Vollastahseil, 9 litzen,gensondert verseiltverseiltverseilt',
            Vollastahseil, 9 litzen,gensondert verseilt',
            Vollastahseil, 9 litzen,gensondert verseiltverseiltverseilt',
            Vollastahseil, 9 litzen,gensondert verseilt',
            Vollastahseil, 9 litzen,gensondert verseilt',
            Vollastahseil, 9 litzen,gensondert verseilt verseilt verseilt',

          ''')

c.drawText(textobject)

c.drawText(textobject)
textobject = c.beginText()
textobject.setTextOrigin(3.5*inch, 6.25*inch)
textobject.setFont("Helvetica", 7)
textobject.textLines('''
'Vollastahseil, 9 litzen,gensondert verseilt ',
          'Vollastahseil, 9 litzen,gensondert verseilt',
''')
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
d.rect(-50, 8.2*inch, 10*inch, 0.6*inch)
d.rect(700, 6.07*inch, 12.5*inch, 0.2*inch)
c.clipPath (d, stroke=0)
c.linearGradient(100*mm,200*mm,100*mm,60*mm, ('#F0E68C','#8B4513'),extend=True)
c.setFont("Helvetica", 20)

c.drawString(30,8.4*inch, "SEILSCHLOSS")
c.setFont("Helvetica", 10)
c.drawString(180,8.4*inch, "symmetrisch [EN-13411-7]")





c.showPage()
c.save()

