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
