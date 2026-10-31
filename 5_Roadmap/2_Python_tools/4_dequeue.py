from collections import deque

# numbers = deque([10, 20, 30, 40])
# print(numbers)

# numbers.append(5)
# numbers.appendleft(10)
# print(numbers)


# numbers.pop(0)
# numbers.popleft()
# print(numbers)

listn = [10, 20, 30, 40]
listn.pop(0)
print(listn)

#code 2
queue = deque([1, 2, 3, 4, 5])
listnew = []

while queue:
    current = queue.popleft()
    listnew.append(current)
    print(current)
print(listnew)


# code 4 using defaultdict
from collections import deque, defaultdict

queue = deque([1, 2, 3, 4, 5])

removed = defaultdict(list)

while queue:
    current = queue.popleft()
    removed["numbers"].append(current)

print(removed["numbers"])


"""
Good question! The reason is that `defaultdict` stores values using keys, just like a normal dictionary.

Let's understand it.

### 1. We created this:

```
removed = defaultdict(list)
```

This creates an empty dictionary.

Initially:

```
{}
```

### 2. Now look at this:

```
removed["numbers"].append(current)
```

Why `"numbers"`?

Because `"numbers"` is the key under which we want to store our removed elements.

When Python sees:

```
removed["numbers"]
```

It checks whether the `"numbers"` key exists.

- If it exists, Python accesses its list.
- If it doesn't exist, `defaultdict(list)` automatically creates an empty list for it.

So it becomes:

```
{    "numbers": []}
```

### 3. Now append(current)

Suppose `current = 1`.

```
removed["numbers"].append(current)
```

Now the dictionary becomes:

```
{    "numbers": [1]}
```

If the next `current = 2`, it becomes:

```
{    "numbers": [1, 2]}
```

### 4. Can we use another key?

Absolutely!

```
removed["numbers"].append(1)removed["ages"].append(21)removed["marks"].append(90)print(removed)
```

Output:

```
{    'numbers': [1],    'ages': [21],    'marks': [90]}
```

### Remember this:

- `removed` → Dictionary.
- `"numbers"` → Key.
- `removed["numbers"]` → List associated with that key.
- `.append(current)` → Adds an element to that list.

One important point: We used `"numbers"` simply because we wanted to store our removed numbers under that key. We could have called it `"data"`, `"items"` or anything else."""