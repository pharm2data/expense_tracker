from expense import Expense

def main ():
    print(f"Running the Expense Tracker!")
    expense = user_expense_amount()
    saving_users_expense()
    summarizing_users_expense()

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
            
def saving_users_expense():
    print("Saving the user's expense!")

def summarizing_users_expense():
    print("Summarizing the users expense!")

if __name__ == "__main__":
    main()