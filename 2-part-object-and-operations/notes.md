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
- `name.isdigit()`
- `name.removeprefix()`
- `name.removesuffix()`
- `name.swapcase()`
- `name.isupper()`
- `name.isalpha()` -> Content tests: isdigit also
- `name.rstrip()` -> strip whitespaces in the right side, probably there is `lstrip`
- This one belows is how we call use string template literals (Not sure if name is same as in JS)
- `"""this is multiline string"""`
- `b'h\xc4ck''` -> byte strings
- `r"C:\new\test.bin"` -> raw strings
- `f"string {kind}"`

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
- `L.append()` -> adds a single item to the end
- `L.pop(2)` -> Deletes the item with index 2
- `del L[2]` -> also works as prev
- `L.sort()` -> can take named args just like `L.sort(key=str.lower)` normalizing to lowercase for comparison sorting. `reverse=True`
- `L.reverse()`
- `L.join()`
- `L.copy()`
- `L.clear()`
- `L.extend([])` -> appends as many in the end
- `L.remove(x)` -> remove x value
- `L.count(x)` -> occurencies of x
- `del L[i]`
- `L = [1, 2, 3]`, `L[1:2] = [4, 5]`, `[1, 4, 5, 3]` -> this is crazy
- `*L` -> finally unpacking just like the boss JS
- `sorted(L, reverse=True)`

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
- `dict(zip(['name', 'last'], ['Uanela', 'Como']))` -> Zipping, zip works like `zip(keyslist, valueslist)`
- `zip([], [])` -> Makes key value pairs, array 1 are keys and the second are value
- `'e' in dog` -> boolean
- `if not 'e' in dog:` -> cool inverse check of prev
- `dog.get('job', 'default dog job')` -> same as `dog['a']` with a default if missing
- `dog['height'] if 'e' in dog else 0` -> if/else ternary expression form
- `dog.keys()` -> returns iterable of dog keys this exactlly `dict_keys([])` if you need a list do `list(dog.keys())`
- `list(dog.keys())` -> returns iterable of dog key
- `dog.values()` -> returns iterable of dog values, same as keys behavior that needs list in order to get a real list
- `list(dog.items())` -> tuple of key/value pairs, same applies as keys needs list wrapper to bet a proper list of items
- `iter(dog.keys())` -> Get an iterator from an iterable
- `D = dict(['name', 'Bod'], ('age', 40))` -> looks like `zip` but not, each tuple represents a pair of key/value
- **Item Iteration**:

```python
for key in dog.keys():
    print(key, dog[key])

for key in dog:
    print(key, dog[key])

for (key, value) in dog.items(): # key/value-pair tuples iteration
    print(key, value)
```

- `D.setdefault(key, default?)` -> dynamically sets the key
- `D.pop(key, default?)` -> if no key, and no default then error
- `D.update(D2)` -> merge by keys, works kind like deepmerge (not sure of high depth)
- `D.clear()` -> remove all items
- `len(D)` -> lenght of items
- `D1 == D2` -> equality only
- `**D` -> unpacking bro
- `dict(key=value)` -> basically can take named arguments
- `dict.fromkeys(keyslist, value)`
- `dict(a=1, b=2) | D` -> the values of D will win
- `D = { k: v for (k, v) in zip(['a', 'b', 'c'], [1, 2, 3]) }` -> been loving this inline sytanx (still weird though)
- `|`-> union operator for dicts, basically will unite all of dicts and right most wins
- `&`-> intersection operator for dics, will only get you what both have in common

### Tuples

- This are basically `Lists` with less methods, the diff is that they immutable
- `T = (1, 2, 4, 4)`
- `T = 1, 2, 4, 4` -> yes without parantheses works
- `T = tuple("hack")`
- `a, b, c = 1, 2, 3`
- `T + (5, 6)` -> concatenates
- `T[2]` -> indexing
- `T[1:]` -> slicing
- `T.index(4)` -> get index of 4
- `T.count(4)` -> how many 4 we've
- You can just create a new tuple
- `T = 'hack', 3.0, [11, 22, 33]` -> yes it creates a tuple
- namedtuples

```python
from collections import namedtuple

Rec = namedtuple("Rec", ['name', 'age', 'jobs'])
pat = Rec('Pat', age=40.5, jobs["dev", "mgr"])

print(pat.name)
```

### Files

- `file = open("file.txt", "w")` -> open a new file in text-output mode, then `file.write("content")` finally `file.close()`
- `file = open("data.tx")` -> withou "w" opens exsting file in text-input mode, then `text = file.read()`
- `for line in open("data.txt"):` -> displays lines in a file
- `file.read()` -> read it to a string
- `open(path, 'w').write(content)` -> write the file
- `open(path, 'w').close()`
- `file.read(N)` -> read up until N line
- `output.flush()` -> flush output buffer to disk without closing
- `anyFile.seek(N)` -> change file position to offset N for next operation, iterator for example
- `file.readlines()` -> read entire file into a list of line strings
- get cwd

```python
import os

print(os.getcwd())
print(os.listdir()) # list cwd()
print(os.listdir('some/path/to/dir'))
```

- `file.readline()` -> read one line and keeps goind each time u call it
- Trying pickle

```python
import pickle # used to serialize and deserialize python objects
D = { 'a': 1, 'b': 2 }
F = open('datafile.pkl', 'wb')
pickle.dump(D, F)
F.close()

F = open('datafile.pkl', 'rb')
E = pickle.load(F)
```

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

### Numbers in Action

- REPL - Read-Execute-Print Loop, it is not python spec I just search about it bc was tired of not knowing it.
- Seems like `1.1 + 2.2` jokes about JS is in all languages when you operate with floating numbers
- We've `repr` kind of print but no

### Comparison operators

- `math.isclose(1.1 + 2.2, 3.3)` -> within default-but-passable tolerances
- `int(2.2)`
- `round(2.2)`
- `math.floor(2.2)`
- `math.trunc(-2.2)`

### Complex Number

- They are represented as two floating-point numbers - the real and imaginary parts - and you code them by adding j or J to the imaginary part.

```python
1j * 1j = -1+0j
```

### Hex, Octal and Binary

- `oct()`
- `hex()`
- `bin()`
- `float()`
- `eval()` -> can convert string to number, becaues it treats the code as python code.
- `^` -> the bitwise XOR

### Other Built-in Math Tools

- `math.pi`
- `math.e`
- `math.sin()`
- `math.sqrt()`
- `min()`
- `max()`
- `1_000_000`
- `import statistics`, `statistics.mean([1, 2, 4, 5, 7])` -> returns the avarage
- `statistics.median([1, 2, 4, 5, 7])` -> the middle
- `random.random()`
- `random.choice()`
- `random.shuffle()`

### Other Number Objects

- `from decimal import Decimal`, `Decimal('1.5')`
- `decimal.getcontext().prec = 4` -> setup a fixed precision of 4
- `Fraction`

### Sets in Action

- `S = { 1.23 }`
- `S.add([ 1, 2, 3 ])`
- `S.remove([ 1, 2, 3 ])`
- `S.update([ 1, 2, 3 ])`

# 6.Chapter - The Dynamic Typing Interlude

- `L2 = L1[:]` -> Make a copy of L1 into L2, there is L1.copy() also
- `import copy`, `copy.deepcopy(Y)` -> deep copy an object
- `a: int = 2`
- `a: list[int] = [ 2, 3, 4 ]`
- Type hints in functions

```python
def func(a: int, b: list[str]) -> float:
    return 'anything' + 2 + b
```

## Strings

- `s[1:10:2]` -> the last 2 means skipping items

### Character-code conversions

- `ord('h')` -> to its int code
- `chr(104)` -> to its character

### String Methods

- Most are just noted before

#### Formatting Expression Custom Formats

This is kind of a C thing, so you can dive deep if you want, we can do things like:

```python
'%e | %f | %g' % (x, x, x)
```

All of them will be printed differently because of the letters modifiers like:

- `f` - floating point decimal
- `o` - octal integer (base 8)
- `x` - x integer (base 16)
- `d` - decimal (base 10)

## 8. Chapter - Lists and Dictionaries

### Lists

We've covered this before probably I will mostly skim around here, just added the new notes also on the section above so go there and find it bro.

### Dictionaries

The famous hashmap (hope I ain't getting it wrong) or even object without Class in JS. probably you will find most the things on the sections above I've read about this before

- Catch key missing erros

```python
try:
    print(Matrix[(2, 3, 6)]) # Yes we can use tuples as dict keys
except KeyError:
    print(0)
```

### Gotchas

- learned shortly that we can have `;` to separte statements
- `sorted(any_iterable)` which means `dict_keys('name', 'age')` can go without `list` wrapper

### Tuples

I just put all up there

### Files

I am doing the same putting all up there
