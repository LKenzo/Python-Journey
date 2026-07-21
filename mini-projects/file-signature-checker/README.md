# File Signature Checker
A Python tool that identifies a file's true format by magic bytes (hex)

## Supported File Types
Currently configured to detect:
* PDF
* PNG
* JPEG / JPG
* ZIP (Standard and Empty)
* EXE (Windows PE)

[!NOTE]
**Limitation:** The MZ header (4D5A) is shared by all Windows PE-format files, not exclusively .exe. This tool will label any PE file as "exe" even if it's actually a .dll or other PE-based format.

## How to Use
Run the script from your terminal. When prompted, enter the name of your file you want to scan, and make sure the file is in the same directory.

```bash
python file_signature_identifier.py <filename>
```

## Testing

Run the test suite with:

```bash
pytest
```