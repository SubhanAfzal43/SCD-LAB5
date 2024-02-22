# In main.py

from shapes import Rectangle, Circle

# Instantiate objects of Rectangle and Circle
rectangle = Rectangle("Rectangle", 5, 3)
circle = Circle("Circle", 4)

# In main.py

def print_details(shape):
    print("Shape:", type(shape).__name__)
    print("Area:", shape.area())
    print("Perimeter:", shape.perimeter())

# In main.py

# Call print_details() with instances of Rectangle and Circle
print_details(rectangle)
print_details(circle)

# In main.py

from data_structures import DataProcessor

# Instantiate DataProcessor
data_processor = DataProcessor()

# Call demonstrate_operations() to test data structure methods
data_processor.demonstrate_operations()
