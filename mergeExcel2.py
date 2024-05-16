import streamlit as st
import pandas as pd


def merge_all_sheets(excel_files):
    """Merges all sheets from multiple Excel files into a single sheet."""
    merged_df = pd.DataFrame()
    for file in excel_files:
        df = pd.read_excel(file, sheet_name=None)
        for sheet_name, sheet_df in df.items():
            # Optionally add sheet name as a new column or prefix to existing columns
            # sheet_df["Sheet_Name"] = sheet_name  # Add sheet name as a new column
            sheet_df.columns = [f"{sheet_name}_{col}" for col in sheet_df.columns]  # Prefix column names with sheet name
            merged_df = pd.concat([merged_df, sheet_df], ignore_index=True)
    return merged_df


def main():
    """Main function to run the Streamlit app."""
    st.title("Excel Sheet Merger (All Sheets into One)")

    allowed_extensions = ['xlsx', 'xls']  # Allow both xlsx and xls files
    uploaded_files = st.file_uploader("Choose Excel files to merge", type='multiple', accept_extensions=allowed_extensions)

    if uploaded_files:
        if len(uploaded_files) > 0:
            try:
                merged_df = merge_all_sheets(uploaded_files)
                st.dataframe(merged_df)

                download_button = st.button("Download Merged Data (CSV)")
                if download_button:
                    merged_df.to_csv("merged_data.csv", index=False)
                    st.success("Merged data downloaded as 'merged_data.csv'")
            except Exception as e:
                st.error(f"Error merging files: {e}")
        else:
            st.warning("Please select at least one Excel file to merge.")
    else:
        st.info("Upload Excel files to begin merging.")


if __name__ == "__main__":
    main()
