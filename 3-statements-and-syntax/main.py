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

# while (reply := input("Enter text: ")) != 'q':
#     if reply == 'q': print("you broke the program"); break
#     elif not reply.isdigit(): print("Put a fucking digit\n" * 8)
#     else: print(int(reply) ** 2)

# a, b, c, d = 'hack'
# a, *b= 'hack'
# print(a, b)

# person = { "name": "Uanela" }
# # dog = ("", name="Max")

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

# sheu = Person("Sheu", 25)

# # person["name"] := 'this' + 'hello'

# print(person["name"])

# choices = { 'macOS': 2001, 'Linux': 1991, 'Windows': 1985 }
# choice = 'amiga'

# try:
#     choices[choice]
#     print("You got it")
# except:
#     print(f'{choice} is not a valid choice, please choose one of {list(choices.keys())}')

# state = input("Enter an state: ")

# match state:
#     case 'go' | 'proceed' | 'siga':
#         print("you can go champ")
#     case 'stop' | 'wait':
#         print("Stop bro...")
#     case other:
#         print("Hmmm wait a sec yet not stop not go, but just stop", other)

# class Emp:
#     def __init__(self, name): 
#         self.name = name

# pat = Emp('Pat')

# # You mentioned state could be 'Pat' (a string) or pat (the object)
# # Let's test it with the object:
# state = pat 

# match state:
#     # This checks if state is EQUAL to the string 'Pat'
#     case pat.name as what: 
#         print('attr', what)
    
#     # This checks if state is an INSTANCE of Emp
#     case Emp(name=what): 
#         print('instance', what)


def function():
    r"""
    This is my badass function
    """
    pass

print(function.__doc__)
help(function)


