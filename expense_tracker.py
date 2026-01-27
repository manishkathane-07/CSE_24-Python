import csv
import datetime
import os
from collections import defaultdict
import matplotlib.pyplot as plt

class ExpenseTracker:
    """Manages a collection of expenses with CSV persistence."""

    def __init__(self, filename='expenses.csv'):
        """
        Initialize ExpenseTracker.

        Args:
            filename (str): CSV file to store expenses
        """
        self.filename = filename
        self.expenses = []
        self.load_expenses()

    def add_expense(self, expense):
        """
        Add a new expense to the tracker.

        Args:
            expense (Expense): Expense object to add
        """
        self.expenses.append(expense)
        self.save_expenses()

    def load_expenses(self):
        """Load expenses from CSV file."""
        if not os.path.exists(self.filename):
            return

        try:
            with open(self.filename, 'r', newline='') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    try:
                        expense = Expense.from_dict(row)
                        self.expenses.append(expense)
                    except (ValueError, KeyError):
                        print(f"Warning: Skipping invalid expense record: {row}")
        except FileNotFoundError:
            pass
        except Exception as e:
            print(f"Error loading expenses: {e}")

    def save_expenses(self):
        """Save expenses to CSV file."""
        try:
            with open(self.filename, 'w', newline='') as file:
                fieldnames = ['date', 'amount', 'category', 'description']
                writer = csv.DictWriter(file, fieldnames=fieldnames)
                writer.writeheader()
                for expense in self.expenses:
                    writer.writerow(expense.to_dict())
        except Exception as e:
            print(f"Error saving expenses: {e}")

    def get_expenses_by_month(self, year, month):
        """
        Get expenses for a specific month.

        Args:
            year (int): Year
            month (int): Month (1-12)

        Returns:
            list: List of Expense objects for the specified month
        """
        month_expenses = []
        for expense in self.expenses:
            expense_date = datetime.datetime.strptime(expense.date, '%Y-%m-%d')
            if expense_date.year == year and expense_date.month == month:
                month_expenses.append(expense)
        return month_expenses

    def generate_monthly_report(self, year, month):
        """
        Generate a monthly expense report with visualization.

        Args:
            year (int): Year
            month (int): Month (1-12)
        """
        month_expenses = self.get_expenses_by_month(year, month)

        if not month_expenses:
            print(f"No expenses found for {year}-{month:02d}")
            return

        # Calculate totals by category
        category_totals = defaultdict(float)
        total_amount = 0

        for expense in month_expenses:
            category_totals[expense.category] += expense.amount
            total_amount += expense.amount

        # Print text report
        print(f"\n=== Expense Report for {year}-{month:02d} ===")
        print(f"Total Expenses: ${total_amount:.2f}")
        print(f"Number of Transactions: {len(month_expenses)}")
        print("\nExpenses by Category:")
        for category, amount in sorted(category_totals.items()):
            print(f"  {category}: ${amount:.2f}")

        # Generate visualization if matplotlib is available
        if HAS_MATPLOTLIB:
            self._create_visual_report(year, month, category_totals)
        else:
            print("Note: Install matplotlib for visual reports (pip install matplotlib)")

    def _create_visual_report(self, year, month, category_totals):
        """
        Create a bar chart visualization of expenses by category.

        Args:
            year (int): Year
            month (int): Month
            category_totals (dict): Dictionary of category totals
        """
        if not HAS_MATPLOTLIB:
            return

        categories = list(category_totals.keys())
        amounts = list(category_totals.values())

        plt.figure(figsize=(10, 6))
        bars = plt.bar(categories, amounts, color='skyblue', edgecolor='navy', linewidth=1)

        plt.title(f'Expense Report - {year}-{month:02d}', fontsize=16, fontweight='bold')
        plt.xlabel('Category', fontsize=12)
        plt.ylabel('Amount ($)', fontsize=12)
        plt.xticks(rotation=45, ha='right')

        # Add value labels on bars
        for bar, amount in zip(bars, amounts):
            plt.text(bar.get_x() + bar.get_width()/2, bar.get_height() + max(amounts)*0.01,
                    f'${amount:.2f}', ha='center', va='bottom', fontsize=10)

        plt.tight_layout()

        # Save the chart
        filename = f'expense_report_{year}_{month:02d}.png'
        plt.savefig(filename, dpi=300, bbox_inches='tight')
        print(f"\nChart saved as: {filename}")

        plt.close()  # Close the figure to free memory

def main():
    """Main function to run the expense tracker application."""
    tracker = ExpenseTracker()

    while True:
        print("\n=== Personal Expense Tracker ===")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. Generate Monthly Report")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ").strip()

        if choice == '1':
            add_expense_interactive(tracker)
        elif choice == '2':
            view_expenses(tracker)
        elif choice == '3':
            generate_report_interactive(tracker)
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

def add_expense_interactive(tracker):
    """Interactive function to add a new expense."""
    try:
        date = input("Enter date (YYYY-MM-DD): ").strip()
        amount = float(input("Enter amount: ").strip())
        category = input("Enter category: ").strip()
        description = input("Enter description: ").strip()

        expense = Expense(date, amount, category, description)
        tracker.add_expense(expense)
        print("Expense added successfully!")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

def view_expenses(tracker):
    """Display all expenses."""
    if not tracker.expenses:
        print("No expenses recorded yet.")
        return

    print("\n=== All Expenses ===")
    for i, expense in enumerate(tracker.expenses, 1):
        print(f"{i}. {expense}")

def generate_report_interactive(tracker):
    """Interactive function to generate monthly report."""
    try:
        year = int(input("Enter year (YYYY): ").strip())
        month = int(input("Enter month (1-12): ").strip())

        if not (1 <= month <= 12):
            print("Invalid month. Please enter 1-12.")
            return

        tracker.generate_monthly_report(year, month)

    except ValueError:
        print("Invalid input. Please enter numeric values.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()

class Expense:
    """Represents a single expense entry."""

    def __init__(self, date, amount, category, description):
        """
        Initialize an Expense object.

        Args:
            date (str): Date in YYYY-MM-DD format
            amount (float): Expense amount
            category (str): Expense category
            description (str): Expense description

        Raises:
            ValueError: If date format is invalid or amount is negative
        """
        try:
            # Validate date format
            datetime.datetime.strptime(date, '%Y-%m-%d')
            self.date = date
        except ValueError:
            raise ValueError("Invalid date format. Use YYYY-MM-DD")

        if amount < 0:
            raise ValueError("Amount cannot be negative")

        self.amount = amount
        self.category = category.strip()
        self.description = description.strip()

    def __str__(self):
        return f"{self.date}: ${self.amount:.2f} - {self.category} - {self.description}"

    def to_dict(self):
        """Convert expense to dictionary for CSV writing."""
        return {
            'date': self.date,
            'amount': str(self.amount),
            'category': self.category,
            'description': self.description
        }

    @classmethod
    def from_dict(cls, data):
        """Create expense from dictionary (for CSV reading)."""
        return cls(
            data['date'],
            float(data['amount']),
            data['category'],
            data['description']
        )