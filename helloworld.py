def print_tree(width, height):
  if width % 2 == 0 or height % 2 == 0:
    print("Invalid input: Width and height should be odd numbers.")
    return

  # Print the crown of the tree
  for i in range(1, height + 1):
    spaces = "*" * ((height - i) // 2)
    stars = "*" * (i * 2 - 1)
    print(spaces + stars + spaces)

  # Print the trunk of the tree
  trunk_height = height // 3
  for i in range(trunk_height):
    spaces = " " * ((width - 3) // 2)
    trunk = "***"
    print(spaces + trunk + spaces)

width = int(input("Enter the width of the tree: "))
height = int(input("Enter the height of the tree: "))

print_tree(width, height)
