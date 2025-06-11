class animal:
    def __init__(self):
        self.name = 'Rockey'

    def cat(self):
        print(f"{self.name} is good.")

class dog(animal):
   def __init__(self,breed):
       super().__init__()
       self.breed = breed

   def german(self):
        # super().cat()
        print(f"His name is {self.name}.He is a {self.breed}")



# ani = animal("cat")
# ani.cat()

dogs = dog("vill")
dogs.german()
