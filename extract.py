# extract.py
import argparse
import json
from pdf_utils import extract_and_combine
from llm_utils import extract_data_with_llm


def main():
    parser = argparse.ArgumentParser(
        description="Extract structured data from a technical PDF datasheet."
    )
    parser.add_argument("pdf", help="Path to the input PDF file")
    parser.add_argument("template", help="Path to the JSON schema template")
    parser.add_argument("output", help="Path to save the extracted JSON output")
    args = parser.parse_args()

    print("[1/3] Extracting text and OCR...")
    combined_text = extract_and_combine(args.pdf)

    print("[2/3] Running LLM extraction...")
    result = extract_data_with_llm(combined_text, args.template)

    print("[3/3] Saving output to JSON...")
    with open(args.output, 'w') as f:
        json.dump(result, f, indent=2)

    print(f"Extraction complete! Output saved to {args.output}")


if __name__ == "__main__":
    main()