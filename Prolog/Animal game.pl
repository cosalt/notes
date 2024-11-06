animal(dog, mammal, domestic, carnivore).
animal(cat, mammal, domestic, carnivore).
animal(deer, mammal, forest, carnivore).
animal(dolphin, mammal, ocean, carnivore).
animal(bear, mammal, forest, carnivore).

animal(chicken, bird, farm, carnivore).
animal(parrot, bird, forest, omnivores).
animal(owl, bird, forest, carnivores).
animal(penguins, bird, antarctic, carnivorous).

animal(blob, fish, ocean, carnivore).
animal(eel, fish, ocean, carnivore).
animal(shark, fish, ocean, carnivore).
animal(salmon, fish, ocean, carnivore).

animal(axoloti, amphibian, water, carnivore).
animal(frog, amphibian, water, carnivore).
animal(lizard, amphibian, water, carnivore).
animal(newt, amphibian, water, carnivore).

start :- write('animal game').
asktype(Animal_name) :- animal(Animal_name, Type, _, _), write(Type).
askhabitat(Animal_name) :- animal(Animal_name, _, Habitat, _), write(Habitat).
askdiet(Animal_name) :- animal(Animal_name, _, _, Diet), write(Diet).

