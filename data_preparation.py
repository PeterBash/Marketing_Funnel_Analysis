import pandas as pd

# Step 1: Load the datasets
deals_data = pd.read_csv('/Users/peterkihara/Downloads/marketing_funnel_data/olist_closed_deals_dataset.csv')
leads_data = pd.read_csv('/Users/peterkihara/Downloads/marketing_funnel_data/olist_marketing_qualified_leads_dataset.csv')

# Step 2: Data Cleaning
deals_data['won_date'] = pd.to_datetime(deals_data['won_date'], errors='coerce')
leads_data['first_contact_date'] = pd.to_datetime(leads_data['first_contact_date'], errors='coerce')

# Drop columns with high missing values
columns_to_drop = ['has_company', 'has_gtin', 'average_stock', 'declared_product_catalog_size']
deals_data_cleaned = deals_data.drop(columns=columns_to_drop)

# Fill missing values
deals_data_cleaned.fillna({
    'business_segment': 'unknown',
    'lead_type': 'unknown',
    'lead_behaviour_profile': 'unknown',
    'business_type': 'unknown'
}, inplace=True)

leads_data['origin'].fillna('unknown', inplace=True)

# Step 3: Merge Datasets
merged_data = pd.merge(deals_data_cleaned, leads_data, on='mql_id', how='inner')

# Add time-to-close column
merged_data['time_to_close_days'] = (merged_data['won_date'] - merged_data['first_contact_date']).dt.days

# Step 4: Funnel Conversion Metrics
total_leads_by_channel = leads_data.groupby('origin').size()
conversions_by_channel = merged_data.groupby('origin').size()
conversion_rate = (conversions_by_channel / total_leads_by_channel * 100).fillna(0)

# Save conversion data to CSV
conversion_data = pd.DataFrame({
    'Origin': total_leads_by_channel.index,
    'Total Leads': total_leads_by_channel.values,
    'Conversions': conversions_by_channel.values,
    'Conversion Rate (%)': conversion_rate.values
})
conversion_data.to_csv('conversion_data.csv', index=False)

# Step 5: Revenue Trend Over Time
merged_data['won_month'] = merged_data['won_date'].dt.to_period('M')
revenue_trend = merged_data.groupby('won_month')['declared_monthly_revenue'].sum()
revenue_trend.to_csv('revenue_trend.csv', index=True)

# Step 6: Top Business Segments
top_segments = merged_data.groupby('business_segment')['declared_monthly_revenue'].sum().nlargest(10)
top_segments.to_csv('top_business_segments.csv', index=True)

# Step 7: Export Processed Data
merged_data.to_csv('processed_data.csv', index=False)

print("Data processing complete! The following files were generated:")
print("- 'processed_data.csv': Full merged dataset.")
print("- 'conversion_data.csv': Funnel conversion metrics.")
print("- 'revenue_trend.csv': Revenue trends over time.")
print("- 'top_business_segments.csv': Top 10 business segments by revenue.")
