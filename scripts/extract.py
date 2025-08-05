import pandas as pd

def load_data():
    products = pd.read_csv("data/products.csv")
    sales = pd.read_csv("data/sales.csv")
    returns = pd.read_csv("data/returns.csv")
    return products, sales, returns
