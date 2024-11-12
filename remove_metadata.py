import sys
import os
from PyPDF2 import PdfReader, PdfWriter

def remove_metadata(pdf_path):
    
    reader = PdfReader(pdf_path)
    writer = PdfWriter()

    
    for page in reader.pages:
        writer.add_page(page)

    
    base, ext = os.path.splitext(pdf_path)
    cleaned_pdf_path = f"{base}_cleaned{ext}"

    
    with open(cleaned_pdf_path, 'wb') as cleaned_file:
        writer.write(cleaned_file)

    
    print(f"Cleaned PDF saved at: {cleaned_pdf_path}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <path_to_pdf>")
    else:
        remove_metadata(sys.argv[1])
