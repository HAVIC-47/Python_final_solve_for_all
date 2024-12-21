x= 132%9

if x%2==0:
    if x%3==0:
       output= "Divisible by both 2 and 3"
    else:
        output="Divisible by 2 onlt"
else:
    output="Not divisible by 2"

print(output)

my_list=[3,6,9,12,15]
output= my_list.pop()+my_list[-1]
print(output)

birth_year=int(input("Enter your birth year: "))
current_age= 2024-birth_year
if current_age<=60:
    print("You are not a senior citizen")
    till_senior=60-current_age
    print(f"you will be a senior citizen in {till_senior} years")
else:
    print("You are a senior citizen")

words = ["apple", "banana", "cherry", "date", "eggplant"]
if not words:
    print("List is empty")
else:
    max_len = 0
    longest_word = []

    for word in words:
        if len(word) > max_len:
            max_len = len(word)
            longest_word = [word]  # Start a new list with this word
        elif len(word) == max_len:
            longest_word.append(word)  # Add to the list of longest words

    print("Longest words are:", longest_word)
