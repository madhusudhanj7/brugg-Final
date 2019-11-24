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
width, height = A4
logo = "brugglifting.svg"
bg = "image1.jpg"
product = "image3.jpg"
b = "1.png"

tss = "tss.png"
ssz = "smz.png"
dcrs1 = "dcr1.png"
dcrs2 = "dcrs2.png"
dcrs3 = "dcrs3.png"

hrs = 'hrs.jpg'
clamp = "rclamp.png"

eb = "es.png"
eye = "eye.png"

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
i16 = "i16.png"
i17 = "i17.png"
i18 = "i18.png"
i19 = "i19.png"
i20 = "i20.png"
i21 = "i21.png"
i22 = "i22.png"
i23 = "i23.png"
i24 = "i24.png"
i25 = "i25.png"
i26 = "i26.png"

rle ="rle.png"

rpm1 = "rpm1.png"
rpm2 = "rpm2.png"

spring = "spring.png"
c = Canvas("Elevatorropesletter.pdf",pagesize=letter)
c.drawImage(bg,0*inch,6*inch,width=12*inch,height=7.25*inch,preserveAspectRatio=True)
drawing = svg2rlg(logo)
scaleFactor = 1./0.9
drawing.width *= scaleFactor
drawing.height *= scaleFactor
drawing.scale(scaleFactor, scaleFactor)
renderPDF.draw(drawing, c, 30,10.5*inch)

c.drawImage(b,30,0,width=1.5*inch,height=7.75*inch,mask='auto')


textobject1 = c.beginText()
textobject1.setTextOrigin(2.5*inch, 7.5*inch)
textobject1.setFont("Helvetica", 7)
textobject1.textLines('''
    Produktdaten
    Vollastahseil, 9 litzen,gensondert verseilt
    Vollastahseil, 9 litzen,gensondert verseilt


           Vorteile
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
d4= Paragraph('<para    fontname = "Helvetica-Bold" fontsize =5>  d4</para>',stylesN)

li1 = Paragraph('<para lindent=-50 fontname = "Helvetica-Bold" fontsize =5>  L1</para>',stylesN)
li2 = Paragraph('<para lindent=-50 fontname = "Helvetica-Bold" fontsize =5>  L2</para>',stylesN)
li3 = Paragraph('<para lindent=-50 fontname = "Helvetica-Bold" fontsize =5>  L3</para>',stylesN)
li4 = Paragraph('<para lindent=-50 fontname = "Helvetica-Bold" fontsize =5>  L4</para>',stylesN)

li5 = Paragraph('<para lindent=-35 fontname = "Helvetica" fontsize =5>dimensions in mm</para>',stylesN)
li6 = Paragraph('<para fontname = "Helvetica" fontsize =5> mm</para>',stylesN)


itemn0 = Paragraph('<para  fontname = "Helvetica" fontsize =5  >10112</para>',stylesN)
rope0 = Paragraph('<para   fontname = "Helvetica" fontsize =5>6.0</para>',stylesN)

d10= Paragraph('<para    fontname = "Helvetica" fontsize =5> M 10</para>',stylesN)
d20= Paragraph('<para    fontname = "Helvetica" fontsize =5>  13</para>',stylesN)
d30= Paragraph('<para    fontname = "Helvetica" fontsize =5>  9.0</para>',stylesN)
d40= Paragraph('<para    fontname = "Helvetica" fontsize =5>  7</para>',stylesN)

li10 = Paragraph('<para lindent=-50 fontname = "Helvetica" fontsize =5>  240</para>',stylesN)
li20 = Paragraph('<para lindent=-50 fontname = "Helvetica" fontsize =5>  150</para>',stylesN)
li30 = Paragraph('<para lindent=-50 fontname = "Helvetica" fontsize =5>  66.0</para>',stylesN)
li40 = Paragraph('<para lindent=-50 fontname = "Helvetica" fontsize =5>  16.6</para>',stylesN)


apag1 = [
        [itemn,rope,d1,d2,d3,d4,'',li1,li2,li3,li4],
        ['','','','','','','','','','',''],
        ['',li6,'','','','',li5,'','','',''],
        [itemn0,rope0,d10,d20,d30,d40,'',li10,li20,li30,li40],
        [itemn0,rope0,d10,d20,d30,d40,'',li10,li20,li30,li40],
        [itemn0,rope0,d10,d20,d30,d40,'',li10,li20,li30,li40],
        [itemn0,rope0,d10,d20,d30,d40,'',li10,li20,li30,li40],
        [itemn0,rope0,d10,d20,d30,d40,'',li10,li20,li30,li40],
        [itemn0,rope0,d10,d20,d30,d40,'',li10,li20,li30,li40],
        [itemn0,rope0,d10,d20,d30,d40,'',li10,li20,li30,li40],
        [itemn0,rope0,d10,d20,d30,d40,'',li10,li20,li30,li40],
        [itemn0,rope0,d10,d20,d30,d40,'',li10,li20,li30,li40],
        [itemn0,rope0,d10,d20,d30,d40,'',li10,li20,li30,li40],
        [itemn0,rope0,d10,d20,d30,d40,'',li10,li20,li30,li40],
        [itemn0,rope0,d10,d20,d30,d40,'',li10,li20,li30,li40],
        [itemn0,rope0,d10,d20,d30,d40,'',li10,li20,li30,li40],
        [itemn0,rope0,d10,d20,d30,d40,'',li10,li20,li30,li40],
        [itemn0,rope0,d10,d20,d30,d40,'',li10,li20,li30,li40],
        [itemn0,rope0,d10,d20,d30,d40,'',li10,li20,li30,li40],
        [itemn0,rope0,d10,d20,d30,d40,'',li10,li20,li30,li40],
        [itemn0,rope0,d10,d20,d30,d40,'',li10,li20,li30,li40],
        [itemn0,rope0,d10,d20,d30,d40,'',li10,li20,li30,li40],
        [itemn0,rope0,d10,d20,d30,d40,'',li10,li20,li30,li40],
        [itemn0,rope0,d10,d20,d30,d40,'',li10,li20,li30,li40],
        [itemn0,rope0,d10,d20,d30,d40,'',li10,li20,li30,li40],
        [itemn0,rope0,d10,d20,d30,d40,'',li10,li20,li30,li40],
        [itemn0,rope0,d10,d20,d30,d40,'',li10,li20,li30,li40],
        [itemn0,rope0,d10,d20,d30,d40,'',li10,li20,li30,li40],
        [itemn0,rope0,d10,d20,d30,d40,'',li10,li20,li30,li40],
        [itemn0,rope0,d10,d20,d30,d40,'',li10,li20,li30,li40],
        [itemn0,rope0,d10,d20,d30,d40,'',li10,li20,li30,li40],
        [itemn0,rope0,d10,d20,d30,d40,'',li10,li20,li30,li40],



   ]

apagt = Table(apag1, colWidths=[1.25* cm, 1.25* cm, 1 * cm,
                            1* cm, 1* cm,1* cm,1.5* cm,1* cm,1*cm,1*cm ],rowHeights=4*mm)
apagt.setStyle(TableStyle([
                     # ('LINEABOVE',(0,2),(-1,-1),0.25,colors.black),
                     # ('LINEABOVE',(0,1),(-1,-1),0.25,colors.black),
                     ('LINEBELOW',(0,1),(-3,-1),0.25,colors.black),
                    ('FONTSIZE', (0, 0), (-1, -1), 5),
                    ('BACKGROUND',(1,0),(-10,-1),'#DCDCDC'),
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



c.setFillColor(colors.black)
c.rect(-50, 8.2*inch, 10*inch, 0.6*inch,stroke=0,fill=1)
c.setFillColor(colors.white)

c.setFont("Helvetica", 10)
c.drawString(90,8.4*inch, "Threaded Swaged Sockets")
c.setFont("Helvetica-Bold", 18)
c.drawString(30,8.4*inch, "APAG")
c.setFont("Helvetica-Bold", 18)

c.showPage()

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
c.drawString(20, 8.55*inch, "DOOR CLOSING ROPE SETS ")
c.setFont("Helvetica",9)


c.drawImage(tss,-20,5*inch,width=2*inch,height=3*inch,preserveAspectRatio=True)
c.drawImage(ssz,1*inch,4.5*inch,width=1.75*inch,height=3*inch,preserveAspectRatio=True)

c.drawImage(dcrs1,0.75*inch,3*inch,width=0.75*inch,height=0.75*inch,preserveAspectRatio=True)
c.drawImage(dcrs2,0.1*inch,2*inch,width=0.75*inch,height=0.75*inch,preserveAspectRatio=True)
c.drawImage(dcrs3,1.5*inch,2*inch,width=0.75*inch,height=0.75*inch,preserveAspectRatio=True)





textobject = c.beginText()
textobject.setTextOrigin(3*inch, 7.75*inch)
c.setFillColor(colors.black)
textobject.setFont("Helvetica", 10)
textobject.textLines('''
                         TSS-Rope Set
                         keep the tension under control
                         ering properties at minimum overall height
                         transverse elongation
                         also applicable on the counterweight side as rope length compensation
                         grease- and oil resistant

                         One packaging unit contains 5 ropes sets each

                         ''')
c.drawText(textobject)

itemn = Paragraph('<para  fontname = "Helvetica-Bold"fontsize =6  >item number</para>',stylesN)
rope = Paragraph('<para lindent=5  fontname = "Helvetica-Bold" fontsize =6>rope-@</para>',stylesN)

rope0 = Paragraph('<para lindent=5  fontname = "Helvetica-Bold"fontsize =5  >mm</para>',stylesN)


itemn2 = Paragraph('<para  fontname = "Helvetica-Bold"fontsize =5>77720</para>',stylesN)
rope2 = Paragraph('<para lindent=5   fontname = "Helvetica-Bold" fontsize =5>3.0</para>',stylesN)



tss1 =[[itemn,rope],
         ['',''],
         ['',''],
        ['',rope0],
        [itemn2,rope2],

]
tsst = Table(tss1,colWidths=[1.25*cm,1.35*cm],rowHeights=4*mm)
tsst.setStyle(TableStyle([
                             # ('LINEBELOW',(0,0),(-1,0),0.25,colors.black),
                            ('LINEBELOW',(0,2),(-1,-1),0.25,colors.black),
                            # ('SPAN',(1,0),(2,0)),
                             ('BACKGROUND',(1,0),(-1,-1),'#DCDCDC'),
                            #  ('ALIGN',(0,0),(-1,-1),'CENTER'),
                              ('VALIGN',(0,0),(-1,-1),'TOP')
                       ]))
tsst.wrapOn(c,width,height)
tsst.drawOn(c,3*inch,5.5*inch)



textobject = c.beginText()
textobject.setTextOrigin(3*inch, 5*inch)
c.setFillColor(colors.black)
textobject.setFont("Helvetica", 10)
textobject.textLines('''
                         SMZ-Rope Set
                         keep the tension under control
                         ering properties at minimum overall height
                         transverse elongation
                         also applicable on the counterweight side as rope length compensation
                         grease- and oil resistant
                         keep the tension under control
                         ering properties at minimum overall height
                         transverse elongation
                         also applicable on the counterweight side as rope length compensation
                         grease- and oil resistant

                         Advantages
                         keep the tension under control
                         ering properties at minimum overall height
                         transverse elongation
                         also applicable on the counterweight side as rope length compensation
                         grease- and oil resistant


                         ''')
c.drawText(textobject)

itemn = Paragraph('<para  fontname = "Helvetica-Bold"fontsize =6  >item number</para>',stylesN)
rope = Paragraph('<para lindent=5  fontname = "Helvetica-Bold" fontsize =6>rope-@</para>',stylesN)

rope0 = Paragraph('<para lindent=5  fontname = "Helvetica-Bold"fontsize =5  >mm</para>',stylesN)


itemn2 = Paragraph('<para  fontname = "Helvetica-Bold"fontsize =5>77720</para>',stylesN)
rope2 = Paragraph('<para lindent=5   fontname = "Helvetica-Bold" fontsize =5>3.0</para>',stylesN)



smz1 =[[itemn,rope],
         ['',''],
         ['',''],
        ['',rope0],
        [itemn2,rope2],

]
smzt = Table(smz1,colWidths=[1.25*cm,1.35*cm],rowHeights=4*mm)
smzt.setStyle(TableStyle([
                             # ('LINEBELOW',(0,0),(-1,0),0.25,colors.black),
                            ('LINEBELOW',(0,2),(-1,-1),0.25,colors.black),
                            # ('SPAN',(1,0),(2,0)),
                             ('BACKGROUND',(1,0),(-1,-1),'#DCDCDC'),
                            #  ('ALIGN',(0,0),(-1,-1),'CENTER'),
                              ('VALIGN',(0,0),(-1,-1),'TOP')
                       ]))
smzt.wrapOn(c,width,height)
smzt.drawOn(c,3*inch,1*inch)
#


c.showPage()

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
c.drawCentredString(70, 8.55*inch, "GDC")

c.setFillColor(colors.white)
c.setFont("Helvetica-Bold",14)
c.drawCentredString(180, 8.55*inch, "Grove Depth Comparator")

c.setFillColor(colors.white)
c.setFont("Helvetica-Bold",20)
c.drawCentredString(300, 8.55*inch, ". RWG")

c.setFillColor(colors.white)
c.setFont("Helvetica-Bold",14)
c.drawCentredString(400, 8.55*inch, "Rope Wear Gauge")


textobject = c.beginText()
textobject.setTextOrigin(315, 7.7*inch)
c.setFillColor(colors.black)
textobject.setFont("Helvetica-Bold", 12)
textobject.textLines('''
                        GDC Groove Depth Comparator
                         ''')
c.drawText(textobject)

textobject = c.beginText()
textobject.setTextOrigin(315, 7.5*inch)
c.setFillColor(colors.black)
textobject.setFont("Helvetica", 8)
textobject.textLines('''
                        The GDC enables you to precisely measure and compare sheave groove
                        variations.  It  serves  to  early  detect  worn-out  drive  sheaves  and  may
                        thus help to increase the service life of ropes.
                         ''')
c.drawText(textobject)

textobject = c.beginText()
textobject.setTextOrigin(315, 6.8*inch)
c.setFillColor(colors.black)
textobject.setFont("Helvetica-Bold", 12)
textobject.textLines('''
                        Advantages
                         ''')
c.drawText(textobject)

textobject = c.beginText()
textobject.setTextOrigin(315, 6.6*inch)
c.setFillColor(colors.black)
textobject.setFont("Helvetica", 8)
textobject.textLines('''
                        Applicable for all common groove shapes
                        Very easy handling
                        Measurement in 1/100mm or 1/1000 inch
                        Measuring accuracy 5/1000mm or 5/10000 inch
                        Total weight of 190 g
                        Switching between metric and imperial system
                         ''')
c.drawText(textobject)


c.drawImage(i24,60,3.6*inch,width=2.6*inch,height=4.25*inch)

c.drawImage(i25,50,0.6*inch,width=3.4*inch,height=2.55*inch)


textobject = c.beginText()
textobject.setTextOrigin(315, 3.35*inch)
c.setFillColor(colors.black)
textobject.setFont("Helvetica-Bold", 12)
textobject.textLines('''
                        RWG Rope Wear Gauge
                           ''')
c.drawText(textobject)

textobject = c.beginText()
textobject.setTextOrigin(315, 3.15*inch)
c.setFillColor(colors.black)
textobject.setFont("Helvetica", 8)
textobject.textLines('''
                        Within seconds, the precision gauge enables you to check, whether
                        the minimum nominal diameter of the rope is below the target.
                        If below limit, the rope must be replaced
                         ''')
c.drawText(textobject)

textobject = c.beginText()
textobject.setTextOrigin(315, 2.55*inch)
c.setFillColor(colors.black)
textobject.setFont("Helvetica-Bold", 12)
textobject.textLines('''
                        Advantages
                           ''')
c.drawText(textobject)

textobject = c.beginText()
textobject.setTextOrigin(315, 2.35*inch)
c.setFillColor(colors.black)
textobject.setFont("Helvetica", 8)
textobject.textLines('''
                         Robust design in aluminum with anodized surface
                         Application in seconds
                         Weight of only 100 g
                         Applicable for diameters from 8 2 mm or 3/8 3/4 inch
                         Precise finish
                         ''')
c.drawText(textobject)

itemn = Paragraph('<para  fontname = "Helvetica-Bold"fontsize =6  >item number</para>',stylesN)
size = Paragraph('<para lindent=10  fontname = "Helvetica-Bold" fontsize =6> size</para>',stylesN)
ver = Paragraph('<para lindent=10  fontname = "Helvetica-Bold" fontsize =6> version</para>',stylesN)

itemn0 = Paragraph('<para  fontname = "Helvetica"fontsize =6  >77768</para>',stylesN)
size0 = Paragraph('<para lindent=10  fontname = "Helvetica" fontsize =6>8-19 mm</para>',stylesN)
ver0 = Paragraph('<para lindent=10  fontname = "Helvetica" fontsize =6> metric</para>',stylesN)

ver0 = Paragraph('<para lindent=10  fontname = "Helvetica" fontsize =6> metric</para>',stylesN)



gdc =[[itemn,size,ver],
         ['','',''],
         ['','',''],
        [itemn0,size0,ver0],
        [itemn0,size0,ver0],

]
gdct = Table(gdc,colWidths=[1.25*cm,1.75*cm,1.75*cm],rowHeights=4*mm)
gdct.setStyle(TableStyle([
                             # ('LINEBELOW',(0,0),(-1,0),0.25,colors.black),
                            ('LINEBELOW',(0,2),(-1,-1),0.25,colors.black),
                            # ('SPAN',(1,0),(2,0)),
                             ('BACKGROUND',(1,0),(-2,-1),'#DCDCDC'),
                            #  ('ALIGN',(0,0),(-1,-1),'CENTER'),
                              ('VALIGN',(0,0),(-1,-1),'TOP')
                       ]))
gdct.wrapOn(c,width,height)
gdct.drawOn(c,4.4*inch,4.3*inch)



itemn = Paragraph('<para  fontname = "Helvetica-Bold"fontsize =6  >item number</para>',stylesN)
size = Paragraph('<para lindent=10  fontname = "Helvetica-Bold" fontsize =6> size</para>',stylesN)
mes = Paragraph('<para lindent=10  fontname = "Helvetica-Bold" fontsize =6> unit of <br/>Measurement</para>',stylesN)

itemn0 = Paragraph('<para  fontname = "Helvetica"fontsize =6  >77768</para>',stylesN)
size0 = Paragraph('<para lindent=10  fontname = "Helvetica" fontsize =6>8-19 mm</para>',stylesN)
mes0 = Paragraph('<para lindent=10  fontname = "Helvetica" fontsize =6>metric</para>',stylesN)



rwg =[[itemn,size,mes],
         ['','',''],
         ['','',''],
        [itemn0,size0,mes0],
        [itemn0,size0,mes0],

]
rwgt = Table(rwg,colWidths=[1.25*cm,1.75*cm,2.25*cm],rowHeights=4*mm)
rwgt.setStyle(TableStyle([
                             # ('LINEBELOW',(0,0),(-1,0),0.25,colors.black),
                            ('LINEBELOW',(0,2),(-1,-1),0.25,colors.black),
                            # ('SPAN',(1,0),(2,0)),
                             ('BACKGROUND',(1,0),(-2,-1),'#DCDCDC'),
                            #  ('ALIGN',(0,0),(-1,-1),'CENTER'),
                              ('VALIGN',(0,0),(-1,-1),'TOP')
                       ]))
rwgt.wrapOn(c,width,height)
rwgt.drawOn(c,4.4*inch,0.8*inch)








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


c.setFillColor(colors.white)
c.setFont("Helvetica-Bold",20)
c.drawCentredString(98, 8.55*inch, "VT-LUBE")
c.drawImage(i26,60, 5.4*inch,width=1.75*inch,height=2*inch)


c.setFillColor(colors.white)
c.setFont("Helvetica-Bold",14)
c.drawCentredString(220, 8.55*inch, "Rope Care Lubricant")



textobject = c.beginText()
textobject.setTextOrigin(308, 7.7*inch)
c.setFillColor(colors.black)
textobject.setFont("Helvetica-Bold", 12)
textobject.textLines('''
                        VT-Lube
                         ''')
c.drawText(textobject)

textobject = c.beginText()
textobject.setTextOrigin(308, 7.5*inch)
c.setFillColor(colors.black)
textobject.setFont("Helvetica", 8)
textobject.textLines('''
                        This rope care lubricant was especially developed for the
                        relubrication of elevator ropes
                         ''')
c.drawText(textobject)

textobject = c.beginText()
textobject.setTextOrigin(308, 6.9*inch)
c.setFillColor(colors.black)
textobject.setFont("Helvetica-Bold", 12)
textobject.textLines('''
                        Advantages
                         ''')
c.drawText(textobject)

textobject = c.beginText()
textobject.setTextOrigin(308, 6.7*inch)
c.setFillColor(colors.black)
textobject.setFont("Helvetica", 8)
textobject.textLines('''
                        excellent penetration quality causes optimum friction reduction
                        in the rope
                        excellent  creep quality enables even lubricant distribution on
                        and in the rope
                        excellent corrosion protection
                        suitable for high rope speed through very good adhesive quality
                        neutral quality towards synthetic materials
                        (no swelling of plastic parts)
                         ''')
c.drawText(textobject)



itemn = Paragraph('<para  fontname = "Helvetica-Bold"fontsize =6  >item number</para>',stylesN)
content = Paragraph('<para  fontname = "Helvetica-Bold"fontsize =6  >content</para>',stylesN)

itemns = Paragraph('<para  fontname = "Helvetica"fontsize =6  ></para>',stylesN)
content0 = Paragraph('<para  fontname = "Helvetica"fontsize =6  >mm</para>',stylesN)

itemns1 = Paragraph('<para  fontname = "Helvetica"fontsize =6  >77738</para>',stylesN)
content1 = Paragraph('<para  fontname = "Helvetica"fontsize =6  >5</para>',stylesN)

vtl = [[itemn,content],
        ['',''],
        ['',''],
        [itemns,content0],
        [itemns1,content1]

]

vtlt = Table(vtl,colWidths=[1.25*cm,1.75*cm],rowHeights=4*mm)
vtlt.setStyle(TableStyle([
                             # ('LINEBELOW',(0,0),(-1,0),0.25,colors.black),
                            ('LINEBELOW',(0,2),(-1,-1),0.25,colors.black),
                            # ('SPAN',(1,0),(2,0)),
                             ('BACKGROUND',(1,0),(-1,-1),'#DCDCDC'),
                            #  ('ALIGN',(0,0),(-1,-1),'CENTER'),
                              ('VALIGN',(0,0),(-1,-1),'TOP')
                       ]))

vtlt.wrapOn(c,width,height)
vtlt.drawOn(c,4.4*inch,4.5*inch)


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
c.rect(-20,8.33*inch, 5*inch, 0.6*inch,stroke=0,fill=1)
c.setFillColor(colors.white)
c.setFont("Helvetica-Bold",13)
c.drawString(20, 8.55*inch, "RLE ")
c.setFont("Helvetica",9)

c.drawString(70, 8.55*inch, "Rope Load Equalizer ")



textobject = c.beginText()
textobject.setTextOrigin(3*inch, 7.5*inch)
c.setFillColor(colors.black)
textobject.setFont("Helvetica", 10)
textobject.textLines('''
                         ering properties at minimum overall height
                         transverse elongation
                         also applicable on the counterweight side as rope length compensation
                         grease- and oil resistant


                        RLE-Kit
                        ering properties at minimum overall height
                        transverse elongation
                        also applicable on the counterweight side as rope length compensation
                        grease- and oil resistant
                        ering properties at minimum overall height
                        transverse elongation
                        also applicable on the counterweight side as rope length compensation


                        Advantages
                        grease- and oil resistant
                        ering properties at minimum overall height
                        transverse elongation
                        also applicable on the counterweight side as rope length compensation
                        grease- and oil resistant

                         ''')
c.drawText(textobject)




c.drawImage(rle,0.25*inch,0.5*inch,width=3.5*inch,height=3.5*inch,preserveAspectRatio=True)


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
c.rect(-20,8.33*inch, 17*inch, 0.75*inch,stroke=0,fill=1)

c.setFillColor(colors.white)
c.setFont("Helvetica-Bold",20)
c.drawCentredString(138, 8.55*inch, "ROPE CUTTERS")

textobject = c.beginText()
textobject.setTextOrigin(380, 7.9*inch)
c.setFillColor(colors.black)
textobject.setFont("Helvetica-Bold", 12)
textobject.textLines('''
                        Rope Cutters
                         ''')
c.drawText(textobject)


c.drawImage(i16,60,6.4*inch,width=3*inch,height=1.75*inch)

c.drawImage(i17,50,3.7*inch,width=3.4*inch,height=1.75*inch)


textobject = c.beginText()
textobject.setTextOrigin(380, 5.4*inch)
c.setFillColor(colors.black)
textobject.setFont("Helvetica-Bold", 12)
textobject.textLines('''
                        Hydraulic Rope Cutters
                           ''')
c.drawText(textobject)


itemn = Paragraph('<para  fontname = "Helvetica-Bold"fontsize =6  >item number</para>',stylesN)
rope = Paragraph('<para lindent=10  fontname = "Helvetica-Bold" fontsize =6> rope @</para>',stylesN)
weight = Paragraph('<para lindent=10  fontname = "Helvetica-Bold" fontsize =6> weight</para>',stylesN)
length =Paragraph('<para lindent=10  fontname = "Helvetica-Bold" fontsize =6> length<br/>cutters</para>',stylesN)

itemn0 = Paragraph('<para  fontname = "Helvetica" fontsize =6  ></para>',stylesN)
ropemm = Paragraph('<para lindent=10  fontname = "Helvetica" fontsize =6> mm</para>',stylesN)
weightkg = Paragraph('<para lindent=10  fontname = "Helvetica" fontsize =6> kg</para>',stylesN)
lengthmm =Paragraph('<para lindent=10  fontname = "Helvetica" fontsize =6> mm</para>',stylesN)

itemn1 = Paragraph('<para  fontname = "Helvetica"fontsize =6  >77790</para>',stylesN)
ropemm1 = Paragraph('<para lindent=10  fontname = "Helvetica" fontsize =6>upto 12 </para>',stylesN)
weightkg1 = Paragraph('<para lindent=10  fontname = "Helvetica" fontsize =6> 1.5</para>',stylesN)
lengthmm1 =Paragraph('<para lindent=10  fontname = "Helvetica" fontsize =6>500</para>',stylesN)





rc =[[itemn,rope,weight,length],
         ['','',''],
         ['','',''],
        [itemn0,ropemm,weightkg,lengthmm],
        [itemn1,ropemm1,weightkg1,lengthmm1],


]
rct = Table(rc,colWidths=[1.25*cm,1.75*cm,2.25*cm],rowHeights=4*mm)
rct.setStyle(TableStyle([
                             # ('LINEBELOW',(0,0),(-1,0),0.25,colors.black),
                            ('LINEBELOW',(0,2),(-1,-1),0.25,colors.black),
                            # ('SPAN',(1,0),(2,0)),
                             ('BACKGROUND',(1,0),(-3,-1),'#DCDCDC'),
                            #  ('ALIGN',(0,0),(-1,-1),'CENTER'),
                              ('VALIGN',(0,0),(-1,-1),'TOP')
                       ]))
rct.wrapOn(c,width,height)
rct.drawOn(c,5.2*inch,6.9*inch)

itemn = Paragraph('<para  fontname = "Helvetica-Bold"fontsize =6  >item number</para>',stylesN)
rope = Paragraph('<para lindent=10  fontname = "Helvetica-Bold" fontsize =6> rope @</para>',stylesN)
weight = Paragraph('<para lindent=10  fontname = "Helvetica-Bold" fontsize =6> weight</para>',stylesN)
length =Paragraph('<para lindent=10  fontname = "Helvetica-Bold" fontsize =6> length<br/>cutters</para>',stylesN)

itemn0 = Paragraph('<para  fontname = "Helvetica" fontsize =6  ></para>',stylesN)
ropemm = Paragraph('<para lindent=10  fontname = "Helvetica" fontsize =6> mm</para>',stylesN)
weightkg = Paragraph('<para lindent=10  fontname = "Helvetica" fontsize =6> kg</para>',stylesN)
lengthmm =Paragraph('<para lindent=10  fontname = "Helvetica" fontsize =6> mm</para>',stylesN)

itemn1 = Paragraph('<para  fontname = "Helvetica"fontsize =6  >77790</para>',stylesN)
ropemm1 = Paragraph('<para lindent=10  fontname = "Helvetica" fontsize =6>upto 12 </para>',stylesN)
weightkg1 = Paragraph('<para lindent=10  fontname = "Helvetica" fontsize =6> 1.5</para>',stylesN)
lengthmm1 =Paragraph('<para lindent=10  fontname = "Helvetica" fontsize =6>500</para>',stylesN)

rc =[[itemn,rope,weight,length],
         ['','',''],
         ['','',''],
        [itemn0,ropemm,weightkg,lengthmm],
        [itemn1,ropemm1,weightkg1,lengthmm1],


]
rct = Table(rc,colWidths=[1.25*cm,1.75*cm,2.25*cm],rowHeights=4*mm)
rct.setStyle(TableStyle([
                             # ('LINEBELOW',(0,0),(-1,0),0.25,colors.black),
                            ('LINEBELOW',(0,2),(-1,-1),0.25,colors.black),
                            # ('SPAN',(1,0),(2,0)),
                             ('BACKGROUND',(1,0),(-3,-1),'#DCDCDC'),
                            #  ('ALIGN',(0,0),(-1,-1),'CENTER'),
                              ('VALIGN',(0,0),(-1,-1),'TOP')
                       ]))
rct.wrapOn(c,width,height)
rct.drawOn(c,5.2*inch,4.4*inch)

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


c.setFillColor(colors.white)
c.setFont("Helvetica-Bold",20)
c.drawCentredString(98, 8.55*inch, "PACKAGING")

c.drawImage(i18,20,6.85*inch,width=1.4*inch,height=1.15*inch)

c.drawImage(i19,145,6.1*inch,width=1.4*inch,height=1.35*inch)

c.drawImage(i20,35,5*inch,width=2*inch,height=1.2*inch)

c.drawImage(i21,60,3*inch,width=2.75*inch,height=1.75*inch)

c.drawImage(i22,35,1.3*inch,width=2*inch,height=1.6*inch)

c.drawImage(i23,165,0.2*inch,width=1.65*inch,height=1.5*inch)

textobject = c.beginText()
textobject.setTextOrigin(308, 7.9*inch)
c.setFillColor(colors.black)
textobject.setFont("Helvetica", 8)
textobject.textLines('''
                        When selecting the packaging, BRUGG LIFTING pays attention to the
                        best transport protection possible. Our ropes are protected in the best
                        possible  way  during  the  transport  with  special  packaging  materials
                        against corrosion and mechanical damaging.

                        BRUGG  LIFTING is  committed  to  handle  ressources  with  great  care.
                        That  is  why  our  ropes,  whenever  possible,  are  delivered  on  sturdy
                        returnable reels and drums that can be reused.
                         ''')
c.drawText(textobject)

textobject = c.beginText()
textobject.setTextOrigin(308, 4.9*inch)
c.setFillColor(colors.black)
textobject.setFont("Helvetica", 8)
textobject.textLines('''
                          Cross Drums
                           capacity according to rope diameter
                           from 100m (16mm) to 400m (6,5mm)
                         ''')
c.drawText(textobject)

textobject = c.beginText()
textobject.setTextOrigin(308, 4.3*inch)
c.setFillColor(colors.black)
textobject.setFont("Helvetica", 8)
textobject.textLines('''
                          Round Reels
                          /width: 300 600mm / 320 530mm
                         ''')
c.drawText(textobject)

textobject = c.beginText()
textobject.setTextOrigin(308, 3.9*inch)
c.setFillColor(colors.black)
textobject.setFont("Helvetica", 8)
textobject.textLines('''
                          Coils
                          up to 50m or 30kg
                         ''')
c.drawText(textobject)

textobject = c.beginText()
textobject.setTextOrigin(308, 3.3*inch)
c.setFillColor(colors.black)
textobject.setFont("Helvetica", 8)
textobject.textLines('''
                          XJ Wooden Reels 100 x 65 cm
                          capacity according to rope diameter
                          from 1000m HRS ( 16mm) or 1132kg reel weight
                          up to 4100m HRS ( 8mm) or 1118kg reel weight
                         ''')
c.drawText(textobject)

textobject = c.beginText()
textobject.setTextOrigin(308, 2.5*inch)
c.setFillColor(colors.black)
textobject.setFont("Helvetica", 8)
textobject.textLines('''
                        System Deliveries on Pallets
                        consisting  of  rope/ end  terminations/ accessories/
                        mounting materia
                         ''')
c.drawText(textobject)

textobject = c.beginText()
textobject.setTextOrigin(308, 1.75*inch)
c.setFillColor(colors.black)
textobject.setFont("Helvetica", 8)
textobject.textLines('''
                        System Deliveries in Sturdy Cardboard Box
                        System Deliveries in Sturdy Cardboard Box
                         ''')
c.drawText(textobject)
c.showPage()

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
c.drawString(20, 8.55*inch, "RPM ")
c.setFont("Helvetica",9)

c.drawString(70, 8.55*inch, "Rope Performance Measurement Device")

c.drawImage(rpm1,20,3*inch,width=2*inch,height=5*inch,preserveAspectRatio=True)


textobject = c.beginText()
textobject.setTextOrigin(3*inch, 7.5*inch)
c.setFillColor(colors.black)
textobject.setFont("Helvetica", 10)
textobject.textLines('''
                         ering properties at minimum overall height
                         transverse elongation
                         also applicable on the counterweight side as rope length compensation
                         grease- and oil resistant


                        Advantages
                        ering properties at minimum overall height
                        transverse elongation
                        also applicable on the counterweight side as rope length compensation
                        grease- and oil resistant
                        ering properties at minimum overall height
                        transverse elongation
                        also applicable on the counterweight side as rope length compensation
                        grease- and oil resistant
                        ering properties at minimum overall height
                        transverse elongation
                        also applicable on the counterweight side as rope length compensation
                        grease- and oil resistant

                         ''')
c.drawText(textobject)

textobject = c.beginText()
textobject.setTextOrigin(3*inch, 3.5*inch)
c.setFillColor(colors.black)
textobject.setFont("Helvetica", 10)
textobject.textLines('''
                         keep the tension under control
                         ering properties at minimum overall height
                         transverse elongation
                         also applicable on the counterweight side as rope length compensation
                         grease- and oil resistant

                         ''')
c.drawText(textobject)

itemn = Paragraph('<para  fontname = "Helvetica-Bold"fontsize =6  >item number</para>',stylesN)
rope = Paragraph('<para lindent=10  fontname = "Helvetica-Bold" fontsize =6>rope-@</para>',stylesN)

rope0 = Paragraph('<para  fontname = "Helvetica-Bold"fontsize =5  >mm</para>',stylesN)
rope1 = Paragraph('<para   fontname = "Helvetica-Bold" fontsize =5>in</para>',stylesN)

itemn2 = Paragraph('<para  fontname = "Helvetica-Bold"fontsize =5>70020</para>',stylesN)
rope2 = Paragraph('<para   fontname = "Helvetica-Bold" fontsize =5>8-22</para>',stylesN)
rope3 = Paragraph('<para   fontname = "Helvetica-Bold" fontsize =5>5/16-7/18</para>',stylesN)


rpm =[[itemn,rope],
         ['',''],
         ['',''],
        ['',rope0,rope1],
        [itemn2,rope2,rope3],

]
rpmt = Table(rpm,colWidths=[1.25*cm,1.25*cm],rowHeights=4*mm)
rpmt.setStyle(TableStyle([
                             # ('LINEBELOW',(0,0),(-1,0),0.25,colors.black),
                            ('LINEBELOW',(0,2),(-1,-1),0.25,colors.black),
                            ('SPAN',(1,0),(2,0)),
                             ('BACKGROUND',(1,0),(-1,-1),'#DCDCDC'),
                            #  ('ALIGN',(0,0),(-1,-1),'CENTER'),
                              ('VALIGN',(0,0),(-1,-1),'TOP')
                       ]))
rpmt.wrapOn(c,width,height)
rpmt.drawOn(c,3*inch,1.5*inch)
c.drawImage(rpm2,5*inch,0.5*inch,width=1.75*inch,height=1.75*inch,preserveAspectRatio=True)


c.showPage()

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
