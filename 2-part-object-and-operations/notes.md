# 2. Part - Object and Operations

## 4.Chapter - Introducing Python Objects

### Python Core Objects

- Numbers -> 7
- Strings -> "The Boss"
- Lists aka Array -> `[]`
- Dictionaries -> `{ 'key': 'value' }`, `dict(hours=10)`
- Tuples -> `(1, "app", 7, "Cacilda")`, `tuple(`macos`)`, `nametuple`
- Files -> `open("file.txt")`, `open(r'C:\data.bin', 'wb')`
- Sets -> `set('ab')`, { "a", "b" }
- Others -> Booleans, types, None
- Programming-unit objects -> Functions, modules, classes
- Implementation objects -> compiled code, stack tracebaks

#### Numbers

- `len` -> get length of array and strings
- `str` -> converts to string
- `import math` -> cool math lib with methods such as `pi`, `sqrt`, `random`, `choice`

#### Strings

- `name[2]` -> third character, can use negative to loop backwards
- `name[1:3]` -> slice of name from offsets 1 through 2 (not 3)
- `name[:-1]` -> everything but the last (0:-1)
- `name[:3]` -> the first 3 (0:3)
- `name[2] = "s"` -> won't work because it is immutable
- `list(name)` -> returns array of chars of name
- `''.join(some_list)` -> will join the list into string
- `name.find(sub_str)` -> You know what it does
- `name.replace('ci', 'si')` -> this one also
- `name.split(',')` -> split at comma and returns array
- `name.upper()`
- `name.lower()`
- `name.isalpha()` -> Content tests: isdigit also
- `name.rstrip()` -> strip whitespaces in the right side, probably there is `lstrip`
- This one belows is how we call use string template literals (Not sure if name is same as in JS)

```python
tool = "Arkos"
major = "2"
minor = "3"

"Using %s version %s.%s" % (tool, major, minor + 9)
"Using {} version {}.{}".format(tool, major, minor + 9) # format method
f"Using {tool} version {major}.{minor + 9}" # The king
```

- Try `name.__add__('head')` would be the same `name + 'head'`, recalls me Lua setmetatable things.
- `name.encode("utf-8")` | `name.decode('utf-8')`
- `hex(name)` -> wil make name into hex

### Lists aka Array

- `L = [1, '2', True, 1.9]`
- `len(L)` -> get the array length
- `L + [4, 5, 6]` -> magically a dumbly becomes `[1, '2', True, 1.9, 4, 5, 6]`, basically concatanates the arrays
- `L * 2` -> if prev concatenated this ones doubles the items inside from `[ 4, 5, 6 ]` to `[ 4, 5, 6, 4, 5, 6 ]`
- `L[:1]` -> the first 2, like 0 1, that cool string things
- `L.append()` -> adds and item to the end
- `L.pop(2)` -> Deletes the item with index 2
- `del L[2]` -> also works as prev
- `L.sort()`
- `L.reverse()`

#### Matrixes

- Just use `NumPy` for the sake of humanity
- `col2 = [row[1] for row in M]` -> Collect the items in column 2
- `[row[1] + 1 for row in M]` -> Add 1 to each in column 2
- `[row[1] for row in M if row[1] % 2 == 0]` -> Filters to get only num dividable by 2, odd items
- `[M[i][i] for i in [0, 1, 2]]` -> Collect a diagonal from matrix
- `[c * 2 for c in 'hack']` -> Repeat charaters in a string
- `list(range(4))` -> Integers 0..N-1, creates a list of 4 items
- `list(range(-6, 7, 2))` -> -6 to +6 by 2
- `[[ x ** 2, x ** 3 ] for x in range(4)]` -> Understand by yourself
- `[[x, x // 2, x * 2] for x in range(-6, 7, 2) if x > 0]`
- `//` -> Does floor division
- `sum(something)` -> means what you read
- `G = (sum(row) for row in M)` -> Make a generator of row sums (not executed yet), `next(G)` Run the iteration protocol (ahead) and if you keep calling `next(G)` it will keep going and summing up each row.
- `{ sum(row) for row in M }` -> Makes an unordred set of rows sums
- ` {i: sum(M[i]) for i in range(3) }` -> Makes key:value table of row sums

### Dictionaries

- `dog = { 'name': 'Max', 'job': 'The guard dog', 'age': 7 }`
- `print(dog['name'])` -> accesses the prop name
- `dog['job'] = 'New job'` -> changes the prop value
- `cat = dict(name="Grifield", kind="Lion", age=300)` -> Creates a dict also
- `dict(zip(['name', 'last'], ['Uanela', 'Como']))` -> Zipping
- `zip([], [])` -> Makes key value pairs, array 1 are keys and the second are value
- `'e' in dog` -> boolean
- `if not 'e' in dog:` -> cool inverse check of prev
- `dog.get('job', 'default dog job')` -> same as `dog['a']` with a default if missing
- `dog['height'] if 'e' in dog else 0` -> if/else ternary expression form
- `dog.keys()` -> returns iterable of dog keys
- `list(dog.keys())` -> returns iterable of dog key
- `dog.values()` -> returns iterable of dog values
- `list(dog.items())` -> tuple of key/value pairs
- `iter(dog.keys())` -> Get an iterator from an iterable
- **Item Iteration**:

```python
for key in dog.keys():
    print(key, dog[key])

for key in dog:
    print(key, dog[key])

for (key, value) in dog.items(): # key/value-pair tuples iteration
    print(key, value)
```

### Tuples

- This are basically `Lists` with less methods, the diff is that they immutable
- `T = (1, 2, 4, 4)`
- `T + (5, 6)` -> concatenates
- `T[2]` -> indexing
- `T[1:]` -> slicing
- `T.index(4)` -> get index of 4
- `T.count(4)` -> how many 4 we've
- You can just create a new tuple
- `T = 'hack', 3.0, [11, 22, 33]` -> yes it creates a tuple

### Files

- `file = open("file.txt", "w")` -> open a new file in text-output mode, then `file.write("content")` finally `file.close()`
- `file = open("data.tx")` -> withou "w" opens exsting file in text-input mode, then `text = file.read()`
- `for line in open("data.txt"):` -> displays lines in a file

#### Unicode and byte files

- `bf = open("data.bin", "wb")` -> opens in write mode binary in a bytes files
- `bf.write(b'\xFFa\xEEc\xDDk\n')` -> write binary data in a bytes
- `bf.close()`
- `open('data.bin', 'rb').read()` -> read binary data to bytes
- `tf = open('unidata.txt', 'w', enconding='utf-8')`, `tf.write(`h\u00c4k`)` -> enconds to utf-8, `tf.close()`
- `open('unidata.txt', 'r', enconding='utf-8').read()` -> Decodes from UTF-8

### Sets

- neither mappings nor sequences, rather are unordered colletions of immutable ("hashable")
- It also is like JS the sets remove duplication
- `x = set('hack')` -> sequence => set
- `y = { 'a', 'b', 'b' }` -> set literal
- `x & y, x | y` -> intersection, union
- `x - y, x > y` -> difference, superset
- `set('code') - set('hack')` -> collestion difference
- `set('code') == set('deoc')` -> order-neutral equality

### Booleans and None

- `True` and `False`
- `None` -> this is null, just more weird things
- `bool('hack')` -> conversion

### Types

- `type([])` -> get type of expression
- `isinstance(L, list)` -> oo way

### Type Hinting (Kind TS but no)

- `x: int = 1` -> this is just optinal hint, `x = "another thing"` but it doesn't have to be `int`

### User-Defined Objects (classes)

- starting just

```python
class Worker:

cacilda = Worker("Cacilda Uanela", 70000)
sheuzia = Worker("Sheuzia Daleula", 90000)

cacilda.lastName()
sheuzia.giveRaise(.10)
cacilda.pay
```

- There object and there are object-oriented (where we need classes)

## 5. Chapter - Numbers and Expressions

### Numeric Literals

- integeres, floating-point, octal, hex, binary literals
- `Decimal('1.5')`, Fraction(19, 2)

### Built-in Numeric Tools

#### Expression operators

- `+, -, *, /, >>, **, &, %` and many more

#### Built-in mathematical functions

- `pow, abs, round, int, hex, bin` and more
- `abs` -> return absolute value
- `bin` -> makes an binary conversion

#### Utility modules

- `random, math, statistics` and more

### Python Expression Operators

- `yield x`, `yield from x` -> generator function send protocol, in iterable for example.
- `x := y` -> walrus operator, allows assign to x and return x as expression at the same time

```python
for (line := file.read())
     print(line)
```

- `square = lambda x: x ** 2` -> lambda expressions (kind of arrow inline function in JS) in JS it `square = x => x ** 2`
- `x if y else z` -> ternary selection (only x if y else z)
- `x and y`
- `x or y`
- `not x`
- `x in y`, `not in y` -> if x is in y
- `x is y`, `is not y` -> read it again
- `x < y`, `x <= y`, `x > y`, `x >= y`
- `x == y`, `x != y`
- `x | y`
- `x ^ y`
- `x & y`
- `x << y`, `x >> y` -> bitwise left shift (binaries bro)
- `x + y`, `x - y`
- `x * y`, `x % y`
- `x / y`, `x // y`, `x @ y` -> divsion, floor division, matrix multiplication (unsed)
- `-x`, `+x` (does nothing), `~x` -> negation, identity, bitwise not (inversion) (~x is x = -(x + 1))
- `x ** y` -> power
- `await fun`
- `x[i]`
- `x[i:j:k]` -> slicing
- `x(...)` -> call
- `x.attr` -> get
- `(...)` -> tuple, expression, generator expression
- `{...}` -> dict, set, dict and set comprehensions
