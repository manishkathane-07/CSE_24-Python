import json
import os
from datetime import datetime
import matplotlib.pyplot as plt
import seaborn as sns
from collections import defaultdict

class ExpenseTracker:
    def __init__(self, filename='expenses.json'):
        self.filename = filename
        self.expenses = self.load_expenses()
        
    def load_expenses(self):
        """Load expenses from JSON file"""
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as f:
                return json.load(f)
        return []
    
    def save_expenses(self):
        """Save expenses to JSON file"""
        with open(self.filename, 'w') as f:
            json.dump(self.expenses, f, indent=4)
    
    def add_expense(self, amount, category, description, date=None):
        """Add a new expense"""
        if date is None:
            date = datetime.now().strftime('%Y-%m-%d')
        
        expense = {
            'date': date,
            'amount': float(amount),
            'category': category,
            'description': description
        }
        
        self.expenses.append(expense)
        self.save_expenses()
        print(f"✓ Expense added: ₹{amount} for {category}")
    
    def view_expenses(self, month=None, year=None):
        """View expenses, optionally filtered by month and year"""
        if not self.expenses:
            print("No expenses recorded yet.")
            return
        
        filtered_expenses = self.expenses
        
        if month and year:
            filtered_expenses = [
                exp for exp in self.expenses 
                if datetime.strptime(exp['date'], '%Y-%m-%d').month == month
                and datetime.strptime(exp['date'], '%Y-%m-%d').year == year
            ]
        
        if not filtered_expenses:
            print(f"No expenses found for {month}/{year}")
            return
        
        print("\n" + "="*70)
        print(f"{'Date':<12} {'Category':<15} {'Amount':<10} {'Description':<30}")
        print("="*70)
        
        total = 0
        for exp in filtered_expenses:
            print(f"{exp['date']:<12} {exp['category']:<15} ₹{exp['amount']:<9.2f} {exp['description']:<30}")
            total += exp['amount']
        
        print("="*70)
        print(f"{'Total:':<27} ₹{total:.2f}")
        print("="*70 + "\n")
    
    def get_category_totals(self, month=None, year=None):
        """Get total spending by category"""
        category_totals = defaultdict(float)
        
        for exp in self.expenses:
            exp_date = datetime.strptime(exp['date'], '%Y-%m-%d')
            
            if month and year:
                if exp_date.month == month and exp_date.year == year:
                    category_totals[exp['category']] += exp['amount']
            else:
                category_totals[exp['category']] += exp['amount']
        
        return dict(category_totals)
    
    def generate_category_pie_chart(self, month=None, year=None):
        """Generate a pie chart showing expenses by category"""
        category_totals = self.get_category_totals(month, year)
        
        if not category_totals:
            print("No data to visualize.")
            return
        
        # Set style
        sns.set_style("whitegrid")
        
        # Create pie chart
        plt.figure(figsize=(10, 7))
        colors = sns.color_palette('Set2', len(category_totals))
        
        plt.pie(category_totals.values(), 
                labels=category_totals.keys(), 
                autopct='%1.1f%%',
                startangle=90,
                colors=colors)
        
        title = "Expenses by Category"
        if month and year:
            title += f" ({month}/{year})"
        
        plt.title(title, fontsize=16, fontweight='bold')
        plt.axis('equal')
        plt.tight_layout()
        plt.savefig('expense_pie_chart.png', dpi=300, bbox_inches='tight')
        plt.show()
        print("✓ Pie chart saved as 'expense_pie_chart.png'")
    
    def generate_monthly_bar_chart(self, year=None):
        """Generate a bar chart showing monthly expenses"""
        if year is None:
            year = datetime.now().year
        
        monthly_totals = defaultdict(float)
        
        for exp in self.expenses:
            exp_date = datetime.strptime(exp['date'], '%Y-%m-%d')
            if exp_date.year == year:
                monthly_totals[exp_date.month] += exp['amount']
        
        if not monthly_totals:
            print(f"No expenses found for year {year}.")
            return
        
        # Prepare data
        months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 
                  'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
        amounts = [monthly_totals.get(i, 0) for i in range(1, 13)]
        
        # Create bar chart
        sns.set_style("whitegrid")
        plt.figure(figsize=(12, 6))
        
        bars = plt.bar(months, amounts, color=sns.color_palette('viridis', 12))
        
        plt.xlabel('Month', fontsize=12, fontweight='bold')
        plt.ylabel('Total Expenses (₹)', fontsize=12, fontweight='bold')
        plt.title(f'Monthly Expenses for {year}', fontsize=16, fontweight='bold')
        plt.xticks(rotation=45)
        
        # Add value labels on bars
        for bar in bars:
            height = bar.get_height()
            if height > 0:
                plt.text(bar.get_x() + bar.get_width()/2., height,
                        f'₹{height:.0f}',
                        ha='center', va='bottom', fontsize=9)
        
        plt.tight_layout()
        plt.savefig('monthly_expenses_bar_chart.png', dpi=300, bbox_inches='tight')
        plt.show()
        print("✓ Bar chart saved as 'monthly_expenses_bar_chart.png'")
    
    def generate_category_bar_chart(self, month=None, year=None):
        """Generate a bar chart showing expenses by category"""
        category_totals = self.get_category_totals(month, year)
        
        if not category_totals:
            print("No data to visualize.")
            return
        
        # Sort by amount
        sorted_categories = sorted(category_totals.items(), 
                                  key=lambda x: x[1], 
                                  reverse=True)
        categories = [item[0] for item in sorted_categories]
        amounts = [item[1] for item in sorted_categories]
        
        # Create bar chart
        sns.set_style("whitegrid")
        plt.figure(figsize=(10, 6))
        
        bars = plt.barh(categories, amounts, color=sns.color_palette('rocket', len(categories)))
        
        plt.xlabel('Total Expenses (₹)', fontsize=12, fontweight='bold')
        plt.ylabel('Category', fontsize=12, fontweight='bold')
        
        title = 'Expenses by Category'
        if month and year:
            title += f' ({month}/{year})'
        plt.title(title, fontsize=16, fontweight='bold')
        
        # Add value labels
        for i, bar in enumerate(bars):
            width = bar.get_width()
            plt.text(width, bar.get_y() + bar.get_height()/2.,
                    f'₹{width:.2f}',
                    ha='left', va='center', fontsize=9, 
                    bbox=dict(boxstyle='round', facecolor='white', alpha=0.7))
        
        plt.tight_layout()
        plt.savefig('category_bar_chart.png', dpi=300, bbox_inches='tight')
        plt.show()
        print("✓ Category bar chart saved as 'category_bar_chart.png'")
    
    def generate_monthly_report(self, month, year):
        """Generate a comprehensive monthly report"""
        print(f"\n{'='*70}")
        print(f"MONTHLY EXPENSE REPORT - {month}/{year}".center(70))
        print(f"{'='*70}\n")
        
        # Filter expenses for the month
        monthly_expenses = [
            exp for exp in self.expenses 
            if datetime.strptime(exp['date'], '%Y-%m-%d').month == month
            and datetime.strptime(exp['date'], '%Y-%m-%d').year == year
        ]
        
        if not monthly_expenses:
            print(f"No expenses recorded for {month}/{year}")
            return
        
        # Calculate totals
        total_expenses = sum(exp['amount'] for exp in monthly_expenses)
        category_totals = self.get_category_totals(month, year)
        
        # Display summary
        print(f"Total Expenses: ₹{total_expenses:.2f}")
        print(f"Number of Transactions: {len(monthly_expenses)}")
        print(f"Average Transaction: ₹{total_expenses/len(monthly_expenses):.2f}")
        print(f"\nExpenses by Category:")
        print("-" * 40)
        
        for category, amount in sorted(category_totals.items(), 
                                      key=lambda x: x[1], 
                                      reverse=True):
            percentage = (amount / total_expenses) * 100
            print(f"{category:<20} ₹{amount:>8.2f} ({percentage:>5.1f}%)")
        
        print(f"\n{'='*70}\n")
        
        # Generate visualizations
        self.generate_category_pie_chart(month, year)
        self.generate_category_bar_chart(month, year)
    
    def clear_all_data(self):
        """Clear all expense data with confirmation"""
        if not self.expenses:
            print("\n⚠ No data to clear. The expense tracker is already empty.")
            return
        
        total_expenses = len(self.expenses)
        total_amount = sum(exp['amount'] for exp in self.expenses)
        
        print(f"\n{'='*70}")
        print("⚠️  WARNING: CLEAR ALL DATA".center(70))
        print(f"{'='*70}")
        print(f"\nYou are about to delete:")
        print(f"  • {total_expenses} expense entries")
        print(f"  • Total worth: ₹{total_amount:.2f}")
        print(f"\n⚠️  This action CANNOT be undone!")
        print(f"{'='*70}\n")
        
        confirmation = input("Type 'DELETE ALL' to confirm (or anything else to cancel): ").strip()
        
        if confirmation == 'DELETE ALL':
            self.expenses = []
            self.save_expenses()
            print("\n✓ All expense data has been cleared successfully.")
            print("  You can start fresh by adding new expenses.\n")
        else:
            print("\n✗ Operation cancelled. Your data is safe.\n")


def main():
    tracker = ExpenseTracker()
    
    # Indian expense categories
    categories = ['Food & Groceries', 'Transportation', 'Entertainment', 'Utilities & Bills', 
                  'Healthcare', 'Shopping & Clothing', 'Education', 'Rent', 
                  'Mobile & Internet', 'Personal Care', 'Other']
    
    while True:
        print("\n" + "="*50)
        print("PERSONAL EXPENSE TRACKER".center(50))
        print("="*50)
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. View Monthly Expenses")
        print("4. Generate Monthly Report")
        print("5. Generate Monthly Bar Chart (Year)")
        print("6. Generate Category Pie Chart")
        print("7. Clear All Data")
        print("8. Exit")
        print("="*50)
        
        choice = input("\nEnter your choice (1-8): ").strip()
        
        if choice == '1':
            print("\nCategories:", ", ".join(categories))
            amount = input("Enter amount: ₹")
            category = input("Enter category: ").strip().capitalize()
            description = input("Enter description: ").strip()
            date = input("Enter date (YYYY-MM-DD) or press Enter for today: ").strip()
            
            if not date:
                date = None
            
            try:
                tracker.add_expense(amount, category, description, date)
            except ValueError:
                print("Invalid amount. Please enter a number.")
        
        elif choice == '2':
            tracker.view_expenses()
        
        elif choice == '3':
            month = int(input("Enter month (1-12): "))
            year = int(input("Enter year (e.g., 2024): "))
            tracker.view_expenses(month, year)
        
        elif choice == '4':
            month = int(input("Enter month (1-12): "))
            year = int(input("Enter year (e.g., 2024): "))
            tracker.generate_monthly_report(month, year)
        
        elif choice == '5':
            year = int(input("Enter year (e.g., 2024): "))
            tracker.generate_monthly_bar_chart(year)
        
        elif choice == '6':
            choice_filter = input("Filter by month? (y/n): ").lower()
            if choice_filter == 'y':
                month = int(input("Enter month (1-12): "))
                year = int(input("Enter year (e.g., 2024): "))
                tracker.generate_category_pie_chart(month, year)
            else:
                tracker.generate_category_pie_chart()
        
        elif choice == '7':
            tracker.clear_all_data()
        
        elif choice == '8':
            print("\nThank you for using Personal Expense Tracker!")
            break
        
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
