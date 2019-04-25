# User custom Exception classes
class AccessException(Exception):
    role: str
    grant: str = 'admin'

    def __init__(self, role: str):
        self.role = role

    def __str__(self):
        return f"Access error: Your role is '{self.role}', needed role: '{self.grant}'"


def check_access(role):
    if role == 'admin':
        return True
    else:
        raise AccessException(role)


# ...
# print(check_access('manager'))
try:
    check_access('manager')
except AccessException as error:
    print(error.role)
