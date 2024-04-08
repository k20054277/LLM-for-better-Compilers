
# Original program
def calculate_area(width, height):
  area = width * height
  return area

# Refactored program
def calculate_area(width, height):
  return width * height


# Test code
area = calculate_area(5, 10)
print(area)  # Output: 50
