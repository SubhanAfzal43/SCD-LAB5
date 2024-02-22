class Shape:
    def __init__(self, name):
        self.name = name

    def area(self):
        raise NotImplementedError("Subclass must implement abstract method")

    def perimeter(self):
        raise NotImplementedError("Subclass must implement abstract method")
# In shapes.py

class Rectangle(Shape):
    def __init__(self, name, length, width):
        super().__init__(name)
        self._length = length
        self._width = width

    def area(self):
        return self._length * self._width

    def perimeter(self):
        return 2 * (self._length + self._width)

class Circle(Shape):
    def __init__(self, name, radius):
        super().__init__(name)
        self._radius = radius

    def area(self):
        return 3.14 * self._radius**2

    def perimeter(self):
        return 2 * 3.14 * self._radius

# In shapes.py

class Rectangle(Shape):
    def __init__(self, name, length, width):
        super().__init__(name)
        self._length = length
        self._width = width

    # Getter and setter for length attribute
    def get_length(self):
        return self._length

    def set_length(self, length):
        self._length = length

    # Getter and setter for width attribute
    def get_width(self):
        return self._width

    def set_width(self, width):
        self._width = width

    def area(self):
        return self._length * self._width

    def perimeter(self):
        return 2 * (self._length + self._width)

class Circle(Shape):
    def __init__(self, name, radius):
        super().__init__(name)
        self._radius = radius

    # Getter and setter for radius attribute
    def get_radius(self):
        return self._radius

    def set_radius(self, radius):
        self._radius = radius

    def area(self):
        return 3.14 * self._radius**2

    def perimeter(self):
        return 2 * 3.14 * self._radius
    
    # In shapes.py

class Rectangle(Shape):
    def __init__(self, name, length, width):
        super().__init__(name)
        self._length = length
        self._width = width

    def get_length(self):
        return self._length

    def set_length(self, length):
        self._length = length

    def get_width(self):
        return self._width

    def set_width(self, width):
        self._width = width

    def area(self):
        return self._length * self._width

    def perimeter(self):
        return 2 * (self._length + self._width)

class Circle(Shape):
    def __init__(self, name, radius):
        super().__init__(name)
        self._radius = radius

    def get_radius(self):
        return self._radius

    def set_radius(self, radius):
        self._radius = radius

    def area(self):
        return 3.14 * self._radius**2

    def perimeter(self):
        return 2 * 3.14 * self._radius
# In data_structures.py

class DataProcessor:
    def __init__(self):
        pass

    def demonstrate_operations(self):
        # Implement methods to demonstrate operations on Python data structures
        pass
# In DataProcessor class

def demonstrate_operations(self):
    # Tuples
    my_tuple = (1, 2, 3)
    print("Tuple:", my_tuple)

    # Lists
    my_list = [4, 5, 6]
    my_list.append(7)
    print("List:", my_list)

    # Dictionaries
    my_dict = {'a': 1, 'b': 2}
    my_dict['c'] = 3
    print("Dictionary:", my_dict)

    # Sets
    my_set = {1, 2, 3}
    my_set.add(4)
    print("Set:", my_set)
# In your main script or wherever you want to test

from shapes import Rectangle, Circle
from data_structures import DataProcessor

# Create instances of Rectangle and Circle
rectangle = Rectangle("Rectangle", 5, 3)
circle = Circle("Circle", 4)

# Call methods to calculate area and perimeter
rectangle_area = rectangle.area()
rectangle_perimeter = rectangle.perimeter()
circle_area = circle.area()
circle_perimeter = circle.perimeter()

# Create instance of DataProcessor and call methods to demonstrate operations
data_processor = DataProcessor()
data_processor.demonstrate_operations()

