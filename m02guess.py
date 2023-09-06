#Nooreddin Hellalat
#M02Guess
#M02 Programming Assignment - Loops and Conditionals
#4.1
secret = input("Enter your secret number guess 1 through 10: ")
guess = input("Enter your number guess 1 through 10: ")

print("Guess value is = ", guess)
print("Secret value is = ", secret)

if guess < secret:
    print("too low!")

elif guess > secret:
    print("too high!")
    
else:
    print("just right!")
 #4.2
small = input("Enter true or false if small: ")
green = input("Enter true or false if green: ")
if small == "true" and green == "true":
    print("pea")
elif small == "true" and green == "false":
    print("cherry")
elif not small== "false" and green == "true":
    print("watermelon")
elif not small == "false" and green == "false":
    print("pumpkin")
#6.1
list=[3,2,1,0]
for x in list:
print(x)
#6.2
guess_me = 7
start = 1

while True:
    if start < guess_me:
        print('too low')
    elif start == guess_me:
        print('found it!')
        break
    else:
        print('oops')
        break
    start += 1
#6.3
guess_me = 5
number = (10)

for number in range(1,10):

    if number < guess_me:
        print("too low")
        number += 1

    elif number == guess_me:
        print("found it!")
        break

    else:
        print("oops")
        exit