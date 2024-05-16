import streamlit as st
import pandas as pd

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
                download_data(xls, selected_sheets)
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
    st.download_button(
        label="Download Selected Sheets",
        data=excel_data,
        file_name="selected_sheets.xlsx",
        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
    )

if __name__ == "__main__":
    main()
