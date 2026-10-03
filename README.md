# ShopSphere
End-to-end e-commerce analytics project using Python, SQL, SQLite, and Power BI to explore customer behavior, sales performance, traffic acquisition, and purchase funnel conversion using synthetic data.

# 🛒 ShopSphere – E-commerce Customer Behavior & Purchase Funnel Analysis

## 📌 Project Overview

ShopSphere is an end-to-end data analytics project that explores e-commerce sales performance, customer behavior, traffic acquisition, and purchase funnel conversion.

The project uses **Python, SQL, SQLite, and Power BI** to clean and analyze synthetic e-commerce data, identify purchasing patterns, and build an interactive dashboard that presents meaningful business insights.

The dashboard is designed to help businesses understand customer engagement, monitor sales performance, analyze traffic sources, and identify opportunities to improve the purchase journey.

> **Note:** This project uses synthetically generated data for learning and portfolio demonstration. The findings represent simulated business scenarios and are not based on a real company's transactions.

---

## 🎯 Project Objectives

* Analyze e-commerce sales and customer purchasing behavior.
* Understand website traffic across different acquisition channels and devices.
* Evaluate the purchase funnel from product views to completed purchases.
* Identify conversion patterns and potential areas of customer drop-off.
* Develop an interactive Power BI dashboard for business reporting.
* Demonstrate practical skills in data cleaning, SQL querying, exploratory data analysis, and data visualization.

---

## 🛠️ Tools & Technologies

| Tool / Technology    | Purpose                                                  |
| -------------------- | -------------------------------------------------------- |
| Python               | Data generation, cleaning, and exploratory data analysis |
| Pandas & NumPy       | Data manipulation and analysis                           |
| SQLite               | Relational database storage and SQL analysis             |
| SQL                  | Data extraction, aggregation, and business analysis      |
| Power BI             | Interactive dashboard development                        |
| Power Query          | Data transformation and preparation                      |
| DAX                  | Measures, KPIs, and analytical calculations              |
| Matplotlib & Seaborn | Exploratory data visualizations                          |
| VS Code              | Development environment                                  |
| Git & GitHub         | Version control and project documentation                |

---

## 📊 Dataset Overview

The project uses a synthetic e-commerce dataset covering **January to March 2026**.

| Dataset     | Records | Description                                                   |
| ----------- | ------: | ------------------------------------------------------------- |
| Customers   |   1,000 | Customer identifiers, signup dates, and customer types        |
| Products    |     100 | Product details, categories, and prices                       |
| Sessions    |   2,500 | Website sessions, devices, traffic sources, and visitors      |
| Events      |   9,310 | Product views, cart additions, checkout events, and purchases |
| Orders      |     303 | Order details, dates, and statuses                            |
| Order Items |     418 | Products, quantities, and unit prices within orders           |

Anonymous sessions are retained in the dataset, with missing customer IDs representing visitors who were not identified.

---

## 🔄 Project Workflow

1. **Data Generation:** Created synthetic e-commerce data representing customers, products, sessions, events, orders, and order items.
2. **Database Creation:** Stored the datasets in a relational SQLite database.
3. **Data Exploration:** Used Python and Pandas to inspect data structures, record counts, missing values, duplicates, and distributions.
4. **SQL Analysis:** Queried the database to analyze sales, traffic sources, devices, product categories, and purchase funnel performance.
5. **Data Preparation:** Cleaned and transformed data for reporting and visualization.
6. **Power BI Modeling:** Loaded the prepared data and established relationships between relevant tables.
7. **DAX Development:** Created measures for revenue, purchasing customers, conversion rates, and other key performance indicators.
8. **Dashboard Development:** Built a three-page interactive Power BI report with slicers, KPI cards, charts, and detailed tables.
9. **Validation:** Tested the dashboard's filters, measures, and visual interactions.

---

## 📈 Power BI Dashboard

The dashboard contains three interactive report pages.

### 1. Performance Overview

Provides a consolidated view of overall e-commerce performance.

**Key components:**

* Total sessions, orders, revenue, and session conversion rate
* Purchase funnel visualization
* Monthly revenue trend
* Revenue by product category
* Interactive slicers for device, traffic source, and product category

### 2. Traffic & Acquisition

Analyzes website traffic and purchase activity across acquisition channels and devices.

**Key components:**

* Session and purchase metrics
* Traffic-source performance and conversion rates
* Device-wise session and purchase analysis
* Traffic acquisition detail table
* Interactive filtering for deeper analysis

### 3. Customer Analysis

Explores customer distribution and purchasing metrics.

**Key components:**

* Total customers and purchasing customers
* Customer purchase rate
* Revenue per purchasing customer
* New versus Returning customer analysis
* Customer-type revenue comparison
* Interactive customer-type filtering

---

## 🔍 Key Insights

The following findings were obtained from the synthetic dataset:

| Metric                          |       Result |
| ------------------------------- | -----------: |
| Total Customers                 |        1,000 |
| Total Products                  |          100 |
| Total Sessions                  |        2,500 |
| Total Events                    |        9,310 |
| Total Orders                    |          303 |
| Total Revenue                   | 5,424,077.73 |
| Average Order Value             |    17,901.25 |
| Session-to-Purchase Conversion  |       12.12% |
| View-to-Cart Conversion         |       39.12% |
| Cart-to-Checkout Conversion     |       61.35% |
| Checkout-to-Purchase Conversion |       50.50% |

*Revenue is reported in the dataset's price units because no real-world currency was specified.*

### Traffic Source Analysis

* **Organic Search** generated the highest session volume, with 807 sessions, and the highest purchase-session volume, with 97.
* **Direct** traffic had the highest observed conversion rate at 14.18%.
* **Email** had the lowest observed conversion rate at 7.08%.

### Device Analysis

* Mobile generated the largest number of sessions, with 1,672, and 207 purchase sessions.
* Desktop recorded 726 sessions and 88 purchase sessions.
* Tablet recorded 102 sessions and 8 purchase sessions. The smaller tablet sample should be considered when interpreting its conversion rate.

### Product Category Analysis

* Electronics generated the highest category revenue in the simulated dataset.
* Home Appliances ranked second in category revenue.
* Clothing had the highest category order-occurrence count.

*Category order occurrences can exceed the number of unique orders because an order may contain products from multiple categories.*

---

## 💡 Business Recommendations

Based on the simulated results, the dashboard demonstrates how an e-commerce business could:

* Investigate the customer journey to identify where visitors leave the purchase funnel.
* Review the acquisition channels generating the most traffic and purchases.
* Examine conversion differences across devices to identify potential user-experience improvements.
* Monitor category-level revenue to support product and merchandising analysis.
* Use customer and purchasing metrics to guide further segmentation and reporting.

These are analytical opportunities suggested by the simulated data, not verified outcomes from a real business.

---

## 📁 Project Structure

```text
ShopSphere-Ecommerce-Analysis/
│
├── data/
│   ├── processed/
│   │   └──               # Cleaned datasets and analysis outputs
│   └── shopsphere.db     # SQLite database (if included)
│
├── src/
│   ├── database.py       # Database creation and setup
│   ├── generate_data.py  # Synthetic data generation
│   └── eda.py            # Exploratory data analysis
│
├── sql/
│   └──                  # SQL queries for business analysis
│
├── reports/
│   └── sql_findings.md  # SQL analysis findings
│
├── dashboard/
│   ├── ShopSphere.pbix  # Power BI dashboard
│   └── screenshots/     # Dashboard screenshots
│
├── README.md
└── .gitignore
```

*Adjust the structure to match the files and folders actually included in your repository.*

---

## 🚀 How to Run the Project

### Prerequisites

Install Python and the required libraries:

```bash
pip install pandas numpy matplotlib seaborn
```

SQLite is used for database storage. Power BI Desktop is required to open and explore the `.pbix` dashboard.

### Steps

1. Clone the repository:

```bash
git clone https://github.com/YOUR-USERNAME/ShopSphere<img width="670" height="378" alt="performance overview" src="https://github.com/user-attachments/assets/be372303-35b2-4560-b407-8cf66c887c22" />
.git
```

2. Navigate to the project directory:

```bash
cd ShopSphere-Ecommerce-Analysis
```

3. Generate the synthetic data:

```bash
python src/generate_data.py
```

4. Create or initialize the database, following the setup in `src/database.py`:

```bash
python src/database.py
```

5. Run the exploratory data analysis:

```bash
python src/eda.py
```

6. Open the Power BI file in Power BI Desktop:

```text
dashboard/ShopSphere.pbix
```

*Run the scripts in the order required by their actual implementation. If the database script is responsible for both generating and loading data, follow its documented setup instead.*

---

## 📷 Dashboard Screenshots

Add screenshots of the three Power BI report pages here.

### Performance Overview

![Performance Overview](main/performance_overview.png)

### Traffic & Acquisition

![Traffic and Acquisition](main/traffic_and_acq.png)

### Customer Analysis

![Customer Analysis](main/customer_analysis.png)

*Replace the image paths with your actual screenshot filenames. GitHub will display the images once they are uploaded to the repository.*

---

## 📚 Skills Demonstrated

* Data cleaning and preprocessing
* Exploratory data analysis (EDA)
* SQL querying and relational databases
* Data modeling and relationships
* Power Query transformations
* DAX measures and KPI development
* Interactive dashboard design
* Business and customer behavior analysis
* Data storytelling and reporting
* Git and GitHub project documentation

---

## ⚠️ Limitations

* The dataset is synthetic and does not represent actual customer transactions.
* Customer types were randomly assigned during data generation and should not be treated as verified purchase-history-based segments.
* The analysis covers only the simulated January–March 2026 period.
* Revenue and conversion patterns are illustrative and should not be generalized to real e-commerce businesses.
* The dataset does not include marketing spend, profit margins, or verified campaign attribution, so profitability and return-on-ad-spend conclusions cannot be drawn.

---

## 👩‍💻 Author

**Vaishnavi Mahesh Morti**

BE in Computer Science & Engineering

**Areas of Interest:** Data Analytics | Business Intelligence | Power BI | SQL | Python

**LinkedIn:** [Add your LinkedIn profile URL]

**GitHub:** [Add your GitHub profile URL]

---

## ⭐ Acknowledgement

This project was developed as a hands-on portfolio project to practice data analytics, SQL, Python, and Power BI skills through a simulated e-commerce business scenario.

If you find this project useful, feel free to explore the repository and share feedback.
