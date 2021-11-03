from PyInquirer import prompt
from csv_handler import append_row, read_all_rows
from user import get_all_users

CSV_FILE = 'expense_report.csv'

fieldnames = [
    "amount",
    "label",
    "spender",
    "involved_users"
]

def get_involed_user_options(answers):
    users = get_all_users()
    users.remove(answers[fieldnames[2]])
    return list(map(lambda user: {"name": user}, users))

def new_expense(*args):
    expense = prompt([
        {
            "type": "input",
            "name": fieldnames[0],
            "message":"New Expense - Amount: ",
        },
        {
            "type": "input",
            "name": fieldnames[1],
            "message":"New Expense - Label: ",
        },
        {
            "type": "list",
            "name": fieldnames[2],
            "message":"New Expense - Spender: ",
            "choices": get_all_users()
        },
        {
            "type": "checkbox",
            "name": fieldnames[3],
            "message":"New Expense - : Involved User(s)",
            "choices": get_involed_user_options,
        },
    ])

    expense[fieldnames[3]].append(expense[fieldnames[2]])
    expense[fieldnames[3]] = ','.join(expense[fieldnames[3]])

    append_row(CSV_FILE, fieldnames, expense)
    print("Expense Added !")
    return True

def get_all_expense():
    expenses = read_all_rows(CSV_FILE, fieldnames)

    for expense in expenses:
        expense['involved_users'] = expense['involved_users'].split(',')

    return expenses