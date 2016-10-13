# Pywesome

Python lists on steroids.

## Getting started

You can install pywesome using pip

```
pip install git+https://github.com/lucasbedout/pywesome.git#egg=pywesome
```

That's it, you can use it

```python
from pywesome import pywesome

pywesome.filter([1, 2, 3], lambda n: n < 3) # [1, 2]
```

## The wrapper

Pywesome can be used with two different syntaxes, the one above (maybe the more pythonic), and with the **wrapper**.

The wrapper is a class wrapping pywesome library, it allows you to write something like this 

```python
from pywesome.wrapper import collect

collection = collect([80,121,119,101,115,111,109,101]) 

collection.count() # 8

collection.map(lambda n: chr(n)).reduce(lambda w, l: w + l) # 'Pywesome'

```
 
The choice is yours, all pywesome functions are available in the wrapper. 

The pywesome library will always return a new list and never update the current one. The wrapper works the same way, but it always return a new pywesome object (except for the methods is the next section).


### Wrapper specific methods

The output of the function (after the # in the code examples) is not the real output but is easier to read, to get the list you can use the method `to_list()`.

You can't chain these methods (as they return void or a specific element)

**count()**

Returns the number of elements in the collection

```python
collection = collect([1, 2, 3, 4]) 

collection.count() # 4
```

**append(*item*)**

Add an element at the end of the collection

```python
collection = collect([1, 2, 3, 4]) 

collection.append(5) # [1, 2, 3, 4, 5]

```

**prepend(*item*)**

Add an element at the end of the collection

```python
collection = collect([1, 2, 3, 4]) 

collection.prepend(0) # [0, 1, 2, 3, 4]

```

**pop(*key=None*)**

Remove an element by key, if no key is provided, it removes the last element. The method returns the removed element

```python
collection = collect([1, 2, 3, 4]) 

collection.pop(2) # [1, 2, 4, 5], returns 3

collection.pop() # [1, 2, 4], returns 5

```


**to_list()**

Return the collection as a list

```python
# This is an example and has absolutely no interest
collection = collect([1, 2, 3, 4]) 

collection.to_list() # [1, 2, 3, 4]

```

**to_json()**

Return the collection as json

```python
# This is an example and has absolutely no interest
collection = collect([{'id': 1}, {'id': 2}, {'id': 3}]) 

collection.to_json() # [{"id": 1}, {"id": 2}, {"id": 3}]

```


### Pywesome methods

We will use the wrapper syntax to describe the methods, but you can easily change the syntax to use the classic notation.

```python
collection = collect([1, 2, 3, 4]) 

collection.map(lambda n: n + 1) 

```

is identical to

```python
from pywesome import pywesome

pywesome.map([1, 2, 3, 4], lambda n: n + 1) 

```

Be careful though, you can chain methods when you use the wrapper, not with the classic notation.