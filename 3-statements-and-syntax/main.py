# Just some code

# a = 1
# b = 2
# c = 3

# if a == 1 and b == 2 and c == 3:
#     print('hack\n' * 3)

# Avoid using `is` with int|string literal

# while True:
#     reply = input( 'Enter text (or q to quite):')
#     if reply == 'q': break
#     print(reply.upper())

# while ( reply := input("Enter text: ") ) != 'q':
#     print(reply.upper())

while (reply := input("Enter text: ")) != 'q':
    if reply == 'q': print("you broke the program"); break
    elif not reply.isdigit(): print("Put a fucking digit\n" * 8)
    else: print(int(reply) ** 2)

