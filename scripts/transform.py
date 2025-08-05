import pandas as pd

def transform_data(products, sales, returns):
    # Merge sales with products
    merged = pd.merge(sales, products, on='product_id', how='left')

    # Calculate total revenue
    merged['total_revenue'] = merged['price'] * merged['quantity']

    # Count returns
    return_counts = returns['product_id'].value_counts().rename('return_count')
    merged = merged.merge(return_counts, on='product_id', how='left')
    merged['return_count'] = merged['return_count'].fillna(0)

    # Calculate return rate
    merged['return_rate'] = merged['return_count'] / merged['quantity']

    # Drop duplicates and keep relevant columns
    final_df = merged[['product_id', 'name', 'category', 'price', 'quantity', 'total_revenue', 'return_count', 'return_rate']]

    return final_df
