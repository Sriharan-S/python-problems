import json

def load_expenses(file_path):
    """Load expenses from the JSON file."""
    try:
        with open(file_path, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        print("Error reading the expense file. It may be corrupted.")
        return []

def save_expenses(file_path, expenses):
    """Save expenses to the JSON file."""
    with open(file_path, 'w') as file:
        json.dump(expenses, file, indent=4)

def add_expense(file_path):
    """Add a new expense."""
    expenses = load_expenses(file_path)
    description = input("Enter expense description: ")
    amount = float(input("Enter expense amount: "))
    date = input("Enter expense date (YYYY-MM-DD): ")
    
    expense = {
        "description": description,
        "amount": amount,
        "date": date
    }
    expenses.append(expense)
    save_expenses(file_path, expenses)
    print("Expense added successfully.")

def view_expenses(file_path):
    """View all expenses."""
    expenses = load_expenses(file_path)
    if expenses:
        print("Expenses List:")
        for expense in expenses:
            print(f"Description: {expense['description']}")
            print(f"Amount: ${expense['amount']:.2f}")
            print(f"Date: {expense['date']}")
            print()
    else:
        print("No expenses found.")

def delete_expense(file_path):
    """Delete an expense by description."""
    expenses = load_expenses(file_path)
    description = input("Enter the description of the expense to delete: ")
    
    new_expenses = [exp for exp in expenses if exp['description'] != description]
    
    if len(new_expenses) < len(expenses):
        save_expenses(file_path, new_expenses)
        print(f"Expense '{description}' deleted successfully.")
    else:
        print(f"Expense with description '{description}' not found.")

def expense_tracker():
    file_path = 'expenses.json'
    
    while True:
        print("\nExpense Tracker")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Delete Expense")
        print("4. Exit")
        
        choice = input("Choose an option (1/2/3/4): ")
        
        if choice == '1':
            add_expense(file_path)
        elif choice == '2':
            view_expenses(file_path)
        elif choice == '3':
            delete_expense(file_path)
        elif choice == '4':
            print("Exiting the expense tracker. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

expense_tracker()
