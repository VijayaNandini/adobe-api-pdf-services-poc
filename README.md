# PoC on Adobe PDF Services APIs

### Objective
Build a solution to process 1000+ pages pdf document by using free tier adobe PDF Services API.<br>
The following operations are being performed:
1. Check page count of input PDF
2. If page count is with in 100 pages, **OCR pdf** and generate output pdf.
3. Else, the following operations are being performed:
   - **split** input pdf with each chunk containing 100 pages
   - **OCR** each pdf chunk 
   - **combine** all OCRed PDFs to generate output pdf

### Limitations
This PoC has following limitations:
- Input PDF file size must be below 100MB.
- Input PDF page count must be below 2000.
- After processing, ouput PDF file size must be below 100MB. To ensure that, input PDF size must be maintained lower than 60MB to 70MB.

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
### To Run application
To run streamlit app
```
streamlit run Home.py
```