# Part 1

## Gotchas

- `print("Spam" * 8)` -> this code does what u r not thinking, it will print Span 8 times, is know as string repetition
- `import os` `os.getcwd()` -> the the CWD
- `for x in "spam":` -> will loop through spam
- `import sys` `sys.platform` -> gets the current OS platform (in macOS I got darwin)
- `#!` -> not python specific I just learned the name it's "Hash Bang", it's for scripts
- You can import local module through `import file.path`
- Use `input()` as `cin` in cpp (I wrote cpp because is something I am studying right now also)
- `from imp import reload` will help reload modules, it will reload him himself and not what it imports.
- is like JS, importing a module means executing it
- `dir(local_module_name)` -> helps getting variables from an module
- Each module is a self contained namespace
- `exec(open('script.py').read())` -> reads the script.py and executes it
- `IDLE` -> Integrated Development and Learning Environment
- `pdb.run('code')` -> Helps debugging, can also be `python3 -m pdb file.py`
