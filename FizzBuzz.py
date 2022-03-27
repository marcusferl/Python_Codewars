counter = 0

for i in range(1,100):
    if i % 15 == 0:
        print('Fizz')
    elif i % 10 == 0:
        print('Buzz')
    elif i % 5 == 0:
        print('FizzBuzz')
    else:
        print(i)