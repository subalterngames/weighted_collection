# Weighted Collection

A WeightedCollection assigns probability weights per elements and returns elements randomly using those weights.

For example: if "anakin" has a weight of 1, "constantine" a weight of 1, and "xenophon" a  weight of 2, then "xenophon" will be randomly selected 50% of the time, "anakin" 25% of the time, and "xenophon" 25% of the time.

## Usage

```python
from weighted_collection.weighted_collection import WeightedCollection

w = WeightedCollection(obj_type=str)

w.add("anakin", 1)
w.add("constantine", 1)
w.add("xenophon", 2)

# 25% of the time, this will return "anakin", 
# 25% of the time "constantine",
# 50% of the time "xenophon".
print(w.get())
```

## Requirements

Python 3.6+

## Installation

```python
pip3 install weighted-collection
```

## WeightedCollection API

#### `WeightedCollection()`

The constructor.

```python
w = WeightedCollection() # Default constructor.
```

```python
w = WeightedCollection(obj_type=str) # All elements in the collection must be strings.
```

```python
w = WeightedCollection(random_seed=0)
```

```python
w = WeightedCollection(obj_type=str, random_seed=0)
```

| Parameter     | Type      | Description                                              | Optional | Default  |
| ------------- | --------- | -------------------------------------------------------- | -------- | -------- |
| `obj_type`    | `Type[T]` | The type of objects that can be added to the collection. |          | `object` |
| `random_seed` | `int`     | The random number generator seed.                        |          | 0        |

***

#### `add(obj, weight)`

Try to add an object to the collection.

- The object's type must be the class or a subclass of the `obj_type` parameter in the constructor.
- The object must not already be in the  collection.
- The weight must be > 0.

_Return: True if the object was added._

```python 
w = WeightedCollection(obj_type=str)

w.add("anakin", 1) # Adds element "anakin" with a weight of 1. Returns True.

w.add("anakin", 3) # Returns False (object is already in the collecction).

w.add(33, 1) # Returns False (wrong type).

w.add("constantine", -2) # Returns False (weight must be > 0).
```

| Parameter | Type                                                         | Description                                                | Optional | Default |
| --------- | ------------------------------------------------------------ | ---------------------------------------------------------- | -------- | ------- |
| `obj`     | `T` (the value of the `obj_type` parameter in the constructor) | The object. Must not already be in the WeightedCollection. |          |         |
| `weight`  | `int`                                                        | The probability weight. Must be > 0.                       |          |         |

***

#### `add_many(objs)`

Try to add many objects to the collection. 

_Return: A dictionary of each object and whether it was added to the collection._

```python
w = WeightedCollection(obj_type=str)

result = w.add_many({"anakin": 1, "constantine": 1, 33: 0, "xenophon": -1})

print(result) # {"anakin": True, "constantine": True, 33: False, "xenophon": False}
```

| Parameter | Type                                                         | Description                                                  | Optional | Default |
| --------- | ------------------------------------------------------------ | ------------------------------------------------------------ | -------- | ------- |
| `objs`    | `Dict[T, int]`<br>(`T` is the value of the `obj_type` parameter in the constructor) | A dictionary of objects. A dictionary of objects. Key = the object. Value = the probability weight.<br><br>See `add(obj, weight)` for object and weight requirements. |          |         |

***

#### `remove(obj)`

Remove an object from the collection.

_Return: True if the object was removed._

```python
w = WeightedCollection(obj_type=str)

w.add("anakin", 1)

w.remove("anakin") # Returns True.
w.remove("constantine") # Returns False.
```

| Parameter | Type                                                         | Description                   | Optional | Default |
| --------- | ------------------------------------------------------------ | ----------------------------- | -------- | ------- |
| `obj`     | `T` (the value of the `obj_type` parameter in the constructor) | The object in the collection. |          |         |

***

#### `get()`

_Return: A randomly selected object using the probability weights per object._

```python
w = WeightedCollection(obj_type=str)

w.add("anakin", 1)
w.add("constantine", 1)
w.add("xenophon", 2)

# 25% of the time, this will return "anakin", 
# 25% of the time "constantine",
# 50% of the time "xenophon".
print(w.get())
```

