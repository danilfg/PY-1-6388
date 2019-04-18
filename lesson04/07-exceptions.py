# try-except syntax
age = input('Your age: ')

try:
    age = int(age)
    new_value = age / 2
except ValueError:
    print("Invalid string number")
except ZeroDivisionError:
    print("Invalid value")
# except:
#     print('Some error')
else:
    print(new_value)
finally:
    print("Thanks")

# else, finally


