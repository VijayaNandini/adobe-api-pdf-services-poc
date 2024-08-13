# PoC on Adobe PDF Services APIs

### Objective
Build a solution to process 500+ pages pdf document by using free tier adobe PDF Services API.
The following operations must be performed:
1. Chunk the document to 10 pages
2. Connect to the API
3. Do the OCR
4. Post processing (flipping the pages if any)
5. Merge the chunks back together

### Virtual Environment
For Windows Machine
1. Create venv
```
python -m venv .venv
```
2. Activate venv
```
.venv/Scripts/activate
```
3. Deactivate venv
```
deactivate
```