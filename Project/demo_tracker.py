from expense_tracker import ExpenseTracker
from datetime import datetime, timedelta
import random

def generate_sample_data():
    """Generate sample expense data for demonstration"""
    tracker = ExpenseTracker('sample_expenses.json')
    
    # Clear any existing data
    tracker.expenses = []
    
    categories = {
        'Food & Groceries': ['Kirana store', 'Vegetable market', 'BigBasket order', 'Swiggy food delivery', 'Zomato order', 'Street food', 'Restaurant dinner', 'Chai & snacks'],
        'Transportation': ['Petrol/Diesel', 'Ola/Uber ride', 'Auto rickshaw', 'Metro card recharge', 'Bus pass', 'Bike service', 'Car maintenance', 'Parking fee'],
        'Entertainment': ['Movie tickets (PVR/INOX)', 'Netflix/Amazon Prime', 'Cricket match', 'Concert/Event', 'Gaming', 'Books', 'Weekend outing', 'Hobbies'],
        'Utilities & Bills': ['Electricity bill', 'Water bill', 'Gas cylinder', 'Society maintenance', 'Broadband bill', 'DTH recharge'],
        'Healthcare': ['Doctor consultation', 'Medicines from pharmacy', 'Health insurance premium', 'Lab tests', 'Gym membership', 'Yoga classes', 'Ayurvedic medicines'],
        'Shopping & Clothing': ['Clothes shopping', 'Footwear', 'Accessories', 'Electronics', 'Home appliances', 'Furniture', 'Gifts', 'Festival shopping'],
        'Education': ['School/College fees', 'Tuition classes', 'Books & stationery', 'Online course', 'Exam fees', 'Educational supplies'],
        'Rent': ['House rent', 'PG accommodation', 'Hostel fees'],
        'Mobile & Internet': ['Mobile recharge', 'Postpaid bill', 'Internet bill', 'OTT subscriptions'],
        'Personal Care': ['Salon/Barber', 'Cosmetics', 'Personal grooming', 'Spa treatment'],
        'Other': ['Pet care', 'Donations', 'Temple offerings', 'Miscellaneous expenses', 'Emergency expenses']
    }
    
    # Indian expense ranges (in Rupees)
    expense_ranges = {
        'Food & Groceries': (50, 3000),
        'Transportation': (20, 800),
        'Entertainment': (100, 2000),
        'Utilities & Bills': (500, 5000),
        'Healthcare': (200, 5000),
        'Shopping & Clothing': (500, 8000),
        'Education': (1000, 15000),
        'Rent': (5000, 25000),
        'Mobile & Internet': (200, 1500),
        'Personal Care': (100, 2000),
        'Other': (50, 2000)
    }
    
    # Generate expenses for the last 3 months
    start_date = datetime.now() - timedelta(days=90)
    
    print("Generating sample expense data...\n")
    
    for i in range(120):  # Generate 120 random expenses
        # Random date in the last 90 days
        random_days = random.randint(0, 89)
        expense_date = (start_date + timedelta(days=random_days)).strftime('%Y-%m-%d')
        
        # Random category
        category = random.choice(list(categories.keys()))
        
        # Random description from category
        description = random.choice(categories[category])
        
        # Random amount within category range
        min_amount, max_amount = expense_ranges[category]
        amount = round(random.uniform(min_amount, max_amount), 2)
        
        tracker.add_expense(amount, category, description, expense_date)
    
    print(f"\n✓ Generated {len(tracker.expenses)} sample expenses!")
    return tracker


def demo_features():
    """Demonstrate all features of the expense tracker"""
    print("\n" + "="*70)
    print("EXPENSE TRACKER DEMO".center(70))
    print("="*70 + "\n")
    
    # Generate sample data
    tracker = generate_sample_data()
    
    # Get current month and year
    now = datetime.now()
    current_month = now.month
    current_year = now.year
    
    # Demo 1: View all expenses
    print("\n1. VIEWING ALL EXPENSES")
    print("-" * 70)
    input("Press Enter to continue...")
    tracker.view_expenses()
    
    # Demo 2: View monthly expenses
    print("\n2. VIEWING CURRENT MONTH EXPENSES")
    print("-" * 70)
    input("Press Enter to continue...")
    tracker.view_expenses(current_month, current_year)
    
    # Demo 3: Generate monthly report
    print("\n3. GENERATING MONTHLY REPORT")
    print("-" * 70)
    input("Press Enter to continue...")
    tracker.generate_monthly_report(current_month, current_year)
    
    # Demo 4: Generate monthly bar chart
    print("\n4. GENERATING MONTHLY BAR CHART FOR THE YEAR")
    print("-" * 70)
    input("Press Enter to continue...")
    tracker.generate_monthly_bar_chart(current_year)
    
    # Demo 5: Generate category pie chart
    print("\n5. GENERATING CATEGORY PIE CHART")
    print("-" * 70)
    input("Press Enter to continue...")
    tracker.generate_category_pie_chart(current_month, current_year)
    
    print("\n" + "="*70)
    print("DEMO COMPLETE!".center(70))
    print("="*70)
    print("\nCheck the following files:")
    print("- sample_expenses.json (expense data)")
    print("- expense_pie_chart.png (pie chart)")
    print("- category_bar_chart.png (category bar chart)")
    print("- monthly_expenses_bar_chart.png (monthly bar chart)")
    print("\nTo use the tracker interactively, run: python expense_tracker.py")


if __name__ == "__main__":
    demo_features()
