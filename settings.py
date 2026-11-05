# import pdb

# def add_setting(settings, item):
#     key = str(item[0]).lower()
#     value = str(item[1]).lower()

#     if key in settings:
#         return f"Setting {key} already exists! Cannot add a new setting with this name."
#     else:
#         pdb.set_trace()  # Set a breakpoint here to inspect the state of the program
#         settings[key] = value
#         return f"Setting {key} added with value {value} successfully."

# def update_setting(settings, item):
#     key = str(item[0]).lower()
#     value = str(item[1]).lower()

#     if key in settings:
#         settings[key] = value
#         return f"Setting {key} updated to {value} successfully."
#     else:
#         return f"Setting {key} does not exist! Cannot update a non-existing setting."

# def delete_setting(settings, item):
#     key = str(item[0]).lower()

#     if key in settings:
#         del settings[key]
#         return f"Setting {key} deleted successfully!"
#     else:
#         return "Setting not found!"

# def view_settings(settings):
#     if not settings:
#         return "No settings available."
#     else:
#         output = "Current User Settings:\n"
#         for k, v in settings.items():
#             output += f"{k.capitalize()}: {v}\n"
#         return output

# test_settings = {
#     "theme": "dark",
#     "notification": "enabled",
#     "volume": "high"
# }

# # view_output = view_settings(test_settings)
# view_output = add_setting(test_settings, ("language", "english"))
# print(view_output)

# name = ''

# while name != 'your name':
#     print("Please type your name.")
#     name = input('> ')
# print("Thank you!")

while True:
    print('Who are you?')
    name = input('> ')
    if name != 'Adamas':
        continue
    print('Hello, Adamas. What is the password? (It is a fish.)')
    password = input('> ')
    if password == 'swordfish':
        break
print('Access granted.')