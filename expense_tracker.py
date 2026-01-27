"""
Personal Expense Tracker
A Python-based application to track daily expenses, categorize them, 
and generate monthly reports with visual analytics.
"""

import json
import os
from datetime import datetime
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from collections import defaultdict

class ExpenseTracker:
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
    
    def generate_monthly_report(self):
        """Generate visual monthly report"""
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
        
        # Prepare data
        df = pd.DataFrame(monthly_expenses)
        df['amount'] = pd.to_numeric(df['amount'])
        
        # Category-wise summary
        category_summary = df.groupby('category')['amount'].sum().sort_values(ascending=False)
        
        # Daily expenses
        daily_summary = df.groupby('date')['amount'].sum().sort_index()
        
        # Set style
        sns.set_style("whitegrid")
        plt.rcParams['figure.figsize'] = (15, 10)
        
        # Create subplots
        fig, axes = plt.subplots(2, 2, figsize=(15, 10))
        fig.suptitle(f'Monthly Expense Report - {month}', fontsize=16, fontweight='bold')
        
        # 1. Category-wise Pie Chart
        colors = sns.color_palette('Set2', len(category_summary))
        axes[0, 0].pie(category_summary.values, labels=category_summary.index, autopct='%1.1f%%',
                       colors=colors, startangle=90)
        axes[0, 0].set_title('Expense Distribution by Category', fontweight='bold')
        
        # 2. Category-wise Bar Chart
        sns.barplot(x=category_summary.values, y=category_summary.index, palette='viridis', ax=axes[0, 1])
        axes[0, 1].set_xlabel('Amount (Rs.)', fontweight='bold')
        axes[0, 1].set_ylabel('Category', fontweight='bold')
        axes[0, 1].set_title('Category-wise Spending', fontweight='bold')
        
        # Add value labels on bars
        for i, v in enumerate(category_summary.values):
            axes[0, 1].text(v + 50, i, f'Rs.{v:.2f}', va='center')
        
        # 3. Daily Expense Trend
        axes[1, 0].plot(daily_summary.index, daily_summary.values, marker='o', 
                        linewidth=2, markersize=6, color='#2E86AB')
        axes[1, 0].set_xlabel('Date', fontweight='bold')
        axes[1, 0].set_ylabel('Amount (Rs.)', fontweight='bold')
        axes[1, 0].set_title('Daily Expense Trend', fontweight='bold')
        axes[1, 0].tick_params(axis='x', rotation=45)
        axes[1, 0].grid(True, alpha=0.3)
        
        # 4. Summary Statistics
        axes[1, 1].axis('off')
        total_expenses = df['amount'].sum()
        avg_daily = df['amount'].mean()
        max_expense = df['amount'].max()
        min_expense = df['amount'].min()
        num_transactions = len(df)
        
        summary_text = f"""
        SUMMARY STATISTICS
        {'='*40}
        
        Total Expenses:        Rs.{total_expenses:.2f}
        Number of Transactions: {num_transactions}
        Average per Transaction: Rs.{avg_daily:.2f}
        Highest Expense:       Rs.{max_expense:.2f}
        Lowest Expense:        Rs.{min_expense:.2f}
        
        TOP SPENDING CATEGORY
        {'='*40}
        {category_summary.index[0]}: Rs.{category_summary.values[0]:.2f}
        ({(category_summary.values[0]/total_expenses*100):.1f}% of total)
        """
        
        axes[1, 1].text(0.1, 0.5, summary_text, fontsize=11, family='monospace',
                        verticalalignment='center')
        
        plt.tight_layout()
        
        # Save report
        report_filename = f'expense_report_{month}.png'
        plt.savefig(report_filename, dpi=300, bbox_inches='tight')
        print(f"\n✓ Report generated successfully: {report_filename}")
        
        # Show plot
        plt.show()
    
    def generate_category_analysis(self):
        """Generate detailed category analysis"""
        if not self.expenses:
            print("\nNo expenses recorded yet.")
            return
        
        df = pd.DataFrame(self.expenses)
        df['amount'] = pd.to_numeric(df['amount'])
        df['date'] = pd.to_datetime(df['date'])
        df['month'] = df['date'].dt.to_period('M')
        
        # Category-wise monthly trend
        monthly_category = df.groupby(['month', 'category'])['amount'].sum().unstack(fill_value=0)
        
        plt.figure(figsize=(14, 8))
        
        # Stacked area chart
        monthly_category.plot(kind='area', stacked=True, alpha=0.7, 
                             colormap='tab10', figsize=(14, 8))
        
        plt.title('Category-wise Monthly Expense Trend', fontsize=16, fontweight='bold')
        plt.xlabel('Month', fontsize=12, fontweight='bold')
        plt.ylabel('Amount (Rs.)', fontsize=12, fontweight='bold')
        plt.legend(title='Category', bbox_to_anchor=(1.05, 1), loc='upper left')
        plt.grid(True, alpha=0.3)
        plt.tight_layout()
        
        # Save report
        report_filename = 'category_analysis.png'
        plt.savefig(report_filename, dpi=300, bbox_inches='tight')
        print(f"\n✓ Category analysis generated: {report_filename}")
        
        plt.show()
    
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
        print("4. Generate Monthly Report (Visual)")
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
                self.generate_monthly_report()
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
    tracker = ExpenseTracker()
    tracker.run()
