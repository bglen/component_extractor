# pdf_utils.py
import pdfplumber
from pdf2image import convert_from_path
import pytesseract
from typing import List

def extract_text_from_pdf(pdf_path: str) -> str:
    """Extracts raw text from PDF pages using pdfplumber."""
    pages_text = []
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            pages_text.append(page.extract_text() or "")
    return "\n".join(pages_text)

def ocr_text_from_pdf(pdf_path: str, dpi: int = 300) -> str:
    """Converts each PDF page to an image and runs OCR via pytesseract."""
    images = convert_from_path(pdf_path, dpi=dpi)
    ocr_results = [pytesseract.image_to_string(img) for img in images]
    return "\n".join(ocr_results)

def extract_and_combine(pdf_path: str) -> str:
    """Combines text and OCR results, removing duplicate lines."""
    text = extract_text_from_pdf(pdf_path)
    ocr_text = ocr_text_from_pdf(pdf_path)
    combined = text + "\n" + ocr_text
    seen = set()
    unique_lines = []
    for line in combined.splitlines():
        clean = line.strip()
        if clean and clean not in seen:
            seen.add(clean)
            unique_lines.append(clean)
    return "\n".join(unique_lines)