### create a matrix of identical
``` python
mat_zeros = [[0] * col_count] for _ in row_count]
mat_falses = [[False for _ in col_count] for _ in row_count]
```

### loop through a list getting the item and its index
``` python
for i, item in enumerate(items):
    print(f'index: {i}')
    print(f'item: {item}')
```

### convert a csv line of ints into a list of ints
``` python
nums = [int(num) for num in open(file_name).read().strip().split(',')]
```

### increment a dictionary entry by 1 or set it to 1 if new
``` python
this_dict[key] = this_dict.get(key, 0) + 1
```

### split a string into a list of tuples of (letter, count) ordered by count desc for x most common letters
``` python
letter_counts = collections.Counter(polymer).most_common(x)
```