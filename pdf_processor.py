from src.combine_pdf import combine_pdf
from src.export_pdf_to_docx import export_pdf_to_docx
from src.ocr_pdf import ocr_pdf
from src.split_pdf_by_number_of_pages import split_pdf
from dotenv import load_dotenv


load_dotenv()


def pdf_processor(input_pdf_name, doc_needed: bool = False):
    print("Inside pdf_prcessor function")
    print(input_pdf_name)
    processed_pdfs = []
    # Splitting PDF to smaller chunks
    pdfs = split_pdf(input_pdf_name,page_count=5)
    for pdf in pdfs:
        print(f'Processing (OCR) for PDF {pdf}')
        processed_pdf = ocr_pdf(input_pdf_name=pdf)
        processed_pdfs.append(processed_pdf)
    #
    combined_pdf = combine_pdf(*processed_pdfs)
    if doc_needed:
        output_docx = export_pdf_to_docx(input_pdf_name=combined_pdf)
        return output_docx
    else:
        return combined_pdf