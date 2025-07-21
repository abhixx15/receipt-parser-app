# 🧾 Receipt Parser App – Python Internship Project

A simple full-stack OCR app that extracts structured information from receipts (vendor, date, amount, category), stores it in a database, and visualizes spend trends using Streamlit.

---

## 🚀 Features

- 🔍 **EasyOCR**-based image text extraction
- 📄 Rule-based parser using regex
- 🧠 Extracts: **Vendor, Date, Amount, Category**
- 💾 Stores data in **SQLite**
- 🔎 Keyword / range / pattern **search**
- 🔃 Simple **bubble sort**
- 📈 Aggregations:
  - Total spend
  - Mean, median, mode
  - Monthly trends
  - Vendor frequency
- 🌐 Streamlit UI for interaction

---

## 📁 Project Structure
<img width="504" height="353" alt="image" src="https://github.com/user-attachments/assets/c09b0c46-502a-486d-a5ef-95bb2888c890" />


---

## 🛠️ Setup Instructions

### 🔧 Prerequisites

- Python 3.8 or higher
- `pip` or `conda`
- A clean environment (recommended)

### 📦 Installation

```bash
git clone https://github.com/YOUR_USERNAME/receipt_parser_app.git
cd receipt_parser_app
conda create -n receipt_env python=3.11 -y
conda activate receipt_env
pip install -r requirements.txt    
    
```
#### Running the App
```bash
streamlit run main.py
```
                      
## ⚠️ Limitations

| Area    | Notes                                                                 |
|---------|-----------------------------------------------------------------------|
| OCR     | Accuracy may fail on blurry, angled, or handwritten receipts          |
| Amount  | Parsing relies on keywords like `Total`, `Rs`, `₹`, `Amount`         |
| Sorting | Bubble sort is basic; only suitable for small datasets                |




# Assumptions  
- One transaction per receipt
- Fields appear in standard text form
- EasyOCR works best on high-resolution text

  
### 🔐 Security Notice
This app does not collect or store personal data online. All data stays in your local SQLite database.

### License
- This project is created for educational and internship evaluation purposes only.
- You may reuse the code with attribution for personal or academic use.



### Screenshots

<img width="1918" height="895" alt="image" src="https://github.com/user-attachments/assets/e51cf625-5f3c-4e27-a2cb-8db257d32090" />

#### ✅ 1. Uploading a Receipt
<img width="1027" height="360" alt="image" src="https://github.com/user-attachments/assets/15599072-4919-4e28-a4f1-0203857af87d" />

#### ✅ 2. Parsed Fields
<img width="444" height="346" alt="image" src="https://github.com/user-attachments/assets/9b322670-99cf-4b97-993b-1d647106f7ef" />

#### ✅ 3. Data Table & Stats
<img width="940" height="285" alt="image" src="https://github.com/user-attachments/assets/8cdb8c29-e312-4df2-8ebd-5b3b3143c71f" />

#### ✅ 4. Charts: Spend Trend and Vendor Frequency
<img width="1143" height="553" alt="image" src="https://github.com/user-attachments/assets/737bbe2f-4870-4d6a-81a9-386c9ff4da1d" />



