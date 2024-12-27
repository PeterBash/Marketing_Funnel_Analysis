# Marketing Dashboard and Data Analysis

This repository contains Python scripts and a Tableau dashboard for analyzing marketing funnel performance, revenue trends, and time-to-close insights. The project demonstrates the use of Python for data preparation and Tableau for data visualization.

---

## Project Structure

### Folders and Files
- **scripts/**: Contains the Python scripts for data processing.
  - `data_processing.py`: Processes and cleans the input data, then exports it as CSV files for Tableau.
- **data/**: Contains the datasets used in the project.
  - `processed_data.csv`: Final dataset imported into Tableau.
  - `conversion_data.csv`: Funnel conversion metrics (leads, conversions, and rates by channel).
  - `revenue_trend.csv`: Revenue trends grouped by month.
  - `top_business_segments.csv`: Revenue breakdown for the top 10 business segments.
- **dashboard/**: Contains the Tableau workbook.
  - `marketing_dashboard.twbx`: Tableau Packaged Workbook showcasing insights.

---

## Features of the Dashboard

1. **Marketing Funnel Analysis**:
   - Visualizes total leads, conversions, and conversion rates by marketing channel.
2. **Revenue Insights**:
   - Highlights top revenue-generating business segments.
   - Shows revenue trends over time.
3. **Time-to-Close Analysis**:
   - Displays the distribution of time it takes to close deals.
   - Analyzes average time-to-close trends monthly.
4. **Key KPIs**:
   - Total Revenue
   - Average Time to Close
   - Top Channel (by revenue)

---

## How to Use

### 1. **Set Up Python Environment**
1. Clone the repository:
   ```bash
   git clone https://github.com/PeterBash/marketing_Funnel_Analysis.git
   cd marketing-dashboard
