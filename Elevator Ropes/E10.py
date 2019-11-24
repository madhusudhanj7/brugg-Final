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
d = "ropetech.png"
bg = "img1.jpg"
logo = "brugglifting.svg"
c = Canvas("ER10.pdf",pagesize=landscape(letter))

c.linearGradient(10*mm, 180*mm, 30*mm, 30*mm, (colors.white,colors.gray),extend=True)

c.drawImage(bg,0*inch,6*inch,width=12*inch,height=3*inch,preserveAspectRatio=True)
drawing = svg2rlg(logo)
scaleFactor = 1./0.9
drawing.width *= scaleFactor
drawing.height *= scaleFactor
drawing.scale(scaleFactor, scaleFactor)
renderPDF.draw(drawing, c, 30, 570)
black50transparent = Color( 0, 0, 0, alpha=0.5)
c.setFillColor(black50transparent)
c.rect(-20, 6.07*inch, 6.5*inch, 1*inch,stroke=0,fill=1)
blue50transparent = Color( 0, 0, 255, alpha=0.75)
c.setFillColor(colors.white)
c.setFont("Helvetica-Bold",20)
c.drawString(30, 6.5*inch, "ELEVATOR ROPES . ACCESSORIES")
c.setFillGray(0.5)
c.rect(448,6.07*inch, 6*inch, 0.25*inch,stroke=0,fill=1)



c.drawImage(i1,280,2.7*inch,width=1.75*inch,height=2.4*inch)

textobject = c.beginText()
textobject.setTextOrigin(0.4*inch, 5.5*inch)
textobject.setFont("Helvetica", 8)
textobject.setFillColorRGB(0,0,0)
textobject.textLines('''
                    BRUGG LIFTING elevator ropes are a symbol of the highest quality.
                      ''')
c.drawText(textobject)


textobject = c.beginText()
textobject.setTextOrigin(0.4*inch, 5*inch)
textobject.setFont("Helvetica", 8)
textobject.setFillColorRGB(0,0,0)
textobject.textLines('''
                    BRUGG LIFTING elevator ropes are a symbol of the highest quality
                    BRUGG LIFTING elevator ropes are a symbol of the highest quality
                    BRUGG LIFTING elevator ropes are a symbol of the highest quality
                    BRUGG LIFTING elevator ropes are a symbol of the highest quality
                    BRUGG LIFTING elevator ropes are a symbol of the highest quality
                    BRUGG LIFTING elevator ropes are a symbol of the highest quality
                    BRUGG LIFTING elevator ropes are a symbol of the highest quality
                    BRUGG LIFTING elevator ropes are a symbol of the highest quality
                    BRUGG LIFTING elevator ropes are a symbol of the highest quality
                    BRUGG LIFTING elevator ropes are a symbol of the highest quality
                    BRUGG LIFTING elevator ropes are a symbol of the highest quality
                    BRUGG LIFTING elevator ropes are a symbol of the highest quality

                    BRUGG LIFTING elevator ropes are a symbol of the highest quality
                    BRUGG LIFTING elevator ropes are a symbol of the highest quality
                    BRUGG LIFTING elevator ropes are a symbol of the highest quality
                    BRUGG LIFTING elevator ropes are a symbol of the highest quality
                    To ensure
                      ''')
c.drawText(textobject)

textobject = c.beginText()
textobject.setTextOrigin(5.9*inch, 5*inch)
textobject.setFont("Helvetica", 8)
textobject.setFillColorRGB(0,0,0)
textobject.textLines('''
                    As system supplier we have the corresponding end termi-
                    As system supplier we have the corresponding end termi-
                    As system supplier we have th

                    As system supplier we have the corresponding end termi-
                    As system supplier we have the corresp

                    As system supplier we have the corresponding end termi-
                    As system supplier we have the corresponding end termi-
                    As system supplier we have th

                      ''')
c.drawText(textobject)

textobject = c.beginText()
textobject.setTextOrigin(1.1*inch, 0.4*inch)
textobject.setFont("Helvetica", 45)
textobject.setFillColorRGB(255,255,255)
textobject.textLines('''
                        brugglifting.com
                      ''')
c.drawText(textobject)

c.drawImage(bg,432,0.4*inch,width=4*inch,height=2.25*inch)
c.drawImage(i2,645,2.3*inch,width=1.75*inch,height=2.25*inch)
c.showPage()
c.save()
