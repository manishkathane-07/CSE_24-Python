"""
Demo script showing the new Clear All Data feature
"""
from expense_tracker import ExpenseTracker

def demo_clear_feature():
    print("="*70)
    print("DEMO: Clear All Data Feature".center(70))
    print("="*70)
    
    # Create tracker with sample data
    tracker = ExpenseTracker('clear_demo.json')
    tracker.expenses = []
    
    # Add sample expenses
    print("\n📝 Adding sample expenses...")
    tracker.add_expense(1500, 'Food & Groceries', 'BigBasket order', '2026-01-15')
    tracker.add_expense(250, 'Transportation', 'Ola ride', '2026-01-16')
    tracker.add_expense(15000, 'Rent', 'Monthly rent', '2026-01-17')
    tracker.add_expense(2500, 'Utilities & Bills', 'Electricity bill', '2026-01-18')
    tracker.add_expense(800, 'Food & Groceries', 'Restaurant', '2026-01-19')
    
    # Show current data
    print("\n" + "="*70)
    print("CURRENT EXPENSE DATA")
    print("="*70)
    tracker.view_expenses()
    
    # Show what the clear function displays
    print("\n" + "="*70)
    print("WHAT YOU'LL SEE WHEN CLEARING DATA")
    print("="*70)
    
    total_expenses = len(tracker.expenses)
    total_amount = sum(exp['amount'] for exp in tracker.expenses)
    
    print(f"\n{'='*70}")
    print("⚠️  WARNING: CLEAR ALL DATA".center(70))
    print(f"{'='*70}")
    print(f"\nYou are about to delete:")
    print(f"  • {total_expenses} expense entries")
    print(f"  • Total worth: ₹{total_amount:.2f}")
    print(f"\n⚠️  This action CANNOT be undone!")
    print(f"{'='*70}\n")
    print("To confirm, you need to type: DELETE ALL")
    print("To cancel, type anything else (or press Enter)")
    
    print("\n" + "="*70)
    print("HOW TO USE")
    print("="*70)
    print("\n1. Run the expense tracker: python expense_tracker.py")
    print("2. Choose option 7: Clear All Data")
    print("3. Review the warning message carefully")
    print("4. Type 'DELETE ALL' (exactly) to confirm deletion")
    print("5. Or type anything else to cancel and keep your data safe")
    
    print("\n" + "="*70)
    print("SAFETY FEATURES")
    print("="*70)
    print("\n✓ Shows total number of entries that will be deleted")
    print("✓ Shows total amount of money in those entries")
    print("✓ Requires exact confirmation text: 'DELETE ALL'")
    print("✓ Any other input cancels the operation")
    print("✓ Clear warning that action cannot be undone")
    
    print("\n" + "="*70)
    print("USE CASES")
    print("="*70)
    print("\n• Starting a new financial year")
    print("• Testing the app with dummy data")
    print("• Switching to a different tracking system")
    print("• Removing old/incorrect entries and starting fresh")
    
    print("\n" + "="*70)
    print("Demo complete! The Clear All Data feature is ready to use.")
    print("="*70 + "\n")

if __name__ == "__main__":
    demo_clear_feature()
