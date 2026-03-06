# -Blinkit-Sales-Data-Analysis-Portfolio
![IMG-20250531-WA0004(1) jpg](https://github.com/user-attachments/assets/4327ab18-abb2-43c1-ab2d-9b32eb128742)

### 📌 Project Overview

This project analyzes Blinkit’s online grocery sales data to understand product demand, revenue trends, discount impact, and delivery performance using **Python, SQL, and Power BI**.

---

# 📁 Dataset Information

Columns included:

* Order ID
* Product
* Category
* Sales
* Profit
* Discount
* Quantity
* City
* Delivery Time

Time Period: **January – April 2025**

Dataset includes **thousands of grocery transactions**.

---

# 🛠 Tools Used

* Python (Pandas, NumPy)
* SQL
* Power BI
* Excel

---

# 🧹 Data Cleaning (Python)

Steps performed:

• Removed missing Order IDs
• Handled null values in **Sales and Profit**
• Converted **Delivery Time to numeric format**
• Standardized product categories

Example Python code:

```python
import pandas as pd

df = pd.read_csv("blinkit_sales.csv")

df.dropna(subset=['Order ID','Sales','Profit'], inplace=True)

df['Delivery Time'] = pd.to_numeric(df['Delivery Time'])

df.drop_duplicates(inplace=True)
```

---

# 📊 Python Analysis

### Category-wise Revenue

```python
df.groupby('Category')['Sales'].sum().sort_values(ascending=False)
```

### Profit by Product

```python
df.groupby('Product')['Profit'].sum().sort_values(ascending=False)
```

### Orders by City

```python
df['City'].value_counts()
```

### Average Delivery Time

```python
df['Delivery Time'].mean()
```

---

# 🗄 SQL Queries Used

### Total Revenue

```sql
SELECT SUM(Sales) AS Total_Revenue
FROM blinkit_sales;
```

### Revenue by Category

```sql
SELECT Category,
SUM(Sales) AS Revenue
FROM blinkit_sales
GROUP BY Category
ORDER BY Revenue DESC;
```

### Profit by Product

```sql
SELECT Product,
SUM(Profit) AS Profit
FROM blinkit_sales
GROUP BY Product
ORDER BY Profit DESC;
```

### Orders by City

```sql
SELECT City,
COUNT(Order_ID) AS Orders
FROM blinkit_sales
GROUP BY City
ORDER BY Orders DESC;
```

### Discount Impact

```sql
SELECT Discount,
AVG(Profit) AS Avg_Profit
FROM blinkit_sales
GROUP BY Discount
ORDER BY Discount;
```

---

# 📈 Power BI Dashboard
![IMG-20250531-WA0004(1) jpg](https://github.com/user-attachments/assets/a22cd002-5bcf-4a64-b56a-ac34579079cb)


### KPIs

* Total Revenue
* Total Orders
* Total Profit
* Average Delivery Time

---

# 📊 Visualizations Used

• KPI Cards – Revenue, Orders, Profit
• Bar Chart – Revenue by Category
• Bar Chart – Profit by Product
• Column Chart – Orders by City
• Line Chart – Delivery Time Trend
• Pie Chart – Category Sales Share
• Table – Product Performance

---

# 📌 Key Insights

1️⃣ **Dairy & Beverages contribute more than 40% of total revenue.**

2️⃣ **Delhi and Mumbai have the highest order frequency.**

3️⃣ Discounts above **20% reduce profit margins significantly**.

4️⃣ **Fruits & Vegetables have high demand but low margins**.

5️⃣ Average delivery time is **~2.5 hours**, indicating efficient logistics.

---

# 3️⃣ Power BI DAX Measures

### Total Revenue

```DAX
Total Revenue = SUM(Sales[Revenue])
```

### Total Profit

```DAX
Total Profit = SUM(Sales[Profit])
```

### Discount %

```DAX
Discount % =
DIVIDE(SUM(Sales[Discount]), SUM(Sales[Revenue]))
```

### Average Delivery Time

```DAX
Avg Delivery Time =
AVERAGE(Sales[Delivery Time])
```

---

# ⭐ Skills Demonstrated

• Data Cleaning
• Data Analysis
• SQL Querying
• Dashboard Development
• Business Insights
