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
de = "ropetech.png"
a = 'A.png'
am = 'AM.png'
d = "D.png"
fp = "FP.png"
fp2 = "FP2.png"
fp3 = "FP3.png"
hrs = "hrs.jpg"
scx9 = "hrs.jpg"
sc8 = "hrs.jpg"
dp9 = "hrs.jpg"
X196 = "hrs.jpg"
X198 = "hrs.jpg"
tsr = "hrs.jpg"
x25 = "hrs.jpg"
sx25 = "hrs.jpg"
ex ="hrs.jpg"

l1 = "e1-01.png"
rope = "ropetech.png"
hrs = "hrs.jpg"
scx9 = "hrs.jpg"
sc8 = "hrs.jpg"
dp9 = "hrs.jpg"
X19 = "hrs.jpg"
tsr = "hrs.jpg"
x25 = "hrs.jpg"
sx25 = "hrs.jpg"
bull1 = "image3.svg"
bull2 = "image3.svg"
bull3 = "image3.svg"
bull4 = "image3.svg"
bull5 = "image3.svg"
bull6 = "image3.svg"
im = "e2-2.png"
iso = "e2-3.png"
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
i8 = "i8.png"
i9 = "i9.png"
i10 = "i10.png"
i11 = "i11.png"
i12 = "i12.png"
i13 = "i13.png"
i14 = "i14.png"
i15 = "i15.png"
width, height = A4
c = Canvas("Erlandscape.pdf",pagesize=landscape(letter))
c.drawImage(bg,0*inch,6*inch,width=12*inch,height=3*inch,preserveAspectRatio=True)
# For HRS
drawing = svg2rlg(logo)
scaleFactor = 1./0.9
drawing.width *= scaleFactor
drawing.height *= scaleFactor
drawing.scale(scaleFactor, scaleFactor)
renderPDF.draw(drawing, c, 20, 570)
c.setFillColor('#87CEFA')
c.rect(-20,6.07*inch, 1.75*inch, 0.5*inch,stroke=0,fill=1)

c.rect(50,6.07*inch, 12*inch, 0.25*inch,stroke=0,fill=1)

c.setFillColor(colors.white)
c.setFont("Helvetica-Bold",20)
c.drawCentredString(50, 6.25*inch, "6x19")

c.setFont("Helvetica-Bold",8)

c.drawString(120, 6.15*inch, "GOVERNOR ROPES")
c.drawString(570, 6.15*inch, "ABBREVIATED DESIGNATIONS")


c.drawImage(X196,30,4.5*inch,width=1*inch,height=1*inch,preserveAspectRatio=True)
c.setFillColor(colors.black)

textobject = c.beginText()
textobject.setTextOrigin(120, 5.7*inch)
c.setFillColor(colors.black)
textobject.setFont("Helvetica", 7)
textobject.textLines('''
                           and number of trips, also under difficult  highest demandas
                           on breaking force, elongation  elongation number of trips,
                           also under difficult instalation''')
c.drawText(textobject)
c.setFillColor('#87CEFA')
c.rect(120,4.75*inch, 0.5*inch, 0.5*inch,stroke=0,fill=1)
textobject = c.beginText()
textobject.setTextOrigin(126, 5.1*inch)
c.setFillColor(colors.black)
textobject.setFont("Helvetica", 5)
textobject.textLines('''
                           125,000
                             N/mm2
                           18.1x10^6
                            psi''')
c.drawText(textobject)
c.drawString(122, 4.6*inch, "E-Module**")

c.setFillColor('#87CEFA')
c.rect(170,4.75*inch, 0.5*inch, 0.5*inch,stroke=0,fill=1)
textobject = c.beginText()
textobject.setTextOrigin(176, 5.1*inch)
c.setFillColor(colors.black)
textobject.setFont("Helvetica", 5)
textobject.textLines('''
                           0.104
                             %
                            1.2
                           in/100ft        ''')
c.drawText(textobject)
c.drawString(176, 4.6*inch, "Elastic")

c.setFillColor('#87CEFA')
c.rect(220,4.75*inch, 0.5*inch, 0.5*inch,stroke=0,fill=1)
textobject = c.beginText()
textobject.setTextOrigin(226, 5*inch)
c.setFillColor(colors.black)
textobject.setFont("Helvetica", 5)
textobject.textLines('''
                           0.13
                             %''')
c.drawText(textobject)
c.drawString(226, 4.6*inch, "permenant")


itemn = Paragraph('<para  fontname = "Helvetica-Bold"fontsize =5  >item number</para>',stylesN)
rope = Paragraph('<para lindent=-5 fontname = "Helvetica-Bold" fontsize =5>rope-@</para>',stylesN)
brk = Paragraph('<para leftindent = -30 fontname = "Helvetica-Bold" fontsize =5>breaking load<br/></para>',stylesN)

weight= Paragraph('<para leftindent=-5 fontname = "Helvetica-Bold" fontsize =5>weight</para>',stylesN)
con = Paragraph('<para leftindent=-50 fontname = "Helvetica-Bold" fontsize =5>construction</para>',stylesN)
min = Paragraph('<para leftindent = -22 fontname = "Helvetica-Bold" fontsize =5>min.</para>',stylesN)



# i = Paragraph('<para> </para>',stylesN)
mm0 = Paragraph('<para leftindent =-4 fontname = "Helvetica" fontsize =5 underlineGap = 1>mm</para>',stylesN)
inc = Paragraph('<para leftindent =10 fontname = "Helvetica" fontsize =5>in</para>',stylesN)
kN= Paragraph('<para leftindent =25 fontname = "Helvetica" fontsize =5>kN</para>',stylesN)
lbs = Paragraph('<para leftindent =-10 fontname = "Helvetica" fontsize =5>lbs</para>',stylesN)
kg = Paragraph('<para leftindent =-15 fontname = "Helvetica" fontsize =5>kg/100m</para>',stylesN)
lb = Paragraph('<para leftindent =-45 fontname = "Helvetica" fontsize =5>lb/ft</para>',stylesN)
# c = Paragraph('<para> </para>',stylesN)
i = Paragraph('<para fontname = "Helvetica" fontsize =5>10699 </para>',stylesN)
mm1 = Paragraph('<para leftindent =-4 fontname = "Helvetica" fontsize =5>6.0</para>',stylesN)
inc1 = Paragraph('<para leftindent =10 fontname = "Helvetica" fontsize =5>5/16</para>',stylesN)
kN1= Paragraph('<para leftindent =25 fontname = "Helvetica" fontsize =5>42.7</para>',stylesN)
lbs1 = Paragraph('<para leftindent =-11 fontname = "Helvetica" fontsize =5>9.599</para>',stylesN)
kg1 = Paragraph('<para leftindent =-15 fontname = "Helvetica" fontsize =5>26.9</para>',stylesN)
lb1 = Paragraph('<para  leftindent =-45 fontname = "Helvetica" fontsize =5>0.181</para>',stylesN)
con1 = Paragraph('<para fontname = "Helvetica" fontsize =5 leftindent=-60>9x19S-PWRC 1570 UsZ.(RRL)</para>',stylesN)




data = [[itemn,'',rope,'',brk,weight,'',con],
        ['','','','',min,'','',''],
            ['',mm0,inc,kN,lbs,kg,lb,''],
             [i,mm1,inc1,kN1,lbs1,kg1,lb1,con1],
             [i,mm1,inc1,kN1,lbs1,kg1,lb1,con1],




            ]


t = Table(data,colWidths=[1.25*cm,1*cm,0.5*cm,2*cm,1*cm,1.75*cm,1.5*cm],rowHeights=4*mm)
t.setStyle(TableStyle([

                             # ('LINEABELOW',(0,2),(-1,-1),0.25,colors.black),
                            ('SPAN',(2,0),(2,0)),
                            ('SPAN',(3,0),(2,0)),

                            ('FONTNAME',(0,0),(-1,-1),'Helvetica-Bold'),
                            ('BACKGROUND',(1,0),(-6,-1),'#DCDCDC'),
                            ('LEFTPADDING',(2,0),(-1,-1),-20),
                            ('LEFTPADDING',(5,0),(-1,-1),-20),


                            ('LINEBELOW',(0,1),(-2,-1),0.25,colors.black),

                             ('ALIGN',(0,0),(-1,-1),'CENTER'),
                            # ('ALIGN',())
                            # ('VALIGN',(0,0),(-1,-1),'TOP'),
                             ('VALIGN',(0,0),(-1,-1),'TOP')
                       ]))

t.wrapOn(c, width,height)
t.drawOn(c, 120,3.5*inch)
textobject = c.beginText()
textobject.setTextOrigin(120, 3.4*inch)
c.setFillColor(colors.black)
textobject.setFont("Helvetica", 5)
textobject.textLines('''
                          Further nominal strengthd diameters (including imperial dimensions)
                          Rope diameter-tolerances according to EN12385-5/ISO 4344.''')
c.drawText(textobject)



c.setFillColor('#87CEFA')
c.rect(-20,2.5*inch, 1.75*inch, 0.5*inch,stroke=0,fill=1)
c.setFillColor(colors.white)
c.setFont("Helvetica-Bold",20)
c.drawCentredString(50, 2.65*inch, "8x19")
c.drawImage(X198,30,1.25*inch,width=1*inch,height=1*inch,preserveAspectRatio=True)
c.setFillColor(colors.black)

textobject = c.beginText()
textobject.setTextOrigin(120, 2.75*inch)
c.setFillColor(colors.black)
textobject.setFont("Helvetica", 7)
textobject.textLines('''
                           and number of trips, also under difficult  highest demandas
                           on breaking force, elongation  elongation number of trips,
                           also under difficult instalation''')
c.drawText(textobject)

c.setFillColor('#87CEFA')
c.rect(120,1.8*inch, 0.5*inch, 0.5*inch,stroke=0,fill=1)
textobject = c.beginText()
textobject.setTextOrigin(126, 2.15*inch)
c.setFillColor(colors.black)
textobject.setFont("Helvetica", 5)
textobject.textLines('''
                           125,000
                             N/mm2
                           18.1x10^6
                            psi''')
c.drawText(textobject)
c.drawString(122, 1.7*inch, "E-Module**")

c.setFillColor('#87CEFA')
c.rect(170,1.8*inch, 0.5*inch, 0.5*inch,stroke=0,fill=1)
textobject = c.beginText()
textobject.setTextOrigin(176, 2.15*inch)
c.setFillColor(colors.black)
textobject.setFont("Helvetica", 5)
textobject.textLines('''
                           0.104
                             %
                            1.2
                           in/100ft        ''')
c.drawText(textobject)
c.drawString(176, 1.7*inch, "Elastic")

c.setFillColor('#87CEFA')
c.rect(220,1.8*inch, 0.5*inch, 0.5*inch,stroke=0,fill=1)
textobject = c.beginText()
textobject.setTextOrigin(226, 2.15*inch)
c.setFillColor(colors.black)
textobject.setFont("Helvetica", 5)
textobject.textLines('''
                           0.13
                             %''')
c.drawText(textobject)
c.drawString(222, 1.7*inch, "permenant")






itemn = Paragraph('<para  fontname = "Helvetica-Bold"fontsize =5 >item number</para>',stylesN)
rope = Paragraph('<para lindent=-5 fontname = "Helvetica-Bold" fontsize =5>rope-@</para>',stylesN)
brk = Paragraph('<para leftindent = -30 fontname = "Helvetica-Bold" fontsize =5>breaking load<br/></para>',stylesN)

weight= Paragraph('<para leftindent=-5 fontname = "Helvetica-Bold" fontsize =5>weight</para>',stylesN)
con = Paragraph('<para leftindent=-50 fontname = "Helvetica-Bold" fontsize =5>construction</para>',stylesN)
min = Paragraph('<para leftindent = -22 fontname = "Helvetica-Bold" fontsize =5>min.</para>',stylesN)



# i = Paragraph('<para> </para>',stylesN)
mm0 = Paragraph('<para leftindent =-4 fontname = "Helvetica" fontsize =5 underlineGap = 1>mm</para>',stylesN)
inc = Paragraph('<para leftindent =10 fontname = "Helvetica" fontsize =5>in</para>',stylesN)
kN= Paragraph('<para leftindent =25 fontname = "Helvetica" fontsize =5>kN</para>',stylesN)
lbs = Paragraph('<para leftindent =-10 fontname = "Helvetica" fontsize =5>lbs</para>',stylesN)
kg = Paragraph('<para leftindent =-15 fontname = "Helvetica" fontsize =5>kg/100m</para>',stylesN)
lb = Paragraph('<para leftindent =-45 fontname = "Helvetica" fontsize =5>lb/ft</para>',stylesN)
# c = Paragraph('<para> </para>',stylesN)
i = Paragraph('<para fontname = "Helvetica" fontsize =5>10699 </para>',stylesN)
mm1 = Paragraph('<para leftindent =-4 fontname = "Helvetica" fontsize =5>6.0</para>',stylesN)
inc1 = Paragraph('<para leftindent =10 fontname = "Helvetica" fontsize =5>5/16</para>',stylesN)
kN1= Paragraph('<para leftindent =25 fontname = "Helvetica" fontsize =5>42.7</para>',stylesN)
lbs1 = Paragraph('<para leftindent =-11 fontname = "Helvetica" fontsize =5>9.599</para>',stylesN)
kg1 = Paragraph('<para leftindent =-15 fontname = "Helvetica" fontsize =5>26.9</para>',stylesN)
lb1 = Paragraph('<para  leftindent =-45 fontname = "Helvetica" fontsize =5>0.181</para>',stylesN)
con1 = Paragraph('<para fontname = "Helvetica" fontsize =5 leftindent=-60>9x19S-PWRC 1570 UsZ.(RRL)</para>',stylesN)




data = [[itemn,'',rope,'',brk,weight,'',con],
        ['','','','',min,'','',''],
            ['',mm0,inc,kN,lbs,kg,lb,''],
             [i,mm1,inc1,kN1,lbs1,kg1,lb1,con1],
             [i,mm1,inc1,kN1,lbs1,kg1,lb1,con1],
             [i,mm1,inc1,kN1,lbs1,kg1,lb1,con1],
             [i,mm1,inc1,kN1,lbs1,kg1,lb1,con1],




            ]


t = Table(data,colWidths=[1.25*cm,1*cm,0.25*cm,2*cm,1*cm,1.75*cm,1.5*cm],rowHeights=4*mm)
t.setStyle(TableStyle([

                             # ('LINEABELOW',(0,2),(-1,-1),0.25,colors.black),
                            ('SPAN',(2,0),(2,0)),
                            ('SPAN',(3,0),(2,0)),

                            ('FONTNAME',(0,0),(-1,-1),'Helvetica-Bold'),
                            ('BACKGROUND',(1,0),(-6,-1),'#DCDCDC'),
                            ('LEFTPADDING',(2,0),(-1,-1),-20),
                            ('LEFTPADDING',(5,0),(-1,-1),-20),


                            ('LINEBELOW',(0,1),(-2,-1),0.25,colors.black),

                             ('ALIGN',(0,0),(-1,-1),'CENTER'),
                            # ('ALIGN',())
                            # ('VALIGN',(0,0),(-1,-1),'TOP'),
                             ('VALIGN',(0,0),(-1,-1),'TOP')
                       ]))

t.wrapOn(c, width,height)
t.drawOn(c, 120,0.5*inch)
textobject = c.beginText()
textobject.setTextOrigin(120, 0.4*inch)
c.setFillColor(colors.black)
textobject.setFont("Helvetica", 5)
textobject.textLines('''
                          Further nominal strengthd diameters (including imperial dimensions)
                          Rope diameter-tolerances according to EN12385-5/ISO 4344.

                          ** E-Module tested according to DIN  18800.The specified E-module is tested with 30-40% of MBL''')
c.drawText(textobject)

c.drawImage(ex,6*inch,4.75*inch,width=1*inch,height=1*inch,preserveAspectRatio=True)
c.setFont("Helvetica-Bold",8)
c.drawString(5.75*inch, 4.5*inch, "12 8 x 19S-NFC 1370/1770 U sZ")
c.line(5.8*inch,4.45*inch,5.8*inch,4.2*inch)
c.setFillColor('#DCDCDC')
c.rect(5.75*inch,4.05*inch,0.35*cm,0.35*cm,stroke=0,fill=1)
c.setFillColor(colors.black)
c.drawCentredString(5.81*inch,4.09*inch,"A")

c.line(6.05*inch,4.45*inch,6.05*inch,4.2*inch)
c.setFillColor('#DCDCDC')
c.rect(6*inch,4.05*inch,0.35*cm,0.35*cm,stroke=0,fill=1)
c.setFillColor(colors.black)
c.drawCentredString(6.05*inch,4.09*inch,"B")

c.line(6.25*inch,4.45*inch,6.25*inch,4.2*inch)
c.setFillColor('#DCDCDC')
c.rect(6.17*inch,4.05*inch,0.35*cm,0.35*cm,stroke=0,fill=1)
c.setFillColor(colors.black)
c.drawCentredString(6.22*inch,4.09*inch,"C")

c.line(6.45*inch,4.45*inch,6.45*inch,4.2*inch)
c.setFillColor('#DCDCDC')
c.rect(6.4*inch,4.05*inch,0.35*cm,0.35*cm,stroke=0,fill=1)
c.setFillColor(colors.black)
c.drawCentredString(6.45*inch,4.09*inch,"D")


c.line(6.85*inch,4.45*inch,6.85*inch,4.2*inch)
c.setFillColor('#DCDCDC')
c.rect(6.8*inch,4.05*inch,0.35*cm,0.35*cm,stroke=0,fill=1)
c.setFillColor(colors.black)
c.drawCentredString(6.85*inch,4.09*inch,"E")

c.line(7.2*inch,4.45*inch,7.2*inch,4.2*inch)
c.setFillColor('#DCDCDC')
c.rect(7.15*inch,4.05*inch,0.35*cm,0.35*cm,stroke=0,fill=1)
c.setFillColor(colors.black)
c.drawCentredString(7.2*inch,4.09*inch,"F")

c.line(7.35*inch,4.45*inch,7.35*inch,4.2*inch)
c.setFillColor('#DCDCDC')
c.rect(7.3*inch,4.05*inch,0.35*cm,0.35*cm,stroke=0,fill=1)
c.setFillColor(colors.black)
c.drawCentredString(7.35*inch,4.09*inch,"G")

textobject = c.beginText()
textobject.setTextOrigin(8.1*inch, 5.7*inch)
c.setFillColor(colors.black)
textobject.setFont("Helvetica", 6)
textobject.textLines('''
                           Desingation and Classification of wire ropes(EN 12385-2 formerly ISO 17893)''')
c.drawText(textobject)

c.setFillColor('#DCDCDC')
c.rect(7.83*inch,5.5*inch,0.35*cm,0.35*cm,stroke=0,fill=1)
c.setFont("Helvetica-Bold",8)

c.setFillColor(colors.black)
c.drawCentredString(7.9*inch,5.55*inch,"A")
textobject = c.beginText()
textobject.setTextOrigin(8.1*inch, 5.55*inch)
c.setFillColor(colors.black)
textobject.setFont("Helvetica", 6)
textobject.textLines('''
                           Rope nominal Diameter in mm
                           (see corresponding table for each)''')
c.drawText(textobject)

c.setFillColor('#DCDCDC')
c.rect(7.83*inch,5.2*inch,0.35*cm,0.35*cm,stroke=0,fill=1)
c.setFont("Helvetica-Bold",8)
c.setFillColor(colors.black)
c.drawCentredString(7.9*inch,5.25*inch,"B")
textobject = c.beginText()
textobject.setTextOrigin(8.1*inch, 5.25*inch)
c.setFillColor(colors.black)
textobject.setFont("Helvetica", 6)
textobject.textLines('''
                          Rope Construction''')
c.drawText(textobject)
textobject = c.beginText()
textobject.setTextOrigin(8.1*inch, 5.02*inch)
c.setFillColor(colors.black)
textobject.setFont("Helvetica", 6)
textobject.textLines('''
                           Construction and Lay Direction''')
c.drawText(textobject)

c.setFillColor('#DCDCDC')
c.rect(7.83*inch,5*inch,0.35*cm,0.35*cm,stroke=0,fill=1)
c.setFont("Helvetica-Bold",8)
c.setFillColor(colors.black)
c.drawCentredString(7.9*inch,5.01*inch,"C")
data1 = [['-','simple lay strand',''],
        ['' , 'example for strand construction','7 d.h.(1-6)'],
        ['s' , 'seale parallel lay',''],
        ['' , 'example for strand construction','19S d.h. (1-9-9)'],
        ['W','Warrington parallel lay',''],
        ['' , 'example for strand construction','19W d.h. (1-6-6+6)'],
        ['F' , 'Filler parallel lay',''],
        ['' , 'example for strand construction','21F d.h. (1-5-5F-10)'],
        ['' , '','25F d.h. (1-6-6F-12)'],
        ['WS' , 'combined (warrington seale) parallel lay',''],
        ['' , 'example for strand construction','31WS d.h. (1-6-6+6-12)'],
]



r = Table(data1,colWidths=17*mm,rowHeights=3*mm)
r.setStyle(TableStyle([
                    ('FONTSIZE',(0,0),(-1,-1),5),
                            ('LEFTPADDING',(1,0),(-1,-1),7),
                             ('LEFTPADDING',(2,0),(-1,-1),45),('VALIGN',(0,0),(-1,-1),'TOP')
                       ]))
r.wrapOn(c,width,height)
r.drawOn(c,8.1*inch,3.7*inch)

c.setFillColor('#DCDCDC')
c.rect(7.83*inch,3.4*inch,0.35*cm,0.35*cm,stroke=0,fill=1)
c.setFont("Helvetica-Bold",8)
c.setFillColor(colors.black)
c.drawCentredString(7.9*inch,3.42*inch,"D")
c.setFont("Helvetica",6)
c.setFillColor(colors.black)
c.drawCentredString(8.5*inch,3.42*inch,"Constructional of Core")

data2 = [['Single layer rope with fibre core FC',''],
        ['NFC' , 'natural fibre core'],
        ['SFC' , 'synthetic fibre core'],
        ['' , ''],
        ['Single layer rope with fibre core WC',''],
        ['WSC' , 'wire strand core'],
        ['IWRC' , 'independant wire rope core',''],
        ['' , ''],
        ['Rope with parallel lay'],
        ['PWRC' , 'parallel wire rope core',''],

]



s = Table(data2,colWidths=17*mm,rowHeights=2.5*mm)
s.setStyle(TableStyle([
                    ('FONTSIZE',(0,0),(-1,-1),5),
                            ('LEFTPADDING',(1,0),(-1,-1),7),
                             ('LEFTPADDING',(2,0),(-1,-1),20),('VALIGN',(0,0),(-1,-1),'TOP')
                       ]))
s.wrapOn(c,width,height)
s.drawOn(c,8.1*inch,2.4*inch)

c.setFillColor('#DCDCDC')
c.rect(7.83*inch,2.2*inch,0.35*cm,0.35*cm,stroke=0,fill=1)
c.setFont("Helvetica-Bold",8)
c.setFillColor(colors.black)
c.drawCentredString(7.9*inch,2.25*inch,"E")
c.setFont("Helvetica",6)
c.setFillColor(colors.black)
c.drawCentredString(8.9*inch,2.25*inch,"Nominal Tensile Grade of wires in N/mm2")

c.setFillColor('#DCDCDC')
c.rect(7.83*inch,2*inch,0.35*cm,0.35*cm,stroke=0,fill=1)
c.setFont("Helvetica-Bold",8)
c.setFillColor(colors.black)
c.drawCentredString(7.9*inch,2.03*inch,"F")
c.setFont("Helvetica",6)
c.setFillColor(colors.black)
c.drawCentredString(8.55*inch,2.03*inch,"Surface Finish of Wires")

data3 = [['U','bright'],
        ['B' , 'zinc coated (classB)'],


]



u = Table(data3,colWidths=17*mm,rowHeights=2.5*mm)
u.setStyle(TableStyle([
                    ('FONTSIZE',(0,0),(-1,-1),5),
                            ('LEFTPADDING',(1,0),(-1,-1),7),
                             # ('LEFTPADDING',(2,0),(-1,-1),20),
                             ('VALIGN',(0,0),(-1,-1),'TOP')
                       ]))
u.wrapOn(c,width,height)
u.drawOn(c,8.1*inch,1.75*inch)

c.setFillColor('#DCDCDC')
c.rect(7.83*inch,1.5*inch,0.35*cm,0.35*cm,stroke=0,fill=1)
c.setFont("Helvetica-Bold",8)
c.setFillColor(colors.black)
c.drawCentredString(7.9*inch,1.5*inch,"G")
c.setFont("Helvetica",6)
c.setFillColor(colors.black)
c.drawCentredString(8.55*inch,1.5*inch,"Type and Direction of Lay")

data3 = [['z','right lay (strand)'],
        ['s','left lay (strand)'],
        ['Z','right lay (rope)'],
        ['S','left lay (rope)'],
        ['sZ(RRL)','regular lay,right hand'],
        ['zS(RLL)','rregular lay,left-hand'],


]



u = Table(data3,colWidths=17*mm,rowHeights=2.5*mm)
u.setStyle(TableStyle([
                    ('FONTSIZE',(0,0),(-1,-1),5),
                            ('LEFTPADDING',(1,0),(-1,-1),7),
                             ('VALIGN',(0,0),(-1,-1),'TOP')
                       ]))
u.wrapOn(c,width,height)
u.drawOn(c,8.1*inch,0.85*inch)


c.showPage()
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
c.drawImage(de,2.1*inch,5.6*inch,width=1*inch,height=1*inch,preserveAspectRatio=True)
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
c.drawImage(bg,0*inch,6*inch,width=12*inch,height=3*inch,preserveAspectRatio=True)
drawing = svg2rlg(logo)
scaleFactor = 1./0.9
drawing.width *= scaleFactor
drawing.height *= scaleFactor
drawing.scale(scaleFactor, scaleFactor)
renderPDF.draw(drawing, c, 30, 570)
c.drawInlineImage(de,8*inch,5.5*inch,width=1*inch,height=1.4*inch,preserveAspectRatio=True)
black50transparent = Color( 0, 0, 0, alpha=0.5)
c.setFillColor(black50transparent)
c.rect(-20, 6.07*inch, 6.5*inch, 1*inch,stroke=0,fill=1)
blue50transparent = Color( 0, 0, 255, alpha=0.75)
c.setFillColor(colors.white)
c.setFont("Helvetica-Bold",20)
c.drawString(30, 6.5*inch, "WE SUPPORT YOU. WORLDWIDE.")
c.setFillGray(0.5)
c.rect(448,6.07*inch, 6*inch, 0.25*inch,stroke=0,fill=1)

c.drawImage(i8,25,4.2*inch,width=2.25*inch,height=1.5*inch)

c.drawImage(i9,60,2.6*inch,width=1.25*inch,height=1.5*inch)

c.drawImage(i10,58,0.4*inch,width=1.45*inch,height=1.75*inch)

c.drawImage(i11,475,5.2*inch,width=0.57*inch,height=0.5*inch)
textobject = c.beginText()
textobject.setTextOrigin(7.25*inch, 5.4*inch)
textobject.setFont("Helvetica-Bold", 8)
textobject.setFillColorRGB(0,0,0)
textobject.textLines('''
                    SWISS
                      ''')
c.drawText(textobject)

textobject = c.beginText()
textobject.setTextOrigin(6.65*inch, 5*inch)
textobject.setFont("Helvetica", 6.6)
textobject.setFillColorRGB(0,0,0)
textobject.textLines('''
                    BRUGG LIFTING
                    Wydenstrasse 36
                    5242 Birr
                    Switzerland
                    T +41 (0) 56 464 42 42
                    F +41 (0) 56 464 42 84
                    info.lifting@brugg.com
                    brugglifting.com
                      ''')
c.drawText(textobject)



c.drawImage(i11,578,5.2*inch,width=0.57*inch,height=0.5*inch)
textobject = c.beginText()
textobject.setTextOrigin(8.7*inch, 5.4*inch)
textobject.setFont("Helvetica-Bold", 8)
textobject.setFillColorRGB(0,0,0)
textobject.textLines('''
                    SWISS
                      ''')
c.drawText(textobject)
textobject = c.beginText()
textobject.setTextOrigin(7.95*inch, 5*inch)
textobject.setFont("Helvetica", 6)
textobject.setFillColorRGB(0,0,0)
textobject.textLines('''
                    BRUGG LIFTING
                    Chemin de Foret 12
                    1024 Ecublens
                    Switzerland
                    T +41 (0) 21 634 20 21
                    F +41 (0) 21 635 09 71
                    vente.lifting@brugg.com
                    brugglifting.com
                      ''')
c.drawText(textobject)




c.drawImage(i12,680,5.2*inch,width=0.57*inch,height=0.5*inch)
textobject = c.beginText()
textobject.setTextOrigin(10.1*inch, 5.4*inch)
textobject.setFont("Helvetica-Bold", 8)
textobject.setFillColorRGB(0,0,0)
textobject.textLines('''
                    USA
                      ''')
c.drawText(textobject)
textobject = c.beginText()
textobject.setTextOrigin(9.4*inch, 5*inch)
textobject.setFont("Helvetica", 6)
textobject.setFillColorRGB(0,0,0)
textobject.textLines('''
                    BRUGG LIFTING
                    1801 Parrish Drive
                    P.O. Box 551
                    US-Rome,  GA  30162-0551
                    T +1 706 235 6315
                    F +1 706 235 6035
                    lifting.usa@brugg.com
                    brugglifting.com
                      ''')
c.drawText(textobject)



c.drawImage(i13,475,3.4*inch,width=0.57*inch,height=0.5*inch)
textobject = c.beginText()
textobject.setTextOrigin(7.37*inch, 3.6*inch)
textobject.setFont("Helvetica-Bold", 8)
textobject.setFillColorRGB(0,0,0)
textobject.textLines('''
                    CHINA
                      ''')
c.drawText(textobject)
textobject = c.beginText()
textobject.setTextOrigin(6.6*inch, 3.2*inch)
textobject.setFont("Helvetica", 6)
textobject.setFillColorRGB(0,0,0)
textobject.textLines('''
                    BRUGG LIFTING
                    Plant 1, Nr. 88 Jinling
                    Suzhou Industrial Park
                    Jiangsu Province, 215121
                    P.R. China
                    T +86 512 6299 0779
                    F +86 512 6299 0774
                    lifting.cn@brugg.com
                    brugglifting.cn
                      ''')
c.drawText(textobject)



c.drawImage(i14,580,3.4*inch,width=0.57*inch,height=0.5*inch)
textobject = c.beginText()
textobject.setTextOrigin(8.8*inch, 3.6*inch)
textobject.setFont("Helvetica-Bold", 8)
textobject.setFillColorRGB(0,0,0)
textobject.textLines('''
                    DUBAI
                      ''')
c.drawText(textobject)
textobject = c.beginText()
textobject.setTextOrigin(8*inch, 3.2*inch)
textobject.setFont("Helvetica", 6)
textobject.setFillColorRGB(0,0,0)
textobject.textLines('''
                    BRUGG LIFTING
                    LOB15 -218
                    Jebel Ali Free Zone
                    Dubai
                    United Arab Emirates
                    T +971 4 887 69 91
                    F +971 4 887 69 92
                    lifting.uae@brugg.com
                    brugglifting.com
                      ''')
c.drawText(textobject)

c.drawImage(i15,680,3.4*inch,width=0.5*inch,height=0.5*inch)
textobject = c.beginText()
textobject.setTextOrigin(10.05*inch, 3.65*inch)
textobject.setFont("Helvetica-Bold", 8)
textobject.setFillColorRGB(0,0,0)
textobject.textLines('''
                    WORLDWIDE
                      ''')
c.drawText(textobject)
textobject = c.beginText()
textobject.setTextOrigin(9.4*inch, 3.1*inch)
textobject.setFont("Helvetica", 6)
textobject.setFillColorRGB(0,0,0)
textobject.textLines('''
                    Our quality products are
                    available from more than
                    20 distributing partners
                    around the world.
                      ''')
c.drawText(textobject)

textobject = c.beginText()
textobject.setTextOrigin(2.95*inch, 5.5*inch)
textobject.setFont("Helvetica", 8)
textobject.setFillColorRGB(0,0,0)
textobject.textLines('''
                    brugglifting.com The compact informative homepage
                    Our Homepage provides you with vivid depictions of our
                    range. You can intuitively make preselections to meet y
                    requirements and find your BRUGG LIFTING contacts all o
                    with just a click. For the latest information, just vis
                      ''')
c.drawText(textobject)

textobject = c.beginText()
textobject.setTextOrigin(2.95*inch, 4.5*inch)
textobject.setFont("Helvetica", 8)
textobject.setFillColorRGB(0,0,0)
textobject.textLines('''
                    RLP Calculate the service life of your ropes
                    Log in to our service life calculator on our website and
                    of your ropes to calculate their service life
                      ''')
c.drawText(textobject)

textobject = c.beginText()
textobject.setTextOrigin(2.95*inch, 3.5*inch)
textobject.setFont("Helvetica", 8)
textobject.setFillColorRGB(0,0,0)
textobject.textLines('''
                    instructions for Use Important tips for rope handling
                    Together with every rope delivered by us, you will be pro
                    illustrated  application  instructions  on  appropriate
                    transport to rope control, you will get all useful inform
                      ''')
c.drawText(textobject)

textobject = c.beginText()
textobject.setTextOrigin(2.95*inch, 1.7*inch)
textobject.setFont("Helvetica", 8)
textobject.setFillColorRGB(0,0,0)
textobject.textLines('''
                    User Reference Guide About the handling our ropes
                    Make  use  of  our  extensive  know-how  about  rope  han
                    Link on our website takes you to our User Reference Guide
                    both find comprehensive technical details and tips and ma
                    requested information via a targeted full-text search. Yo
                    data as a PDF file.
                      ''')
c.drawText(textobject)


textobject = c.beginText()
textobject.setTextOrigin(6.6*inch, 1.3*inch)
textobject.setFont("Helvetica-Bold", 35)
textobject.setFillColorRGB(0,0,0,alpha=0.4)
textobject.textLines('''
                    brugglifting.com
                      ''')
c.drawText(textobject)

textobject = c.beginText()
textobject.setTextOrigin(6.6*inch, 0.75*inch)
textobject.setFont("Helvetica-Bold", 5)
textobject.setFillColorRGB(0,0,0,alpha=0.4)
textobject.textLines('''
                    Creation date 09/2016
                    Subject to changes. Nonbinding indication of measures. No warranty for printing errors or errors.
                    If not agreed otherwise, our general conditions of sale and delivery are valid.
                    We thank OSMA-Aufzuge for the provision of the photos on the following pages 9, 15
                    Design, realization www.schaefer design.com
                      ''')
c.drawText(textobject)


c.showPage()
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
c.drawImage(bg,0*inch,6*inch,width=12*inch,height=3*inch,preserveAspectRatio=True)
# For HRS
drawing = svg2rlg(logo)
scaleFactor = 1./0.9
drawing.width *= scaleFactor
drawing.height *= scaleFactor
drawing.scale(scaleFactor, scaleFactor)
renderPDF.draw(drawing, c, 20, 570)
black50transparent = Color(0,0,0, alpha=0.5)
c.setFillColor(black50transparent)
c.rect(-20,6.07*inch, 8.5*inch, 0.75*inch,stroke=0,fill=1)
c.setFillColor(colors.white)
c.setFont("Helvetica-Bold",20)
c.drawString(20, 6.4*inch, "WEDGE SOCKET")
c.setFont("Helvetica",10)

c.drawString(190, 6.4*inch, "Symmetrical [EN 13411-7] with Eyelet Bolt [DIN 444]")

black50transparent = Color(169,169,169, alpha=0.35)
c.setFillColor(black50transparent)
c.rect(585,6.07*inch, 12*inch, 0.25*inch,stroke=0,fill=1)

textobject = c.beginText()
textobject.setTextOrigin(20, 5.7*inch)
c.setFillColor(colors.black)
textobject.setFont("Helvetica", 7)
textobject.textLines('''
                           Product Data
                           wedge socket welded, steel zinc-plated
                            incl. wedge, bolt and safety pins pre-assembled
                           wedge socket transmits 80% of minimal breaking load
                           of traction rope or governor rope
                           eyelet bolt welded, steel zinc-plated
                           in connection with the wedge socket the eyelet bolt transmits
                           80% of the minimal breaking load of the elevator rope
                           for mounting and operation the explanations in appendix B
                            of the norm EN 13411-7 are valid''')
c.drawText(textobject)

textobject = c.beginText()
textobject.setTextOrigin(3.5*inch, 5.7*inch)
c.setFillColor(colors.black)
textobject.setFont("Helvetica", 7)
textobject.textLines('''
                           Advantages
                            can be assembled safely and simply on-site
                            springs, buffers and other accessories can
                            be mounted individually
                            ''')
c.drawText(textobject)


c.drawImage(a,1*inch,1.5*inch,width=0.75*inch,height=3*inch,preserveAspectRatio=True)
c.drawImage(am,2*inch,1.7*inch,width=0.75*inch,height=2.75*inch,preserveAspectRatio=True)
c.drawImage(d,3*inch,1.65*inch,width=0.75*inch,height=2.75*inch,preserveAspectRatio=True)
c.drawImage(fp,4*inch,1.45*inch,width=0.75*inch,height=3*inch,preserveAspectRatio=True)
c.drawImage(fp2,5*inch,1.4*inch,width=0.75*inch,height=3*inch,preserveAspectRatio=True)
c.drawImage(fp3,6*inch,1.4*inch,width=0.75*inch,height=3*inch,preserveAspectRatio=True)

itemn = Paragraph('<para  fontname = "Helvetica-Bold"fontsize =4  >item number</para>',stylesN)
rope = Paragraph('<para lindent=15 fontname = "Helvetica-Bold" fontsize =4>rope-@</para>',stylesN)
di = Paragraph('<para fontname = "Helvetica-Bold" fontsize =4>d<br/></para>',stylesN)

di1= Paragraph('<para  fontname = "Helvetica-Bold" fontsize =4>d1</para>',stylesN)
l1 = Paragraph('<para  fontname = "Helvetica-Bold" fontsize =4>L1</para>',stylesN)
l2 = Paragraph('<para  fontname = "Helvetica-Bold" fontsize =4>L2</para>',stylesN)
l3 = Paragraph('<para fontname = "Helvetica-Bold" fontsize =4>L3</para>',stylesN)

p1 = Paragraph('<para align = "LEFT" leftindent=5 fontname = "Helvetica-Bold" fontsize =7>A</para>',stylesN)
p2 = Paragraph('<para  fontname = "Helvetica-Bold" fontsize =4>mm</para>',stylesN)
p3 = Paragraph('<para align = "LEFT" leftindent=3 fontname = "Helvetica-Bold" fontsize =7>AM</para>',stylesN)
p4 = Paragraph('<para align = "LEFT" leftindent=3 fontname = "Helvetica-Bold" fontsize =7>D</para>',stylesN)
p5 = Paragraph('<para leftindent=3 align = "LEFT" fontname = "Helvetica-Bold" fontsize =7>FP</para>',stylesN)
p6 = Paragraph('<para leftindent=3 align = "LEFT" fontname = "Helvetica-Bold" fontsize =7>FP2</para>',stylesN)
p7 = Paragraph('<para leftindent=3 align = "LEFT" fontname = "Helvetica-Bold" fontsize =7>FP3</para>',stylesN)

itemn1 = Paragraph('<para  fontname = "Helvetica"fontsize =4  >64109</para>',stylesN)
rope1 = Paragraph('<para  fontname = "Helvetica" fontsize =4>5.0</para>',stylesN)
rope2 = Paragraph('<para  fontname = "Helvetica" fontsize =4>6.5</para>',stylesN)

dit = Paragraph('<para fontname = "Helvetica" fontsize =4>M10<br/></para>',stylesN)

di1t= Paragraph('<para  fontname = "Helvetica" fontsize =4></para>',stylesN)
l1t = Paragraph('<para  fontname = "Helvetica" fontsize =4>265</para>',stylesN)
l2t = Paragraph('<para  fontname = "Helvetica" fontsize =4>180</para>',stylesN)
l3t = Paragraph('<para fontname = "Helvetica" fontsize =4></para>',stylesN)
d1 = [[itemn,rope,'', di,di1,l1,l2,l3],
        ['','','','','','','','',],
      [p1,p2,'','','','','',''],
      [itemn1,rope1,rope2,dit,di1t,l1t,l2t,l3t],
      [itemn1,rope1,rope2,dit,di1t,l1t,l2t,l3t],
      [itemn1,rope1,rope2,dit,di1t,l1t,l2t,l3t],
      [itemn1,rope1,rope2,dit,di1t,l1t,l2t,l3t],
      [itemn1,rope1,rope2,dit,di1t,l1t,l2t,l3t],
      [itemn1,rope1,rope2,dit,di1t,l1t,l2t,l3t],
      [p3,'','','','','','',''],
      [itemn1,rope1,rope2,dit,di1t,l1t,l2t,l3t],
      [itemn1,rope1,rope2,dit,di1t,l1t,l2t,l3t],
      [itemn1,rope1,rope2,dit,di1t,l1t,l2t,l3t],
      [itemn1,rope1,rope2,dit,di1t,l1t,l2t,l3t],
      [itemn1,rope1,rope2,dit,di1t,l1t,l2t,l3t],
      [itemn1,rope1,rope2,dit,di1t,l1t,l2t,l3t],
      [p4,'','','','','','',''],
      [itemn1,rope1,rope2,dit,di1t,l1t,l2t,l3t],
      [itemn1,rope1,rope2,dit,di1t,l1t,l2t,l3t],
      [itemn1,rope1,rope2,dit,di1t,l1t,l2t,l3t],
      [itemn1,rope1,rope2,dit,di1t,l1t,l2t,l3t],
      [itemn1,rope1,rope2,dit,di1t,l1t,l2t,l3t],
      [itemn1,rope1,rope2,dit,di1t,l1t,l2t,l3t],
      [p5,'','','','','','',''],
      [itemn1,rope1,rope2,dit,di1t,l1t,l2t,l3t],
      [itemn1,rope1,rope2,dit,di1t,l1t,l2t,l3t],
      [itemn1,rope1,rope2,dit,di1t,l1t,l2t,l3t],
      [itemn1,rope1,rope2,dit,di1t,l1t,l2t,l3t],
      [p6,'','','','','','',''],
      [itemn1,rope1,rope2,dit,di1t,l1t,l2t,l3t],
      [itemn1,rope1,rope2,dit,di1t,l1t,l2t,l3t],
      [itemn1,rope1,rope2,dit,di1t,l1t,l2t,l3t],
      [itemn1,rope1,rope2,dit,di1t,l1t,l2t,l3t],
      [p7,'','','','','','',''],
      [itemn1,rope1,rope2,dit,di1t,l1t,l2t,l3t],
      [itemn1,rope1,rope2,dit,di1t,l1t,l2t,l3t],
      [itemn1,rope1,rope2,dit,di1t,l1t,l2t,l3t],
      [itemn1,rope1,rope2,dit,di1t,l1t,l2t,l3t],
      ]

t1 = Table(d1,colWidths=[1.25*cm,2*cm,1*cm,1*cm,1*cm,1*cm,1*cm,1*cm],rowHeights=3.5*mm)
t1.setStyle(TableStyle([

                            ('SPAN',(1,0),(2,0)),
                            ('FONTNAME',(0,0),(-1,-1),'Helvetica-Bold'),
                            ('BACKGROUND',(0,2),(-8,-36),'#DCDCDC'),#for A
                            ('BACKGROUND',(2,3),(-8,-30),'#DCDCDC'),#for A
                             ('BACKGROUND',(0,9),(-8,-29),'#DCDCDC'),#for AM
                             ('BACKGROUND',(1,10),(-7,-23),'#DCDCDC'),#for AM
                             ('BACKGROUND',(0,16),(-8,-22),'#DCDCDC'),#for D
                              ('BACKGROUND',(1,17),(-7,-16),'#DCDCDC'),#for D
                              ('BACKGROUND',(0,23),(-8,-15),'#DCDCDC'),#for FP
                              ('BACKGROUND',(1,24),(-7,-11),'#DCDCDC'),#for FP
                              ('BACKGROUND',(0,29),(-8,-11),'#DCDCDC'),#for FP2
                              ('BACKGROUND',(1,29),(-7,-6),'#DCDCDC'),#for FP2
                              ('BACKGROUND',(0,34),(-8,-6),'#DCDCDC'),#for FP3
                              ('BACKGROUND',(1,34),(-7,-1),'#DCDCDC'),#for FP3
                               # ('BACKGROUND',(2,10),(-8,-1),'#DCDCDC'),

                            ('LEFTPADDING',(2,0),(-1,-1),-20),
                            ('LEFTPADDING',(5,0),(-1,-1),-20),


                            ('LINEBELOW',(0,1),(-2,-1),0.25,colors.black),

                             ('ALIGN',(1,0),(-1,-1),'CENTER'),
                            # ('ALIGN',())
                            # ('VALIGN',(0,0),(-1,-1),'TOP'),
                             ('VALIGN',(0,0),(-1,-1),'TOP')
                       ]))

t1.wrapOn(c,width,height)
t1.drawOn(c,7.25*inch,0.75*inch)

textobject = c.beginText()
textobject.setTextOrigin(7.25*inch, 0.65*inch)
c.setFillColor(colors.black)
textobject.setFont("Helvetica", 5)
textobject.textLines('''
                          Other sizes available upon request.
                           You will find the item numbers for all combination possibilities in the price list.
                            ''')
c.drawText(textobject)

c.showPage()
c.drawImage(bg,0*inch,6*inch,width=12*inch,height=3*inch,preserveAspectRatio=True)
# For HRS
drawing = svg2rlg(logo)
scaleFactor = 1./0.9
drawing.width *= scaleFactor
drawing.height *= scaleFactor
drawing.scale(scaleFactor, scaleFactor)
renderPDF.draw(drawing, c, 20, 570)
c.setFillColor('#87CEFA')
c.rect(-20,6.07*inch, 1.75*inch, 0.5*inch,stroke=0,fill=1)

c.rect(50,6.07*inch, 12*inch, 0.25*inch,stroke=0,fill=1)
c.rect(670,6.07*inch, 1.75*inch, 0.5*inch,stroke=0,fill=1)

c.setFillColor(colors.white)
c.setFont("Helvetica-Bold",20)
c.drawCentredString(50, 6.25*inch, "8x19")
c.drawCentredString(740, 6.25*inch, "6x25")

c.setFont("Helvetica-Bold",8)

c.drawString(120, 6.15*inch, "COMPENSATION ROPES")

c.drawImage(X19,30,4.5*inch,width=1*inch,height=1*inch,preserveAspectRatio=True)
c.setFillColor(colors.black)

textobject = c.beginText()
textobject.setTextOrigin(120, 5.45*inch)
c.setFillColor(colors.black)
textobject.setFont("Helvetica", 7)
textobject.textLines('''
                           and number of trips, also under difficult  highest demandas
                           on breaking force, elongation  elongation number of trips,
                           also under difficult instalation''')
c.drawText(textobject)

itemn = Paragraph('<para  fontname = "Helvetica-Bold"fontsize =4  >item number</para>',stylesN)
rope = Paragraph('<para lindent=-5 fontname = "Helvetica-Bold" fontsize =4>rope-@</para>',stylesN)
brk = Paragraph('<para leftindent = -30 fontname = "Helvetica-Bold" fontsize =4>breaking load<br/>min.</para>',stylesN)
weight= Paragraph('<para leftindent=-5 fontname = "Helvetica-Bold" fontsize =4>weight</para>',stylesN)
con = Paragraph('<para leftindent=-50 fontname = "Helvetica-Bold" fontsize =4>construction</para>',stylesN)



# i = Paragraph('<para> </para>',stylesN)
mm = Paragraph('<para leftindent =-4 fontname = "Helvetica" fontsize =4 underlineGap = 1>mm</para>',stylesN)
inc = Paragraph('<para leftindent =10 fontname = "Helvetica" fontsize =4>in</para>',stylesN)
kN= Paragraph('<para leftindent =25 fontname = "Helvetica" fontsize =4>kN</para>',stylesN)
lbs = Paragraph('<para leftindent =-10 fontname = "Helvetica" fontsize =4>lbs</para>',stylesN)
kg = Paragraph('<para leftindent =-15 fontname = "Helvetica" fontsize =4>kg/100m</para>',stylesN)
lb = Paragraph('<para leftindent =-45 fontname = "Helvetica" fontsize =4>lb/ft</para>',stylesN)
# c = Paragraph('<para> </para>',stylesN)
i = Paragraph('<para fontname = "Helvetica" fontsize =4>10699 </para>',stylesN)
mm1 = Paragraph('<para leftindent =-4 fontname = "Helvetica" fontsize =4>6.0</para>',stylesN)
inc1 = Paragraph('<para leftindent =10 fontname = "Helvetica" fontsize =4>5/16</para>',stylesN)
kN1= Paragraph('<para leftindent =25 fontname = "Helvetica" fontsize =4>42.7</para>',stylesN)
lbs1 = Paragraph('<para leftindent =-11 fontname = "Helvetica" fontsize =4>9.599</para>',stylesN)
kg1 = Paragraph('<para leftindent =-15 fontname = "Helvetica" fontsize =4>26.9</para>',stylesN)
lb1 = Paragraph('<para  leftindent =-45 fontname = "Helvetica" fontsize =4>0.181</para>',stylesN)
con1 = Paragraph('<para fontname = "Helvetica" fontsize =4 leftindent=-70>9x19S-PWRC 1570 UsZ.(RRL)</para>',stylesN)




data = [[itemn,'',rope,'',brk,weight,'',con],
            ['',mm,inc,kN,lbs,kg,lb,''],
             [i,mm1,inc1,kN1,lbs1,kg1,lb1,con1],




            ]


t = Table(data,colWidths=[1*cm,1*cm,0.2*cm,2*cm,1*cm,1.75*cm,1.5*cm],rowHeights=0.7*cm)
t.setStyle(TableStyle([

                             # ('LINEABELOW',(0,2),(-1,-1),0.25,colors.black),
                            ('SPAN',(2,0),(2,0)),
                            ('SPAN',(3,0),(2,0)),

                            ('FONTNAME',(0,0),(-1,-1),'Helvetica-Bold'),
                            ('BACKGROUND',(1,0),(-6,-1),'#DCDCDC'),
                            ('LEFTPADDING',(2,0),(-1,-1),-20),
                            ('LEFTPADDING',(5,0),(-1,-1),-20),


                            ('LINEBELOW',(0,0),(-1,-1),0.25,colors.black),

                             ('ALIGN',(0,0),(-1,-1),'CENTER'),
                            # ('ALIGN',())
                            # ('VALIGN',(0,0),(-1,-1),'TOP'),
                             ('VALIGN',(0,0),(-1,-1),'TOP')
                       ]))

t.wrapOn(c, width,height)
t.drawOn(c, 120,4*inch)
textobject = c.beginText()
textobject.setTextOrigin(120, 3.85*inch)
c.setFillColor(colors.black)
textobject.setFont("Helvetica", 7)
textobject.textLines('''
                          Further nominal strengthd diameters (including imperial dimensions)
                          Rope diameter-tolerances according to EN12385-5/ISO 4344.''')
c.drawText(textobject)
c.drawImage(sx25,5.75*inch,4.5*inch,width=1*inch,height=1*inch,preserveAspectRatio=True)
c.setFillColor(colors.black)

textobject = c.beginText()
textobject.setTextOrigin(7*inch, 5.45*inch)
c.setFillColor(colors.black)
textobject.setFont("Helvetica", 7)
textobject.textLines('''
                           and number of trips, also under difficult  highest demandas
                           on breaking force, elongation  elongation number of trips,
                           also under difficult instalation''')
c.drawText(textobject)

itemn = Paragraph('<para  fontname = "Helvetica-Bold"fontsize =4  >item number</para>',stylesN)
rope = Paragraph('<para lindent=-5 fontname = "Helvetica-Bold" fontsize =4>rope-@</para>',stylesN)
brk = Paragraph('<para leftindent = -30 fontname = "Helvetica-Bold" fontsize =4>breaking load<br/>min.</para>',stylesN)
weight= Paragraph('<para leftindent=-5 fontname = "Helvetica-Bold" fontsize =4>weight</para>',stylesN)
con = Paragraph('<para leftindent=-50 fontname = "Helvetica-Bold" fontsize =4>construction</para>',stylesN)



# i = Paragraph('<para> </para>',stylesN)
mm = Paragraph('<para leftindent =-4 fontname = "Helvetica" fontsize =4 underlineGap = 1>mm</para>',stylesN)
inc = Paragraph('<para leftindent =10 fontname = "Helvetica" fontsize =4>in</para>',stylesN)
kN= Paragraph('<para leftindent =25 fontname = "Helvetica" fontsize =4>kN</para>',stylesN)
lbs = Paragraph('<para leftindent =-10 fontname = "Helvetica" fontsize =4>lbs</para>',stylesN)
kg = Paragraph('<para leftindent =-15 fontname = "Helvetica" fontsize =4>kg/100m</para>',stylesN)
lb = Paragraph('<para leftindent =-45 fontname = "Helvetica" fontsize =4>lb/ft</para>',stylesN)
# c = Paragraph('<para> </para>',stylesN)
i = Paragraph('<para fontname = "Helvetica" fontsize =4>10699 </para>',stylesN)
mm1 = Paragraph('<para leftindent =-4 fontname = "Helvetica" fontsize =4>6.0</para>',stylesN)
inc1 = Paragraph('<para leftindent =10 fontname = "Helvetica" fontsize =4>5/16</para>',stylesN)
kN1= Paragraph('<para leftindent =25 fontname = "Helvetica" fontsize =4>42.7</para>',stylesN)
lbs1 = Paragraph('<para leftindent =-11 fontname = "Helvetica" fontsize =4>9.599</para>',stylesN)
kg1 = Paragraph('<para leftindent =-15 fontname = "Helvetica" fontsize =4>26.9</para>',stylesN)
lb1 = Paragraph('<para  leftindent =-45 fontname = "Helvetica" fontsize =4>0.181</para>',stylesN)
con1 = Paragraph('<para fontname = "Helvetica" fontsize =4 leftindent=-70>9x19S-PWRC 1570 UsZ.(RRL)</para>',stylesN)




data = [[itemn,'',rope,'',brk,weight,'',con],
            ['',mm,inc,kN,lbs,kg,lb,''],
             [i,mm1,inc1,kN1,lbs1,kg1,lb1,con1],




            ]


t = Table(data,colWidths=[1*cm,1*cm,0.2*cm,2*cm,1*cm,1.75*cm,1.5*cm],rowHeights=0.7*cm)
t.setStyle(TableStyle([

                             # ('LINEABELOW',(0,2),(-1,-1),0.25,colors.black),
                            ('SPAN',(2,0),(2,0)),
                            ('SPAN',(3,0),(2,0)),

                            ('FONTNAME',(0,0),(-1,-1),'Helvetica-Bold'),
                            ('BACKGROUND',(1,0),(-6,-1),'#DCDCDC'),
                            ('LEFTPADDING',(2,0),(-1,-1),-20),
                            ('LEFTPADDING',(5,0),(-1,-1),-20),


                            ('LINEBELOW',(0,0),(-1,-1),0.25,colors.black),

                             ('ALIGN',(0,0),(-1,-1),'CENTER'),
                            # ('ALIGN',())
                            # ('VALIGN',(0,0),(-1,-1),'TOP'),
                             ('VALIGN',(0,0),(-1,-1),'TOP')
                       ]))

t.wrapOn(c, width,height)
t.drawOn(c, 7*inch,4*inch)




textobject = c.beginText()
textobject.setTextOrigin(7*inch, 3.85*inch)
c.setFillColor(colors.black)
textobject.setFont("Helvetica", 7)
textobject.textLines('''
                          Further nominal strengthd diameters (including imperial dimensions)
                          Rope diameter-tolerances according to EN12385-5/ISO 4344.''')
c.drawText(textobject)

c.setFillColor('#87CEFA')
c.rect(-20,2.5*inch, 1.75*inch, 0.5*inch,stroke=0,fill=1)
c.setFillColor(colors.white)
c.setFont("Helvetica-Bold",20)
c.drawCentredString(50, 2.65*inch, "8x25")
c.drawImage(x25,30,1.25*inch,width=1*inch,height=1*inch,preserveAspectRatio=True)
c.setFillColor(colors.black)

textobject = c.beginText()
textobject.setTextOrigin(120, 2.2*inch)
c.setFillColor(colors.black)
textobject.setFont("Helvetica", 7)
textobject.textLines('''
                           and number of trips, also under difficult  highest demandas
                           on breaking force, elongation  elongation number of trips,
                           also under difficult instalation''')
c.drawText(textobject)
itemn = Paragraph('<para  fontname = "Helvetica-Bold"fontsize =4  >item number</para>',stylesN)
rope = Paragraph('<para lindent=-5 fontname = "Helvetica-Bold" fontsize =4>rope-@</para>',stylesN)
brk = Paragraph('<para leftindent = -30 fontname = "Helvetica-Bold" fontsize =4>breaking load<br/>min.</para>',stylesN)
weight= Paragraph('<para leftindent=-5 fontname = "Helvetica-Bold" fontsize =4>weight</para>',stylesN)
con = Paragraph('<para leftindent=-50 fontname = "Helvetica-Bold" fontsize =4>construction</para>',stylesN)



# i = Paragraph('<para> </para>',stylesN)
mm = Paragraph('<para leftindent =-4 fontname = "Helvetica" fontsize =4 underlineGap = 1>mm</para>',stylesN)
inc = Paragraph('<para leftindent =10 fontname = "Helvetica" fontsize =4>in</para>',stylesN)
kN= Paragraph('<para leftindent =25 fontname = "Helvetica" fontsize =4>kN</para>',stylesN)
lbs = Paragraph('<para leftindent =-10 fontname = "Helvetica" fontsize =4>lbs</para>',stylesN)
kg = Paragraph('<para leftindent =-15 fontname = "Helvetica" fontsize =4>kg/100m</para>',stylesN)
lb = Paragraph('<para leftindent =-45 fontname = "Helvetica" fontsize =4>lb/ft</para>',stylesN)
# c = Paragraph('<para> </para>',stylesN)
i = Paragraph('<para fontname = "Helvetica" fontsize =4>10699 </para>',stylesN)
mm1 = Paragraph('<para leftindent =-4 fontname = "Helvetica" fontsize =4>6.0</para>',stylesN)
inc1 = Paragraph('<para leftindent =10 fontname = "Helvetica" fontsize =4>5/16</para>',stylesN)
kN1= Paragraph('<para leftindent =25 fontname = "Helvetica" fontsize =4>42.7</para>',stylesN)
lbs1 = Paragraph('<para leftindent =-11 fontname = "Helvetica" fontsize =4>9.599</para>',stylesN)
kg1 = Paragraph('<para leftindent =-15 fontname = "Helvetica" fontsize =4>26.9</para>',stylesN)
lb1 = Paragraph('<para  leftindent =-45 fontname = "Helvetica" fontsize =4>0.181</para>',stylesN)
con1 = Paragraph('<para fontname = "Helvetica" fontsize =4 leftindent=-70>9x19S-PWRC 1570 UsZ.(RRL)</para>',stylesN)




data = [[itemn,'',rope,'',brk,weight,'',con],
            ['',mm,inc,kN,lbs,kg,lb,''],
             [i,mm1,inc1,kN1,lbs1,kg1,lb1,con1],
             [i,mm1,inc1,kN1,lbs1,kg1,lb1,con1],



            ]


t = Table(data,colWidths=[1*cm,1*cm,0.2*cm,2*cm,1*cm,2*cm,1.5*cm],rowHeights=0.7*cm)
t.setStyle(TableStyle([

                             ('LINEABELOW',(0,2),(-1,-1),0.25,colors.black),
                            ('SPAN',(2,0),(2,0)),
                            ('SPAN',(3,0),(2,0)),

                            ('FONTNAME',(0,0),(-1,-1),'Helvetica-Bold'),
                            ('BACKGROUND',(1,0),(-6,-1),'#DCDCDC'),
                            ('LEFTPADDING',(2,0),(-1,-1),-20),
                            ('LEFTPADDING',(5,0),(-1,-1),-20),


                            ('LINEBELOW',(0,0),(-1,-1),0.25,colors.black),
                             ('ALIGN',(0,0),(-1,-1),'CENTER'),
                            # ('ALIGN',())
                            # ('VALIGN',(0,0),(-1,-1),'TOP'),
                             ('VALIGN',(0,0),(-1,-1),'TOP')
                       ]))

t.wrapOn(c, width,height)
t.drawOn(c, 120,0.75*inch)
textobject = c.beginText()
textobject.setTextOrigin(120, 0.65*inch)
c.setFillColor(colors.black)
textobject.setFont("Helvetica", 7)
textobject.textLines('''
                          Further nominal strengthd diameters (including imperial dimensions)
                          Rope diameter-tolerances according to EN12385-5/ISO 4344.''')
c.drawText(textobject)
c.showPage()
c.save()
