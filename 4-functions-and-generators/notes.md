# 4 Functions And Generators

## 16. Chapter - Functions Basics

You will see small notes because I know many of this already

- `def func(): pass` -> u got a function
- `def fn(): return 2` -> I do not why take those 2 notes
- `global x` -> it makes them in global context of the file
- `nonlocal x` -> go one level outside this scope looking for x
- `yield` -> `def squares(x): for i in range(x): yield i ** 2`, still gotta master this one
- `(i ** 2 for i in range(x))` -> generator expressions
- `async/await` -> you know how it works
- decorators -> `@tracer def fn(a: 'hack' = None) -> None`
- `times = lambda x, y: x * y` -> this is just inline arrow function

## 17. Chapter - Scope

Just programming scope bro, trust your guts

- `global x` -> this will always make it go grab x from global scope

### the nonlocal

- Makes it remember state in enclosing scope

```python
def outer(start: int):
    state = start
    def inner(label: str):
        nonlocal state # If this wasn't here, code below would not work
        state += 1
        print(label, state)
    return inner
```

### State-Retention Options

- If you pass global to variable inside function, first call the function and then try to reference the variable it will work otherwise not.

### Function Attributes

- Can be access outside the closure

```python
def outer(start: int):
    state = start
    def inner(label: str):
        inner.state += 1
        print(label, state)
    inner.state
    return inner

F = outer(0)
print(F.state) # this works
```

### Scopes and Argument Defaults

```python
def f1():
    x = 88
    def f2(x=x): # remember enclosing scope x with defaults
        print(x + 1)
    f2()
f1() # print 89
```

```python
def f1():
    x = 88
    f2 = lambda x=x: print(x + 1)
    f2()
```

### Loops Require Defaults, Not Scopes

- In this case all `acts` will only remember the value of `i` in last iteration

```python
def makeActions():
    acts[]
    for i in range(5):
        acts.append(lambda x: x ** i) # This is make remeber only last
        acts.append(lambda x, i = i: x ** i) # This will preserver state
    return acts
```
