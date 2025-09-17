class Cat:
    def __init__(self, cat_name, cat_age):
        self.name = cat_name
        self.age = cat_age

cat_1 = Cat("mimi", 8)
cat_2 = Cat("momo", 4)
cat_3 = Cat("miami", 1)

def find_old_cat(Cat1, Cat2, Cat3):

    if Cat1.age > Cat2.age:
        if Cat1.age > Cat3.age:
            oldest_cat = Cat1
        else:
            oldest_cat = Cat3

    elif Cat2.age > Cat1.age:
        if Cat2.age > Cat3.age:
            oldest_cat = Cat2
        else:
            oldest_cat = Cat3

    print(f"The oldest cat is {oldest_cat.name} and it is {oldest_cat.age} years old")


find_old_cat(cat_1, cat_2, cat_3)
