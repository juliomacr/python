from pdfquery import PDFQuery

pdf = PDFQuery('test.pdf')
pdf.load()

#convert the pdf to XML
pdf.tree.write('customers.xml', pretty_print = True)
#pdf
#print(pdf)


# Use CSS-like selectors to locate the elements
#text_elements = pdf.pq('LTTextLineHorizontal')

text_elements = pdf.pq('LTTextBoxHorizontal')

#print(text_elements)

# Extract the text from the elements
text = [t.text for t in text_elements]
print(text)