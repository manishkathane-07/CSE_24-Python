"""
Test script to demonstrate report generation
Automatically generates reports without user interaction
"""

import json
from datetime import datetime
from collections import defaultdict

def generate_automated_report():
    """Generate report automatically for current month"""
    
    # Load expenses
    try:
        with open('expenses.json', 'r') as f:
            expenses = json.load(f)
    except FileNotFoundError:
        print("No expenses.json found. Please run demo_data_generator.py first.")
        return
    
    if not expenses:
        print("No expenses found.")
        return
    
    # Use current month
    month = datetime.now().strftime('%Y-%m')
    monthly_expenses = [exp for exp in expenses if exp['date'].startswith(month)]
    
    if not monthly_expenses:
        # Use the most recent month with data
        all_months = sorted(set(exp['date'][:7] for exp in expenses), reverse=True)
        month = all_months[0]
        monthly_expenses = [exp for exp in expenses if exp['date'].startswith(month)]
        print(f"No data for current month. Using {month} instead.\n")
    
    # Calculate statistics
    total = sum(exp['amount'] for exp in monthly_expenses)
    avg = total / len(monthly_expenses)
    max_exp = max(monthly_expenses, key=lambda x: x['amount'])
    min_exp = min(monthly_expenses, key=lambda x: x['amount'])
    
    # Category-wise summary
    category_totals = defaultdict(float)
    category_counts = defaultdict(int)
    
    for exp in monthly_expenses:
        category_totals[exp['category']] += exp['amount']
        category_counts[exp['category']] += 1
    
    # Daily summary
    daily_totals = defaultdict(float)
    for exp in monthly_expenses:
        daily_totals[exp['date']] += exp['amount']
    
    # Generate report
    report = []
    report.append("\n" + "="*70)
    report.append(f"MONTHLY EXPENSE REPORT - {month}".center(70))
    report.append("="*70)
    
    # Summary Statistics
    report.append("\nSUMMARY STATISTICS")
    report.append("-"*70)
    report.append(f"Total Expenses:          Rs.{total:.2f}")
    report.append(f"Number of Transactions:  {len(monthly_expenses)}")
    report.append(f"Average per Transaction: Rs.{avg:.2f}")
    report.append(f"Highest Expense:         Rs.{max_exp['amount']:.2f} ({max_exp['category']})")
    report.append(f"Lowest Expense:          Rs.{min_exp['amount']:.2f} ({min_exp['category']})")
    
    # Category-wise breakdown
    report.append("\nCATEGORY-WISE BREAKDOWN")
    report.append("-"*70)
    report.append(f"{'Category':<20} {'Transactions':<15} {'Amount':<12} {'Percentage'}")
    report.append("-"*70)
    
    sorted_categories = sorted(category_totals.items(), key=lambda x: x[1], reverse=True)
    for cat, amount in sorted_categories:
        count = category_counts[cat]
        percentage = (amount / total) * 100
        report.append(f"{cat:<20} {count:<15} Rs.{amount:<10.2f} {percentage:>5.1f}%")
    
    # Top spending category
    top_cat, top_amount = sorted_categories[0]
    report.append("\nTOP SPENDING CATEGORY")
    report.append("-"*70)
    report.append(f"{top_cat}: Rs.{top_amount:.2f} ({(top_amount/total*100):.1f}% of total)")
    
    # Daily breakdown (show first 10 days)
    report.append("\nDAILY BREAKDOWN (Sample)")
    report.append("-"*70)
    report.append(f"{'Date':<12} {'Amount':<12} {'Visual Bar'}")
    report.append("-"*70)
    
    max_daily = max(daily_totals.values())
    for i, date in enumerate(sorted(daily_totals.keys())):
        if i >= 10:  # Show only first 10 days
            break
        amount = daily_totals[date]
        bar_length = int((amount / max_daily) * 40)
        bar = '█' * bar_length
        report.append(f"{date:<12} Rs.{amount:<10.2f} {bar}")
    
    if len(daily_totals) > 10:
        report.append(f"... and {len(daily_totals) - 10} more days")
    
    report.append("="*70)
    
    # Print report
    report_text = '\n'.join(report)
    print(report_text)
    
    # Save to file
    report_filename = f'expense_report_{month}.txt'
    with open(report_filename, 'w') as f:
        f.write(report_text)
    
    print(f"\n✓ Report saved to: {report_filename}")
    
    # Generate category analysis
    print("\n" + "="*70)
    print("GENERATING CATEGORY ANALYSIS...")
    print("="*70)
    
    monthly_data = defaultdict(lambda: defaultdict(float))
    
    for exp in expenses:
        exp_month = exp['date'][:7]
        monthly_data[exp_month][exp['category']] += exp['amount']
    
    all_months = sorted(monthly_data.keys())
    all_categories = set()
    for month_data in monthly_data.values():
        all_categories.update(month_data.keys())
    all_categories = sorted(all_categories)
    
    print(f"\n{'Month':<12} {'Total Expenses':<20} {'Top Category'}")
    print("-"*70)
    
    for m in all_months:
        month_total = sum(monthly_data[m].values())
        top_cat = max(monthly_data[m].items(), key=lambda x: x[1])
        print(f"{m:<12} Rs.{month_total:<18.2f} {top_cat[0]} (Rs.{top_cat[1]:.2f})")
    
    print("="*70)
    print("\n✓ All reports generated successfully!")


if __name__ == "__main__":
    generate_automated_report()
