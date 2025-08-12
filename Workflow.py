import pandas as pd
from datetime import datetime
import os

# File names
past_file = "past_purchases.xlsx"
tracker_file = "demand_tracker.xlsx"

# Load past purchases
if os.path.exists(past_file):
    past_df = pd.read_excel(past_file)

    # Ensure date column is in datetime format
    if 'Last Purchase Date' in past_df.columns:
        past_df['Last Purchase Date'] = pd.to_datetime(past_df['Last Purchase Date'], errors='coerce')
else:
    print(f"Error: {past_file} not found!")
    exit()

# Ask user for item details
item_name = input("Enter Item Name: ").strip()
required_qty = input("Enter Required Quantity: ").strip()
demand_date = datetime.today().strftime("%Y-%m-%d")

# Search in past purchases (case-insensitive)
match = past_df[past_df['Item Name'].str.lower() == item_name.lower()]

if not match.empty:
    # Get latest purchase
    latest = match.sort_values(by='Last Purchase Date', ascending=False).iloc[0]

    last_price = latest['Last Price']
    last_date = latest['Last Purchase Date'].strftime("%Y-%m-%d") if pd.notnull(latest['Last Purchase Date']) else "N/A"
    vendor = latest['Vendor']
    category = latest['Category']

    print("\n Past Purchase Details Found (Latest):")
    print(f"  Last Price: {last_price}")
    print(f"  Last Purchase Date: {last_date}")
    print(f"  Vendor: {vendor}")
    print(f"  Category: {category}")
else:
    last_price, last_date, vendor, category = ("N/A", "N/A", "N/A", "N/A")
    print("\n No past purchase record found.")

# Prepare new entry
new_entry = {
    "Item Name": item_name,
    "Required Quantity": required_qty,
    "Demand Date": demand_date,
    "Last Price": last_price,
    "Last Purchase Date": last_date,
    "Vendor": vendor,
    "Category": category,
    "Cart Given Date": "",
    "Proposal Concurred Date": "",
    "Order Date": "",
    "Delivery Date": "",
    "Billing Date": ""
}

# Save to tracker Excel
if os.path.exists(tracker_file):
    tracker_df = pd.read_excel(tracker_file)

    # Make sure new_entry is a DataFrame and align columns
    new_entry_df = pd.DataFrame([new_entry], columns=tracker_df.columns)

    tracker_df = pd.concat([tracker_df, new_entry_df], ignore_index=True)
else:
    tracker_df = pd.DataFrame([new_entry])

tracker_df.to_excel(tracker_file, index=False)
print("\n✅ Demand saved to tracker!")
