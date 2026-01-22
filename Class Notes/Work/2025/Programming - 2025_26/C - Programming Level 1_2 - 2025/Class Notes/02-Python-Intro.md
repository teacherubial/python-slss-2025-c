# Variables, Data, Input and Output

16 September 2025

## Designing Algorithms

> A step-by-step procedure for solving a problem or accomplishing some end.
> Merriam-Webster

An algorithm is like a recipe. If you follow the steps, you should be able to solve the problem.

## Variables 

We use variables to *store* values. 
Variables have two parts: a **name** and a **value**.

Example:
```python
greeting = "Hello. I am a chatbot."
```

`greeting` is the **name**.
`"Hello..."` is the **value**.

### Getting the Type

We can use the `type()` function to get the type of a variable.

`type()` is a function, just like `print()` is a *function*.

*Values*, in Python can be grouped based on their type, also known as a **data type**.

We'll look at **data types** more specifically in the next section.

### Variables names

When naming our variables, we need to follow Python's rules.

## Data

So far, we've used two **types of data**.

`"Mr. Ubial"` is an example of a **string**.

`32` is an example of a **integer**.

`32.2` is a number, but more specifically it's an example of a **float**.

### F-String
This exists only in Python. The F in f-string stands for **format**. To create an f-string, you put an `f` in front of the opening quotation.

```python
name = f"Mr. Ubial"
```

```python
friends_name = "Bro"
print(f"Hey {friends_name}!")
```

You  can use `{}` inside of an f-string to evaluate an expression.

## Input and output

Whenever we want to get information from the user, we can use the `input()` function.

```python
# prompt the user for their name
# store their name in a variable
print("What's your name?")
user_name = input()
```