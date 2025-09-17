class Dog:
    def __init__(self, name, height):
        self.dog_name = name
        self.dog_height = height

    def bark(self):
        print(f"{self.dog_name} goes woof!")

    def jump(self):
        print(f"{self.dog_name} jumps {self.dog_height * 2}cm")

davids_dog = Dog("Rex", 50)

sarahs_dog = Dog("Reacup", 20)

print(f"{davids_dog.dog_name}\n{davids_dog.dog_height}cm")

davids_dog.bark()
davids_dog.jump()

print(f"{sarahs_dog.dog_name}\n{sarahs_dog.dog_height}cm")

sarahs_dog.bark()
sarahs_dog.jump()


if sarahs_dog.dog_height > davids_dog.dog_height:
    print(f"{sarahs_dog.dog_name} is the bigger")

else:
    print(f"{davids_dog.dog_name} is the bigger")
