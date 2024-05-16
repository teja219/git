import streamlit as st
import pandas as pd


def merge_sheets_with_filename(excel_files):
    """Merges dataframes from multiple Excel files, appending filenames to sheet names."""
    merged_df = None
    for file in excel_files:
        df = pd.read_excel(file)
        df.columns = [f"{col}_{file.name.split('.')[0]}" for col in df.columns]
        if merged_df is None:
            merged_df = df.copy()
        else:
            merged_df = pd.concat([merged_df, df])
    return merged_df


def main():
    """Main function to run the Streamlit app."""
    st.title("Excel File Merger with Filename in Sheets")

    uploaded_files = st.file_uploader("Choose Excel files to merge", accept_multiple=True)

    if uploaded_files:
        if len(uploaded_files) > 1:
            try:
                merged_df = merge_sheets_with_filename(uploaded_files)
                st.dataframe(merged_df)

                download_button = st.button("Download Merged Data (CSV)")
                if download_button:
                    merged_df.to_csv("merged_data.csv", index=False)
                    st.success("Merged data downloaded as 'merged_data.csv'")
            except Exception as e:
                st.error(f"Error merging files: {e}")
        else:
            st.warning("Please select at least two Excel files to merge.")
    else:
        st.info("Upload Excel files to begin merging.")


if __name__ == "__main__":
    main()
