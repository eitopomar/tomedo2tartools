import pandas as pd
import sys


def main():
    filename = sys.argv[1]
    df = pd.read_csv(filename, sep=';', converters={'tarmed_code': str})
    df.rename({'tarmed_code': 'PosNo', 'anzahl': 'Menge'}, axis=1, inplace=True)
    result = df.groupby("PosNo")["Menge"].sum().reset_index()
    result.sort_values(by=['PosNo'], inplace=True)
    result.insert(1, 'ZSR', 'Praxis 1')
    result.to_excel('leistungen.xlsx', index=False)


if __name__ == "__main__":
    main()
