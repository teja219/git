import streamlit as st
import pandas as pd

def merge_excel_files(excel_files):
    combined_dataframes = []
    for file in excel_files:
        data = pd.read_excel(file, sheet_name=None)
        for sheet_name, df in data.items():
            combined_dataframes.append(df)
    combined_df = pd.concat(combined_dataframes, ignore_index=True)
    return combined_df

def main():
    st.title("Excel File Merger")

    st.write("Upload Excel Files")
    uploaded_files = st.file_uploader("Choose Excel files", accept_multiple_files=True, type="xlsx")

    if uploaded_files:
        st.write("Files uploaded successfully!")
        st.write("Merging files...")

        combined_df = merge_excel_files(uploaded_files)

        st.write("Merged Data:")
        st.write(combined_df)

        st.write("Save Merged Excel File")
        file_name = st.text_input("Enter the filename for the merged Excel file (without extension):")
        if file_name:
            st.write(combined_df.to_excel(f"{file_name}.xlsx", index=False, header=True), unsafe_allow_html=True)
            st.success(f"File '{file_name}.xlsx' saved successfully!")

if __name__ == "__main__":
    main()
