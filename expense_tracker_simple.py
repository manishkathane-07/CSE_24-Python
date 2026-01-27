"""
Personal Expense Tracker - Simplified Version
A Python-based application to track daily expenses without visualization dependencies.
Works without matplotlib/seaborn - generates text-based reports.
"""

import json
import os
from datetime import datetime
from collections import defaultdict

class ExpenseTrackerSimple:
    def __init__(self, data_file='expenses.json'):
        self.data_file = data_file
        self.expenses = self.load_expenses()
        self.categories = [
            'Food & Dining',
            'Transportation',
            'Shopping',
            'Entertainment',
            'Bills & Utilities',
            'Healthcare',
            'Education',
            'Others'
        ]
    
    def load_expenses(self):
        """Load expenses from JSON file"""
        if os.path.exists(self.data_file):
            try:
                with open(self.data_file, 'r') as f:
                    return json.load(f)
            except json.JSONDecodeError:
                return []
        return []
    
    def save_expenses(self):
        """Save expenses to JSON file"""
        with open(self.data_file, 'w') as f:
            json.dump(self.expenses, f, indent=4)
    
    def add_expense(self):
        """Add a new expense entry"""
        print("\n--- Add New Expense ---")
        
        # Get date
        date_input = input("Enter date (YYYY-MM-DD) or press Enter for today: ").strip()
        if date_input:
            try:
                date = datetime.strptime(date_input, '%Y-%m-%d').strftime('%Y-%m-%d')
            except ValueError:
                print("Invalid date format. Using today's date.")
                date = datetime.now().strftime('%Y-%m-%d')
        else:
            date = datetime.now().strftime('%Y-%m-%d')
        
        # Get amount
        while True:
            try:
                amount = float(input("Enter amount (Rs.): "))
                if amount <= 0:
                    print("Amount must be positive.")
                    continue
                break
            except ValueError:
                print("Invalid amount. Please enter a number.")
        
        # Get category
        print("\nSelect Category:")
        for i, cat in enumerate(self.categories, 1):
            print(f"{i}. {cat}")
        
        while True:
            try:
                cat_choice = int(input("Enter category number: "))
                if 1 <= cat_choice <= len(self.categories):
                    category = self.categories[cat_choice - 1]
                    break
                else:
                    print(f"Please enter a number between 1 and {len(self.categories)}.")
            except ValueError:
                print("Invalid input. Please enter a number.")
        
        # Get description
        description = input("Enter description: ").strip()
        
        # Create expense entry
        expense = {
            'date': date,
            'amount': amount,
            'category': category,
            'description': description
        }
        
        self.expenses.append(expense)
        self.save_expenses()
        print("\n✓ Expense added successfully!")
    
    def view_all_expenses(self):
        """Display all expenses"""
        if not self.expenses:
            print("\nNo expenses recorded yet.")
            return
        
        print("\n--- All Expenses ---")
        print(f"{'Date':<12} {'Category':<20} {'Amount':<10} {'Description'}")
        print("-" * 70)
        
        total = 0
        for exp in self.expenses:
            print(f"{exp['date']:<12} {exp['category']:<20} Rs.{exp['amount']:<8.2f} {exp['description']}")
            total += exp['amount']
        
        print("-" * 70)
        print(f"{'Total:':<32} Rs.{total:.2f}")
    
    def view_monthly_expenses(self):
        """Display expenses for a specific month"""
        if not self.expenses:
            print("\nNo expenses recorded yet.")
            return
        
        month_input = input("\nEnter month (YYYY-MM) or press Enter for current month: ").strip()
        if month_input:
            try:
                datetime.strptime(month_input, '%Y-%m')
                month = month_input
            except ValueError:
                print("Invalid format. Using current month.")
                month = datetime.now().strftime('%Y-%m')
        else:
            month = datetime.now().strftime('%Y-%m')
        
        monthly_expenses = [exp for exp in self.expenses if exp['date'].startswith(month)]
        
        if not monthly_expenses:
            print(f"\nNo expenses found for {month}.")
            return
        
        print(f"\n--- Expenses for {month} ---")
        print(f"{'Date':<12} {'Category':<20} {'Amount':<10} {'Description'}")
        print("-" * 70)
        
        total = 0
        for exp in monthly_expenses:
            print(f"{exp['date']:<12} {exp['category']:<20} Rs.{exp['amount']:<8.2f} {exp['description']}")
            total += exp['amount']
        
        print("-" * 70)
        print(f"{'Total:':<32} Rs.{total:.2f}")
    
    def generate_text_report(self):
        """Generate text-based monthly report"""
        if not self.expenses:
            print("\nNo expenses recorded yet.")
            return
        
        month_input = input("\nEnter month (YYYY-MM) or press Enter for current month: ").strip()
        if month_input:
            try:
                datetime.strptime(month_input, '%Y-%m')
                month = month_input
            except ValueError:
                print("Invalid format. Using current month.")
                month = datetime.now().strftime('%Y-%m')
        else:
            month = datetime.now().strftime('%Y-%m')
        
        monthly_expenses = [exp for exp in self.expenses if exp['date'].startswith(month)]
        
        if not monthly_expenses:
            print(f"\nNo expenses found for {month}.")
            return
        
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
        
        # Daily breakdown
        report.append("\nDAILY BREAKDOWN")
        report.append("-"*70)
        report.append(f"{'Date':<12} {'Amount':<12} {'Bar Chart'}")
        report.append("-"*70)
        
        max_daily = max(daily_totals.values())
        for date in sorted(daily_totals.keys()):
            amount = daily_totals[date]
            bar_length = int((amount / max_daily) * 40)
            bar = '█' * bar_length
            report.append(f"{date:<12} Rs.{amount:<10.2f} {bar}")
        
        report.append("="*70)
        
        # Print report
        report_text = '\n'.join(report)
        print(report_text)
        
        # Save to file
        report_filename = f'expense_report_{month}.txt'
        with open(report_filename, 'w') as f:
            f.write(report_text)
        
        print(f"\n✓ Report saved to: {report_filename}")
    
    def generate_category_analysis(self):
        """Generate category-wise analysis"""
        if not self.expenses:
            print("\nNo expenses recorded yet.")
            return
        
        # Group by month and category
        monthly_data = defaultdict(lambda: defaultdict(float))
        
        for exp in self.expenses:
            month = exp['date'][:7]  # YYYY-MM
            monthly_data[month][exp['category']] += exp['amount']
        
        # Generate report
        print("\n" + "="*70)
        print("CATEGORY-WISE MONTHLY ANALYSIS".center(70))
        print("="*70)
        
        # Get all unique months and categories
        all_months = sorted(monthly_data.keys())
        all_categories = set()
        for month_data in monthly_data.values():
            all_categories.update(month_data.keys())
        all_categories = sorted(all_categories)
        
        # Print header
        print(f"\n{'Month':<12}", end='')
        for cat in all_categories:
            print(f"{cat[:15]:<17}", end='')
        print("Total")
        print("-"*70)
        
        # Print data
        for month in all_months:
            print(f"{month:<12}", end='')
            month_total = 0
            for cat in all_categories:
                amount = monthly_data[month].get(cat, 0)
                month_total += amount
                if amount > 0:
                    print(f"Rs.{amount:<14.2f}", end='')
                else:
                    print(f"{'-':<17}", end='')
            print(f"Rs.{month_total:.2f}")
        
        # Category totals
        print("-"*70)
        print(f"{'Total':<12}", end='')
        grand_total = 0
        for cat in all_categories:
            cat_total = sum(monthly_data[month].get(cat, 0) for month in all_months)
            grand_total += cat_total
            print(f"Rs.{cat_total:<14.2f}", end='')
        print(f"Rs.{grand_total:.2f}")
        
        print("="*70)
    
    def delete_expense(self):
        """Delete an expense entry"""
        if not self.expenses:
            print("\nNo expenses to delete.")
            return
        
        self.view_all_expenses()
        
        print("\nEnter the details of the expense to delete:")
        date = input("Date (YYYY-MM-DD): ").strip()
        description = input("Description: ").strip()
        
        found = False
        for i, exp in enumerate(self.expenses):
            if exp['date'] == date and exp['description'].lower() == description.lower():
                confirm = input(f"\nDelete expense: {exp['category']} - Rs.{exp['amount']} on {exp['date']}? (y/n): ")
                if confirm.lower() == 'y':
                    self.expenses.pop(i)
                    self.save_expenses()
                    print("✓ Expense deleted successfully!")
                    found = True
                    break
        
        if not found:
            print("Expense not found.")
    
    def display_menu(self):
        """Display main menu"""
        print("\n" + "="*50)
        print("     PERSONAL EXPENSE TRACKER")
        print("="*50)
        print("1. Add New Expense")
        print("2. View All Expenses")
        print("3. View Monthly Expenses")
        print("4. Generate Monthly Report (Text)")
        print("5. Generate Category Analysis")
        print("6. Delete Expense")
        print("7. Exit")
        print("="*50)
    
    def run(self):
        """Main application loop"""
        while True:
            self.display_menu()
            choice = input("\nEnter your choice (1-7): ").strip()
            
            if choice == '1':
                self.add_expense()
            elif choice == '2':
                self.view_all_expenses()
            elif choice == '3':
                self.view_monthly_expenses()
            elif choice == '4':
                self.generate_text_report()
            elif choice == '5':
                self.generate_category_analysis()
            elif choice == '6':
                self.delete_expense()
            elif choice == '7':
                print("\nThank you for using Personal Expense Tracker!")
                break
            else:
                print("\nInvalid choice. Please try again.")


if __name__ == "__main__":
    tracker = ExpenseTrackerSimple()
    tracker.run()
