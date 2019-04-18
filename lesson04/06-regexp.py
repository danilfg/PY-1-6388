# raw strings
a = r"Hello, World!  \r\n\t 0123456789 #$"

# regexp example
country_code = r"\b[A-z]{3}\b"
test_string = "Countries: RUS, ENG"

import re

# matching
is_match = re.match(country_code, test_string) is not None  # None

# finding
telephone_string_test1 = "88001112233"
telephone_string_test2 = "+8(800)111 22-33"

is_telephone = r"^\+[0-9]{1,5}\(?[0-9]+\)?+[0-9\s-]+$"

matches = re.findall(is_telephone, telephone_string_test1)

# sub (replace)
password_pattern = r"[A-Z]{1,}[\w]{1,}[_@#$][\d]{1,}"

re.sub(r"[a-z]", 'X', 'SIMPLe TESt')  # SIMPLX TESX
