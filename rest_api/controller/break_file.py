from PyPDF2 import PdfFileWriter, PdfFileReader

inputpdf = PdfFileReader(open("/Users/manpreet.singh/git/deeplearning/deepmind/haystack/dataset/postgresql-12-A4.pdf", "rb"))
for i in range(inputpdf.numPages):
    output = PdfFileWriter()
    output.addPage(inputpdf.getPage(i))
    with open("/Users/manpreet.singh/git/deeplearning/deepmind/haystack/dataset/db/document-page%s.pdf" % i, "wb") as outputStream:
        output.write(outputStream)