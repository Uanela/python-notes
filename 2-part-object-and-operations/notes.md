# Object and Operations

## 4.Chap - Introducing Python Objects

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

### Lists
