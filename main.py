# Task1 Number of instances of character in string
def count(string, char):  # Count instances of character in string
    num = 0
    for i in range(len(string)):
        if char == string[i]:
            num = num + 1
    return num


x = input("Enter something: ")
y = input("Character you would like to count: ")
print("")
print("There are {} {}'s".format(count(x, y), y))


# Task2 Number to word
def num_to_word(number):
    words = {"0": "Zero", "1": "One", "2": "Two", "3": "Three", "4": "Four", "5": "Five", "6": "Six", "7": "Seven",
             "8": "Eight", "9": "Nine"}
    numlist = list(number)
    num_word = ""
    for i in numlist:
        num_word = num_word + words[i] + " "
    return num_word


try:
    numb = str(int(input("Enter integer: ")))  # gets input from user and makes sure no float is accepted
    print(num_to_word(numb))

except ValueError:
    print("Not a number")

