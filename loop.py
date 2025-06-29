# break - example

print("The break instruction:")
for i in range(1, 6):
    if i == 3:
        break
    print("Inside the loop.", i)
print("Outside the loop.")


# continue - example

print("\nThe continue instruction:")
for i in range(1, 6):
    if i == 3:
        continue
    print("Inside the loop.", i)
print("Outside the loop.")

text="umair"
vowel="UAIEOouaie"
upper_name=text.upper()
for i in upper_name:
    if i in vowel:
        continue
   
print(i)



# Example 2
counter = 5
while counter > 2:
    print(counter)
    counter -= 1

    word = "Python"
for letter in word:
    print(letter, end="*")


    # Example 2
for i in range(1, 10):
    if i % 2 == 0:
        print('\n',i)


 
text = "OpenEDG Python Institute"
for letter in text:
    if letter == "P":
        break
    print(letter, end="")     


    text = "pyxpyxpyx"
for letter in text:
    if letter == "x":
        continue
    print(letter, end="")  


    n = 0

while n != 3:
    print(n)
    n += 1
else:
    print(n, "else")

print()

for i in range(0, 3):
    print(i)
else:
    print(i, "else")



for digit in "0165031806510":
    if digit == "0":
        print("x", end="")
        continue
    print(digit, end="") 