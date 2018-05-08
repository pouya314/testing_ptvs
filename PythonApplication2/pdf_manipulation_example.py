from PyPDF2 import PdfFileWriter, PdfFileReader

inputpdf = PdfFileReader(open("IMMI_Grant_Notification.pdf", "rb"))

for i in range(inputpdf.numPages):
    output = PdfFileWriter()
    output.addPage(inputpdf.getPage(i))
    with open("document-page-{}.pdf".format(i+1), "wb") as outputStream:
        output.write(outputStream)