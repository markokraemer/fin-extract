import time
from pathlib import Path
import PyPDF2
import os

def _export_single_converted_document_lite(pdf_path: Path, output_dir: Path) -> None:
    """
    Extract text from PDF using PyPDF2 and save as markdown
    """
    doc_filename = pdf_path.stem
    
    try:
        # Extract text from PDF
        with open(pdf_path, 'rb') as file:
            pdf_reader = PyPDF2.PdfReader(file)
            text_content = ""
            
            for page_num, page in enumerate(pdf_reader.pages):
                try:
                    page_text = page.extract_text()
                    if page_text.strip():
                        text_content += f"\n\n## Page {page_num + 1}\n\n"
                        text_content += page_text
                except Exception as e:
                    print(f"[warning] Failed to extract text from page {page_num + 1}: {e}")
                    continue
        
        # Save as markdown
        md_filename = output_dir / f"{doc_filename}-with-no-image-refs.md"
        
        # Ensure output directory exists
        output_dir.mkdir(parents=True, exist_ok=True)
        
        with open(md_filename, 'w', encoding='utf-8') as f:
            f.write(f"# {doc_filename}\n\n")
            f.write(text_content)
        
        print(f"[export] {doc_filename}: Successfully extracted text to {md_filename}")
        
    except Exception as e:
        print(f"[error] Failed to process {pdf_path}: {e}")
        raise


def file_data_extraction_lite(reports_folder_name: str, output_folder_name: str):
    """
    Lightweight version: Reads PDFs and extracts text using PyPDF2 instead of docling
    """
    data_folder = Path(__file__).parent / reports_folder_name
    output_dir = Path(output_folder_name)
    
    # Ensure output directory exists
    output_dir.mkdir(parents=True, exist_ok=True)
    
    # Collect all PDFs in the reports folder
    input_doc_paths = sorted(data_folder.glob("*.pdf"))
    if not input_doc_paths:
        print(f"No PDFs found in {data_folder}")
        return
    
    print(f"Found {len(input_doc_paths)} PDF(s) in {data_folder}:")
    for p in input_doc_paths:
        print(f"  - {p.name}")
    
    start_time = time.time()
    
    print(f"Starting lightweight conversion of {len(input_doc_paths)} document(s)...")
    
    # Process each PDF
    success_count = 0
    failure_count = 0
    total_count = 0
    
    for pdf_path in input_doc_paths:
        total_count += 1
        print(f"[convert] Processing {total_count}: {pdf_path.name}")
        
        try:
            _export_single_converted_document_lite(pdf_path, output_dir)
            success_count += 1
        except Exception as e:
            failure_count += 1
            print(f"[warning] Conversion failed for: {pdf_path.name} - {e}")
            continue
    
    end_time = time.time() - start_time
    
    print(
        f"\nProcessed {total_count} document(s). Successful: {success_count}, "
        f"Failed: {failure_count}. "
        f"Elapsed: {end_time:.2f} seconds."
    )


if __name__ == "__main__":
    import time
    start_time = time.time()
    file_data_extraction_lite(reports_folder_name="reports", output_folder_name="out")
    elapsed = time.time() - start_time
    print(f"file_data_extraction_lite completed in {elapsed:.2f} seconds")