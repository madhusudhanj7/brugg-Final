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

c = Canvas("HOIST.pdf",pagesize=landscape(letter))

c.drawImage(bg,0*inch,6*inch,width=12*inch,height=3*inch,preserveAspectRatio=True)
drawing = svg2rlg(logo)
scaleFactor = 1./0.9
drawing.width *= scaleFactor
drawing.height *= scaleFactor
drawing.scale(scaleFactor, scaleFactor)
renderPDF.draw(drawing, c, 20, 570)
black50transparent = Color(169,169,169, alpha=0.35)
c.setFillColor(black50transparent)
c.rect(150,6.07*inch, 12*inch, 0.25*inch,stroke=0,fill=1)
black50transparent = Color(0,0,0, alpha=0.5)
c.setFillColor(black50transparent)
c.rect(8*inch,2.5*inch, 12*inch, 0.25*inch,stroke=0,fill=1)
c.setFillColor(colors.white)
c.setFont("Helvetica-Bold",8)
c.drawString(160, 6.15*inch, "HOIST ROPES")
c.drawString(8*inch, 6.15*inch, "COMPENSATION ROPES")
c.setFillColor(colors.white)

c.drawString(8.1*inch, 2.6*inch, "GOVERNOR  ROPES")

black50transparent = Color( 0, 0, 0, alpha=0.5)
c.setFillColor(black50transparent)
c.rect(-20, 6.07*inch, 6.5*inch, 1*inch,stroke=0,fill=1)
blue50transparent = Color( 0, 0, 255, alpha=0.75)
c.setFillColor(colors.white)
c.setFont("Helvetica-Bold",20)
c.drawString(20, 6.5*inch, "ROPES AT A GLANCE")
c.drawImage(hrs,20,5*inch,width=0.75*inch,height=0.75*inch,preserveAspectRatio=True)
c.setFillColor(colors.black)

textobject = c.beginText()
textobject.setTextOrigin(85, 5.55*inch)
c.setFillColor(colors.black)
textobject.setFont("Helvetica-Bold", 7)
textobject.textLines('''
                           .Steel core Rope
                           .9 Strands
                           .Parallel Lay''')
c.drawText(textobject)

c.setFillColor('#1E90FF')
c.rect(150,5.15*inch, 1*inch, 0.5*inch,stroke=0,fill=1)
c.setFillColor(colors.white)
c.setFont("Helvetica-Bold",20)
c.drawCentredString(185, 5.3*inch, "HRS")

c.setFillColor('#87CEFA')
c.rect(240,5.15*inch, 0.5*inch, 0.5*inch,stroke=0,fill=1)
textobject = c.beginText()
textobject.setTextOrigin(240, 5.55*inch)
c.setFillColor(colors.black)
textobject.setFont("Helvetica", 7)
textobject.textLines('''
                           125,000
                             N/mm2
                           18.1x10^6
                            psi''')
c.drawText(textobject)

c.setFillColor('#87CEFA')
c.rect(290,5.15*inch, 0.5*inch, 0.5*inch,stroke=0,fill=1)
textobject = c.beginText()
textobject.setTextOrigin(290, 5.55*inch)
c.setFillColor(colors.black)
textobject.setFont("Helvetica", 7)
textobject.textLines('''
                           0.104
                             %
                            1.2
                           in/100ft        ''')
c.drawText(textobject)

c.setFillColor('#87CEFA')
c.rect(340,5.15*inch, 0.5*inch, 0.5*inch,stroke=0,fill=1)
textobject = c.beginText()
textobject.setTextOrigin(340, 5.55*inch)
c.setFillColor(colors.black)
textobject.setFont("Helvetica", 7)
textobject.textLines('''
                           0.13
                             %''')
c.drawText(textobject)

c.setFillColor('#87CEFA')
c.rect(390,5.15*inch, 0.5*inch, 0.5*inch,stroke=0,fill=1)
textobject0 = c.beginText()
textobject0.setTextOrigin(390, 5.55*inch)
c.setFillColor(colors.black)
textobject0.setFont("Helvetica", 7)
textobject0.textLines('''
                           < 425
                             m
                            <14000
                              ft ''')
c.drawText(textobject0)

c.drawImage(scx9,20,4*inch,width=0.75*inch,height=0.75*inch,preserveAspectRatio=True)
textobject = c.beginText()
textobject.setTextOrigin(85, 4.5*inch)
c.setFillColor(colors.black)
textobject.setFont("Helvetica-Bold", 7)
textobject.textLines('''
                           .Steel core Rope
                           .9 Strands
                           .Seperate Lay''')
c.drawText(textobject)

# c.setFillColor('#1E90FF')
# c.setFillColor(colors.white)
# c.setFont("Helvetica-Bold",20)
# c.drawString(185, 4.25*inch, "SCX9")
c.setFillColor('#1E90FF')
c.rect(150,4.25*inch, 1*inch, 0.5*inch,stroke=0,fill=1)
c.setFillColor(colors.white)
c.setFont("Helvetica-Bold",20)
c.drawCentredString(185, 4.4*inch, "SCX9")


c.setFillColor('#87CEFA')
c.rect(240,4.25*inch, 0.5*inch, 0.5*inch,stroke=0,fill=1)
textobject1 = c.beginText()
textobject1.setTextOrigin(240, 4.65*inch)
c.setFillColor(colors.black)
textobject1.setFont("Helvetica", 7)
textobject1.textLines('''
                           120,000
                             N/mm2
                           17.4x10^6
                            psi''')
c.drawText(textobject1)


c.setFillColor('#87CEFA')
c.rect(290,4.25*inch, 0.5*inch, 0.5*inch,stroke=0,fill=1)
textobject1 = c.beginText()
textobject1.setTextOrigin(290, 4.65*inch)
c.setFillColor(colors.black)
textobject1.setFont("Helvetica", 7)
textobject1.textLines('''
                           0.108
                             %
                            1.3
                          in/100ft
                           ''')
c.drawText(textobject1)

c.setFillColor('#87CEFA')
c.rect(340,4.25*inch, 0.5*inch, 0.5*inch,stroke=0,fill=1)
textobject1 = c.beginText()
textobject1.setTextOrigin(340,4.65*inch)
c.setFillColor(colors.black)
textobject1.setFont("Helvetica", 7)
textobject1.textLines('''
                           0.16
                             %
                             2
                             in/100ft''')
c.drawText(textobject1)


c.setFillColor('#87CEFA')
c.rect(390,4.25*inch, 0.5*inch, 0.5*inch,stroke=0,fill=1)
textobject1 = c.beginText()
textobject1.setTextOrigin(390, 4.65*inch)
c.setFillColor(colors.black)
textobject1.setFont("Helvetica", 7)
textobject1.textLines('''
                           <325
                             m
                            <14000ft''')
c.drawText(textobject1)

c.drawImage(sc8,20,3*inch,width=0.75*inch,height=0.75*inch,preserveAspectRatio=True)
textobject = c.beginText()
textobject.setTextOrigin(85, 3.5*inch)
c.setFillColor(colors.black)
textobject.setFont("Helvetica-Bold", 7)
textobject.textLines('''
                           .Steel core Rope
                           .9 Strands
                           .Seperate Lay''')
c.drawText(textobject)
c.setFillColor('#32CD32')
c.rect(150,3.25*inch, 1*inch, 0.5*inch,stroke=0,fill=1)
c.setFillColor(colors.white)
c.setFont("Helvetica-Bold",20)
c.drawCentredString(185, 3.4*inch, "SC8")




c.setFillColor('#32CD32')
c.rect(240,3.25*inch, 0.5*inch, 0.5*inch,stroke=0,fill=1)
textobject1 = c.beginText()
textobject1.setTextOrigin(240, 3.65*inch)
c.setFillColor(colors.black)
textobject1.setFont("Helvetica", 7)
textobject1.textLines('''
                           120,000
                             N/mm2
                           17.4x10^6
                            psi''')
c.drawText(textobject1)

c.setFillColor('#98FB98')
c.rect(290,3.25*inch, 0.5*inch, 0.5*inch,stroke=0,fill=1)
textobject1 = c.beginText()
textobject1.setTextOrigin(290, 3.65*inch)
c.setFillColor(colors.black)
textobject1.setFont("Helvetica", 7)
textobject1.textLines('''
                           0.108
                             %
                            1.3
                          in/100ft''')
c.drawText(textobject1)

c.setFillColor('#90EE90')
c.rect(340,3.25*inch, 0.5*inch, 0.5*inch,stroke=0,fill=1)
textobject1 = c.beginText()
textobject1.setTextOrigin(340, 3.65*inch)
c.setFillColor(colors.black)
textobject1.setFont("Helvetica", 7)
textobject1.textLines('''
                           0.13
                             %
                             1.6
                             in/100ft''')
c.drawText(textobject1)
c.setFillColor('#90EE90')
c.rect(390,3.25*inch, 0.5*inch, 0.5*inch,stroke=0,fill=1)
textobject1 = c.beginText()
textobject1.setTextOrigin(390, 3.65*inch)
c.setFillColor(colors.black)
textobject1.setFont("Helvetica", 7)
textobject1.textLines('''
                           <275
                             m
                            <900
                            ft''')
c.drawText(textobject1)

c.drawImage(dp9,20,2*inch,width=0.75*inch,height=0.75*inch,preserveAspectRatio=True)
textobject = c.beginText()
textobject.setTextOrigin(85, 2.55*inch)
c.setFillColor(colors.black)
textobject.setFont("Helvetica-Bold", 7)
textobject.textLines('''
                           .Wire Rope with
                            polupropylene
                            Fiber Core
                           .9 Strands
                           .Parallel Lay''')
c.drawText(textobject)
c.setFillColor('#FFFF00')
c.rect(150,2.2*inch, 1*inch, 0.5*inch,stroke=0,fill=1)
c.setFillColor(colors.black)
c.setFont("Helvetica-Bold",20)
c.drawCentredString(185, 2.35*inch, "DP9")

c.setFillColor('#FFFF00')
c.rect(240,2.2*inch, 0.5*inch, 0.5*inch,stroke=0,fill=1)
textobject1 = c.beginText()
textobject1.setTextOrigin(240, 2.6*inch)
c.setFillColor(colors.black)
textobject1.setFont("Helvetica", 7)
textobject1.textLines('''
                           120,000
                             N/mm2
                           17.4x10^6
                            psi''')
c.drawText(textobject1)
c.setFillColor('#FFFF00')
c.rect(240,2.2*inch, 0.5*inch, 0.5*inch,stroke=0,fill=1)
textobject1 = c.beginText()
textobject1.setTextOrigin(240, 2.6*inch)
c.setFillColor(colors.black)
textobject1.setFont("Helvetica", 7)
textobject1.textLines('''
                           120,000
                             N/mm2
                           17.4x10^6
                            psi''')
c.drawText(textobject1)

c.setFillColor('#FFFF00')
c.rect(290,2.2*inch, 0.5*inch, 0.5*inch,stroke=0,fill=1)
textobject1 = c.beginText()
textobject1.setTextOrigin(290, 2.6*inch)
c.setFillColor(colors.black)
textobject1.setFont("Helvetica", 7)
textobject1.textLines('''
                           120,000
                             N/mm2
                           17.4x10^6
                            psi''')
c.drawText(textobject1)

c.setFillColor('#FFFF00')
c.rect(340,2.2*inch, 0.5*inch, 0.5*inch,stroke=0,fill=1)
textobject1 = c.beginText()
textobject1.setTextOrigin(340, 2.6*inch)
c.setFillColor(colors.black)
textobject1.setFont("Helvetica", 7)
textobject1.textLines('''
                           120,000
                             N/mm2
                           17.4x10^6
                            psi''')
c.drawText(textobject1)
c.setFillColor('#FFFF00')
c.rect(390,2.2*inch, 0.5*inch, 0.5*inch,stroke=0,fill=1)
textobject1 = c.beginText()
textobject1.setTextOrigin(390, 2.6*inch)
c.setFillColor(colors.black)
textobject1.setFont("Helvetica", 7)
textobject1.textLines('''
                           120,000
                             N/mm2
                           17.4x10^6
                            psi''')
c.drawText(textobject1)

c.drawImage(X19,20,1*inch,width=0.75*inch,height=0.75*inch,preserveAspectRatio=True)
textobject = c.beginText()
textobject.setTextOrigin(85, 1.5*inch)
c.setFillColor(colors.black)
textobject.setFont("Helvetica-Bold", 7)
textobject.textLines('''
                           .Steel core Rope
                           .9 Strands
                           .Parallel Lay''')
c.drawText(textobject)
c.setFillColor(colors.white)
c.rect(150,1.2*inch, 1*inch, 0.5*inch,stroke=1,fill=1)
c.setFillColor(colors.black)
c.setFont("Helvetica-Bold",20)
c.drawCentredString(185, 1.35*inch, "8x19")

c.setFillColor(colors.white)
c.rect(240,1.2*inch, 0.5*inch, 0.5*inch,stroke=1,fill=1)
textobject1 = c.beginText()
textobject1.setTextOrigin(242, 1.6*inch)
c.setFillColor(colors.black)
textobject1.setFont("Helvetica", 7)
textobject1.textLines('''
                           120,000
                             N/mm2
                           17.4x10^6
                            psi''')
c.drawText(textobject1)

c.setFillColor(colors.white)
c.rect(290,1.2*inch, 0.5*inch, 0.5*inch,stroke=1,fill=1)
textobject1 = c.beginText()
textobject1.setTextOrigin(292, 1.6*inch)
c.setFillColor(colors.black)
textobject1.setFont("Helvetica", 7)
textobject1.textLines('''
                           120,000
                             N/mm2
                           17.4x10^6
                            psi''')
c.drawText(textobject1)

c.setFillColor(colors.white)
c.rect(340,1.2*inch, 0.5*inch, 0.5*inch,stroke=1,fill=1)
textobject1 = c.beginText()
textobject1.setTextOrigin(342, 1.6*inch)
c.setFillColor(colors.black)
textobject1.setFont("Helvetica", 7)
textobject1.textLines('''
                           120,000
                             N/mm2
                           17.4x10^6
                            psi''')
c.drawText(textobject1)
c.setFillColor(colors.white)
c.rect(390,1.2*inch, 0.5*inch, 0.5*inch,stroke=1,fill=1)
textobject1 = c.beginText()
textobject1.setTextOrigin(392, 1.6*inch)
c.setFillColor(colors.black)
textobject1.setFont("Helvetica", 7)
textobject1.textLines('''
                           120,000
                             N/mm2
                           17.4x10^6
                            psi''')
c.drawText(textobject1)

c.drawImage(tsr,20,0.1*inch,width=0.75*inch,height=0.75*inch,preserveAspectRatio=True)
textobject = c.beginText()
textobject.setTextOrigin(85, 0.6*inch)
c.setFillColor(colors.black)
textobject.setFont("Helvetica-Bold", 7)
textobject.textLines('''
                           .Steel core Rope
                           .6 Strands
                           .Zinc-Plated
                           .Seperate Lay''')
c.drawText(textobject)
c.setFillColor(colors.gray)
c.rect(150,0.2*inch, 1*inch, 0.5*inch,stroke=0,fill=1)
c.setFillColor(colors.white)
c.setFont("Helvetica-Bold",20)
c.drawCentredString(185, 0.35*inch, "TSR")

c.setFillColor(colors.gray)
c.rect(240,0.2*inch, 0.5*inch, 0.5*inch,stroke=0,fill=1)
textobject1 = c.beginText()
textobject1.setTextOrigin(242, 0.6*inch)
c.setFillColor(colors.black)
textobject1.setFont("Helvetica", 7)
textobject1.textLines('''
                           120,000
                             N/mm2
                           17.4x10^6
                            psi''')
c.drawText(textobject1)
c.setFillColor(colors.gray)
c.rect(290,0.2*inch, 0.5*inch, 0.5*inch,stroke=0,fill=1)
textobject1 = c.beginText()
textobject1.setTextOrigin(292, 0.6*inch)
c.setFillColor(colors.black)
textobject1.setFont("Helvetica", 7)
textobject1.textLines('''
                           120,000
                             N/mm2
                           17.4x10^6
                            psi''')
c.drawText(textobject1)

c.setFillColor(colors.gray)
c.rect(340,0.2*inch, 0.5*inch, 0.5*inch,stroke=0,fill=1)
textobject1 = c.beginText()
textobject1.setTextOrigin(342, 0.6*inch)
c.setFillColor(colors.black)
textobject1.setFont("Helvetica", 7)
textobject1.textLines('''
                           120,000
                             N/mm2
                           17.4x10^6
                            psi''')
c.drawText(textobject1)
c.setFillColor(colors.gray)
c.rect(390,0.2*inch, 0.5*inch, 0.5*inch,stroke=0,fill=1)
textobject1 = c.beginText()
textobject1.setTextOrigin(392, 0.6*inch)
c.setFillColor(colors.black)
textobject1.setFont("Helvetica", 7)
textobject1.textLines('''
                           120,000
                             N/mm2
                           17.4x10^6
                            psi''')
c.drawText(textobject1)
c.drawImage(X19,6.1*inch,5*inch,width=0.7*inch,height=0.75*inch,preserveAspectRatio=True)
textobject = c.beginText()
textobject.setTextOrigin(7*inch, 5.5*inch)
c.setFillColor(colors.black)
textobject.setFont("Helvetica-Bold", 7)
textobject.textLines('''
                           .Wire Rope with
                            polupropylene core
                           .8 Strands-Seale
                           ''')
c.drawText(textobject)
c.setFillColor(colors.gray)
c.rect(8*inch, 5.25*inch, 1*inch,0.5*inch,stroke=0,fill=1)
c.setFillColor(colors.white)
c.setFont("Helvetica-Bold",20)
c.drawCentredString(8.5*inch, 5.4*inch, "8X19")

c.drawImage(x25,6.1*inch,4*inch,width=0.7*inch,height=0.75*inch,preserveAspectRatio=True)
textobject = c.beginText()
textobject.setTextOrigin(7*inch, 4.5*inch)
c.setFillColor(colors.black)
textobject.setFont("Helvetica-Bold", 7)
textobject.textLines('''
                           .Wire Rope with
                            polupropylene core
                           .8 Strands-Seale
                           ''')
c.drawText(textobject)

c.setFillColor(colors.gray)
c.rect(8*inch, 4.25*inch, 1*inch,0.5*inch,stroke=0,fill=1)
c.setFillColor(colors.white)
c.setFont("Helvetica-Bold",20)
c.drawCentredString(8.5*inch, 4.4*inch, "8X25")

c.drawImage(sx25,6.1*inch,3*inch,width=0.7*inch,height=0.75*inch,preserveAspectRatio=True)
textobject = c.beginText()
textobject.setTextOrigin(7*inch, 3.5*inch)
c.setFillColor(colors.black)
textobject.setFont("Helvetica-Bold", 7)
textobject.textLines('''
                           .Wire Rope with
                            polupropylene core
                           .8 Strands-Seale
                           ''')
c.drawText(textobject)
c.setFillColor(colors.gray)
c.rect(8*inch, 3.25*inch, 1*inch,0.5*inch,stroke=0,fill=1)
c.setFillColor(colors.white)
c.setFont("Helvetica-Bold",20)
c.drawCentredString(8.5*inch, 3.4*inch, "6X25")

c.drawImage(X19,6.1*inch,1.1*inch,width=0.7*inch,height=0.75*inch,preserveAspectRatio=True)
textobject = c.beginText()
textobject.setTextOrigin(7*inch, 1.5*inch)
c.setFillColor(colors.black)
textobject.setFont("Helvetica-Bold", 7)
textobject.textLines('''
                           .Wire Rope with
                            polupropylene core
                           .6 Strands-Seale
                           ''')
c.drawText(textobject)

c.setFillColor(colors.gray)
c.rect(9.1*inch,1.25*inch, 0.5*inch, 0.5*inch,stroke=0,fill=1)
textobject1 = c.beginText()
textobject1.setTextOrigin(9.1*inch, 1.66*inch)
c.setFillColor(colors.black)
textobject1.setFont("Helvetica", 7)
textobject1.textLines('''
                           120,000
                             N/mm2
                           17.4x10^6
                            psi''')
c.drawText(textobject1)

c.setFillColor(colors.gray)
c.rect(9.75*inch,1.25*inch, 0.5*inch, 0.5*inch,stroke=0,fill=1)
textobject1 = c.beginText()
textobject1.setTextOrigin(9.75*inch, 1.66*inch)
c.setFillColor(colors.black)
textobject1.setFont("Helvetica", 7)
textobject1.textLines('''
                           120,000
                             N/mm2
                           17.4x10^6
                            psi''')
c.drawText(textobject1)

c.setFillColor(colors.gray)
c.rect(10.4*inch,1.25*inch, 0.5*inch, 0.5*inch,stroke=0,fill=1)
textobject1 = c.beginText()
textobject1.setTextOrigin(10.4*inch, 1.66*inch)
c.setFillColor(colors.black)
textobject1.setFont("Helvetica", 7)
textobject1.textLines('''
                           120,000
                             N/mm2
                           17.4x10^6
                            psi''')
c.drawText(textobject1)


c.setFillColor(colors.gray)
c.rect(8*inch, 1.25*inch, 1*inch,0.5*inch,stroke=0,fill=1)
c.setFillColor(colors.white)
c.setFont("Helvetica-Bold",20)
c.drawCentredString(8.5*inch, 1.4*inch, "6x19")
c.drawImage(X19,6.1*inch,0.1*inch,width=0.7*inch,height=0.75*inch,preserveAspectRatio=True)
textobject = c.beginText()
textobject.setTextOrigin(7*inch, 0.5*inch)
c.setFillColor(colors.black)
textobject.setFont("Helvetica-Bold", 7)
textobject.textLines('''
                           .Wire Rope with
                            polupropylene core
                           .6 Strands-Seale
                           ''')
c.drawText(textobject)
c.setFillColor(colors.gray)
c.rect(8*inch, 0.25*inch, 1*inch,0.5*inch,stroke=0,fill=1)
c.setFillColor(colors.white)
c.setFont("Helvetica-Bold",20)
c.drawCentredString(8.5*inch, 0.4*inch, "8x19")
c.setFillColor(colors.gray)
c.rect(9.1*inch,0.3*inch, 0.5*inch, 0.5*inch,stroke=0,fill=1)
textobject1 = c.beginText()
textobject1.setTextOrigin(9.1*inch, 0.66*inch)
c.setFillColor(colors.black)
textobject1.setFont("Helvetica", 7)
textobject1.textLines('''
                           120,000
                             N/mm2
                           17.4x10^6
                            psi''')
c.drawText(textobject1)

c.setFillColor(colors.gray)
c.rect(9.75*inch,0.3*inch, 0.5*inch, 0.5*inch,stroke=0,fill=1)
textobject1 = c.beginText()
textobject1.setTextOrigin(9.75*inch, 0.66*inch)
c.setFillColor(colors.black)
textobject1.setFont("Helvetica", 7)
textobject1.textLines('''
                           120,000
                             N/mm2
                           17.4x10^6
                            psi''')
c.drawText(textobject1)
c.setFillColor(colors.gray)
c.rect(10.4*inch,0.3*inch, 0.5*inch, 0.5*inch,stroke=0,fill=1)
textobject1 = c.beginText()
textobject1.setTextOrigin(10.4*inch, 0.66*inch)
c.setFillColor(colors.black)
textobject1.setFont("Helvetica", 7)
textobject1.textLines('''
                           120,000
                             N/mm2
                           17.4x10^6
                            psi''')
c.drawText(textobject1)

c.showPage()
c.save()
