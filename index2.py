fruits = ["orange", "apple", "pineapple", "watermelon", "banana"]
if  "orange" in fruits:
    print("Fruit used to make orange juice:", "Orange")
else:
    print("No orange in the list.")
def make_medicine(fruit3, fruit4):
    return f"{fruit3}-{fruit4} medicine"
medicine = make_medicine("pineapple", "watermelon")
print("Medicine produced from two fruits:", medicine)
def print_fruit_count(fruits):
    print("Number of fruits in the array:", len(fruits))
print_fruit_count(fruits)