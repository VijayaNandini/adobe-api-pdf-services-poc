from src.combine_pdf import combine_pdf
from src.export_pdf_to_docx import export_pdf_to_docx
from src.ocr_pdf import ocr_pdf
from src.split_pdf_by_number_of_pages import split_pdf
from src.get_pdf_properties import get_pdf_properties
from dotenv import load_dotenv
import math
import os


load_dotenv()

# Refer the following link to understand the limitations of Adobe PDF Services API:
# https://developer.adobe.com/document-services/docs/overview/limits/

def pdf_processor(input_pdf_name, doc_needed: bool = False):
    print("Inside pdf_prcessor function")
    print(input_pdf_name)
    # Fetching PDF Properties
    pdf_properties = get_pdf_properties(input_pdf_name)
    pdf_page_count = pdf_properties.get("document").get("page_count")
    chunk_page_count = int(os.getenv('CHUNK_PAGE_COUNT')) # Page limit of scanned images is 150, so max value is 150
    if pdf_page_count > chunk_page_count: 
        num_of_chunks = math.ceil(pdf_page_count / 100) 
        if num_of_chunks > 20: # File limit for combine pdf is 20
            return False # Rare case scenario: PDF page count is greater than 2000 (= 100 * 20), we won't process it. Error will be displayed in the input.
        #
        processed_pdfs = []
        # Splitting PDF to smaller chunks
        pdfs = split_pdf(input_pdf_name,page_count=chunk_page_count)
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
    else:
        processed_pdf = ocr_pdf(input_pdf_name)
        return processed_pdf
