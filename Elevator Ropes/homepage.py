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
b1 = "b1.png"
b2 = "b2.png"
b3 = "b3.png"
b4 = "b4.png"
b5 = "b5.png"
b6 = "b6.png"
b7 = "b7.png"
l1 = "e1-01.png"
rope = "ropetech.png"
bg = "img1.jpg"
logo = "brugglifting.svg"
c = Canvas("homepage.pdf",pagesize=landscape(letter))

c.linearGradient(90*mm, 150*mm, 30*mm, 70*mm, (colors.white,colors.gray),extend=True)

c.drawImage(l1,0,3*inch,width=2*inch,height=2*inch,preserveAspectRatio=True)

textobject = c.beginText()
textobject.setTextOrigin(2.1*inch, 5*inch)
textobject.setFont("Helvetica", 8)
textobject.setFillColorRGB(0,0,0)
textobject.textLines('''
                    For highest demandas on breaking force, elongation  elongation
                    and number of trips, also under difficult instalationFor highest
                    on breaking force, elongation  elongation elongationand of trips,
                    also under difficult instalationFor higheston breaking force,
                    elongation  elongation elongationand  also under difficult
                    instalation


                    For highest demandas on breaking force, elongation  elongation
                    and number of trips, also under difficultFor highest  demandas
                    on breaking force, elongation  elongation  number of     trips,
                    also under difficult instalation

                    For highest demandas on breaking  elongation  elongation
                    and number of trips, also under difficulr highestdemandas
                    on breaking force, elongation  elongation number of trips,
                    also under difficult instalation

                    and number of trips, also under difficult  highest demandas
                    on breaking force, elongation  elongation number of trips,
                    also under difficult instalation

                    and number of trips, also under  instalationFor highest
                    on breaking force, elongation   elongationand number of
                    also under difficult instalation
                      ''')
c.drawText(textobject) #End of first Page
# Second page start
c.drawImage(b1,5*inch,0*inch,width=0.5*inch,height=4*inch,preserveAspectRatio=True)
c.line(5*inch,3.2*inch,10.75*inch,3.2*inch)
c.drawCentredString(10*inch, 3*inch, "553m 1.814ft CN Tower.Tornto.CDN")
c.drawCentredString(10*inch, 2.9*inch, "553m 1.814ft CN Tower.Tornto.CDN")
c.drawCentredString(10*inch, 2.8*inch, "553m 1.814ft CN Tower.Tornto.CDN")
c.drawCentredString(10*inch, 2.7*inch, "553m 1.814ft CN Tower.Tornto.CDN")
c.drawCentredString(10*inch, 2.6*inch, "553m 1.814ft CN Tower.Tornto.CDN")
c.drawCentredString(10*inch, 2.5*inch, "553m 1.814ft CN Tower.Tornto.CDN")
c.drawCentredString(10*inch, 2.4*inch, "553m 1.814ft CN Tower.Tornto.CDN")
c.drawCentredString(10*inch, 2.3*inch, "553m 1.814ft CN Tower.Tornto.CDN")
c.drawCentredString(10*inch, 2.2*inch, "553m 1.814ft CN Tower.Tornto.CDN")
c.drawCentredString(10*inch, 1.8*inch, "553m 1.814ft CN Tower.Tornto.CDN")
c.drawCentredString(10*inch, 1.7*inch, "553m 1.814ft CN Tower.Tornto.CDN")
c.drawCentredString(10*inch, 1.6*inch, "553m 1.814ft CN Tower.Tornto.CDN")
c.drawCentredString(10*inch, 1.5*inch, "553m 1.814ft CN Tower.Tornto.CDN")
c.drawCentredString(10*inch, 1.2*inch, "553m 1.814ft CN Tower.Tornto.CDN")
c.drawCentredString(10*inch, 0.9*inch, "553m 1.814ft CN Tower.Tornto.CDN")


c.drawImage(b2,5.5*inch,0.8*inch,width=0.5*inch,height=3.8*inch,preserveAspectRatio=True)
c.line(5.75*inch,4.75*inch,10.75*inch,4.75*inch)
c.drawCentredString(10*inch, 4.5*inch, "553m 1.814ft CN Tower.Tornto.CDN")

c.drawImage(b3,5.9*inch,0.8*inch,width=0.75*inch,height=4.75*inch,preserveAspectRatio=True)
c.line(6.2*inch,5.5*inch,10.75*inch,5.5*inch)
c.drawCentredString(10*inch, 5.15*inch, "553m 1.814ft CN Tower.Tornto.CDN")
c.drawCentredString(10*inch, 5.0*inch, "553m 1.814ft CN Tower.Tornto.CDN")
c.drawCentredString(10*inch, 4.85*inch, "553m 1.814ft CN Tower.Tornto.CDN")

c.drawImage(b4,6.25*inch,0.8*inch,width=1.25*inch,height=8*inch,preserveAspectRatio=True)
c.line(7*inch,8*inch,10.75*inch,8*inch)
c.drawCentredString(10*inch, 7.75*inch, "828m 2.717ft Burj Khalifa. Dubai.UAE")
c.drawImage(b5,6.7*inch,0.8*inch,width=1.5*inch,height=5*inch,preserveAspectRatio=True)
c.line(7.5*inch,5.75*inch,10.75*inch,5.75*inch)
c.drawCentredString(10*inch, 5.65*inch, "553m 1.814ft CN Tower.Tornto.CDN")

c.drawImage(b6,7.15*inch,0.8*inch,width=1.5*inch,height=4.5*inch,preserveAspectRatio=True)
c.line(7.9*inch,5.3*inch,10.75*inch,5.3*inch)

c.drawImage(b7,7.75*inch,0.8*inch,width=1*inch,height=3.5*inch,preserveAspectRatio=True)
c.line(8.15*inch,4.35*inch,10.75*inch,4.35*inch)
c.drawCentredString(10*inch, 4.1*inch, "553m 1.814ft CN Tower.Tornto.CDN")
c.drawCentredString(10*inch, 3.5*inch, "553m 1.814ft CN Tower.Tornto.CDN")
c.line(5*inch,0.8*inch,10.75*inch,0.8*inch)




c.drawImage(bg,0*inch,6*inch,width=12*inch,height=3*inch,preserveAspectRatio=True)
drawing = svg2rlg(logo)
scaleFactor = 1./0.9
drawing.width *= scaleFactor
drawing.height *= scaleFactor
drawing.scale(scaleFactor, scaleFactor)
renderPDF.draw(drawing, c, 30, 570)
c.drawImage(rope,2.1*inch,5.6*inch,width=1*inch,height=1*inch,preserveAspectRatio=True)
black50transparent = Color( 0, 0, 0, alpha=0.5)
c.setFillColor(black50transparent)
c.rect(-20, 6.07*inch, 6.5*inch, 1*inch,stroke=0,fill=1)
blue50transparent = Color( 0, 0, 255, alpha=0.75)

c.setFont("Helvetica-Bold",30)
c.setFillColor(blue50transparent)
c.drawString(30, 6.5*inch, "GOING UP IS OUR MOTTO")

c.setFillGray(0.5)
c.rect(448,6.07*inch, 6*inch, 0.25*inch,stroke=0,fill=1)

c.showPage()
c.save()
