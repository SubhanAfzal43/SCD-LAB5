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

