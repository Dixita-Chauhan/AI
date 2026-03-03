
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("Coffee Shop Sales.csv")
# Create total_amount column (if not present)
data["total_amount"] = data["unit_price"] * data["transaction_qty"]

# Create Pivot Table
pivot_df = data.pivot_table(
    values="total_amount",
    index="store_location",
    columns="product_category",
    aggfunc="sum"
)

# Plot Chart
pivot_df.plot(kind="bar")


plt.title("Total Sales of Product Category per Store Location")
plt.xlabel("Store Location")
plt.ylabel("Total Sales")
plt.xticks(rotation=0)
plt.legend(title="Product Category")

plt.show()
