# receipt-parser-app
A simple full-stack app to extract structured data (vendor, date, amount, category) from receipts using OCR or rule-based logic, store it in a database, and analyze expenses with search, sort, and aggregation.

Features  
Upload .jpg, .png, .pdf, .txt receipt files
Extract text using EasyOCR
Parse fields: Vendor, Date, Amount, Category
Store data in SQLite
Search by keyword, range (min/max amount), pattern
Bubble Sort by amount/date/vendor
View:  
Aggregates (sum, mean, median, mode)
Monthly spend trends
Vendor frequency charts
Built with Streamlit

# Project Structure
├── main.py          # Streamlit app UI   
├── parser.py        # Regex-based text field extraction    
├── ocr.py           # EasyOCR image text extractor
├── database.py      # SQLite database manager
├── sort.py          # Bubble sort implementation
├── search.py        # Search utilities (keyword, range, pattern)
├── aggregate.py     # Stats & time-series aggregation
├── requirements.txt # Python dependencies
└── README.md        # Project documentation

Setup Instructions
Prerequisites
Python 3.8+
Conda or venv (recommended)
Step-by-Step Setup
# Create environment
conda create -n receipt_env python=3.11 -y
conda activate receipt_env
# Clone repository
git clone https://github.com/YOUR_USERNAME/receipt-parser-app.git
cd receipt-parser-app
# Install dependencies
pip install -r requirements.txt
If installing manually:
pip install streamlit easyocr pandas
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu
Run the App
streamlit run main.py


# Limitations
Area	     Notes  
OCR        Accuracy	May fail on blurry/angled/handwritten receipts   
Amount     Parsing	Relies on keywords like Total, Rs, ₹, Amount   
Sorting    Speed	Bubble sort is basic; works for small datasets  


# Assumptions  
One transaction per receipt
Fields appear in standard text form
EasyOCR works best on high-resolution text
