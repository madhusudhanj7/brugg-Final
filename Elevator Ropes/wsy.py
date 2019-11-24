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
from reportlab.lib.colors import Color, black, blue, red

styles=getSampleStyleSheet()
stylesN = styles['Normal']
stylesH =styles['Heading1']
i1 = "i1.png"
i2 = "i2.png"
b1 = "b1.png"
b2 = "b2.png"
b3 = "b3.png"
b4 = "b4.png"
b5 = "b5.png"
b6 = "b6.png"
b7 = "b7.png"
l1 = "e1-01.png"
i8 = "i8.png"
i9 = "i9.png"
i10 = "i10.png"
i11 = "i11.png"
i12 = "i12.png"
i13 = "i13.png"
i14 = "i14.png"
i15 = "i15.png"

rope = "ropetech.png"
bg = "img1.jpg"
logo = "brugglifting.svg"
c = Canvas("wsy.pdf",pagesize=landscape(letter))


c.drawImage(bg,0*inch,6*inch,width=12*inch,height=3*inch,preserveAspectRatio=True)
drawing = svg2rlg(logo)
scaleFactor = 1./0.9
drawing.width *= scaleFactor
drawing.height *= scaleFactor
drawing.scale(scaleFactor, scaleFactor)
renderPDF.draw(drawing, c, 30, 570)
c.drawInlineImage(rope,8*inch,5.5*inch,width=1*inch,height=1.4*inch,preserveAspectRatio=True)
black50transparent = Color( 0, 0, 0, alpha=0.5)
c.setFillColor(black50transparent)
c.rect(-20, 6.07*inch, 6.5*inch, 1*inch,stroke=0,fill=1)
blue50transparent = Color( 0, 0, 255, alpha=0.75)
c.setFillColor(colors.white)
c.setFont("Helvetica-Bold",20)
c.drawString(30, 6.5*inch, "WE SUPPORT YOU. WORLDWIDE.")
c.setFillGray(0.5)
c.rect(448,6.07*inch, 6*inch, 0.25*inch,stroke=0,fill=1)

c.drawImage(i8,25,4.2*inch,width=2.25*inch,height=1.5*inch)

c.drawImage(i9,60,2.6*inch,width=1.25*inch,height=1.5*inch)

c.drawImage(i10,58,0.4*inch,width=1.45*inch,height=1.75*inch)

c.drawImage(i11,475,5.2*inch,width=0.57*inch,height=0.5*inch)
textobject = c.beginText()
textobject.setTextOrigin(7.25*inch, 5.4*inch)
textobject.setFont("Helvetica-Bold", 8)
textobject.setFillColorRGB(0,0,0)
textobject.textLines('''
                    SWISS
                      ''')
c.drawText(textobject)

textobject = c.beginText()
textobject.setTextOrigin(6.65*inch, 5*inch)
textobject.setFont("Helvetica", 6.6)
textobject.setFillColorRGB(0,0,0)
textobject.textLines('''
                    BRUGG LIFTING
                    Wydenstrasse 36
                    5242 Birr
                    Switzerland
                    T +41 (0) 56 464 42 42
                    F +41 (0) 56 464 42 84
                    info.lifting@brugg.com
                    brugglifting.com
                      ''')
c.drawText(textobject)



c.drawImage(i11,578,5.2*inch,width=0.57*inch,height=0.5*inch)
textobject = c.beginText()
textobject.setTextOrigin(8.7*inch, 5.4*inch)
textobject.setFont("Helvetica-Bold", 8)
textobject.setFillColorRGB(0,0,0)
textobject.textLines('''
                    SWISS
                      ''')
c.drawText(textobject)
textobject = c.beginText()
textobject.setTextOrigin(7.95*inch, 5*inch)
textobject.setFont("Helvetica", 6)
textobject.setFillColorRGB(0,0,0)
textobject.textLines('''
                    BRUGG LIFTING
                    Chemin de Foret 12
                    1024 Ecublens
                    Switzerland
                    T +41 (0) 21 634 20 21
                    F +41 (0) 21 635 09 71
                    vente.lifting@brugg.com
                    brugglifting.com
                      ''')
c.drawText(textobject)




c.drawImage(i12,680,5.2*inch,width=0.57*inch,height=0.5*inch)
textobject = c.beginText()
textobject.setTextOrigin(10.1*inch, 5.4*inch)
textobject.setFont("Helvetica-Bold", 8)
textobject.setFillColorRGB(0,0,0)
textobject.textLines('''
                    USA
                      ''')
c.drawText(textobject)
textobject = c.beginText()
textobject.setTextOrigin(9.4*inch, 5*inch)
textobject.setFont("Helvetica", 6)
textobject.setFillColorRGB(0,0,0)
textobject.textLines('''
                    BRUGG LIFTING
                    1801 Parrish Drive
                    P.O. Box 551
                    US-Rome,  GA  30162-0551
                    T +1 706 235 6315
                    F +1 706 235 6035
                    lifting.usa@brugg.com
                    brugglifting.com
                      ''')
c.drawText(textobject)



c.drawImage(i13,475,3.4*inch,width=0.57*inch,height=0.5*inch)
textobject = c.beginText()
textobject.setTextOrigin(7.37*inch, 3.6*inch)
textobject.setFont("Helvetica-Bold", 8)
textobject.setFillColorRGB(0,0,0)
textobject.textLines('''
                    CHINA
                      ''')
c.drawText(textobject)
textobject = c.beginText()
textobject.setTextOrigin(6.6*inch, 3.2*inch)
textobject.setFont("Helvetica", 6)
textobject.setFillColorRGB(0,0,0)
textobject.textLines('''
                    BRUGG LIFTING
                    Plant 1, Nr. 88 Jinling
                    Suzhou Industrial Park
                    Jiangsu Province, 215121
                    P.R. China
                    T +86 512 6299 0779
                    F +86 512 6299 0774
                    lifting.cn@brugg.com
                    brugglifting.cn
                      ''')
c.drawText(textobject)



c.drawImage(i14,580,3.4*inch,width=0.57*inch,height=0.5*inch)
textobject = c.beginText()
textobject.setTextOrigin(8.8*inch, 3.6*inch)
textobject.setFont("Helvetica-Bold", 8)
textobject.setFillColorRGB(0,0,0)
textobject.textLines('''
                    DUBAI
                      ''')
c.drawText(textobject)
textobject = c.beginText()
textobject.setTextOrigin(8*inch, 3.2*inch)
textobject.setFont("Helvetica", 6)
textobject.setFillColorRGB(0,0,0)
textobject.textLines('''
                    BRUGG LIFTING
                    LOB15 -218
                    Jebel Ali Free Zone
                    Dubai
                    United Arab Emirates
                    T +971 4 887 69 91
                    F +971 4 887 69 92
                    lifting.uae@brugg.com
                    brugglifting.com
                      ''')
c.drawText(textobject)

c.drawImage(i15,680,3.4*inch,width=0.5*inch,height=0.5*inch)
textobject = c.beginText()
textobject.setTextOrigin(10.05*inch, 3.65*inch)
textobject.setFont("Helvetica-Bold", 8)
textobject.setFillColorRGB(0,0,0)
textobject.textLines('''
                    WORLDWIDE
                      ''')
c.drawText(textobject)
textobject = c.beginText()
textobject.setTextOrigin(9.4*inch, 3.1*inch)
textobject.setFont("Helvetica", 6)
textobject.setFillColorRGB(0,0,0)
textobject.textLines('''
                    Our quality products are
                    available from more than
                    20 distributing partners
                    around the world.
                      ''')
c.drawText(textobject)

textobject = c.beginText()
textobject.setTextOrigin(2.95*inch, 5.5*inch)
textobject.setFont("Helvetica", 8)
textobject.setFillColorRGB(0,0,0)
textobject.textLines('''
                    brugglifting.com The compact informative homepage
                    Our Homepage provides you with vivid depictions of our
                    range. You can intuitively make preselections to meet y
                    requirements and find your BRUGG LIFTING contacts all o
                    with just a click. For the latest information, just vis
                      ''')
c.drawText(textobject)

textobject = c.beginText()
textobject.setTextOrigin(2.95*inch, 4.5*inch)
textobject.setFont("Helvetica", 8)
textobject.setFillColorRGB(0,0,0)
textobject.textLines('''
                    RLP Calculate the service life of your ropes
                    Log in to our service life calculator on our website and
                    of your ropes to calculate their service life
                      ''')
c.drawText(textobject)

textobject = c.beginText()
textobject.setTextOrigin(2.95*inch, 3.5*inch)
textobject.setFont("Helvetica", 8)
textobject.setFillColorRGB(0,0,0)
textobject.textLines('''
                    instructions for Use Important tips for rope handling
                    Together with every rope delivered by us, you will be pro
                    illustrated  application  instructions  on  appropriate
                    transport to rope control, you will get all useful inform
                      ''')
c.drawText(textobject)

textobject = c.beginText()
textobject.setTextOrigin(2.95*inch, 1.7*inch)
textobject.setFont("Helvetica", 8)
textobject.setFillColorRGB(0,0,0)
textobject.textLines('''
                    User Reference Guide About the handling our ropes
                    Make  use  of  our  extensive  know-how  about  rope  han
                    Link on our website takes you to our User Reference Guide
                    both find comprehensive technical details and tips and ma
                    requested information via a targeted full-text search. Yo
                    data as a PDF file.
                      ''')
c.drawText(textobject)


textobject = c.beginText()
textobject.setTextOrigin(6.6*inch, 1.3*inch)
textobject.setFont("Helvetica-Bold", 35)
textobject.setFillColorRGB(0,0,0,alpha=0.4)
textobject.textLines('''
                    brugglifting.com
                      ''')
c.drawText(textobject)

textobject = c.beginText()
textobject.setTextOrigin(6.6*inch, 0.75*inch)
textobject.setFont("Helvetica-Bold", 5)
textobject.setFillColorRGB(0,0,0,alpha=0.4)
textobject.textLines('''
                    Creation date 09/2016
                    Subject to changes. Nonbinding indication of measures. No warranty for printing errors or errors.
                    If not agreed otherwise, our general conditions of sale and delivery are valid.
                    We thank OSMA-Aufzuge for the provision of the photos on the following pages 9, 15
                    Design, realization www.schaefer design.com
                      ''')
c.drawText(textobject)


c.showPage()
c.save()
