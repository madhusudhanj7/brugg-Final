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
logo = "brugglifting.svg"
bg = "img1.jpg"
hrs = "hrs.jpg"
scx9 = "hrs.jpg"
sc8 = "hrs.jpg"
dp9 = "hrs.jpg"
X19 = "hrs.jpg"
tsr = "hrs.jpg"
x25 = "hrs.jpg"
sx25 = "hrs.jpg"
i3 = "i3.png"
i4 = "i4.png"
i5 = "i5.png"
i6 = "i6.png"
i7 = "i7.png"

width, height = A4
c = Canvas("rc1.pdf",pagesize=letter)
c.drawImage(bg,0*inch,8.25*inch,width=12*inch,height=3*inch,preserveAspectRatio=True)
# For HRS
drawing = svg2rlg(logo)
scaleFactor = 1./0.9
drawing.width *= scaleFactor
drawing.height *= scaleFactor
drawing.scale(scaleFactor, scaleFactor)
renderPDF.draw(drawing, c, 20,10.5*inch)
c.setFillColor('#696969')
c.rect(-20,8.33*inch, 17*inch, 0.75*inch,stroke=0,fill=1)

c.setFillColor(colors.white)
c.setFont("Helvetica-Bold",20)
c.drawCentredString(138, 8.55*inch, "ROPE COMPARISON")

textobject = c.beginText()
textobject.setTextOrigin(40, 7.9*inch)
c.setFillColor(colors.black)
textobject.setFont("Helvetica-Bold", 12)
textobject.textLines('''
                        Elastic Elongation
                         ''')
c.drawText(textobject)


c.drawImage(i3,40,4.2*inch,width=3.5*inch,height=3.5*inch)

c.drawImage(i4,43,0.5*inch,width=5*inch,height=3*inch)


textobject = c.beginText()
textobject.setTextOrigin(400, 7.4*inch)
c.setFillColor(colors.black)
textobject.setFont("Helvetica", 8)
textobject.textLines('''
                        Elongation of the rope occuring whenever a rope is
                        Elongation of the rope occuring whenever a rope is
                        Elongation of
                        Elongation of the rope occuring whenever a rope is
                        Elongation of the rope occuring whenever a rope is
                        Elongation of the rope occuring whenever a rope is
                        Elongation of the rope
                        Elongation of the rope occuring whenever a rope is
                        Elongation of the rope occuring whenever
                           ''')
c.drawText(textobject)

textobject = c.beginText()
textobject.setTextOrigin(40, 3.7*inch)
c.setFillColor(colors.black)
textobject.setFont("Helvetica-Bold", 12)
textobject.textLines('''
                        Permanent Elongation
                         ''')
c.drawText(textobject)

textobject = c.beginText()
textobject.setTextOrigin(400, 3.3*inch)
c.setFillColor(colors.black)
textobject.setFont("Helvetica", 8)
textobject.textLines('''
                        Elongation of the rope occuring whenever a rope is
                        Elongation of the rope occuring whenever a rope is
                        Elongation of the rope occuring whenever a rope is
                        Elongation of the rope occuring whenever a rope is
                        Elongation of the rope occurin
                        Elongation of the rope occuring whenever a rope is
                        Elongation of the rope occuring whenever a
                           ''')
c.drawText(textobject)
c.showPage()



c.drawImage(bg,0*inch,8.25*inch,width=12*inch,height=3*inch,preserveAspectRatio=True)
# For HRS
drawing = svg2rlg(logo)
scaleFactor = 1./0.9
drawing.width *= scaleFactor
drawing.height *= scaleFactor
drawing.scale(scaleFactor, scaleFactor)
renderPDF.draw(drawing, c, 20,10.5*inch)
c.setFillColor('#696969')
c.rect(-20,8.33*inch, 5.5*inch, 0.75*inch,stroke=0,fill=1)

c.rect(150,8.33*inch, 12*inch, 0.25*inch,stroke=0,fill=1)

c.setFillColor(colors.white)
c.setFont("Helvetica-Bold",20)
c.drawCentredString(178, 8.55*inch, "ROPE COMPARISON .iLINE")

textobject = c.beginText()
textobject.setTextOrigin(40, 7.9*inch)
c.setFillColor(colors.black)
textobject.setFont("Helvetica-Bold", 12)
textobject.textLines('''
                        Minimum Breaking Load
                         ''')
c.drawText(textobject)


c.drawImage(i5,40,4.7*inch,width=4*inch,height=3*inch)

c.drawImage(i6,365,1.3*inch,width=2*inch,height=2.5*inch)

c.drawImage(i7,525,0.7*inch,width=1*inch,height=3*inch)

textobject = c.beginText()
textobject.setTextOrigin(40, 3.75*inch)
c.setFillColor(colors.black)
textobject.setFont("Helvetica-Bold", 12)
textobject.textLines('''
                        iLine & Color Coding
                         ''')
c.drawText(textobject)

textobject = c.beginText()
textobject.setTextOrigin(340, 7.4*inch)
c.setFillColor(colors.black)
textobject.setFont("Helvetica", 8)
textobject.textLines('''
                        MBL represents the minimum load that can be applied
                        MBL represents the minimum
                        MBL represents the minimum load that can be applied
                        MBL represents the minimum load that can
                        MBL represents the minimum load that can be applied
                        MBL represents
                           ''')
c.drawText(textobject)

textobject = c.beginText()
textobject.setTextOrigin(40, 3.45*inch)
c.setFillColor(colors.black)
textobject.setFont("Helvetica", 8)
textobject.textLines('''
                        Correctly installed hoist ropes increase the service life and the safety.
                        Correctly installed hoist ropes increase the service life and the safety.
                        Correctly installed hoist ropes increase the service life and the safety.
                        Correctly installed hoist ropes.


                        Correctly installed hoist ropes increase the service life and the safety.
                        Correctly installed hoist ropes increase the service life and the safety.
                        Correctly installed hoist ropes.
                           ''')
c.drawText(textobject)


textobject = c.beginText()
textobject.setTextOrigin(40, 1.75*inch)
c.setFillColor(colors.black)
textobject.setFont("Helvetica-Bold", 10)
textobject.textLines('''
                        Advantages of the iLINE
                         ''')
c.drawText(textobject)

textobject = c.beginText()
textobject.setTextOrigin(40, 1.55*inch)
c.setFillColor(colors.black)
textobject.setFont("Helvetica", 8)
textobject.textLines('''
                        simple and correct installation
                        safe installation aid
                        optimizes product performance
                        colour code for the identification of the rope type
                           ''')
c.drawText(textobject)
c.showPage()
c.save()
