# print("Recipe completed successfully!")
# # print(missing_ingredient)

# banana_count = 2
# message = "I have " + str(banana_count) + " bananas"
# print(message)

# user_input = "3"

# if user_input.isdigit():
#     banana_count = int(user_input)
#     print("Conversion successful!")
# else:
#     print("This is not a valid number. Defaulting to 0")
#     banana_count = 0

# for char in 'code':
#     print(char)

# secret_number = 7
# guess = 0

# while guess != secret_number:
#     guess = int(input("Guess a number between 1 and 10: "))
#     if guess < secret_number:
#         print("Too low!")
#     elif guess > secret_number:
#         print("Too high!")
# print("Congratulations! You guessed the secret number.")

# languages = ["Python", "JavaScript", "C++", "Java"]
# id = [1, 2, 3, 4]

# print(list(enumerate(languages)))
# for languages, id in zip(languages, id):
#     print(f"Language: {languages}, ID: {id}")

even_numebers = [num for num in range(1, 21) if num % 2 == 0]
print(even_numebers)

name = "Alice"
listed = list(name)
listed.append("!")
listed.insert(0, "Hello, ")
listed.remove("i")
listed.clear()
print(listed)

developer = ("John", "Doe", 30, "Python Developer", "Doe")
print(developer.index("Doe", 2))
