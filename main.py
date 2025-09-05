import pandas as pd
import sys


def main():
    filename = sys.argv[1]
    df = pd.read_csv(filename, sep=';', converters={'tarmed_code': str})
    df.rename({'tarmed_code': 'PosNo', 'anzahl': 'Menge'}, axis=1, inplace=True)
    result = df.groupby("PosNo")["Menge"].sum().reset_index()
    result.sort_values(by=['PosNo'], inplace=True)
    result.insert(1, 'ZSR', 'Praxis 1')
    writer = pd.ExcelWriter("leistungen.xlsx", engine="xlsxwriter")
    result.to_excel(writer, sheet_name="Sheet1", index=False)
    workbook = writer.book
    worksheet = writer.sheets["Sheet1"]
    format1 = workbook.add_format({"num_format": "###0"})
    worksheet.set_column(2, 2, 18, format1)
    writer.close()
    # result.astype({'Menge': 'int'})
    # result.to_excel('leistungen.xlsx', index=False)


if __name__ == "__main__":
    main()
