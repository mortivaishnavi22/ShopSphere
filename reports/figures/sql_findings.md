
# ShopSphere E-commerce Business Analysis
## SQL Analysis Report

**Project:** ShopSphere – E-commerce Customer Behavior & Purchase Funnel Analysis  
**Tools:** SQL, SQLite, Python, Pandas  
**Dataset:** Synthetic e-commerce data  
**Analysis Period:** January – March 2026

---

## 1. Project Overview

ShopSphere is a fictional e-commerce company experiencing potential customer drop-offs during the online shopping journey.

The objective of this analysis is to understand customer behavior, evaluate the conversion funnel, compare traffic-source and device performance, and identify revenue trends and product-category contributions.

SQL was used to analyze customer sessions, website events, orders, and order items.

## 2. Dataset Overview

| Dataset | Records |
|---|---:|
| Customers | 1,000 |
| Products | 100 |
| Sessions | 2,500 |
| Events | 9,310 |
| Orders | 303 |
| Order Items | 418 |

The dataset contains six relational tables: customers, products, sessions, events, orders, and order_items.

## 3. Data Quality Assessment

Python and Pandas were used to inspect the dataset before SQL analysis.

| Table | Rows | Duplicate Rows | Missing Values |
|---|---:|---:|---|
| Customers | 1,000 | 0 | None |
| Products | 100 | 0 | None |
| Sessions | 2,500 | 0 | 529 customer IDs |
| Events | 9,310 | 0 | None |
| Orders | 303 | 0 | None |
| Order Items | 418 | 0 | None |

**Data quality observations:**

- No duplicate rows were detected in the six tables.
- No missing values were detected in the events, products, orders, or order_items tables.
- The sessions table contains 529 missing customer IDs, representing anonymous sessions in the synthetic dataset.
- Date columns were converted to datetime format for analysis.
- Text values were standardized, and processed CSV files were saved.

Anonymous sessions were retained because they are relevant to understanding visitor behavior.

## 4. Conversion Funnel Analysis

The conversion funnel measures how many distinct sessions reached each shopping stage.

### Funnel Results

| Funnel Stage | Unique Sessions | Conversion from Previous Stage |
|---|---:|---:|
| Product View | 2,500 | 100% |
| Add to Cart | 978 | 39.12% |
| Begin Checkout | 600 | 61.35% |
| Purchase | 303 | 50.50% |

**Overall session conversion rate:** 12.12%

### Key Findings

- All 2,500 sessions recorded a product-view event.
- 978 sessions included an add-to-cart event.
- 600 sessions reached the checkout stage.
- 303 sessions recorded a purchase.
- The largest proportional drop-off occurs between product viewing and adding to cart.

### Business Insight

The product-view-to-cart transition represents a major opportunity for further investigation. Product presentation, pricing, product information, and customer experience could be examined to understand why visitors do not add products to their carts.

The checkout-to-purchase transition also warrants investigation, as approximately half of checkout sessions did not record a purchase.

*Note: These are stage-level session ratios. Event ordering and funnel nesting should be validated before treating them as a strictly sequential customer funnel.*

## 5. Traffic Source Analysis

Traffic-source performance was evaluated using total sessions, purchase sessions, and session conversion rate.

### Results

| Traffic Source | Total Sessions | Purchase Sessions | Conversion Rate |
|---|---:|---:|---:|
| Direct | 395 | 56 | 14.18% |
| Paid Search | 500 | 68 | 13.60% |
| Social | 440 | 53 | 12.05% |
| Organic Search | 807 | 97 | 12.02% |
| Referral | 132 | 13 | 9.85% |
| Email | 226 | 16 | 7.08% |
| **Total** | **2,500** | **303** | **12.12%** |

### Key Findings

- **Highest conversion rate:** Direct, at 14.18%.
- **Highest traffic volume:** Organic Search, with 807 sessions.
- **Most purchase sessions:** Organic Search, with 97 purchases.
- **Lowest conversion rate:** Email, at 7.08%.
- Paid Search achieved a 13.60% conversion rate across 500 sessions.

### Business Insight

Direct traffic had the highest observed conversion rate, while Organic Search contributed the largest number of sessions and purchases.

Paid Search also showed a relatively high conversion rate. Email and Referral had lower observed conversion rates and could be investigated further.

Conversion rate alone does not establish marketing profitability. Campaign costs, order values, attribution, and customer lifetime value would be needed to evaluate channel effectiveness.

## 6. Device Performance Analysis

Device performance was compared to understand differences in visitor volume and purchasing behavior.

### Results

| Device | Total Sessions | Purchase Sessions | Conversion Rate |
|---|---:|---:|---:|
| Mobile | 1,672 | 207 | 12.38% |
| Desktop | 726 | 88 | 12.12% |
| Tablet | 102 | 8 | 7.84% |
| **Total** | **2,500** | **303** | **12.12%** |

### Key Findings

- **Most-used device:** Mobile, with 1,672 sessions.
- **Highest conversion rate:** Mobile, at 12.38%.
- Desktop had a conversion rate of 12.12%.
- Tablet had the lowest observed conversion rate, at 7.84%.

### Business Insight

Mobile accounts for the majority of sessions and purchase sessions. Its conversion rate is slightly higher than Desktop's.

Tablet has a lower observed conversion rate, but its sample size is relatively small at 102 sessions. Further data would be useful before drawing firm conclusions about tablet performance.

The business could investigate device-specific user experience, including page loading, navigation, product display, and checkout usability.

## 7. Revenue and Average Order Value Analysis

Revenue was calculated from completed orders and their associated order items.

### Results

| Metric | Result |
|---|---:|
| Completed Orders | 303 |
| Total Revenue | 5,424,077.73 |
| Average Order Value | 17,901.25 |

### Key Findings

- The dataset contains 303 completed orders.
- Total revenue from completed order items is 5,424,077.73.
- Average order value is 17,901.25.

### Business Insight

The average order value provides a baseline for evaluating customer spending. Further analysis could compare order values across traffic sources, customer groups, devices, and product categories.

The currency is not specified in the dataset, so these figures are reported in the dataset's price units.

## 8. Product Category Revenue Analysis

Product categories were compared using order counts, units sold, and revenue.

### Results

| Category | Orders | Units Sold | Revenue |
|---|---:|---:|---:|
| Electronics | 73 | 91 | 2,739,312.16 |
| Home Appliances | 79 | 100 | 1,719,040.40 |
| Sports | 74 | 92 | 534,426.61 |
| Clothing | 89 | 107 | 295,531.97 |
| Beauty | 82 | 98 | 135,766.59 |
| **Total** | **397** | **488** | **5,424,077.73** |

### Key Findings

- **Highest revenue category:** Electronics, contributing 2,739,312.16.
- **Second-highest revenue category:** Home Appliances, contributing 1,719,040.40.
- **Highest units sold:** Clothing, with 107 units.
- **Highest order count:** Clothing, with 89 orders.
- Beauty generated the lowest revenue, at 135,766.59.

### Business Insight

Electronics generated the largest share of revenue despite having fewer orders and units sold than some other categories. This suggests a higher average selling price for its products in this dataset.

Clothing had the highest order count and units sold but generated substantially less revenue than Electronics and Home Appliances.

These results indicate that revenue contribution and sales volume provide different views of category performance. Further analysis of margins, discounts, returns, and inventory would help inform merchandising decisions.

## 9. Overall Business Insights

1. **Conversion funnel:** The largest proportional loss occurs between product viewing and adding to cart. Product discovery and product-page experience warrant further investigation.

2. **Traffic sources:** Direct has the highest observed conversion rate, while Organic Search generates the most traffic and purchases.

3. **Device performance:** Mobile drives the largest share of sessions and purchases. Tablet has a lower observed conversion rate, but the sample is smaller.

4. **Revenue contribution:** Electronics and Home Appliances contribute the majority of revenue in the synthetic dataset.

5. **Sales volume:** Clothing records the highest number of orders and units sold, despite having a relatively low revenue contribution.

## 10. Business Recommendations

### 1. Improve Product Discovery and Add-to-Cart Engagement

Investigate product-page performance, product descriptions, pricing presentation, product images, and navigation. Test changes and compare add-to-cart rates across sessions.

### 2. Evaluate Marketing Channels Beyond Conversion Rate

Compare revenue, average order value, acquisition costs, and repeat-purchase behavior by traffic source. Use these metrics alongside conversion rates when evaluating channel performance.

### 3. Investigate Device-Specific Shopping Experiences

Review mobile, desktop, and tablet browsing and checkout journeys. Examine page speed, layout, navigation, and payment experience, while collecting more tablet-session data.

### 4. Review Category-Level Merchandising

Examine pricing, margins, inventory, and customer demand for Electronics and Home Appliances, which contribute the most revenue. Explore cross-selling opportunities between higher-revenue and higher-volume categories.

### 5. Investigate Checkout Drop-Off

Analyze checkout events and purchase outcomes to identify potential friction points. Examine checkout steps, payment methods, delivery costs, and errors if those data become available.

## 11. Conclusion

The SQL analysis of ShopSphere's synthetic e-commerce dataset examined the conversion funnel, traffic-source performance, device usage, revenue, and product-category performance.

The analysis identified a substantial drop between product viewing and adding to cart, differences in observed conversion rates across traffic sources and devices, and a concentration of revenue in Electronics and Home Appliances.

These findings provide a foundation for further analysis and dashboard development. The results are based on simulated data and should be treated as learning examples rather than evidence about an actual business.

## 12. Tools and Technologies

- **SQL:** Data querying, aggregation, joins, and KPI calculations.
- **SQLite:** Relational database management.
- **Python:** Data generation, cleaning, and exploratory analysis.
- **Pandas and NumPy:** Data processing and validation.
- **Power BI:** Planned interactive reporting and visualization.

## 13. Project Limitations

- The dataset is synthetic and does not represent real customer behavior.
- Customer types were assigned during data generation and are not independently verified purchase-history classifications.
- The funnel ratios are based on distinct sessions per event type; strict event sequence and stage nesting require additional validation.
- Marketing costs, profit margins, discounts, refunds, and customer lifetime value are not included.
- The dataset's currency is unspecified.

These limitations should be considered when interpreting the findings and formulating business recommendations.