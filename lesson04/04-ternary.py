# ternary condition
users = [
    {'role': 'admin', 'login': 'John'},
    {'role': 'manager', 'login': 'Artur'}
]


def is_admin(user):
    # return True if user['role'] == 'admin' else False
    return user['role'] == 'admin'


for x in users:
    message = 'Hello, admin' if is_admin(x) else 'Hello, manager'
