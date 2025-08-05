# 🛒 Retail Product Data Merger & Analyzer

## 📌 Overview
This project simulates a **local data pipeline** using **Python**, **Pandas**, and **SQL (SQLite)** to perform **data extraction, transformation, and loading (ETL)** on retail product data.

The pipeline:
- Merges product, sales, and return datasets (CSV files)
- Cleans and transforms the data
- Generates product-level KPIs like **total revenue** and **return rate**
- Saves the final dataset to both **CSV** and **SQLite database**

---

## 📁 Project Structure
```
retail_data_pipeline/
├── data/ # Raw input CSV files
│ ├── products.csv
│ ├── sales.csv
│ └── returns.csv
├── processed/ # Output folder for cleaned files
│ └── final_report.csv
├── database/ # Local SQLite DB
│ └── retail.db
├── scripts/ # Modular pipeline scripts
│ ├── extract.py
│ ├── transform.py
│ ├── load.py
│ └── main.py
└── README.md
```

## 🧪 Sample KPIs Generated

- 🔢 **Total Revenue** per product
- 📉 **Return Rate** = (Returns / Units Sold)
- 📊 Group-level summaries (can be extended by category/brand)

---

## ⚙️ Tech Stack

- **Language**: Python 3.8+
- **Libraries**: Pandas, SQLite3
- **Data Sources**: CSV files
- **Storage**: SQLite DB (`retail.db`)

---

## 🚀 How to Run the Pipeline

### 1. Clone the Repository

```
git clone https://github.com/your-username/retail-data-analyzer.git
cd retail-data-analyzer
```

### 2. Install Required Libraries
```
pip install pandas
```
### 3. Run the Main Script
```
python scripts/main.py
This will:
Load the CSVs from /data
Transform and clean the data
Save outputs to /processed/final_report.csv and /database/retail.db
```

✅ Sample Output
```
product_id	name	category	price	quantity	total_revenue	return_count	return_rate
P001	Laptop	Electronics	65000	2	130000	1	0.50
P002	Smartphone	Electronics	30000	5	150000	1	0.20
```

📚 What This Project Demonstrates
---
- 📥 Data ingestion from CSV
- 🧹 Data cleaning and merging using Pandas
- 📐 Feature engineering (revenue, return rate)
- 🗃️ Data loading into a relational database (SQLite)
- 🧩 Reusable pipeline design
---

🧠 Future Improvements
---
- Add CLI support for dynamic inputs
- Include visualizations with Matplotlib/Seaborn
- Integrate with cloud storage (S3/GCS) for data I/O
- Use Airflow or Prefect for orchestration (in cloud version)
---

👤 Author
---
- Mohamed Azarudeen S
- Aspiring Cloud Data Engineer | Python | SQL | Data Pipelines

📄 License
This project is licensed under the MIT License.
---
Let me know if you'd like:
- The CSV files are auto-generated and zipped
- The README exported as a `.md` file
- Custom GitHub repo name or branding
---


