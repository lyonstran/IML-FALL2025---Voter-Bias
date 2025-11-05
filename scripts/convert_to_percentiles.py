import pandas as pd

def convert_to_percentiles(input_file, columns):
    print("INPUT", input_file)
    df = pd.read_csv(input_file)

    # Standardize column names
    df.columns = df.columns.str.lower().str.replace('_', '-').str.strip()
    exclude_cols = {"season", "year", "Week",  "week"}

    # option to select all columns
    if len(columns) == 1 and columns[0].lower() == "all":
        numeric_cols = df.select_dtypes(include=["number"]).columns
        columns = []
        for col in numeric_cols:
            if col not in exclude_cols:
                columns.append(col)

        print("Automatically selected numeric columns:")
        for col in columns:
            print(f"  - {col}")

    missing = []
    for col in columns:
        if col not in df.columns:
            missing.append(col)
    if len(missing) > 0:
        raise ValueError(f"Missing columns in file: {missing}")

    numeric_cols = df.select_dtypes(include=["number"]).columns
    numeric_target_cols = []

    for col in columns:
        if col in numeric_cols and col not in exclude_cols:
            numeric_target_cols.append(col)
        else:
            print(f"Skipping non-numeric or excluded column: {col}")

    if len(numeric_target_cols) == 0:
        print("No numeric columns found among specified columns.")
        return

    
    for col in numeric_target_cols:
        print(f"Converting column: {col}")
        df[col] = df[col].rank(pct = True)  # 0–1 percentile rank 

    #   Select a numeric column
    #   Assigns rank positions to each value
    #	Expresses ranks as percentiles (0–1)                            
    #   Replaces original column with percentile ranks 
    #   np.percentile returns value at a percentile, .rank with pct = TRUE returns corresponding relative/percentile values 

    output_file = input_file.replace(".csv", "_relative.csv")
    df.to_csv(output_file, index=False)
    print("Saved percentile-converted file")


if __name__ == "__main__":
    import sys
    input_file = sys.argv[1]
    columns = sys.argv[2:]
    convert_to_percentiles(input_file, columns)


                                                  