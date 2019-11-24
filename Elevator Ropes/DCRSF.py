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

hrs = 'hrs.jpg'
clamp = "rclamp.png"


width, height = A4
c = Canvas("DCRSF.pdf",pagesize=letter)
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
c.rect(-20,8.33*inch, 9*inch, 0.6*inch,stroke=0,fill=1)
c.setFillColor(colors.white)
c.setFont("Helvetica-Bold",13)
c.drawString(20, 8.55*inch, "DOOR CLOSING ROPE FLEX. ROPE CLAMP")
c.setFont("Helvetica",9)


c.drawImage(hrs,30,6.5*inch,width=1.5*inch,height=1.5*inch,preserveAspectRatio=True)
c.setFillColor(colors.black)

textobject = c.beginText()
textobject.setTextOrigin(190, 8*inch)
c.setFillColor(colors.black)
textobject.setFont("Helvetica", 7)
textobject.textLines('''
                           Steel Core Rope,6 Strands, Seperate Lay
                           and number of trips, also under difficult  highest demandas
                           on breaking force, elongation  elongation number of trips,
                           also under difficult instalation''')
c.drawText(textobject)
c.setFillColor('#87CEFA')
c.rect(190,6.9*inch, 0.5*inch, 0.5*inch,stroke=0,fill=1)
textobject = c.beginText()
textobject.setTextOrigin(196, 7.25*inch)
c.setFillColor(colors.black)
textobject.setFont("Helvetica", 5)
textobject.textLines('''
                           125,000
                             N/mm2
                           18.1x10^6
                            psi''')
c.drawText(textobject)
c.drawString(194, 6.75*inch, "E-Module**")

c.setFillColor('#87CEFA')
c.rect(240,6.9*inch, 0.5*inch, 0.5*inch,stroke=0,fill=1)
textobject = c.beginText()
textobject.setTextOrigin(246, 7.25*inch)
c.setFillColor(colors.black)
textobject.setFont("Helvetica", 5)
textobject.textLines('''
                           0.104
                             %
                            1.2
                           in/100ft        ''')
c.drawText(textobject)
c.drawString(246, 6.75*inch, "Elastic")

c.setFillColor('#87CEFA')
c.rect(290,6.9*inch, 0.5*inch, 0.5*inch,stroke=0,fill=1)
textobject = c.beginText()
textobject.setTextOrigin(296, 7.25*inch)
c.setFillColor(colors.black)
textobject.setFont("Helvetica", 5)
textobject.textLines('''
                           0.13
                             %''')
c.drawText(textobject)
c.drawString(296, 6.75*inch, "permenant")


itemn = Paragraph('<para  fontname = "Helvetica-Bold"fontsize =5  >item number</para>',stylesN)
rope = Paragraph('<para  fontname = "Helvetica-Bold" fontsize =5>rope-@</para>',stylesN)
brk = Paragraph('<para  fontname = "Helvetica-Bold" fontsize =5>breaking load<br/></para>',stylesN)

weight= Paragraph('<para lindent = -15 fontname = "Helvetica-Bold" fontsize =5>weight</para>',stylesN)
con = Paragraph('<para lindent = -25 fontname = "Helvetica-Bold" fontsize =5>construction</para>',stylesN)
min = Paragraph('<para  fontname = "Helvetica-Bold" fontsize =5>min.</para>',stylesN)



# i = Paragraph('<para> </para>',stylesN)
mm0 = Paragraph('<para  fontname = "Helvetica" fontsize =5 underlineGap = 1>mm</para>',stylesN)

kN= Paragraph('<para fontname = "Helvetica" fontsize =5>kN</para>',stylesN)

kg = Paragraph('<para lindent =-15 fontname = "Helvetica" fontsize =5>kg/100m</para>',stylesN)

# c = Paragraph('<para> </para>',stylesN)
i = Paragraph('<para fontname = "Helvetica" fontsize =5>10699 </para>',stylesN)
mm1 = Paragraph('<para  fontname = "Helvetica" fontsize =5>6.0</para>',stylesN)

kN1= Paragraph('<para  fontname = "Helvetica" fontsize =5>42.7</para>',stylesN)
kg1 = Paragraph('<para lindent = -15 fontname = "Helvetica" fontsize =5>26.9</para>',stylesN)

con1 = Paragraph('<para lindent = -30 fontname = "Helvetica" fontsize =5>9x19S-PWRC 1570 UsZ.(RRL)</para>',stylesN)




dcrsf1 = [[itemn,rope,brk,weight,con],
        ['','',min,'',''],
            ['',mm0,kN,kg,''],
             [i,mm1,kN1,kg1,con1],
             [i,mm1,kN1,kg1,con1],
             [i,mm1,kN1,kg1,con1],




            ]


dcrsft = Table(dcrsf1,colWidths=[1.25*cm,1.25*cm,2*cm,2*cm,2*cm],rowHeights=4*mm)
dcrsft.setStyle(TableStyle([




                            ('BACKGROUND',(1,0),(-4,-1),'#DCDCDC'),



                            ('LINEBELOW',(0,1),(-1,-1),0.25,colors.black),

                             ('ALIGN',(0,0),(-1,-1),'CENTER'),
                            # ('ALIGN',())
                            # ('VALIGN',(0,0),(-1,-1),'TOP'),
                             ('VALIGN',(0,0),(-1,-1),'TOP')
                       ]))

dcrsft.wrapOn(c, width,height)
dcrsft.drawOn(c, 190,5.25*inch)




textobject = c.beginText()
textobject.setTextOrigin(190,4.75*inch)
c.setFillColor(colors.black)
textobject.setFont("Helvetica", 7)
textobject.textLines('''
                         Rope Clamp
                         keep the tension under control
                         ering properties at minimum overall height
                         transverse elongation

                         Advantages
                         also applicable on the counterweight side as rope length compensation



                         ''')
c.drawText(textobject)

c.drawImage(clamp,30,2*inch,width=1.5*inch,height=1.5*inch,preserveAspectRatio=True)
itemn = Paragraph('<para  fontname = "Helvetica-Bold"fontsize =5  >item number</para>',stylesN)
rope = Paragraph('<para   fontname = "Helvetica-Bold" fontsize =5>rope-@*</para>',stylesN)

di= Paragraph('<para    fontname = "Helvetica-Bold" fontsize =5>  d</para>',stylesN)
li1 = Paragraph('<para lindent=-20 fontname = "Helvetica-Bold" fontsize =5>  L1</para>',stylesN)
li2 = Paragraph('<para lindent=-20 fontname = "Helvetica-Bold" fontsize =5>  L2</para>',stylesN)
rq = Paragraph('<para   lindent=-20  fontname = "Helvetica-Bold" fontsize =5>  max.<br/>required torque</para>',stylesN)
loop = Paragraph('<para fontname = "Helvetica-Bold" fontsize =5>rode clamp/<br/>loop</para>',stylesN)


itemn1 = Paragraph('<para  fontname = "Helvetica"fontsize =5  ></para>',stylesN)
rope1 = Paragraph('<para  fontname = "Helvetica" fontsize =5>mm</para>',stylesN)

di1= Paragraph('<para  fontname = "Helvetica" fontsize =5></para>',stylesN)

li11 = Paragraph('<para lindent=-10 fontname = "Helvetica" fontsize =5>dimensions in mm</para>',stylesN)
li21 = Paragraph('<para  fontname = "Helvetica" fontsize =5></para>',stylesN)
rq1 = Paragraph('<para  lindent=-20 fontname = "Helvetica" fontsize =5>Nm</para>',stylesN)
loop1 = Paragraph('<para  fontname = "Helvetica" fontsize =5>pcs</para>',stylesN)



itemn11 = Paragraph('<para  fontname = "Helvetica"fontsize =5  >49459</para>',stylesN)
rope11 = Paragraph('<para  fontname = "Helvetica" fontsize =5>5.0</para>',stylesN)

di11= Paragraph('<para  fontname = "Helvetica" fontsize =5>M5</para>',stylesN)

li111 = Paragraph('<para lindent=-20 fontname = "Helvetica" fontsize =5>25</para>',stylesN)
li211 = Paragraph('<para lindent=-20 fontname = "Helvetica" fontsize =5>12</para>',stylesN)
rq11 = Paragraph('<para  lindent=-20 fontname = "Helvetica" fontsize =5>2.0</para>',stylesN)
loop11 = Paragraph('<para  fontname = "Helvetica" fontsize =5>3</para>',stylesN)
dcrsf2 =[[itemn,rope,di,li1,li2,rq,loop],
         ["",'','','','','',''],
         ["",'','','','','',''],

         [itemn1,rope1,di1,li11,li21,rq1,loop1],
         [itemn11,rope11,di11,li111,li211,rq11,loop11],
         [itemn11,rope11,di11,li111,li211,rq11,loop11],
         [itemn11,rope11,di11,li111,li211,rq11,loop11],
         [itemn11,rope11,di11,li111,li211,rq11,loop11],
         [itemn11,rope11,di11,li111,li211,rq11,loop11],
         [itemn11,rope11,di11,li111,li211,rq11,loop11],
         [itemn11,rope11,di11,li111,li211,rq11,loop11],
         [itemn11,rope11,di11,li111,li211,rq11,loop11],
         [itemn11,rope11,di11,li111,li211,rq11,loop11],
         [itemn11,rope11,di11,li111,li211,rq11,loop11]]
dcrsft = Table(dcrsf2,colWidths=[1.25*cm,1.25*cm,1.75*cm,1.75*cm,1.25*cm,0.75*cm,1.25*cm],rowHeights=4*mm)

dcrsft.setStyle(TableStyle([
                             # ('LINEBELOW',(0,0),(-1,0),0.25,colors.black),
                            ('LINEBELOW',(0,2),(-1,-1),0.25,colors.black),
                            # ('SPAN',(1,0),(2,0)),
                             ('BACKGROUND',(1,0),(-6,-1),'#DCDCDC'),
                            #  ('ALIGN',(0,0),(-1,-1),'CENTER'),
                              ('VALIGN',(0,0),(-1,-1),'TOP')
                       ]))

dcrsft.wrapOn(c,width,height)
dcrsft.drawOn(c,190,1*inch)

textobject = c.beginText()
textobject.setTextOrigin(190,0.85*inch)
c.setFillColor(colors.black)
textobject.setFont("Helvetica", 5)
textobject.textLines('''
                         * Corresponds to the maximum rope diameter.
                           For interim sizes of the rope diameter the next-largest clamp size is to be used



                         ''')
c.drawText(textobject)


c.showPage()
c.save()
