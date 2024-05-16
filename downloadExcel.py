import streamlit as st
import pandas as pd


def get_sheet_names(uploaded_file):
    """Reads sheet names from the uploaded Excel file."""
    df = pd.read_excel(uploaded_file, sheet_name=None)
    return list(df.keys())


def download_selected_sheets(dataframes, sheet_names, download_path):
    """Downloads a single Excel file containing selected sheets to the specified path."""
    try:
        with pd.ExcelWriter(download_path) as writer:
            for i, sheet_name in enumerate(sheet_names):
                dataframes[sheet_name].to_excel(writer, sheet_name=sheet_name, index=False)
        st.success(f"Excel file downloaded to '{download_path}'")
    except Exception as e:
        st.error(f"Error reading sheets: {e}")


def main():
    """Main function to run the Streamlit app."""
    st.title("Excel Sheet Downloader")

    uploaded_file = st.file_uploader("Choose an Excel file")

    if uploaded_file is not None:
        sheet_names = get_sheet_names(uploaded_file)

        if sheet_names:
            selected_sheets = st.multiselect("Select sheets to download", sheet_names)

            if selected_sheets:
                download_path = st.text_input("Enter download path (including filename.xlsx):")
                download_button = st.button("Download Selected Sheets")

                if download_button:
                    # Check if path is empty
                    if download_path:
                        try:
                            # Read all sheets into a dictionary
                            dataframes = {sheet_name: pd.read_excel(uploaded_file, sheet_name=sheet_name) for sheet_name in sheet_names}

                            # Download only selected sheets
                            download_selected_sheets(dataframes, selected_sheets, download_path)
                        except Exception as e:
                            st.error(f"Error reading sheets: {e}")
                    else:
                        st.warning("Please enter a download path.")
        else:
            st.warning("No sheets found in the uploaded file.")

    else:
        st.info("Upload an Excel file to get started.")


if __name__ == "__main__":
    main()
