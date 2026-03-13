items = int(input("Enter the number of manufactured items:"))

items_per_box = int(input("Enter the number of items that can be packed in a box:"))

if items % items_per_box == 0:
    boxes_needed = items // items_per_box
else:
    boxes_needed = (items // items_per_box) + 1

print(f"Number of boxes needed: {boxes_needed}")