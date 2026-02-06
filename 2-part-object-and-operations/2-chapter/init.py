def classic_fn(n):
  result = []
  for i in range(n):
    result.append(i * 2)
  return result

def gen_fn(n):
  for i in range(n):
    yield i * 2 # yields value one by one and make
    # it available to operate

for val in gen_fn(10):
  print(val)
