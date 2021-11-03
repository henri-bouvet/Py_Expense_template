from expense import get_all_expense


from expense import get_all_expense
from user import get_all_users


def show_status():
    users = get_all_users()
    expenses = get_all_expense()

    ba_map = []

    for user in users:
        bu_map = []
        for sub_user in users:
            bu_map.append(0)
        ba_map.append(bu_map)

    for expense in expenses:
        user_index = users.index(expense['spender'])
        amount = float(expense['amount'])
        share = amount / len(expense['involved_users'])
        for sub_user in expense['involved_users']:
            sub_user_index = users.index(sub_user)
            if user_index == sub_user_index:
                continue

            new_amount = ba_map[user_index][sub_user_index] + share

            if (new_amount > 0):
                ba_map[user_index][sub_user_index] = 0
                ba_map[sub_user_index][user_index] = -new_amount
            else:
                ba_map[user_index][sub_user_index] = new_amount

    for i in range(len(users)):
        nothing = True
        output = users[i] + ' owes '
        for j in range(len(users)):
            if i == j:
                continue
            amount = float(ba_map[i][j])
            if amount < 0:
                if not nothing:
                    output += ', '
                nothing = False
                output += str(round(-amount, 2)) + '€ to ' + users[j]
        if nothing:
            output += 'nothing !'
        print(output)
