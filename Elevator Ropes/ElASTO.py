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

eb = "es.png"

width, height = A4
c = Canvas("Elastobuffers.pdf",pagesize=letter)
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
c.rect(-20,8.33*inch, 8.5*inch, 0.6*inch,stroke=0,fill=1)
c.setFillColor(colors.white)
c.setFont("Helvetica-Bold",13)
c.drawString(20, 8.55*inch, "ELASTOMER BUFFERS ")
c.setFont("Helvetica",9)

c.drawString(170, 8.55*inch, "for Rope Attachment")
c.drawImage(eb,20,6*inch,width=2*inch,height=2*inch,preserveAspectRatio=True)
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
di2 = Paragraph('<para lindent=-5 fontname = "Helvetica-Bold" fontsize =4>  d2<br/></para>',stylesN)
di3 = Paragraph('<para lindent=-20 fontname = "Helvetica-Bold" fontsize =4>  d3<br/></para>',stylesN)
li1 = Paragraph('<para lindent=-20 fontname = "Helvetica-Bold" fontsize =4>  L1</para>',stylesN)
li2 = Paragraph('<para lindent=-20 fontname = "Helvetica-Bold" fontsize =4>  L2</para>',stylesN)
mx = Paragraph('<para   lindent=-20  fontname = "Helvetica-Bold" fontsize =4>  max.<br/>stat.<br/>weight</para>',stylesN)
mxp = Paragraph('<para fontname = "Helvetica-Bold" fontsize =4>  max.<br/>pressure<br/>force</para>',stylesN)

itemn1 = Paragraph('<para  fontname = "Helvetica"fontsize =4  ></para>',stylesN)
tread1 = Paragraph('<para  fontname = "Helvetica" fontsize =4>mm</para>',stylesN)

di11= Paragraph('<para  fontname = "Helvetica" fontsize =4></para>',stylesN)
di21 = Paragraph('<para   lindent=-5 fontname = "Helvetica" fontsize =4>dimensions in mm<br/></para>',stylesN)
di31 = Paragraph('<para fontname = "Helvetica" fontsize =4><br/></para>',stylesN)
li11 = Paragraph('<para  fontname = "Helvetica" fontsize =4></para>',stylesN)
li21 = Paragraph('<para  fontname = "Helvetica" fontsize =4></para>',stylesN)
mx1 = Paragraph('<para  lindent=-20 fontname = "Helvetica" fontsize =4>kg</para>',stylesN)
mxp1 = Paragraph('<para  fontname = "Helvetica" fontsize =4>kN</para>',stylesN)

itemn11 = Paragraph('<para  fontname = "Helvetica"fontsize =4  >77658 *</para>',stylesN)
tread11 = Paragraph('<para   fontname = "Helvetica" fontsize =4>M12</para>',stylesN)

di111= Paragraph('<para   fontname = "Helvetica" fontsize =4>50</para>',stylesN)
di211 = Paragraph('<para  lindent=-5 fontname = "Helvetica" fontsize =4>13<br/></para>',stylesN)
di311 = Paragraph('<para   lindent=-20 fontname = "Helvetica" fontsize =4>22<br/></para>',stylesN)
li111 = Paragraph('<para   lindent=-20 fontname = "Helvetica" fontsize =4>28</para>',stylesN)
li211 = Paragraph('<para  lindent=-20 fontname = "Helvetica" fontsize =4>33</para>',stylesN)
mx11 = Paragraph('<para lindent=-20 fontname = "Helvetica" fontsize =4>170</para>',stylesN)
mxp11 = Paragraph('<para  fontname = "Helvetica" fontsize =4>6.867</para>',stylesN)

itemn111 = Paragraph('<para  fontname = "Helvetica"fontsize =4  >77658 </para>',stylesN)
tread111 = Paragraph('<para   fontname = "Helvetica" fontsize =4>M12</para>',stylesN)

di1111= Paragraph('<para    fontname = "Helvetica" fontsize =4>50</para>',stylesN)
di2111 = Paragraph('<para  lindent=-5 fontname = "Helvetica" fontsize =4>13<br/></para>',stylesN)
di3111 = Paragraph('<para   lindent=-20 fontname = "Helvetica" fontsize =4>22<br/></para>',stylesN)
li1111 = Paragraph('<para  lindent=-20 fontname = "Helvetica" fontsize =4>28</para>',stylesN)
li2111 = Paragraph('<para lindent=-20  fontname = "Helvetica" fontsize =4>33</para>',stylesN)
mx111 = Paragraph('<para  lindent=-20  fontname = "Helvetica" fontsize =4>170</para>',stylesN)
mxp111 = Paragraph('<para  fontname = "Helvetica" fontsize =4>6.867</para>',stylesN)


eb1 = [[itemn,tread,di1,di2,di3,li1,li2,mx,mxp],
        ['','','','','','','','',''],
        ['','','','','','','','',''],
        [itemn1,tread1,di11,di21,di31,li11,li21,mx1,mxp1],
        [itemn11,tread11,di111,di211,di311,li111,li211,mx11,mxp11],
        [itemn111,tread111,di1111,di2111,di3111,li1111,li2111,mx111,mxp111],
        [itemn11,tread11,di111,di211,di311,li111,li211,mx11,mxp11],
        [itemn111,tread111,di1111,di2111,di3111,li1111,li2111,mx111,mxp111],
        [itemn11,tread11,di111,di211,di311,li111,li211,mx11,mxp11],
        [itemn111,tread111,di1111,di2111,di3111,li1111,li2111,mx111,mxp111],]
ebt =Table(eb1,colWidths=[1*cm,1*cm,1*cm,1.75*cm,1*cm,1*cm,1*cm,1*cm,1.1*cm],rowHeights=3.75*mm)
ebt.setStyle(TableStyle([
                            ('LINEBELOW',(0,2),(-1,-1),0.25,colors.black),
                            ('BACKGROUND',(1,0),(-8,-1),'#DCDCDC'),
                             ('ALIGN',(0,0),(-1,-1),'CENTER'),
                             ('VALIGN',(0,0),(-1,-1),'TOP')
                       ]))
ebt.wrapOn(c,width,height)
ebt.drawOn(c,2.5*inch,5*inch)

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
