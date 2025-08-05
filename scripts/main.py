# main.py
from scripts.extract import load_data
from scripts.transform import transform_data
from scripts.load import save_to_csv, save_to_sqlite

def main():
    print("Starting Retail Data Pipeline...")

    # Step 1: Extract
    products, sales, returns = load_data()

    # Step 2: Transform
    final_df = transform_data(products, sales, returns)

    # Step 3: Load
    save_to_csv(final_df, "processed/final_report.csv")
    save_to_sqlite(final_df, "database/retail.db")

    print("Pipeline completed successfully.")

if __name__ == "__main__":
    main()
