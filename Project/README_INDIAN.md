# Personal Expense Tracker - Indian Edition 🇮🇳

A Python-based application designed for Indian users to track daily expenses in **Indian Rupees (₹)**, categorize them with Indian expense categories, and generate monthly reports with beautiful visualizations using Matplotlib and Seaborn.

## Features

- **Add Expenses**: Record expenses with amount (₹), category, description, and date
- **View Expenses**: Display all expenses or filter by month and year
- **Indian Categories**: Organized for Indian lifestyle (Rent, Food & Groceries, Mobile & Internet, etc.)
- **Monthly Reports**: Generate comprehensive reports with statistics and breakdowns
- **Visual Analytics**:
  - Pie charts showing expense distribution by category
  - Bar charts showing monthly spending trends
  - Horizontal bar charts comparing category expenses
- **Data Persistence**: Expenses are saved to JSON file for easy access

## Indian Expense Categories

- **Food & Groceries** - Kirana store, BigBasket, Swiggy, Zomato, restaurant meals
- **Transportation** - Petrol/Diesel, Ola/Uber, Metro, Auto rickshaw, Bus pass
- **Entertainment** - Movies (PVR/INOX), Netflix, Amazon Prime, Cricket matches
- **Utilities & Bills** - Electricity, Water, Gas cylinder, Society maintenance
- **Healthcare** - Doctor visits, Pharmacy, Gym, Insurance premium
- **Shopping & Clothing** - Myntra, Flipkart, Mall shopping, Festival shopping
- **Education** - School fees, Tuition, Online courses, Books
- **Rent** - House rent, PG accommodation
- **Mobile & Internet** - Mobile recharge, Postpaid bill, Broadband
- **Personal Care** - Salon, Barber, Cosmetics, Spa
- **Other** - Pet care, Donations, Temple offerings, Miscellaneous

## Installation

### Requirements
- Python 3.7 or higher
- Windows / Mac / Linux

### Step 1: Install Python Libraries

Open terminal/command prompt and run:
```bash
pip install matplotlib seaborn
```

Or use the requirements file:
```bash
pip install -r requirements.txt
```

## Usage

### Method 1: Interactive Mode (Recommended for Beginners)

Run the main application:
```bash
python expense_tracker.py
```

**Menu Options:**
1. Add Expense - Input your daily expenses
2. View All Expenses - See complete expense history
3. View Monthly Expenses - Filter by specific month
4. Generate Monthly Report - Get detailed analysis with charts
5. Generate Monthly Bar Chart - Year-long spending overview
6. Generate Category Pie Chart - Visual breakdown by category
7. **Clear All Data** - Delete all expenses (with safety confirmation) ⚠️
8. Exit - Close the application

### Method 2: Demo Mode (See Sample Indian Data)

Run the demo with pre-filled Indian expense data:
```bash
python demo_tracker.py
```

## Example Indian Expenses

Here are typical Indian expenses you might track:

| Amount | Category | Description |
|--------|----------|-------------|
| ₹1,500 | Food & Groceries | BigBasket order |
| ₹250 | Transportation | Ola ride to office |
| ₹15,000 | Rent | Monthly house rent |
| ₹2,500 | Utilities & Bills | Electricity bill |
| ₹350 | Mobile & Internet | Jio postpaid bill |
| ₹450 | Entertainment | Movie tickets at PVR |
| ₹1,200 | Shopping & Clothing | Myntra shopping |

## How to Run in VS Code

1. **Open VS Code** and open the project folder
2. **Open Terminal** (Ctrl + `)
3. **Install libraries**: `pip install matplotlib seaborn`
4. **Run the app**: `python expense_tracker.py`
5. Follow the on-screen menu and enter your expenses

## Sample Output

```
======================================================================
Date         Category        Amount     Description                   
======================================================================
2026-01-05   Food & Groceries ₹1500.00   BigBasket grocery order       
2026-01-06   Transportation  ₹250.00    Ola ride to office            
2026-01-11   Rent            ₹15000.00  Monthly house rent            
======================================================================
Total:                      ₹32050.00
======================================================================

MONTHLY EXPENSE REPORT - 1/2026
Total Expenses: ₹32,050.00
Number of Transactions: 20
Average Transaction: ₹1,602.50

Expenses by Category:
Rent                 ₹15,000.00 (46.8%)
Utilities & Bills    ₹ 5,500.00 (17.2%)
Food & Groceries     ₹ 4,500.00 (14.0%)
```

## Visualizations Generated

The application creates beautiful charts:
- **expense_pie_chart.png** - Colorful pie chart showing category distribution
- **category_bar_chart.png** - Horizontal bar chart comparing categories
- **monthly_expenses_bar_chart.png** - 12-month spending overview

All charts are in high-resolution (300 DPI) suitable for printing or sharing.

## File Structure

```
expense_tracker.py       # Main application
demo_tracker.py          # Demo with Indian sample data
requirements.txt         # Python dependencies
indian_expenses.json     # Your expense data (auto-created)
*.png                    # Generated charts
```

## Quick Start Example

```python
from expense_tracker import ExpenseTracker

# Create tracker
tracker = ExpenseTracker()

# Add expense
tracker.add_expense(
    amount=500,
    category='Food & Groceries',
    description='Swiggy dinner order',
    date='2026-01-27'
)

# View expenses
tracker.view_expenses(1, 2026)

# Generate report
tracker.generate_monthly_report(1, 2026)
```

## Tips for Indian Users

- **Track Daily**: Add expenses daily for accurate records
- **Rent Day**: Add your rent on the 1st of each month
- **Bill Payments**: Log all utility bills when paid
- **Food Delivery**: Track Swiggy/Zomato orders separately
- **Transportation**: Include petrol, metro, and ride-sharing apps
- **Monthly Review**: Generate reports to understand spending patterns
- **Festival Season**: Use "Shopping & Clothing" for festival expenses
- **Healthcare**: Track insurance premiums and medical expenses

## Clear All Data Feature ⚠️

The application includes a **Clear All Data** option with built-in safety features:

### How It Works
1. Select option **7** from the main menu
2. Review the warning showing:
   - Total number of expense entries
   - Total amount (₹) that will be deleted
3. Type **`DELETE ALL`** (exactly) to confirm
4. Type anything else to cancel

### Safety Features
✓ Shows detailed information before deletion  
✓ Requires exact confirmation text: `DELETE ALL`  
✓ Any other input cancels the operation  
✓ Clear warning that action cannot be undone  
✓ Empty trackers show appropriate message

### When to Use
- Starting a new financial year
- Testing with dummy data
- Switching tracking systems
- Starting fresh after major life changes

**⚠️ Warning**: This permanently deletes ALL your expense data. Always create a backup if needed!

## Common Indian Expense Ranges

| Category | Typical Monthly Range |
|----------|----------------------|
| Rent (Metro cities) | ₹10,000 - ₹30,000 |
| Food & Groceries | ₹3,000 - ₹8,000 |
| Transportation | ₹1,000 - ₹5,000 |
| Utilities & Bills | ₹2,000 - ₹6,000 |
| Mobile & Internet | ₹500 - ₹1,500 |
| Entertainment | ₹1,000 - ₹3,000 |

## Troubleshooting

**Issue**: Charts not displaying  
**Solution**: Make sure matplotlib is installed: `pip install matplotlib`

**Issue**: Can't enter ₹ symbol  
**Solution**: Just type the number, the app adds ₹ automatically

**Issue**: Wrong date format  
**Solution**: Use YYYY-MM-DD format (e.g., 2026-01-27)

## Future Enhancements

- Budget alerts when spending exceeds limits
- WhatsApp integration for expense notifications
- UPI payment tracking integration
- GST calculation for business expenses
- Multiple currency support
- Mobile app for Android/iOS

## Support

For issues or suggestions, feel free to modify the code or reach out!

## License

Free to use for personal and educational purposes.

---

**Made in India 🇮🇳 | Track Smart, Save More! 💰**
