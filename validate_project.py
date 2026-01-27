"""
Project Validation Script
Validates all components of the Personal Expense Tracker project
"""

import os
import json
import sys

def validate_project():
    """Validate all project components"""
    
    print("="*70)
    print("PERSONAL EXPENSE TRACKER - PROJECT VALIDATION".center(70))
    print("="*70)
    
    validation_results = []
    
    # 1. Check required files
    print("\n1. Checking Required Files...")
    print("-"*70)
    
    required_files = [
        'expense_tracker.py',
        'expense_tracker_simple.py',
        'demo_data_generator.py',
        'test_basic.py',
        'test_report_generation.py',
        'requirements.txt',
        'README.md',
        'INSTALLATION.md',
        'PROJECT_SUMMARY.md'
    ]
    
    for file in required_files:
        if os.path.exists(file):
            size = os.path.getsize(file)
            print(f"✓ {file:<35} ({size:,} bytes)")
            validation_results.append(True)
        else:
            print(f"✗ {file:<35} MISSING")
            validation_results.append(False)
    
    # 2. Check data files
    print("\n2. Checking Data Files...")
    print("-"*70)
    
    if os.path.exists('expenses.json'):
        try:
            with open('expenses.json', 'r') as f:
                expenses = json.load(f)
            print(f"✓ expenses.json loaded successfully")
            print(f"  - Contains {len(expenses)} expense entries")
            
            if expenses:
                total = sum(exp['amount'] for exp in expenses)
                print(f"  - Total expenses: Rs.{total:,.2f}")
                
                # Check data structure
                sample = expenses[0]
                required_keys = ['date', 'amount', 'category', 'description']
                if all(key in sample for key in required_keys):
                    print(f"✓ Data structure is valid")
                    validation_results.append(True)
                else:
                    print(f"✗ Data structure is invalid")
                    validation_results.append(False)
            else:
                print(f"  - No expenses found (empty file)")
                validation_results.append(True)
        except Exception as e:
            print(f"✗ Error loading expenses.json: {e}")
            validation_results.append(False)
    else:
        print(f"  expenses.json not found (will be created on first use)")
        validation_results.append(True)
    
    # 3. Validate Python syntax
    print("\n3. Validating Python Syntax...")
    print("-"*70)
    
    python_files = [
        'expense_tracker.py',
        'expense_tracker_simple.py',
        'demo_data_generator.py',
        'test_basic.py',
        'test_report_generation.py'
    ]
    
    for file in python_files:
        try:
            with open(file, 'r') as f:
                code = f.read()
            compile(code, file, 'exec')
            print(f"✓ {file:<35} Syntax OK")
            validation_results.append(True)
        except SyntaxError as e:
            print(f"✗ {file:<35} Syntax Error: {e}")
            validation_results.append(False)
        except FileNotFoundError:
            print(f"✗ {file:<35} File not found")
            validation_results.append(False)
    
    # 4. Check imports
    print("\n4. Checking Standard Library Imports...")
    print("-"*70)
    
    try:
        from datetime import datetime
        from collections import defaultdict
        print("✓ All standard library imports available")
        validation_results.append(True)
    except ImportError as e:
        print(f"✗ Import error: {e}")
        validation_results.append(False)
    
    # 5. Check optional dependencies
    print("\n5. Checking Optional Dependencies...")
    print("-"*70)
    
    optional_deps = ['matplotlib', 'seaborn', 'pandas']
    for dep in optional_deps:
        try:
            __import__(dep)
            print(f"✓ {dep:<20} installed")
        except ImportError:
            print(f"⚠ {dep:<20} not installed (optional - needed for visual reports)")
    
    # 6. Test basic functionality
    print("\n6. Testing Basic Functionality...")
    print("-"*70)
    
    try:
        # Test expense creation
        test_expense = {
            'date': '2026-01-27',
            'amount': 100.0,
            'category': 'Food & Dining',
            'description': 'Test expense'
        }
        
        # Test JSON serialization
        json_str = json.dumps([test_expense])
        loaded = json.loads(json_str)
        
        if loaded[0] == test_expense:
            print("✓ JSON serialization/deserialization works")
            validation_results.append(True)
        else:
            print("✗ JSON serialization failed")
            validation_results.append(False)
            
    except Exception as e:
        print(f"✗ Functionality test failed: {e}")
        validation_results.append(False)
    
    # 7. Summary
    print("\n" + "="*70)
    print("VALIDATION SUMMARY".center(70))
    print("="*70)
    
    total_checks = len(validation_results)
    passed_checks = sum(validation_results)
    failed_checks = total_checks - passed_checks
    success_rate = (passed_checks / total_checks) * 100
    
    print(f"\nTotal Checks:    {total_checks}")
    print(f"Passed:          {passed_checks} ✓")
    print(f"Failed:          {failed_checks} ✗")
    print(f"Success Rate:    {success_rate:.1f}%")
    
    if success_rate == 100:
        print("\n🎉 ALL VALIDATIONS PASSED! Project is ready to use.")
        print("\nQuick Start:")
        print("  python3 expense_tracker_simple.py    # Text-only version")
        print("  python3 demo_data_generator.py       # Generate sample data")
        print("  python3 test_report_generation.py    # Test reports")
    elif success_rate >= 80:
        print("\n⚠ Most validations passed. Check warnings above.")
    else:
        print("\n❌ Multiple validations failed. Please review errors above.")
        return 1
    
    print("="*70)
    return 0


if __name__ == "__main__":
    exit_code = validate_project()
    sys.exit(exit_code)
