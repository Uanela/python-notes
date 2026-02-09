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
