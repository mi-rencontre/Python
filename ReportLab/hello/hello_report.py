from reportlab.graphics.shapes import Drawing, String
from reportlab.graphics import renderPDF

d = Drawing(500, 500)
s = String(250, 250, 'Hello World!', textAnchor='middle')

d.add(s)

renderPDF.drawToFile(d, 'hello.pdf','A simple PDF file')
