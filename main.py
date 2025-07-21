import streamlit as st
from parser import parse_text
from ocr import extract_text_from_image
from database import init_db, insert_data, fetch_all_data
from sort import bubble_sort
from search import keyword_search, range_search, pattern_search
from aggregate import compute_stats, vendor_frequency, monthly_spend
import pandas as pd

init_db()

st.title("Receipt Parser App (Full Stack)")

uploaded_file = st.file_uploader("Upload receipt (.jpg/.png/.pdf/.txt)", type=["jpg", "png", "pdf", "txt"])

if uploaded_file:
    file_type = uploaded_file.type
    with open("temp_input", "wb") as f:
        f.write(uploaded_file.getbuffer())

    if file_type.startswith("image/"):
        text = extract_text_from_image("temp_input")
    else:
        text = uploaded_file.read().decode("utf-8", errors="ignore")

    st.subheader("OCR / Text Output")
    st.code(text)

    parsed = parse_text(text)

    st.subheader("Parsed Fields")
    st.write(parsed)

    if st.button("Save to Database"):
        insert_data(parsed['vendor'], parsed['date'], parsed['amount'], parsed['category'])
        st.success("Data saved successfully!")

st.subheader("View Receipts")
data = fetch_all_data()

if data:
    st.sidebar.header("Search & Filter")
    search_kw = st.sidebar.text_input("Keyword Search")
    if search_kw:
        data = keyword_search(data, search_kw)

    min_amt = st.sidebar.number_input("Min Amount", value=0.0)
    max_amt = st.sidebar.number_input("Max Amount", value=10000.0)
    if st.sidebar.button("Filter by Amount"):
        data = range_search(data, 3, min_amt, max_amt)

    sort_field = st.sidebar.selectbox("Sort By", ["Amount", "Date", "Vendor"])
    reverse = st.sidebar.checkbox("Descending Order")
    field_map = {"Amount": 3, "Date": 2, "Vendor": 1}
    data = bubble_sort(data, field_map[sort_field], reverse)

    df = pd.DataFrame(data, columns=["ID", "Vendor", "Date", "Amount", "Category"])
    st.dataframe(df)

    st.subheader("Aggregated Statistics")
    stats = compute_stats(data)
    st.write(stats)

    st.subheader("Monthly Spend Trend")
    trend = monthly_spend(data)
    st.line_chart(trend)

    st.subheader("Vendor Frequency")
    freq = vendor_frequency(data)
    st.bar_chart(pd.Series(freq))
else:
    st.info("No receipts found in database.")
