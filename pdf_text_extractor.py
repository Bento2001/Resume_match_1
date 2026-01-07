from pypdf import PdfReader

def extract_text(pdf_path):
    pdf = PdfReader(pdf_path)
    text_date = ''

    for page in pdf.pages:
        content = page.extract_text()
        text_date += content

    return text_date