"""
Demo Data Generator for Personal Expense Tracker
Generates sample expense data for testing and demonstration
"""

import json
import random
from datetime import datetime, timedelta

def generate_demo_data():
    """Generate sample expense data for the last 3 months"""
    
    categories = [
        'Food & Dining',
        'Transportation',
        'Shopping',
        'Entertainment',
        'Bills & Utilities',
        'Healthcare',
        'Education',
        'Others'
    ]
    
    descriptions = {
        'Food & Dining': ['Grocery shopping', 'Restaurant dinner', 'Coffee shop', 'Lunch', 'Breakfast', 'Food delivery'],
        'Transportation': ['Fuel', 'Bus fare', 'Auto rickshaw', 'Taxi', 'Metro card recharge', 'Bike maintenance'],
        'Shopping': ['Clothing', 'Electronics', 'Books', 'Shoes', 'Accessories', 'Home decor'],
        'Entertainment': ['Movie tickets', 'Concert', 'Gaming', 'Streaming subscription', 'Sports event'],
        'Bills & Utilities': ['Electricity bill', 'Water bill', 'Internet bill', 'Phone bill', 'Gas cylinder'],
        'Healthcare': ['Medicine', 'Doctor consultation', 'Lab tests', 'Pharmacy', 'Health checkup'],
        'Education': ['Course fee', 'Books', 'Online course', 'Stationery', 'Tuition'],
        'Others': ['Gift', 'Donation', 'Miscellaneous', 'Repairs', 'Subscription']
    }
    
    expenses = []
    
    # Generate expenses for the last 3 months
    end_date = datetime.now()
    start_date = end_date - timedelta(days=90)
    
    current_date = start_date
    while current_date <= end_date:
        # Generate 1-4 expenses per day randomly
        num_expenses = random.randint(0, 4)
        
        for _ in range(num_expenses):
            category = random.choice(categories)
            description = random.choice(descriptions[category])
            
            # Generate realistic amounts based on category
            amount_ranges = {
                'Food & Dining': (50, 800),
                'Transportation': (20, 500),
                'Shopping': (200, 3000),
                'Entertainment': (100, 1500),
                'Bills & Utilities': (500, 2500),
                'Healthcare': (100, 2000),
                'Education': (500, 5000),
                'Others': (50, 1000)
            }
            
            min_amt, max_amt = amount_ranges[category]
            amount = round(random.uniform(min_amt, max_amt), 2)
            
            expense = {
                'date': current_date.strftime('%Y-%m-%d'),
                'amount': amount,
                'category': category,
                'description': description
            }
            
            expenses.append(expense)
        
        current_date += timedelta(days=1)
    
    # Save to JSON file
    with open('expenses.json', 'w') as f:
        json.dump(expenses, f, indent=4)
    
    print(f"✓ Generated {len(expenses)} sample expense entries")
    print(f"✓ Date range: {start_date.strftime('%Y-%m-%d')} to {end_date.strftime('%Y-%m-%d')}")
    print("✓ Data saved to expenses.json")
    
    # Display summary
    total = sum(exp['amount'] for exp in expenses)
    print(f"\nTotal expenses: Rs.{total:.2f}")
    
    # Category-wise summary
    from collections import defaultdict
    category_totals = defaultdict(float)
    for exp in expenses:
        category_totals[exp['category']] += exp['amount']
    
    print("\nCategory-wise breakdown:")
    for cat, amt in sorted(category_totals.items(), key=lambda x: x[1], reverse=True):
        print(f"  {cat:<20}: Rs.{amt:>10.2f}")


if __name__ == "__main__":
    generate_demo_data()
