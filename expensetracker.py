from expense import Expense
import calendar
import datetime

def main ():
    print(f"Running the Expense Tracker!")
    expense_file_pathway = "expenses.csv"
    expense = user_expense_amount()
    budget = 3000

    saving_users_expense(expense, expense_file_pathway)
    summarizing_users_expense(expense_file_pathway)

def user_expense_amount():
    print("Obtaining the user's expense")
    name_expense = input("Please enter the name of the expense: ")
    amount_expense = float(input("Please enter the amount of the expense: "))

    categories_expense = [
        "Food" , "Home" , "Work" , "Fun" , "Misc"
    ]

    while True: 
        print("Please select a category for the expense: ")
        for i, category_name in enumerate(categories_expense):
            print(f" {i + 1.} {category_name}" )

        value_range = f"[1 - {len(categories_expense)}]"
        selected_index = int(input("Please select a category number {value_range}: ")) -1

        if selected_index in range(len(categories_expense)):
            selected_category = categories_expense[selected_index]
            new_expense = Expense(name=name_expense, category= selected_category, amount=amount_expense)
            return
        else: 
            print("Invalid category number inputted. Please reenter a valid number")
            
def saving_users_expense(expense, expense_file_pathway):
    print("Saving the user's expense!: {expense} to {expense_file_pathway}") 
    with open(expense_file_pathway, "a") as f:
        f.write(f"{expense.name},{expense.amount},{expense.category}\n")

def summarizing_users_expense(expense_file_pathway, budget):
    print("Summarizing the users expense!")
    expenses: list[Expense] = []
    with open( expense_file_pathway , "r") as f:
        lines = f.readlines()
        for line in lines:
            stripped_line = line.strip()
            expense_name, expense_amount, expense_category = stripped_line.split(",")
            line_expense = Expense(name=expense_name, amount=float(expense_amount), category=expense_category)
            expenses.append(line_expense)

    category_amount = {}
    for expense in expenses:
        key = expense.category
        if key in category_amount:
            category_amount[key] += expense.amount
        else: 
            category_amount[key] = expense.amount
    print(category_amount)

    total_spent = sum([ex.amount for ex in expenses])
    print("The total that has been spent is ${total_spent:.2f} this month!")

    budget_remaining = budget - total_spent
    print("The total budget remaining is ${total_spent:.2f} this month!")

    now = datetime.datetime.now()

    days_in_month = calendar.monthrange(now.year, now.month)[1]
    remaining_days = days_in_month - now.day    
    daily_budget = budget_remaining / remaining_days
    print("Budget per day: $ {daily_budget:.2f}")

if __name__ == "__main__":
    main()