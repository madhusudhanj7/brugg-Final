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
X196 = "hrs.jpg"
X198 = "hrs.jpg"
tsr = "hrs.jpg"
x25 = "hrs.jpg"
sx25 = "hrs.jpg"
ex ="hrs.jpg"
width, height = A4
c = Canvas("ER8.pdf",pagesize=landscape(letter))
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
c.save()
