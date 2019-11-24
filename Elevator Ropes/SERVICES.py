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
bull1 = "image3.svg"
bull2 = "image3.svg"
bull3 = "image3.svg"
bull4 = "image3.svg"
bull5 = "image3.svg"
bull6 = "image3.svg"
im = "e2-2.png"
iso = "e2-3.png"
c = Canvas("SERVICES.pdf",pagesize=landscape(letter))

c.linearGradient(50*mm, 400*mm, 30*mm, 30*mm, (colors.gray,colors.white),extend=True)
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
c.setFont("Helvetica-Bold",30)
c.drawString(30, 6.5*inch, "SERVICES")
c.setFillGray(0.5)
c.rect(448,6.07*inch, 6*inch, 0.25*inch,stroke=0,fill=1)


c.setFillColor(colors.blue)
c.rect(30,5*inch, 0.5*inch, 0.5*inch,stroke=0,fill=1)
drawing = svg2rlg(bull1)
scaleFactor = 0.1/1.6
drawing.width *= scaleFactor
drawing.height *= scaleFactor
drawing.scale(scaleFactor, scaleFactor)
renderPDF.draw(drawing, c, 30,5.05*inch)
textobject = c.beginText()
textobject.setTextOrigin(1.1*inch,  5.4*inch)
c.setFont('Helvetica', 8)
c.setFillColorRGB(0,0,0)
textobject.textLines('''
Systemlieferant
Sie finden bei uns ein umfassendes Sortiment an Aufzugseilen, Zubehor -
mitteln, um ihre Bedurfnisse vollstandig abzudecker. Wir beliefern Sie
losungen oder individuell zusammengestellten Komponenten,als Einzelteile
''')
c.drawText(textobject)

c.setFillColor(colors.blue)
c.rect(30,4.2*inch, 0.5*inch, 0.5*inch,stroke=0,fill=1)
drawing = svg2rlg(bull2)
scaleFactor = 0.1/1.6
drawing.width *= scaleFactor
drawing.height *= scaleFactor
drawing.scale(scaleFactor, scaleFactor)
renderPDF.draw(drawing, c, 30,4.25*inch)
textobject = c.beginText()
textobject.setTextOrigin(1.1*inch,  4.6*inch)
c.setFont('Helvetica', 8)
c.setFillColorRGB(0,0,0)
textobject.textLines('''
Systemlieferant
Sie finden bei uns ein umfassendes Sortiment an Aufzugseilen, Zubehor -
mitteln, um ihre Bedurfnisse vollstandig abzudecker. Wir beliefern Sie
losungen oder individuell zusammengestellten Komponenten,als Einzelteile''')
c.drawText(textobject)


c.setFillColor(colors.blue)
c.rect(30,3.4*inch, 0.5*inch, 0.5*inch,stroke=0,fill=1)
drawing = svg2rlg(bull3)
scaleFactor = 0.1/1.6
drawing.width *= scaleFactor
drawing.height *= scaleFactor
drawing.scale(scaleFactor, scaleFactor)
renderPDF.draw(drawing, c, 30,3.45*inch)
textobject = c.beginText()
textobject.setTextOrigin(1.1*inch,  3.8*inch)
c.setFont('Helvetica', 8)
c.setFillColorRGB(0,0,0)
textobject.textLines('''
Systemlieferant
Sie finden bei uns ein umfassendes Sortiment an Aufzugseilen, Zubehor -
mitteln, um ihre Bedurfnisse vollstandig abzudecker. Wir beliefern Sie
losungen oder individuell zusammengestellten Komponenten,als Einzelteile''')
c.drawText(textobject)

c.setFillColor(colors.blue)
c.rect(30,2.6*inch, 0.5*inch, 0.5*inch,stroke=0,fill=1)
drawing = svg2rlg(bull2)
scaleFactor = 0.1/1.6
drawing.width *= scaleFactor
drawing.height *= scaleFactor
drawing.scale(scaleFactor, scaleFactor)
renderPDF.draw(drawing, c, 30,2.65*inch)
textobject = c.beginText()
textobject.setTextOrigin(1.1*inch,  3*inch)
c.setFont('Helvetica', 8)
c.setFillColorRGB(0,0,0)
textobject.textLines('''
Systemlieferant
Sie finden bei uns ein umfassendes Sortiment an Aufzugseilen, Zubehor -
mitteln, um ihre Bedurfnisse vollstandig abzudecker. Wir beliefern Sie
losungen oder individuell zusammengestellten Komponenten,als Einzelteile''')
c.drawText(textobject)

c.setFillColor(colors.blue)
c.rect(30,1.8*inch, 0.5*inch, 0.5*inch,stroke=0,fill=1)
drawing = svg2rlg(bull2)
scaleFactor = 0.1/1.6
drawing.width *= scaleFactor
drawing.height *= scaleFactor
drawing.scale(scaleFactor, scaleFactor)
renderPDF.draw(drawing, c, 30,1.85*inch)
textobject = c.beginText()
textobject.setTextOrigin(1.1*inch,  2.2*inch)
c.setFont('Helvetica', 8)
c.setFillColorRGB(0,0,0)
textobject.textLines('''
Systemlieferant
Sie finden bei uns ein umfassendes Sortiment an Aufzugseilen, Zubehor -
mitteln, um ihre Bedurfnisse vollstandig abzudecker. Wir beliefern Sie
losungen oder individuell zusammengestellten Komponenten,als Einzelteile''')
c.drawText(textobject)

c.setFillColor(colors.blue)
c.rect(30,1*inch, 0.5*inch, 0.5*inch,stroke=0,fill=1)
drawing = svg2rlg(bull2)
scaleFactor = 0.1/1.6
drawing.width *= scaleFactor
drawing.height *= scaleFactor
drawing.scale(scaleFactor, scaleFactor)
renderPDF.draw(drawing, c, 30,1.05*inch)
textobject = c.beginText()
textobject.setTextOrigin(1.1*inch,  1.4*inch)
c.setFont('Helvetica', 8)
c.setFillColorRGB(0,0,0)
textobject.textLines('''
Systemlieferant
Sie finden bei uns ein umfassendes Sortiment an Aufzugseilen, Zubehor -
mitteln, um ihre Bedurfnisse vollstandig abzudecker. Wir beliefern Sie
losungen oder individuell zusammengestellten Komponenten,als Einzelteile''')
c.drawText(textobject)

# Second page
c.drawImage(im,5*inch,3.15*inch,width=3*inch,height=3*inch,preserveAspectRatio=True)
c.drawImage(iso,5.5*inch,1*inch,width=1.5*inch,height=1.5*inch,preserveAspectRatio=True)

data = [['Going up is our Motto','2'],['Services','4'],['Ropes at Glance','6'],['Rope  Comparision','8'],
        ['Rope  Comparision.i-Line','9'],['',''],['Elevator Ropes.Accessories','10'],['Hoist Ropes',''],
        ['HRS','12'],['SCX9','13'],['SC8','14'],['DP9','15'],
        ['8x19','16'],['TSR','17'],['Compensation Ropes',''],['8x19.8x25','18'],
        ['6x25','19'],['Governor Ropes',''],['6x19.8x19','20'],['Desingations and Classifications','21'],
        ['APAG Threaded Swaged Sockets','22'],['Eyelet Bolt With Swaged Sockets','23'],['Wedge Socket Symmetrical','24'],['Wedge Socket Asymmetrical','26'],
        ['Elastomer Buffers','28'],['Spring','29'],['Door closing Rope Sets','30'],['Door Closing Rope Flex.Rope Clamp','31'],
        ['RPM Rope Performance Measurement Device','32'],['RLE Rope Load Equalizer','33'],['GDC Grove Depth Comparator','34'],['Rwg Rope Wear Gauge','34'],
        ['VT-Lube Lubricant','35'],['Rope Cutters','36'],['Packaging','37'],['',''],['Support','37'],['Contacts','39']
        ]
t = Table(data,colWidths=[4.25* cm, 2* cm] ,rowHeights=3.5*mm)
t.setStyle(TableStyle([
                    ('LINEABOVE',(0,0),(-1,-1),0.25,colors.white),
                    ('LINEBELOW',(0,0),(-1,-1),0.25,colors.white),
                    ('FONTSIZE', (0, 0), (-1, -1), 5),
                    ('FONTNAME',(0,6),(-2,-32),'Helvetica-Bold'),
                    ('ALIGN',(0,8),(-2,-23),'CENTER'),
                    ('LEFTPADDING',(0,8),(-2,-23),-60),
                    ('ALIGN',(0,13),(-2,-16),'CENTER'),
                    ('LEFTPADDING',(0,15),(-2,-17),-40),
                    ('ALIGN',(0,19),(-2,-10),'CENTER'),
                    ('LEFTPADDING',(0,18),(-2,-11),-40),
                    ('ALIGN',(0,20),(-2,-3),'LEFT'),
                    ('LEFTPADDING',(0,20),(-2,-3),17),
                    ('FONTNAME',(0,35),(-2,-2),'Helvetica-Bold'),
                    ('VALIGN', (0, 0), (-1, -1), 'TOP'),
                     ]))

t.wrapOn(c, 150, 100)
t.drawOn(c, 8.5*inch,0.25*inch)





c.showPage()
c.save()
