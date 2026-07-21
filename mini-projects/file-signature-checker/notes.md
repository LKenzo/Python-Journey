## What I need to start
How do program identify content of a file.
-> Identifying the file signature or magic bytes (Hex).

How to use magic bytes to Identify file extensions
-> By comparing their magic bytes we can get the extension of that file.

How many bytes do I need to read file magic bytes?
-> First 8 bytes, but some signatures are 2 to 4 bytes.

How to read file as hex in Python
-> open file method with "rb"

## What To Use
- open file with "rb" -> to read in binary mode.
- Build a dict to add key and value for signatures