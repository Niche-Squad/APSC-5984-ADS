# APSC-5984 Lab 3: Python Basics II

Due: 2023-02-06 (Monday) 23:59:59

- [APSC-5984 Lab 3: Python Basics II](#apsc-5984-lab-3-python-basics-ii)
  - [0. Overview](#0-overview)
  - [1. Lists](#1-lists)
    - [1.1 Assign values to a list](#11-assign-values-to-a-list)
    - [1.2 Accessing elements in a list](#12-accessing-elements-in-a-list)
  - [2. Dictionaries](#2-dictionaries)
    - [2.1 Creating a dictionary](#21-creating-a-dictionary)
    - [2.2 Accessing elements in a dictionary](#22-accessing-elements-in-a-dictionary)
  - [3. Loops](#3-loops)
    - [3.1 `for` loops](#31-for-loops)
    - [3.2 `while` loops](#32-while-loops)
    - [3.3 `break` and `continue`](#33-break-and-continue)

## 0. Overview

In this lab, you will learn more Python syntax. We will cover the essential concepts of Python:

- Lists

- Dictionaries

- Control structures: `For` loops and `while` loops

As usual, you will need to open the `labs/lab_03/assignment.ipynb` file in VS Code and follow the instruction to complete this lab assignment.

([Back to top](#apsc-5984-lab-3-python-basics-ii))

## 1. Lists

### 1.1 Assign values to a list

A list is a collection of items in a particular order. You can make a list that includes variables, numbers, or strings. For example, you can make a list that includes the letters [a, b, c, d, e]:

```Python
letters = ['a', 'b', 'c', 'd', 'e']
print(letters) # ['a', 'b', 'c', 'd', 'e']
```

Same rules apply to numbers:

```Python
numbers = [1, 2, 3, 4, 5]
print(numbers) # [1, 2, 3, 4, 5]
```

You can also make a list that includes both strings and numbers:

```Python
mixed = ['a', 1, 'b', 2, 'c', 3]
print(mixed) # ['a', 1, 'b', 2, 'c', 3]
```

You might notice that there is a case where certain items in a list are related to each other. For example, you might want to store the name and age of a person in a list. In this case, you can use a nested list:

```Python
person_age_1 = ['John', 20]
person_age_2 = ['Mary', 25]
person_age_3 = ['Michael', 30]
nested_list = [person_age_1, person_age_2, person_age_3]
print(nested_list) # [['John', 20], ['Mary', 25], ['Michael', 30]]
```

Append a new element to a list is easy. We can add a new person to the list `nested_list` by using the `append` method:

```Python
nested_list.append(['Elizabeth', 35])
print(nested_list) # [['John', 20], ['Mary', 25], ['Michael', 30], ['Elizabeth', 35]]
```

### 1.2 Accessing elements in a list

You can access elements in a list by using the index (i.e., the position) of the element. In Python, the index of a list starts from 0, which means the first element in a list has index 0, the second element has index 1, and so on. For example, you can access the first element in the list `letters` by using `letters[0]`:

```Python
letters = ['a', 'b', 'c', 'd', 'e']
print(letters[0]) # a
```

The third element in the list `nested_list` can be accessed by using `nested_list[2]`:

```Python
nested_list = [['John', 20], ['Mary', 25], ['Michael', 30]]
print(nested_list[2]) # ['Michael', 30]
```

In addition, indexing can be concatenated. Following the same list `nested_list`, if you want to obtain the age of the third person in the list `nested_list`, you can do `nested_list[2][1]`:

```Python
mike_age = nested_list[2][1]
print(mike_age) # 30
```

What if you want to access the last element in a list? You can use negative index to access the last element in a list. For example, you can access the last element in the list `letters` by using `letters[-1]`:

```Python
letters = ['a', 'b', 'c', 'd', 'e']
print(letters[-1]) # e
```

Alright, now you know how to access elements in a list. What if you want to access a range of elements in a list? You can use the `:` operator to access a range of elements in a list. For example, you can access the first three elements in the list `letters` by using `letters[0:3]`:

```Python
letters = ['a', 'b', 'c', 'd', 'e']
print(letters[0:3]) # ['a', 'b', 'c']
```

It is noted that the number after the `:` operator is not included in the range. In the above example, the number 3 is not included in the range. If you want to access the first four elements (i.e., 0, 1, 2, and 3) in the list `letters`, you can use `letters[0:4]`:

```Python
letters = ['a', 'b', 'c', 'd', 'e']
print(letters[0:4]) # ['a', 'b', 'c', 'd']
```

If you have a long list and you do not want to specify the end index, you can use `letters[3:]` to access the elements from the fourth element to the last element:

```Python
letters = ['a', 'b', 'c', 'd', 'e']
print(letters[3:]) # ['d', 'e']
```

Same rules apply to negative index. If you want to access the last three elements in the list `letters`, you can use `letters[-3:]`:

```Python
letters = ['a', 'b', 'c', 'd', 'e']
print(letters[-3:]) # ['c', 'd', 'e']
```

You can mix the positive index and negative index. For example, you can access elements from the second position to the last second position in the list `letters` by using `letters[1:-1]`:

```Python
letters = ['a', 'b', 'c', 'd', 'e']
print(letters[1:-1]) # ['b', 'c', 'd']
```

([Back to top](#apsc-5984-lab-3-python-basics-ii))

## 2. Dictionaries

### 2.1 Creating a dictionary

A dictionary is a collection of key-value pairs. Unlike a list, where items are accessed by their position, items in a dictionary are accessed via keys. A key's value can be a number, a string, a list, or even another dictionary. In Python, a dictionary is defined by curly brackets `{}`. Here is an example:

```Python
person_age = {'John': 20, 'Mary': 25, 'Michael': 30, 'Elizabeth': 35}
print(person_age) # {'John': 20, 'Mary': 25, 'Michael': 30, 'Elizabeth': 35}
```

In this case, the keys are `John`, `Mary`, `Michael`, and `Elizabeth`, and the values are 20, 25, 30, and 35, respectively. To add a new key-value pair to a dictionary, you have two options. First, you can use the `update` method. For example, you can add a new key-value pair to the dictionary `person_age` by using `person_age.update({'David': 40})`:

```Python
person_age.update({'David': 40})
print(person_age) # {'John': 20, 'Mary': 25, 'Michael': 30, 'Elizabeth': 35, 'David': 40}
```

Second, you can use the `[]` operator. For example, you can add a new key-value pair to the dictionary `person_age` by using `person_age['David'] = 40`:

```Python
person_age['David'] = 40
print(person_age) # {'John': 20, 'Mary': 25, 'Michael': 30, 'Elizabeth': 35, 'David': 40}
```

You can also use integers as keys:

```Python
dict_int = {3: "three", 10: "ten", 2: "two"}
print(dict_int) # {3: 'three', 10: 'ten', 2: 'two'}
```

### 2.2 Accessing elements in a dictionary

You can access the value of a key by using the key name. For example, you can access the age of John by using `person_age['John']` or `person_age.get('John')`:

```Python
john_age = person_age['John']
print(john_age) # 20\
john_age = person_age.get('John')
print(john_age) # 20
```

What if you want to access to the value of the last key in a dictionary? Although you cannot use negative index like you did in a list, you can still access the value in a dictionary. You can use the `keys()` method to get a list of keys in a dictionary, and this function should return a list of keys. With this list, you can access the last key in the dictionary and get the value of the last key. Here is an example:

```Python
# step 1: get a list of keys in a dictionary
keys = person_age.keys()
print(keys) # dict_keys(['John', 'Mary', 'Michael', 'Elizabeth', 'David'])

# step 2: access the last key in the dictionary
last_key = list(keys)[-1]
print(last_key) # David

# step 3: access the value of the last key
last_value = person_age[last_key]
print(last_value) # 40
```

On the other hand, you can use the `values()` method to get a list of values in a dictionary. For example, you can get a list of ages in the dictionary `person_age` by using `person_age.values()`:

```Python
values = person_age.values()
print(values) # dict_values([20, 25, 30, 35, 40])
```

It is also possible to query whether a key exists in a dictionary. You can use the `in` operator to check whether a key exists in a dictionary. For example, you can check whether the key `David` exists in the dictionary `person_age` by using `if 'David' in person_age:`:

```Python
if 'David' in person_age:
    print("David exists in the dictionary person_age")
else:
    print("David does not exist in the dictionary person_age")
```

([Back to top](#apsc-5984-lab-3-python-basics-ii))

## 3. Loops

It is quite a hassle to repeatly access elements in a list or a dictionary. In this section, we will introduce how to use `for` loops and `while` loops in Python. These two types of loops are very useful to interact with these data structures.

### 3.1 `for` loops

A `for` loop is used to iterate over a sequence (e.g., a list, a dictionary, or a string). There are two components in a `for` statement: `variable` and `iterators`. Let's take a look at an example:

```Python
for i in [0, 1, 2]:
    print(i)
# 0
# 1
# 2
```

In this example, `i` is the variable, and `[0, 1, 2]`, a list, is the iterator. The `for` loop will iterate over the iterator and assign the value of each element to the variable. In this case, the value of `i` will be 0, 1, and 2, respectively. After the value of `i` is assigned, the code block `print(i)` will be executed. The variable name can be anything you want. Conventionally, we use `i` as the variable name.

In Python, `range(3)` is a built-in function that returns a list of integers from 0 to 2. You can use `range(3)` to replace `[0, 1, 2]` in the above example:

```Python
for i in range(3):
    print(i)
# 0
# 1
# 2
```

As we mentioned above, the iterators can be a list, a dictionary. Let's see what happens if we use the dictionary `person_age` as the iterator:

```Python
for i in person_age:
    print(i)
# John
# Mary
# Michael
# Elizabeth
# David
```

You would see that the variable `i` is assigned to the keys (not the values) in the dictionary `person_age`. In this case, the variable `i` is assigned to `John`, `Mary`, `Michael`, `Elizabeth`, and `David`, respectively. If you want to access the values in the dictionary `person_age`, you can use the `[]` operator:

```Python
for key in person_age:
    print(person_age[key])
# 20
# 25
# 30
# 35
# 40
```

The above example is equivalent to the following example:

```Python
print(person_age['John'])
print(person_age['Mary'])
print(person_age['Michael'])
print(person_age['Elizabeth'])
print(person_age['David'])
# 20
# 25
# 30
# 35
# 40
```

There is a handy alternative to get both the keys and values in a dictionary is to use the `items()` method:

```Python
for key, value in person_age.items():
    print(key, value)
# John 20
# Mary 25
# Michael 30
# Elizabeth 35
# David 40
```

### 3.2 `while` loops

A `while` loop is used to repeat a block of code until a condition is met. Again, let's take a look at an example:

```Python
i = 0
while i < 3:
    print(i)
    i = i + 1
# 0
# 1
# 2
```

In this example, The value of `i` was assigned to 0 before the loop starts. And the `while` loop will check the condition `i < 3` before each iteration. If the condition is met, the code block will be executed. Otherwise, the `while` loop will be terminated. In each iteration, the value of `i` will be increased by 1. After the value of `i` is increased, the condition `i < 3` will be checked again. If the condition is met, the iteration will continue.

The above example is equivalent to the following code:

```Python
i = 0
if i < 3:
    print(i)
    i = i + 1
    if i < 3:
        print(i)
        i = i + 1
        if i < 3:
            print(i)
            i = i + 1
            # ... and so on
        else:
            pass
    else:
        pass
else:
    pass
```

A quick summary: In practice, there is no strict rule to decide whether to use `for` loops or `while` loops. If you need to iterate over a sequence, a `for` loop is usually the better choice. If you need to repeat a block of code until a condition is met, a while `loop` could.

### 3.3 `break` and `continue`

In the above cases, the `for` loop and `while` loop will iterate over the entire sequence or continue to execute the code block until the condition is met. However, there are cases that you want to stop the iteration or skip the current iteration. In this case, you can use the `break` and `continue` statements.

The `break` statement is used to stop the iteration. For example, you can use `break` to stop the iteration when the value of `i` is 2:

```Python
for i in range(5):
    if i == 2:
        break
    print(i)
# 0
# 1
```

When `i` is 2, the `break` statement will stop the iteration and the code block `print(i)` will not be executed. It is noted that once the `break` statement is executed, the `for` loop will be terminated immediately; the value of `i` will not be printed.

The `continue` statement is used to skip the current iteration. For example, you can use `continue` to skip the iteration when the value of `i` is 2:

```Python
for i in range(5):
    if i == 2:
        continue
    print(i)
# 0
# 1
# 3
# 4
```

When `i` is 2, the `continue` statement will skip the current iteration and the code block `print(i)` will not be executed. The value of `i` will be increased by 1 and the condition `i < 5` will be checked again. If the condition is met, the iteration will continue.

([Back to top](#apsc-5984-lab-3-python-basics-ii))