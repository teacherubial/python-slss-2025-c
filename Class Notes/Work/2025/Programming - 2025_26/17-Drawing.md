# Python Turtle Artist

![ninja turtles](https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fimages.fineartamerica.com%2Fimages%2Fartworkimages%2Fmediumlarge%2F3%2Fnage-mutant-ninja-turtles-megan-cooper.jpg&f=1&nofb=1&ipt=aef7b0d41b5ce04c4da8206fc70570de89c487b54bc9b6ae277b8264950e8c47)

## Purpose
Use the Python `turtle` library to create an original piece of digital art. This assignment is tiered to let you choose the complexity level.

### Core Requirements (All Tiers):

* Your code must run without errors.
* Your final image must be your own original design.
* Your code must be clean, well-commented, and use good variable names.
* You must use the turtle library.

## Base Requirements

**Goal**: Create a simple, recognizable drawing using fundamental turtle commands.

Requirements:

* Use fundamental commands: Your drawing must use `forward()`, `backward()`, `left()`, `right()`.
* Use at least 3 di`fferent colors: Use `pencolor()` or color() to change the turtle's pen color.
* Use pen control: Use `penup()` and `pendown()` at least once to move the turtle without drawing.

## Intermediate 

**Goal**: Create a more complex or detailed drawing by using functions, and variables to create repeating elements.

Requirements:
* Meet all Tier 1 requirements.
* Define and use at least one custom function: Create your own function to draw a repeated element. For example, `def draw_star(size, color):` or `def draw_window():`. Your main code should call this function.
* Use variables: Use variables to control aspects of your drawing, such as side lengths, angles, or number of repetitions.

Project Ideas:
* A cityscape with multiple buildings of different heights (using a function and a loop).
* A detailed snowflake with 6 repeating branches.
* A field of flowers, using a function to draw each flower.

## Expert

**Goal**: Create a highly complex, generative, or intricate piece of art by designing and implementing an original recursive function.

Requirements:
* Meet all Tier 1 and Tier 2 requirements (though your main focus will be on the recursive element).
* Create an original recursive function: You must design and code a function that calls itself to create a complex, self-similar pattern.
* Must be original: You cannot simply copy a classic fractal like the "Koch snowflake" or "Sierpinski triangle" from an online tutorial. You can use them as inspiration, but your implementation and final design must be your own.
* In-Code Documentation: Your recursive function must be documented with comments explaining:

  * Purpose: What does the function draw?
  * Parameters: What does each argument (e.g., level, size) control?
  * Base Case: What condition stops the recursion?
  * Recursive Step: How does the function call itself with modified arguments?