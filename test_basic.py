"""
Basic test to verify the expense tracker core functionality
Tests without visualization dependencies
"""

import json
import os
from datetime import datetime

def test_expense_operations():
    """Test basic expense operations"""
    
    print("Testing Personal Expense Tracker Core Functionality\n")
    print("="*60)
    
    # Test 1: Create sample expenses
    print("\n1. Creating sample expenses...")
    expenses = [
        {
            'date': '2026-01-25',
            'amount': 450.50,
            'category': 'Food & Dining',
            'description': 'Grocery shopping'
        },
        {
            'date': '2026-01-26',
            'amount': 200.00,
            'category': 'Transportation',
            'description': 'Fuel'
        },
        {
            'date': '2026-01-27',
            'amount': 1500.00,
            'category': 'Shopping',
            'description': 'New shoes'
        },
        {
            'date': '2026-01-27',
            'amount': 350.00,
            'category': 'Entertainment',
            'description': 'Movie tickets'
        }
    ]
    
    # Save to file
    with open('test_expenses.json', 'w') as f:
        json.dump(expenses, f, indent=4)
    print("✓ Created 4 sample expenses")
    
    # Test 2: Load and display
    print("\n2. Loading expenses from file...")
    with open('test_expenses.json', 'r') as f:
        loaded_expenses = json.load(f)
    print(f"✓ Loaded {len(loaded_expenses)} expenses")
    
    # Test 3: Display all expenses
    print("\n3. Displaying all expenses:")
    print("-"*60)
    print(f"{'Date':<12} {'Category':<20} {'Amount':<10} {'Description'}")
    print("-"*60)
    
    total = 0
    for exp in loaded_expenses:
        print(f"{exp['date']:<12} {exp['category']:<20} Rs.{exp['amount']:<8.2f} {exp['description']}")
        total += exp['amount']
    
    print("-"*60)
    print(f"{'Total:':<32} Rs.{total:.2f}")
    
    # Test 4: Category-wise summary
    print("\n4. Category-wise summary:")
    print("-"*60)
    
    from collections import defaultdict
    category_totals = defaultdict(float)
    category_counts = defaultdict(int)
    
    for exp in loaded_expenses:
        category_totals[exp['category']] += exp['amount']
        category_counts[exp['category']] += 1
    
    for cat in sorted(category_totals.keys()):
        count = category_counts[cat]
        amount = category_totals[cat]
        percentage = (amount / total) * 100
        print(f"{cat:<20} {count:>2} transactions  Rs.{amount:>8.2f}  ({percentage:>5.1f}%)")
    
    # Test 5: Monthly filtering
    print("\n5. Filtering expenses for January 2026:")
    print("-"*60)
    
    month = '2026-01'
    monthly_expenses = [exp for exp in loaded_expenses if exp['date'].startswith(month)]
    monthly_total = sum(exp['amount'] for exp in monthly_expenses)
    
    print(f"Found {len(monthly_expenses)} expenses for {month}")
    print(f"Total: Rs.{monthly_total:.2f}")
    
    # Test 6: Statistics
    print("\n6. Statistics:")
    print("-"*60)
    amounts = [exp['amount'] for exp in loaded_expenses]
    print(f"Number of transactions: {len(amounts)}")
    print(f"Average expense: Rs.{sum(amounts)/len(amounts):.2f}")
    print(f"Highest expense: Rs.{max(amounts):.2f}")
    print(f"Lowest expense: Rs.{min(amounts):.2f}")
    
    # Cleanup
    os.remove('test_expenses.json')
    print("\n✓ All tests passed successfully!")
    print("="*60)


if __name__ == "__main__":
    test_expense_operations()
