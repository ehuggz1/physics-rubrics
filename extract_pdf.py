"""Extract text from sample physics clusters PDF using pdfminer"""
from pdfminer.high_level import extract_text
import sys

pdf_path = r'e:\EVHGH\physics-rubrics\Sample Clusters\sample-physics-clusters-2025.pdf'

try:
    text = extract_text(pdf_path)
    print(text)
        
except Exception as e:
    print(f"Error: {e}", file=sys.stderr)
    sys.exit(1)
