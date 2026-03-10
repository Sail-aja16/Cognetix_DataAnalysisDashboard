import pandas as pd

data = {
    "Product": ["Laptop", "Phone", "Tablet", "Headphones"],
    "Sales": [120, 200, 90, 150]
}

df = pd.DataFrame(data)

print("Sales Data:")
print(df)

total_sales = df["Sales"].sum()
print("\nTotal Sales:", total_sales)

highest_sale = df.loc[df["Sales"].idxmax()]
print("\nTop Selling Product:")
print(highest_sale)
