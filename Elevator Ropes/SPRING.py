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

spring = "spring.png"

width, height = A4
c = Canvas("spring.pdf",pagesize=letter)
c.drawImage(bg,0*inch,7.25*inch,width=12*inch,height=5*inch,preserveAspectRatio=True)
# For HRS
drawing = svg2rlg(logo)
scaleFactor = 1./0.9
drawing.width *= scaleFactor
drawing.height *= scaleFactor
drawing.scale(scaleFactor, scaleFactor)
renderPDF.draw(drawing, c, 20, 10.5*inch)
# black50transparent = Color(0,0,0, alpha=0.8)
c.setFillColor(colors.black)
c.rect(-20,8.33*inch, 4*inch, 0.6*inch,stroke=0,fill=1)
c.setFillColor(colors.white)
c.setFont("Helvetica-Bold",13)
c.drawString(20, 8.55*inch, "SPRING ")
c.drawImage(spring,20,4.5*inch,width=2*inch,height=3*inch,preserveAspectRatio=True)
textobject = c.beginText()
textobject.setTextOrigin(2.5*inch, 7.9*inch)
c.setFillColor(colors.black)
textobject.setFont("Helvetica", 5)
textobject.textLines('''
                          Product Data
                          polyurethane elastomer with cells
                          suitable for APAG, eyelet bolt, wedge socket symmetricaland asymmetrical''')
c.drawText(textobject)
textobject = c.beginText()
textobject.setTextOrigin(2.5*inch, 7.5*inch)
c.setFillColor(colors.black)
textobject.setFont("Helvetica", 5)
textobject.textLines('''
                         Advantages
                         excellent buffering properties at minimum overall height
                         transverse elongation
                         also applicable on the counterweight side as rope length compensation
                         grease- and oil resistant''')
c.drawText(textobject)

itemn = Paragraph('<para  fontname = "Helvetica-Bold"fontsize =4  >item number</para>',stylesN)
tread = Paragraph('<para   fontname = "Helvetica-Bold" fontsize =4>for <br/>tread</para>',stylesN)

di1= Paragraph('<para    fontname = "Helvetica-Bold" fontsize =4>  d1</para>',stylesN)
di2 = Paragraph('<para lindent=-45 fontname = "Helvetica-Bold" fontsize =4>  d2<br/></para>',stylesN)
di3 = Paragraph('<para lindent=-65 fontname = "Helvetica-Bold" fontsize =4>  d3<br/></para>',stylesN)
li1 = Paragraph('<para lindent=-70 fontname = "Helvetica-Bold" fontsize =4>  L1</para>',stylesN)
sprate = Paragraph('<para lindent=-70 fontname = "Helvetica-Bold" fontsize =4>spring <br/>rate</para>',stylesN)
spf = Paragraph('<para   lindent=-70  fontname = "Helvetica-Bold" fontsize =4>  spring<br/>force</para>',stylesN)

itemn1 = Paragraph('<para  fontname = "Helvetica"fontsize =4  ></para>',stylesN)
tread1 = Paragraph('<para  fontname = "Helvetica" fontsize =4>mm</para>',stylesN)
di11= Paragraph('<para  fontname = "Helvetica" fontsize =4></para>',stylesN)
di21 = Paragraph('<para   lindent=-48 fontname = "Helvetica" fontsize =4>dimensions in mm<br/></para>',stylesN)
di31 = Paragraph('<para fontname = "Helvetica" fontsize =4><br/></para>',stylesN)
li11 = Paragraph('<para  fontname = "Helvetica" fontsize =4></para>',stylesN)
sprate1 = Paragraph('<para  lindent=-70 fontname = "Helvetica" fontsize =4>N/mm2</para>',stylesN)
spf1 = Paragraph('<para lindent=-70 fontname = "Helvetica" fontsize =4>kN</para>',stylesN)

itemn12 = Paragraph('<para  fontname = "Helvetica"fontsize =4  >77658 </para>',stylesN)
tread12 = Paragraph('<para   fontname = "Helvetica" fontsize =4>M12</para>',stylesN)
di112= Paragraph('<para   fontname = "Helvetica" fontsize =4>50</para>',stylesN)
di212 = Paragraph('<para  lindent=-45 fontname = "Helvetica" fontsize =4>13<br/></para>',stylesN)
di312 = Paragraph('<para   lindent=-65 fontname = "Helvetica" fontsize =4>22<br/></para>',stylesN)
li112 = Paragraph('<para   lindent=-70 fontname = "Helvetica" fontsize =4>28</para>',stylesN)
sprate12 = Paragraph('<para  lindent=-70 fontname = "Helvetica" fontsize =4>33</para>',stylesN)
spf12 = Paragraph('<para lindent=-70 fontname = "Helvetica" fontsize =4>170</para>',stylesN)
req = Paragraph('<para  lindent=-5 fontname = "Helvetica" fontsize =4>on request</para>',stylesN)
sub = Paragraph('<para   fontname = "Helvetica" fontsize =4>substitute for 64469 of 64470</para>',stylesN)





spring1 = [[itemn,tread,di1,di2,di3,li1,sprate,spf],
        ['','','','','','','','',],
        ['','','','','','','','',],
        [itemn1,tread1,di11,di21,di31,li11,sprate1,spf1],
        [itemn12,tread12,di112,di212,di312,li112,sprate12,spf12],
        [itemn12,tread12,di112,di212,di312,li112,sprate12,spf12],
        [itemn12,tread12,di112,di212,di312,li112,sprate12,spf12],
        [itemn12,tread12,di112,di212,di312,li112,sprate12,spf12],
        [itemn12,tread12,di112,di212,di312,li112,sprate12,spf12],
        [req,tread12,di112,di212,di312,li112,sprate12,spf12],
        ['','',sub,'','','','',''],
        [itemn12,tread12,di112,di212,di312,li112,sprate12,spf12],
        [itemn12,tread12,di112,di212,di312,li112,sprate12,spf12],
]
springt =Table(spring1,colWidths=[1*cm,1*cm,2.25*cm,1.5*cm,1*cm,1*cm,1*cm,1*cm,1.1*cm],rowHeights=3.75*mm)
springt.setStyle(TableStyle([
                            ('LINEBELOW',(0,2),(-3,-1),0.25,colors.black),
                            ('BACKGROUND',(1,0),(-7,-4),'#DCDCDC'),
                             ('ALIGN',(0,0),(-1,-1),'CENTER'),
                             ('VALIGN',(0,0),(-1,-1),'TOP'),
                             ('BACKGROUND',(1,11),(-7,-1),'#DCDCDC'),
                       ]))
springt.wrapOn(c,width,height)
springt.drawOn(c,2.5*inch,5*inch)

textobject = c.beginText()
textobject.setTextOrigin(2.5*inch, 4.9*inch)
c.setFillColor(colors.black)
textobject.setFont("Helvetica", 5)
textobject.textLines('''
                        * with collar. If not expressly desired differently. we supply rope   attachments with a buffer always with a
                          collar. in case of  several buffers always the top one with collar''')
c.drawText(textobject)

c.showPage()
c.save()
