print("Name: Kushagra Suri")
print("USN: 1AY24AI058")
print("Section: M")
items = ['bananas', 'python', 'chilli', 'abrupt', 'programming']
result = ''

for i in range(len(items)):
    if i == len(items) - 1 and len(items) > 1:
        result += 'and ' + items[i]
    elif i == len(items) - 1:
        result += items[i]
    else:
        result += items[i] + ', '

print(result)
