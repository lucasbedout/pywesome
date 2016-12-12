# Pywesome

Python lists on steroids.

**Table of Contents**

- [Getting started](#)
- [The wrapper](#)
- [Wrapper specific methods](#)
	- [count](#)
	- [append](#)
	- [prepend](#)
	- [pop](#)
	- [to_list](#)
	- [to_json](#)
- [Pywesome methods](#)
	- [map](#)
	- [reduce](#)
	- [filter](#)
	- [reject](#)
	- [contains](#)
	- [search](#)
	- [random](#)
	- [only](#)
	- [chunk](#)
	- [merge](#)
	- [collapse](#)
	- [sort](#)
	- [sort_by](#)
	- [first](#)
	- [last](#)
	- [get](#)
	- [sum](#)
	- [avg](#)
	- [join](#)

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

The pywesome library will always return a new list and never update the current one. The wrapper works the same way, but it always returns a new pywesome object (except for the methods is the next section).


## Wrapper specific methods

The output of the function (after the # in the code examples) is not the real output but is easier to read, to get the list you can use the method `to_list()`.

You can't chain these methods (as they return void or a specific element)

###count()

Returns the number of elements in the collection

```python
collection = collect([1, 2, 3, 4]) 

collection.count() # 4
```

###append(*item*)

Add an element at the end of the collection

```python
collection = collect([1, 2, 3, 4]) 

collection.append(5) # [1, 2, 3, 4, 5]

```

###prepend(*item*)

Add an element at the beginning of the collection

```python
collection = collect([1, 2, 3, 4]) 

collection.prepend(0) # [0, 1, 2, 3, 4]

```

###pop(*key=None*)

Remove an element by key, if no key is provided, it removes the last element. The method returns the removed element

```python
collection = collect([1, 2, 3, 4]) 

collection.pop(2) # [1, 2, 4, 5], returns 3

collection.pop() # [1, 2, 4], returns 5

```


###to_list()

Return the collection as a list

```python
# This is an example and has absolutely no interest
collection = collect([1, 2, 3, 4]) 

collection.to_list() # [1, 2, 3, 4]

```

###to_json()

Return the collection as json

```python
# This is an example and has absolutely no interest
collection = collect([{'id': 1}, {'id': 2}, {'id': 3}]) 

collection.to_json() # [{"id": 1}, {"id": 2}, {"id": 3}]

```


## Pywesome methods

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


###map(`function`)

Creates a new collection by applying *function* on all elements and returns it. 

The function takes 1 parameter which is the current element.

```python
collection = collect([1, 2, 3, 4]) 

collection.map(lambda el: el + 1) # [2, 3, 4, 5]
```

###reduce(`function`, `carry=None`)

Returns one element by applying a function on all elements. 

The function takes 2 parameters, the previously generated object and the current element. 

You can pass an optional parameter carry to initialize the generated object.

```python
collection = collect([1, 2, 3, 4]) 

collection.reduce(lambda carry, el: carry + el) # 10

collection.reduce(lambda carry, el: carry + el, 10) # 20
```

If you want to return a dict or a list, you need to initialize `carry` to `{}` or `[]`

###filter(`function`)

Filter the collection based on the result of `function`, the current element is added only if `function(element)` is True.


```python
collection = collect([1, 2, 3, 4]) 

collection.filter(lambda n: n < 3) # [1, 2]
```

###reject(`function`)

Reject is the opposite of filter, the current element is added only if `function(element)` is False.


```python
collection = collect([1, 2, 3, 4]) 

collection.reject(lambda n: n < 3) # [3, 4]
```


###contains(`haystack`, `needle`)

Returns `True` if the collections contains `needle`. 

```python
collection = collect([1, 2, 3, 4]) 

collection.contains(3) # True
collection.contains(12) # False
```

You can also pass a `function` as the needle. It takes the element as only parameter and must return True or False.


```python
collection = collect([1, 2, 3, 4]) 

collection.contains(lambda el: el < 4) # True
collection.contains(lambda el: isinstance(el, str)) # False
```

###search(`haystack`, `needle`)

Same as contains but returns the index of the first matching element. 

You can pass a value or a function as `needle`.

```python
collection = collect([1, 2, 3, 4]) 

collection.search(3) # 2
collection.search(12) # False

```

###random(`offset=1`)

Returns `offset` random values from the collection


```python
collection = collect([1, 2, 3, 4]) 

collection.random() # 2
collection.random() # 4

collection.random(2) # [2, 3]

```

###only(`property`)

Returns a collection filled with only the `property` value for each element of the current collection.

The collection needs to contain iterable objects (dicts, etc..)

```python
collection = collect([{'id': 1, 'name': 'Name'}, {'id': 2, 'name': 'Name', 'prop': 'value'}])

collection.only('id') # [1, 2]

```


###chunk(`parts`)

Split the collections in `parts` chunks.

```python
collection = collect([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

collection.chunk(3) # [[0, 1, 2], [3, 4, 5], [6, 7, 8], [9, 10]]

collection.chunk(-10) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

```

###merge(`col1`, `col2`, `col3`, `...`)

Merge all the collections passed as parameters,


```python
col1 = collect([1, 2, 3, 4]) 
col2 = collect([4, 5, 6, 7]) 


col1.merge(col2) # [1, 2, 3, 4, 4, 5, 6, 7]
```

Hint: Using the `pywesome` syntax

```python
col1 = [1, 2, 3, 4]
col2 = [4, 5, 6, 7] 


pywesome.merge(col1, col2)
```

###collapse(collections)

Split the collections in `parts` chunks.

```python
collection = collect([[0, 1, 2, 3], [4, 5, 6], [7, 8, 9]])

collection.collapse() # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
```

Hint: Using the `pywesome` syntax

```python
collection = [[0, 1, 2, 3], [4, 5, 6], [7, 8, 9]]
pywesome.collapse(collection) #  [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
```

###sort(`desc=False`)

Sort the collection.

Default order is ascendant, set desc to `True` if you want to reverse.


```python
collection = collect([2, 1, 2, 5, 5]) 

collection.sort() # [1, 2, 2, 5, 5]

collection.sort(desc=True) # [5, 5, 2, 2, 1]
```


###sort_by(`prop`, `desc=False`)

Sort the collection by property. The collection must be a collection of dict-like objects.

Default order is ascendant, set desc to `True` if you want to reverse.


```python
collection = collect([{'id': 4, 'name': 'Name'}, {'id': 32, 'name': 'Name', 'prop': 'value'},{'id': 24, 'name': 'Name', 'prop': 'value'}])) 

# Use only for readability
collection.sort_by('id').only('id') # [4, 24, 32]

collection.sort_by('id', desc=True).only('id') # [32, 24, 4]
```

###where(`prop`, `value`)

Same as a SQL where, a simple `filter` shorthand.

```python
collection = collect([{'id': 4, 'name': 'Name'}, {'id': 32, 'name': 'Name'},{'id': 24, 'name': 'Name'}])) 

collection.where('id', 4) # [{'id': 4, 'name': 'Name'}]
```

###where_in(`prop`, `values`)

Same as a SQL where ... between, another `filter` shorthand.

```python
collection = collect([{'id': 1, 'name': 'Name'}, {'id': 2, 'name': 'Name'},{'id': 4, 'name': 'Name'}])) 

collection.where_in('id', [1,3]) # [{'id': 1, 'name': 'Name'}, {'id': 2, 'name': 'Name'}]
```

###first()

Returns the first element of the collection


```python
collection = collect([1, 2, 3, 4]) 

collection.first() # 1

```

###last()

Returns the last element of the collection


```python
collection = collect([1, 2, 3, 4]) 

collection.last() # 4

```

###get(`index`)

Returns element at `index` in the collection.


```python
collection = collect([1, 2, 3, 4]) 

collection.get(2) # 3

```

###sum(`prop=None`)

Sums the collection (numbers only). If you have a collection of dict-like objects, you can pass `prop`.


```python
collection = collect([1, 2, 3, 4]) 

collection.sum() # 10

collection = collect([{'id': 1, 'name': 'Name'}, {'id': 2, 'name': 'Name', 'prop': 'value'}])

collection.sum('id') # 3

```

###avg()

Returns the average of the collection. As in sum, you can pass `prop` if you have a collection of dict-like objects.


```python
collection = collect([1, 2, 3, 4]) 

collection.avg() # 2.5

collection = collect([{'id': 1, 'name': 'Name'}, {'id': 2, 'name': 'Name', 'prop': 'value'}])

collection.avg('id') # 1.5
```

###join(`char=','`)

Join the collection elements into a string, separated by `char`.


```python
collection = collect([1, 2, 3, 4]) 

collection.join() # '1,2,3,4'

collection.join('') # '1234'

```






