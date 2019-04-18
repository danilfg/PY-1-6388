# create, open, write files
# 'with' construction

# w - write (w+)
# r - read (r+)
# a - append (a+)

filename = open('test.txt', 'w')
filename.write('Hello world!')
filename.close()

second_test = open('test.txt')
content = second_test.readline()
second_test.close()
print(content)

with open('test.txt') as file:
    # file = open('test.txt')
    content = file.readline()
    print(content)
