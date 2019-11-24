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
c = Canvas("EYELET.pdf",pagesize=letter)
logo = "brugglifting.svg"
bg = "image1.jpg"
eye = "eye.png"

c.drawImage(bg,0*inch,6*inch,width=12*inch,height=7.25*inch,preserveAspectRatio=True)
drawing = svg2rlg(logo)
scaleFactor = 1./0.9
drawing.width *= scaleFactor
drawing.height *= scaleFactor
drawing.scale(scaleFactor, scaleFactor)
renderPDF.draw(drawing, c, 30,10.5*inch)

c.setFillColor(colors.black)
c.rect(-50, 8.2*inch, 10*inch, 0.6*inch,stroke=0,fill=1)
c.setFillColor(colors.white)

c.setFont("Helvetica", 10)
c.drawString(160,8.4*inch, "with Swaged Thimble")
c.setFont("Helvetica-Bold", 18)
c.drawString(30,8.4*inch, "EYELET BOLT")
c.setFont("Helvetica-Bold", 18)
c.drawImage(eye,10,0,width=2*inch,height=7*inch,mask='auto')

c.setFillColor(colors.black)

textobject1 = c.beginText()
textobject1.setTextOrigin(2.5*inch, 8*inch)
textobject1.setFont("Helvetica", 7)
textobject1.textLines('''
    Produktdaten
    Vollastahseil, 9 litzen,gensondert verseilt
    Vollastahseil, 9 litzen,gensondert verseilt

      Advantages
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

itemn = Paragraph('<para  fontname = "Helvetica-Bold"fontsize =5  >item number</para>',stylesN)
rope = Paragraph('<para   fontname = "Helvetica-Bold" fontsize =5>rope-@</para>',stylesN)

d1= Paragraph('<para    fontname = "Helvetica-Bold" fontsize =5>  d1</para>',stylesN)
d2= Paragraph('<para    fontname = "Helvetica-Bold" fontsize =5>  d2</para>',stylesN)
d3= Paragraph('<para    fontname = "Helvetica-Bold" fontsize =5>  d3</para>',stylesN)
li1 = Paragraph('<para lindent=10 fontname = "Helvetica-Bold" fontsize =5>  L1</para>',stylesN)
li2 = Paragraph('<para lindent=10 fontname = "Helvetica-Bold" fontsize =5>  L2</para>',stylesN)
load = Paragraph('<para  fontname = "Helvetica-Bold" fontsize =5>  breaking <br/>load</para>',stylesN)

li5 = Paragraph('<para lindent=-20 fontname = "Helvetica" fontsize =5>dimensions in mm</para>',stylesN)
li6 = Paragraph('<para fontname = "Helvetica" fontsize =5> mm</para>',stylesN)
li7 = Paragraph('<para fontname = "Helvetica" fontsize =5> kN</para>',stylesN)

itemn0= Paragraph('<para  fontname = "Helvetica"fontsize =5  >64250</para>',stylesN)
rope0 = Paragraph('<para   fontname = "Helvetica" fontsize =5>6.0</para>',stylesN)

d10= Paragraph('<para    fontname = "Helvetica" fontsize =5>  M 12</para>',stylesN)
d20= Paragraph('<para    fontname = "Helvetica" fontsize =5>  26.0</para>',stylesN)
d30= Paragraph('<para    fontname = "Helvetica" fontsize =5>  50.0</para>',stylesN)
li10 = Paragraph('<para lindent=10 fontname = "Helvetica" fontsize =5> 260</para>',stylesN)
li20 = Paragraph('<para lindent=10 fontname = "Helvetica" fontsize =5>  60</para>',stylesN)
load0 = Paragraph('<para  fontname = "Helvetica" fontsize =5>  33.7</para>',stylesN)



apag1 = [
        [itemn,rope,d1,d2,d3,li1,li2,load],
        ['','','','','','','','','','',''],
        ['',li6,'','',li5,'','',li7],
        [itemn0,rope0,d10,d20,d30,li10,li20,load0],
        [itemn0,rope0,d10,d20,d30,li10,li20,load0],
        [itemn0,rope0,d10,d20,d30,li10,li20,load0],
        [itemn0,rope0,d10,d20,d30,li10,li20,load0],
        [itemn0,rope0,d10,d20,d30,li10,li20,load0],
        [itemn0,rope0,d10,d20,d30,li10,li20,load0],
        [itemn0,rope0,d10,d20,d30,li10,li20,load0],
        [itemn0,rope0,d10,d20,d30,li10,li20,load0],
        [itemn0,rope0,d10,d20,d30,li10,li20,load0],
        [itemn0,rope0,d10,d20,d30,li10,li20,load0],
        [itemn0,rope0,d10,d20,d30,li10,li20,load0],
        [itemn0,rope0,d10,d20,d30,li10,li20,load0],
        [itemn0,rope0,d10,d20,d30,li10,li20,load0],
        [itemn0,rope0,d10,d20,d30,li10,li20,load0],
        [itemn0,rope0,d10,d20,d30,li10,li20,load0],
        [itemn0,rope0,d10,d20,d30,li10,li20,load0],
        [itemn0,rope0,d10,d20,d30,li10,li20,load0],
        [itemn0,rope0,d10,d20,d30,li10,li20,load0],
        [itemn0,rope0,d10,d20,d30,li10,li20,load0],
        [itemn0,rope0,d10,d20,d30,li10,li20,load0],
        [itemn0,rope0,d10,d20,d30,li10,li20,load0],
        [itemn0,rope0,d10,d20,d30,li10,li20,load0],
        [itemn0,rope0,d10,d20,d30,li10,li20,load0],
        [itemn0,rope0,d10,d20,d30,li10,li20,load0],
        [itemn0,rope0,d10,d20,d30,li10,li20,load0],
        [itemn0,rope0,d10,d20,d30,li10,li20,load0],
        [itemn0,rope0,d10,d20,d30,li10,li20,load0],
        [itemn0,rope0,d10,d20,d30,li10,li20,load0],
        [itemn0,rope0,d10,d20,d30,li10,li20,load0],
        [itemn0,rope0,d10,d20,d30,li10,li20,load0],



   ]

apagt = Table(apag1, colWidths=[1.25* cm, 1.25* cm, 1.25 * cm,
                            1.25* cm, 1.25* cm,1.25* cm,1.5* cm,1.5* cm ],rowHeights=4*mm)
apagt.setStyle(TableStyle([
                     # ('LINEABOVE',(0,2),(-1,-1),0.25,colors.black),
                     # ('LINEABOVE',(0,1),(-1,-1),0.25,colors.black),
                     ('LINEBELOW',(0,1),(-4,-1),0.25,colors.black),
                     ('BACKGROUND',(1,0),(-10,-1),'#DCDCDC'),
                     ('ALIGN', (1,0), (-1, -1), 'CENTER'),
                    ('ALIGN', (0, 1), (-1, -1), 'CENTER'),
                    ('VALIGN', (0, 0), (-1, -1), 'TOP'),

                     ]))

apagt.wrapOn(c, 30, 300)
apagt.drawOn(c, 2.5*inch,0.5*inch)

textobject1 = c.beginText()
textobject1.setTextOrigin(2.5*inch, 0.4*inch)
textobject1.setFont("Helvetica", 5)
textobject1.textLines('''
                     Other sizes avaliable upon request.


''')



c.drawText(textobject1)

c.showPage()
c.save()
