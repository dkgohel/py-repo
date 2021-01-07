import PyPDF2
#Loading the PDF file
pdffile = open('hadoop.pdf', 'rb')
#Reader object to read PDFs
Reader = PyPDF2.PdfFileReader(pdffile)

print(Reader.numPages)
#Getting a page by page number
page = Reader.getPage(1)
print(page.getContents())