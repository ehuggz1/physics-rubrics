import json
import urllib.parse
import sys
import os
import glob

def extract_text_from_json(json_path):
    try:
        with open(json_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        full_text = ""
        for page in data.get('Pages', []):
            texts = page.get('Texts', [])
            # Simple extraction, just concatenating
            for text_item in texts:
                for run in text_item.get('R', []):
                    raw_text = run.get('T', '')
                    # pdf2json uses URL encoding
                    decoded_text = urllib.parse.unquote(raw_text)
                    full_text += decoded_text
                full_text += " " 
            full_text += "\n\n"
            
        return full_text
    except Exception as e:
        return f"Error processing {json_path}: {str(e)}"

if __name__ == "__main__":
    # Find all json files that look like our targets
    files = glob.glob("*.json")
    
    for filename in files:
        if "Reducing Token Costs" in filename or "You Don’t Need RAG" in filename or "You Dont Need RAG" in filename or "You_Do_Not_Need_RAG" in filename:
            print(f"Processing {filename}...")
            text = extract_text_from_json(filename)
            out_name = filename.replace('.json', '.extracted.txt')
            with open(out_name, 'w', encoding='utf-8') as f:
                f.write(text)
            print(f"Wrote {out_name}")
