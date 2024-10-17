password = input("Enter new password: ")

result = {}

if len(password) >= 8:
    result['length'] = True
else:
    result['length'] = False

digit = False

for i in password:
    if i.isdigit():
        digit = True

result['digits'] = digit

uppercase = False

for i in password:
    if i.isupper():
        uppercase = True

result['uppercase'] = uppercase

# all returns true when all the items of the list are True

print(result)

if all(result.values()):
    print('Strong password!')
else:
    print("Weak password!")