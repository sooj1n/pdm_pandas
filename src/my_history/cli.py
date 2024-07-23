import pandas as pd
import sys

def main():
    command = str(sys.argv[1])

    df = pd.read_parquet("~/tmp/history.parquet")

    fdf = df[df['cmd'].str.contains(command)]

    cnt = fdf['cnt'].sum()

    print(cnt)

if __name__ == "__main__":
    main()
