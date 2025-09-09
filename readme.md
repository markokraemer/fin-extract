# Reports Field Extractor

Takes in all the reports in a given folder and export a extracted aggregated data into an excel in another given out folder

## Installation

```bash
pip install -r requirements.txt
```

## Usage

```bash
python main.py reports out
```

Where:
- `reports` is the folder containing input PDF files
- `out` is the output folder for processed markdown/json and final Excel file

## Structure

```
main.py                    # entry point
requirements.txt           # dependencies
file_data_extraction.py    # PDF to markdown conversion
agent_field_matching.py    # LLM-based field extraction
excel_exporting.py         # Excel export functionality
models.py                  # Pydantic data models
reports/                   # input folder (create this)
out/                       # output folder (created automatically)
```