greeting = input('Greeting: ').strip().lower()
greeting = greeting.split()[0]
print(greeting)
if 'hello' in greeting:
    print('$0')
elif greeting[0] == 'h':
    print('$20')
else:
    print('$100')