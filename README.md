# Personal Expense Tracker

A comprehensive Python-based application for tracking daily expenses, categorizing them, and generating detailed monthly reports with visual analytics using Matplotlib and Seaborn.

## Features

### Core Functionality
- **Add Expenses**: Record daily expenses with date, amount, category, and description
- **View Expenses**: Display all expenses or filter by month
- **Delete Expenses**: Remove unwanted expense entries
- **Persistent Storage**: All data saved in JSON format for easy access

### Categories
- Food & Dining
- Transportation
- Shopping
- Entertainment
- Bills & Utilities
- Healthcare
- Education
- Others

### Visual Reports
1. **Monthly Report** - Comprehensive dashboard with:
   - Category-wise pie chart showing expense distribution
   - Bar chart for category-wise spending comparison
   - Daily expense trend line graph
   - Summary statistics panel

2. **Category Analysis** - Stacked area chart showing:
   - Monthly trends for each category
   - Overall spending patterns over time

## Installation

### Prerequisites
- Python 3.7 or higher
- pip (Python package manager)

### Install Dependencies

```bash
pip install -r requirements.txt
```

This will install:
- matplotlib (for plotting)
- seaborn (for enhanced visualizations)
- pandas (for data manipulation)

## Usage

### Running the Application

```bash
python expense_tracker.py
```

### Menu Options

1. **Add New Expense**
   - Enter date (or use today's date)
   - Enter amount in Rupees
   - Select category from the list
   - Add description

2. **View All Expenses**
   - Displays complete expense history
   - Shows total spending

3. **View Monthly Expenses**
   - Filter expenses by month (YYYY-MM format)
   - Shows monthly total

4. **Generate Monthly Report (Visual)**
   - Creates comprehensive visual report
   - Saves as PNG file (expense_report_YYYY-MM.png)
   - Displays interactive charts

5. **Generate Category Analysis**
   - Shows spending trends across categories
   - Saves as PNG file (category_analysis.png)

6. **Delete Expense**
   - Remove specific expense entries

7. **Exit**
   - Close the application

### Demo Data

To test the application with sample data:

```bash
python demo_data_generator.py
```

This generates 3 months of realistic expense data.

## File Structure

```
.
├── expense_tracker.py          # Main application
├── demo_data_generator.py      # Sample data generator
├── requirements.txt            # Python dependencies
├── expenses.json              # Data storage (auto-created)
├── expense_report_*.png       # Generated monthly reports
└── category_analysis.png      # Category trend analysis
```

## Data Storage

Expenses are stored in `expenses.json` with the following structure:

```json
[
    {
        "date": "2026-01-27",
        "amount": 450.50,
        "category": "Food & Dining",
        "description": "Grocery shopping"
    }
]
```

## Visual Reports

### Monthly Report Components

1. **Pie Chart**: Shows percentage distribution across categories
2. **Bar Chart**: Compares spending amounts by category
3. **Line Graph**: Displays daily spending trends
4. **Statistics Panel**: Shows:
   - Total expenses
   - Number of transactions
   - Average per transaction
   - Highest and lowest expenses
   - Top spending category

### Category Analysis

- Stacked area chart showing monthly trends
- Color-coded categories for easy identification
- Helps identify spending patterns over time

## Example Workflow

1. Start the application
2. Add daily expenses as they occur
3. At month-end, generate monthly report
4. Review visual analytics to understand spending patterns
5. Use insights to plan budget for next month

## Tips

- Enter expenses daily for accurate tracking
- Use consistent descriptions for similar expenses
- Generate monthly reports regularly
- Review category analysis to identify spending trends
- Keep the application running in background for quick access

## Technical Details

- **Language**: Python 3
- **Data Format**: JSON
- **Visualization**: Matplotlib, Seaborn
- **Data Processing**: Pandas
- **Storage**: File-based (expenses.json)

## Future Enhancements

Potential features for future versions:
- Budget setting and alerts
- Export to PDF/Excel
- Multi-user support
- Cloud synchronization
- Mobile app integration
- Recurring expense tracking
- Income tracking
- Savings goals

## License

This project is created for educational purposes.

## Author

Developed as part of Python programming coursework.
