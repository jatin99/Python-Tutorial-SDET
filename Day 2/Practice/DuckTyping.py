
def dog_speak():
    return "Dog speaks!!"


def cat_speak():
     return "Cat speaks!!"

def duck_speak():
    return "Duck speaks!!"

def make_speak(animal_sound):
    return animal_sound()

print(make_speak(duck_speak))