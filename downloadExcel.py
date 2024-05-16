import streamlit as st
import pandas as pd
import io

def main():
    st.title("Excel Sheet Selector")

    # File upload
    uploaded_file = st.file_uploader("Upload an Excel file", type=["xlsx", "xls"])

    if uploaded_file is not None:
        # Read the Excel file
        try:
            xls = pd.ExcelFile(uploaded_file)
            sheet_names = xls.sheet_names
            selected_sheets = st.multiselect("Select sheets", sheet_names)
            
            if st.button("Download Selected Sheets"):
                excel_data = download_data(xls, selected_sheets)
                download_location = st.text_input("Enter download location", value="selected_sheets.xlsx")
                st.markdown(get_binary_file_downloader_html(excel_data, download_location), unsafe_allow_html=True)
        except Exception as e:
            st.error(f"Error: {e}")

def download_data(xls, selected_sheets):
    # Prepare a buffer for storing the Excel data
    excel_data = io.BytesIO()
    with pd.ExcelWriter(excel_data, engine="xlsxwriter") as writer:
        for sheet_name in selected_sheets:
            df = pd.read_excel(xls, sheet_name)
            df.to_excel(writer, sheet_name=sheet_name, index=False)

    excel_data.seek(0)
    return excel_data

def get_binary_file_downloader_html(bin_file, file_label='Excel File'):
    with open(bin_file.name, 'wb') as f:
        f.write(bin_file.read())
    return f'<a href="data:application/octet-stream;base64,{bin_file}">Download {file_label}</a>'

if __name__ == "__main__":
    main()
