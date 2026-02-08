import io
import pdfplumber

def extract_text_from_pdf(file_bytes: bytes) -> str:
    pages_text: list[str] = []
    with pdfplumber.open(io.BytesIO(file_bytes)) as pdf:
        for i, page in enumerate(pdf.pages):
            text = page.extract_text()
            if text:
                pages_text.append(f"--- Page {i + 1} ---\n{text}")
    if not pages_text:
        raise ValueError("Could not extract any text from the PDF.")
    return "\n\n".join(pages_text)
