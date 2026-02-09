# 3 Statements and Syntax

## 10. Chapter - Introducing Python Statements

### Python's Statements

I will just take note of the most important ones for me and those I am not that clear

- `a := b` -> the walrus bro
- Switch statement

```python
match var:
    case 1:
        print("It is one bro")
    case _:
        print("I couldn't get it dude")
```

- `for x in myiter: print(x)`
- `while x := file.readline(): print(x)`
- `pass` -> a simple placeholder
- `try/except/finally`
- `raise EndSearch(location)` -> basically `throw new Error()`
- `assert X > Y, 'X too small'` -> debugging checks
- `with open('data') as file: process(file)` -> context managers
- `type vector = list[float]` -> Type hinting alias

## 11. Chapter - Assigments, Expressions and Prints

### Assigments

Once again I will just pass what I do not know and what is kind still new

- `code, hack = 'py', 'PY'` -> tuple assignment
- `[code, hack] = ['py', 'PY']` -> list assigment
- `a, b, c, d = 'hack'`
- `a, *b= 'hack'` -> b will be a list of strings
- `*a, b= 'hack'` -> a will be a list of strings, liked this inversion
- `a, *c, b = 'hack'` -> works like this also, this is chief kiss
- `code = hack = 'python'` -> multiple-target assigment
- `(a, b), c = string[:2], string[2:]` -> also works with nested sequences
- `*args` -> collects position args and returns a tuple
- `**kwargs` -> For named args and returns dictionary

### Expression Statements

Just pointing out new things

- `print(a, b, c, sep="**", end="...\n")` -> see those cool separator (sep) and end named arguments bro

### Print Operations

- By default `print` sends stream to stdout, now see printing the hard way:

```python
import sys

sys.stdout.write('hello world\n')
```

- By pass the standard output and pass a file

```python
import sys

org_stdout = sys.stdout
sys.stdout = open('file/path/here', 'a') # Open in append mode
print(x, y, z) # Now this will print to the file above

sys.stdout.close() # flush output to disk
sys.stdout = tem
```

- can also do `print(1, 3, 4, file=a_file)`, `a_file.close()`

## 12. Chapter - if and match selections

Most of the things just took note above

- this cool match statement
- we can do it with `lists`, 'tuples' and `objects` also
- `10 if x else 5` -> ternary `if/else`

```python
state = input("Enter an state: ")

match state:
    case 'go' | 'proceed' | 'siga':
        print("you can go champ")
    case 'stop' | 'wait':
        print("Stop bro...")
    case other:
        print("Hmmm wait a sec yet not stop not go, but just stop", other)
```

- This weired usage of `as` and `what`:

```python
class Emp:
    def __init__(self, name):
        self.name = name

pat = Emp('Pat')

# You mentioned state could be 'Pat' (a string) or pat (the object)
# Let's test it with the object:
state = pat

match state:
    # This checks if state is EQUAL to the string 'Pat'
    case pat.name as what:
        print('attr', what)

    # This checks if state is an INSTANCE of Emp
    case Emp(name=what):
        print('instance', what)
```
