## Pixel Mapping Python Script

A program that calculates pixel coordinate values for an image that is to be displayed on a two dimensional surface given the dimensions of the image and the corner points of the image as it is to be displayed.

For example, if an image is defined by a 3x3 grid of pixel values, and the (x, y) coordinates of the four corner points to display the image at are: (1, 1), (3, 1), (1, 3), and (3, 3) then the program should calculate and return the coordinates: (1, 1), (2, 1), (3, 1), (1, 2), (2, 2), (3, 2), (3, 1), (3, 2), (3, 3) which are the coordinates at which to place the 9 pixels in the image such that they’re evenly spaced within the corner points. The solution can be seen visually in the image below.

![Plot Image](https://github.com/RazYasuke/Python/blob/main/Pixel%20Mapping/images/img_1.png)

### Script Execution 

![Plot Image](https://github.com/RazYasuke/Python/blob/main/Pixel%20Mapping/images/script_execution.png)

The Numpy module is needed to run this code. The command "pip install numpy" is needed to install the module.

Unauthorized reuse/modification/copying is prohibited!