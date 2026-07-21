# URL Sanitizer
A Python tool that cleans and validates messy URLs — strips protocols, `www.`, 
and trailing slashes, then checks the domain against a real TLD list before 
accepting it as valid.

## What It Does
* Strips `http://`, `https://`, `www.`, and trailing `/` from raw URLs
* Validates the remaining domain against a TLD list (loaded once into a set 
  for fast O(1) lookup, not re-read from disk per check)
* Rejects malformed input (embedded whitespace, missing/invalid TLD, empty 
  segments) by raising a `ValueError`
* Can process a single URL, or a text file of many URLs line-by-line — 
  invalid lines are skipped and reported, not fatal to the whole run

[!NOTE]
**Limitation:** TLD validation is only as good as `tld_list.txt` any TLD not in that file 
(even a real, valid one) will be rejected. A small hand-picked list 
for practice purposes, not a full public suffix list.

## How to Use
Run the script in your terminal. Program will ask you to input the name of your txt file that contains unsanitized url. Please make sure that the file is in the same directory with the script. 

```bash
python sanitizer.py  #enter
<filename>
```

## Testing

Run the test suite with:

```bash
pytest
```