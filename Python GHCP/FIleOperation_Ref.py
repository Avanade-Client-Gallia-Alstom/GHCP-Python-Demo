import PyPDF2

def read_pdf(file_path):    
    with open(file_path, 'rb') as file:
        pdf_reader = PyPDF2.PdfFileReader(file)
        num_pages = pdf_reader.numPages
        text = ''
        for page_num in range(num_pages):
            page = pdf_reader.getPage(page_num)
            text += page.extract_text()
    return text

def main():
    file_path = 'LLMApp.pdf'
    text = read_pdf(file_path)
    print(text)


    