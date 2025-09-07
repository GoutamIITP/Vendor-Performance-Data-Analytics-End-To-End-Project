# Power BI Data Dictionary - Vendor Performance Analysis

## 📊 Data Source
- **File**: `final_table_for_powerbi.csv`
- **Location**: `E:\Data analytics\Vendor-Performance-Data-Analytics-End-To-End-Project\final_table_for_powerbi.csv`
- **Records**: 10,692 rows
- **File Size**: 1.84 MB

## 📋 Column Descriptions

| Column Name | Data Type | Description | Business Meaning |
|-------------|-----------|-------------|------------------|
| **VendorNumber** | Integer | Unique vendor identifier | Primary key for vendor identification |
| **VendorName** | Text | Name of the vendor/company | Business partner name |
| **Brand** | Integer | Unique brand identifier | Product brand code |
| **Description** | Text | Product description | Product name/details |
| **PurchasePrice** | Decimal | Price paid per unit | Cost per unit purchased |
| **ActualPrice** | Decimal | Standard retail price | Market price for the product |
| **Volume** | Decimal | Product volume (ml) | Physical size of the product |
| **TotalPurchaseQuantity** | Integer | Total units purchased | Sum of all purchases |
| **TotalPurchaseDollars** | Decimal | Total purchase value ($) | Total amount spent on purchases |
| **TotalSalesQuantity** | Integer | Total units sold | Sum of all sales |
| **TotalSalesDollars** | Decimal | Total sales revenue ($) | Total revenue generated |
| **TotalSalesPrice** | Decimal | Total sales price ($) | Sum of individual sale prices |
| **TotalExciseTax** | Decimal | Total excise tax ($) | Tax amount collected |
| **FreightCost** | Decimal | Shipping/freight cost ($) | Logistics cost per vendor |
| **GrossProffit** | Decimal | Gross profit ($) | Sales - Purchase costs |
| **SalesToPurchaseRatio** | Decimal | Sales efficiency ratio | Sales $ / Purchase $ |
| **ProfitMargin** | Decimal | Profit margin (%) | (Gross Profit / Sales) × 100 |

## 🎯 Key Metrics for Power BI Analysis

### **Financial Performance**
- **Gross Profit**: `TotalSalesDollars - TotalPurchaseDollars`
- **Profit Margin**: `(GrossProffit / TotalSalesDollars) * 100`
- **Sales Efficiency**: `SalesToPurchaseRatio`

### **Volume Analysis**
- **Purchase Volume**: `TotalPurchaseQuantity`
- **Sales Volume**: `TotalSalesQuantity`
- **Product Volume**: `Volume` (ml)

### **Cost Analysis**
- **Purchase Cost**: `TotalPurchaseDollars`
- **Freight Cost**: `FreightCost`
- **Excise Tax**: `TotalExciseTax`

## 📈 Recommended Power BI Visualizations

### **1. Vendor Performance Dashboard**
- Top vendors by sales volume
- Profit margin by vendor
- Sales vs Purchase ratio

### **2. Product Analysis**
- Best performing brands
- Volume vs Profit analysis
- Price comparison (Purchase vs Actual)

### **3. Financial Metrics**
- Gross profit trends
- Profit margin distribution
- Cost breakdown (Purchase + Freight + Tax)

### **4. Operational Insights**
- Sales efficiency ratios
- Vendor performance comparison
- Product profitability analysis

## 🔧 Power BI Import Instructions

1. **Open Power BI Desktop**
2. **Get Data** → **Text/CSV**
3. **Browse** to: `E:\Data analytics\Vendor-Performance-Data-Analytics-End-To-End-Project\final_table_for_powerbi.csv`
4. **Load** the data
5. **Create relationships** if needed
6. **Build your dashboard** using the metrics above

## 📊 Sample Data Preview
The dataset contains 10,692 records with vendor performance data including:
- 17 different columns
- Financial metrics (sales, purchases, profits)
- Operational data (quantities, volumes)
- Performance ratios (margins, efficiency)

## 🎯 Business Questions to Answer
1. Which vendors provide the best profit margins?
2. What products have the highest sales efficiency?
3. How do freight costs impact overall profitability?
4. Which brands should be promoted or discontinued?
5. What's the optimal pricing strategy based on actual vs purchase prices?
