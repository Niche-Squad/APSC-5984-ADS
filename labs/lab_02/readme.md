# APSC-5984 Lab 2: Python Basics I

Due: 2023-01-30 (Monday) 23:59:59

## 0. Overview

In this lab, you will learn basic Python syntax. You will need to open the `lab_02/main.ipynb` file in VS Code and follow the instruction to complete this lab assignment.

## 1. Variables

There are several rules for naming variables in Python:

- A variable name can only contain letters (`A-Za-z`), numbers(`0-9`), and underscores(`_`).
- A variable name is case sensitive. For example, `first_var` and `First_var` are two different variables.
- There are two ways to name a variable: `snake_case` and `camelCase`. In `snake_case`, all letters are lowercase and words are separated by underscores. In `camelCase`, the first letter of each word is capitalized. For example, `first_var` and `firstVar` are both valid variable names.

Things you cannot do:

- A variable name cannot start with a number.
- A variable name cannot contain spaces.

Examples:

- Valid variable names: `first_var`, `firstVar`, `first_var_1`, `firstVar1`, `first_var_1_2_3`, `firstVar123`
- Invalid variable names: `1st_var`, `first var`, `first-var`

In Python, you can use `=` to assign a value to a variable. For example, you can assign an integer value `3` to a variable `first_var` by running the following code:

```Python
first_var = 3
```

And we can print the value of `first_var` by running the following code:

```Python
print(first_var) # 3
```

## 2. Data Types

There are several data types in Python:

- `int`: an integer number, e.g., `3`, `0`, `-1`
- `float`: a floating point number, e.g., `3.14`, `0.0`, `-1.0`
- `bool`: a boolean value, e.g., `True`, `False`
- `str`: a string, e.g., `"hello"`, `"2023-01-30"`

```Python
var_int = 3
var_float = 3.14
var_bool = True
var_str = "hello"
```

You can use `type()` function to check the type of a variable. For example, you can check the type of `a` by running the following code:

```Python
print(type(var_float)) # <class 'float'>
```

It is possible to convert a variable from one type to another. For example, you can convert a `float` to an `int` by running the following code:

From `float` to `int`:

```Python
var_float = 3.14
var_int = int(var_float)
print(var_int) # 3
```

From `int` to `string`:

```Python
var_int = 3
var_str = str(var_int)
print(var_str) # "3"
```