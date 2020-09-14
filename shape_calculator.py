class Rectangle:
  """When a Rectangle object is created, it should be initialized with width and height attributes."""
  def __init__(self, width, height):
    self.width = width
    self.height = height
    


  def set_width(self, width):
    self.width = width
    return

  def set_height(self, height):
    self.height = height
    return

  def get_area(self):
    """Returns area (width * height)"""
    area = self.width * self.height
    return area


  def get_perimeter(self):
    """Returns perimeter (2 * width + 2 * height)"""
    perimeter = (2 * self.width + 2 * self.height)
    return perimeter

  def get_diagonal(self):
    """Returns diagonal ((width ** 2 + height ** 2) ** .5)"""
    diagonal = ((self.width ** 2 + self.height ** 2) ** .5)
    return diagonal
  

  def get_picture(self):
    """Returns a string that represents the shape using lines of "*". The number of lines should be equal to the height and the number of "*" in each line should be equal to the width. There should be a new line (\\n) at the end of each line. If the width or height is larger than 50, this should return the string: \"Too big for picture.\"."""
    
    picture = ""

    if self.width > 50 or self.height > 50:
      return "Too big for picture."
    else:
      for i in range (self.height):
        picture += self.width * "*" + "\n"
      return picture


  def get_amount_inside(self, shape):
    """Takes another shape (square or rectangle) as an argument. Returns the number of times the passed in shape could fit inside the shape (with no rotations). For instance, a rectangle with a width of 4 and a height of 8 could fit in two squares with sides of 4."""

    width_fit = self.width // shape.width
    height_fit = self.height // shape.height
    return width_fit * height_fit

  def __str__(self):
    """if an instance of a Rectangle is represented as a string, it should look like: Rectangle(width=5, height=10)"""
    return "Rectangle(width=" + str(self.width) + ", height=" + str(self.height) + ")"


class Square(Rectangle):
  """The Square class should be a subclass of Rectangle. When a Square object is created, a single side length is passed in. The __init__ method should store the side length in both the width and height attributes from the Rectangle class.

  The Square class should be able to access the Rectangle class methods but should also contain a set_side method. If an instance of a Square is represented as a string, it should look like: Square(side=9)

  Additionally, the set_width and set_height methods on the Square class should set both the width and height."""
  def __init__(self, side):
    self.width = side
    self.height = side
    self.side = side

  def set_side(self, side):
    self.side = side
    self.width = side
    self.height = side
  
  def set_width(self, width):
    self.width = width
    self.height = width
    self.side = width
    return

  def set_height(self, height):
    self.height = height
    self.width = height
    self.height = height
    return



  def __str__(self):
    """If an instance of a Square is represented as a string, it should look like: Square(side=9)"""
    return "Square(side=" + str(self.side) + ")"