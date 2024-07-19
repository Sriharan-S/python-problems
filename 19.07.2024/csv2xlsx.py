import pandas as pd

def csv_to_excel(csv_file_path, excel_file_path):
    df = pd.read_csv(csv_file_path)
    df.to_excel(excel_file_path, index=False, engine='openpyxl')
    print(f"CSV file '{csv_file_path}' has been converted to Excel file '{excel_file_path}'.")

csv_file_path = 'input_file.csv'
excel_file_path = 'output_file.xlsx'

csv_to_excel(csv_file_path, excel_file_path)
