# (String) Methods
6 October 2025

## Slide Deck
[3 - String Methods.pdf](../../../../../_resources/3%20-%20String%20Methods-1.pdf)

## `in` keyword --> `Str`

If you want to see if a string contains some characters
or if it contains a **substring** we can use the `in`
keyword.

```python
# Ask the customer if they want fries
fries_reply = input("Do you want fries?") 

# "Yes!"
if "yes" in fries_reply:
	print("Here are your fries.")
else:
	print("OK. You will not have fries.")
```