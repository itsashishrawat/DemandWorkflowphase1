# 📦 Demand Tracker

A simple Python script to log and track material demands using Excel files.  
It checks your past purchases, retrieves the latest details if available, and appends new requests to a demand tracker file.

---

## ✨ Features
- Reads **past purchase history** from `past_purchases.xlsx`
- Accepts **item name** and **required quantity** from the user
- Retrieves **latest purchase price, date, vendor, and category** if available
- Appends the entry to `demand_tracker.xlsx` (or creates one if missing)
- Formats dates automatically
- Leaves placeholders for future procurement milestones

---

## 🗂 File Requirements
1. **past_purchases.xlsx**  
   Must contain at least these columns:
   - Item Name
   - Last Price
   - Last Purchase Date
   - Vendor
   - Category

2. **demand_tracker.xlsx** (created automatically if missing)  
   Stores all demand entries with columns for procurement process stages.

---

## 📥 Installation
```bash
# Clone this repository
git clone https://github.com/YourUsername/demand-tracker.git
cd demand-tracker



# Install required Python packages
pip install pandas openpyxl


## Program Flow
flowchart TD
    A[Start] --> B[Load past purchases]
    B --> C[Get item details from user]
    C --> D{Match found?}
    D -->|Yes| E[Get latest purchase details]
    D -->|No| F[Set details to N/A]
    E --> G[Prepare new entry]
    F --> G[Prepare new entry]
    G --> H[Save to tracker Excel]
    H --> I[End]
