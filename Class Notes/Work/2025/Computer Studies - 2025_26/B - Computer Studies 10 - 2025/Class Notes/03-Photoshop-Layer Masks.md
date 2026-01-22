# Photoshop - 2 Placing Images and Masks

## Big Questions

What's the best way to import an image into a Photoshop document?

How can we extract an object from an image?

##  Placing an Image

We often want to work with an image that we've downloaded from the internet or taken on our cameras. There are different ways to put this into our document. We'll use one way, primarily.

When we've created a Photoshop document, we can place the image using the following:

`File -> Place Embedded...`

Then, find your image and place it in.

Photoshop will add the image as a new **Smart Layer**. This means that any changes you make in the layer are **non-destructive**.

You can then manipulate the layer using the **Free Transform** tool.  You can reach the tool by going to:

`Edit -> Free Transform`
or
Press Command + T

Commit your changes by clicking the check box in the property tool bar or by pressing the return/enter key.

## Masks

**Masks** help us to hide things that we don't want to show.

We can access masks by choosing any of the **Selection** tools. One selection tool I use the most is the Rectangular Marquee Tool. Once we make a selection, we can only change that part that we select.

If we want to "deselect" our selection, we click:

`Select -> Deselect`

Select the *Rectangular Marquee Tool* and click Select Subject in the top Tool Property Bar.

Here you can ask a computational model to best guess what the subject is.

When you're satisfied with the selection, in **Output** select **Output to Layer Mask**. This will create a mask that hides *everything but the subject*.