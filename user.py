from PyInquirer import prompt
from csv_handler import append_row, read_all_rows

CSV_FILE = 'users.csv'

fieldnames = [
    "name"
]

def add_user():
    user = prompt([
        {
            "type": "input",
            "name": fieldnames[0],
            "message":"New User - Name: ",
        }
    ])

    append_row(CSV_FILE, fieldnames, user)
    print("User Added !")
    return


def get_all_users():
    users = read_all_rows(CSV_FILE, fieldnames)
    return list(map(lambda user: user[fieldnames[0]], users))
