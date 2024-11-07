person(dave, 25, male).
person(emma, 25, female).
person(john, 32, male).
person(sally, 25, female).


animal(dog, mammal, domestic, carnivore).
animal(cat, mammal, domestic, herbivore).
animal(deer, mammal, forest, carnivore).
animal(dolphin, mammal, ocean, omnivore).
animal(bear, mammal, forest, carnivore).

animal(chicken, bird, farm, carnivore).
animal(parrot, bird, forest, omnivore).
animal(owl, bird, forest, carnivores).
animal(penguins, bird, antarctic, carnivore).

animal(blob, fish, ocean, carnivore).
animal(eel, fish, ocean, herbivore).
animal(shark, fish, ocean, omnivore).
animal(salmon, fish, ocean, carnivore).

animal(axoloti, amphibian, water, carnivore).
animal(frog, amphibian, water, herbivore).
animal(lizard, amphibian, water, omnivore).
animal(newt, amphibian, water, carnivore).

start :-
    write('animal game'),
    write("i'll try to guess your animal"),
    asktype.

asktype :-
    write("Enter the type of animal (e.g., mammal, bird, fish, amphibian): "),
    read(Type),
    (
        animal(_, Type, _, _) ->
        askfood(Type);
        write("no"),
        asktype
    ).



askfood(Type) :-
    write("Is it a (herbivore, carnivore or omnivore): "),
    read(Food),
    (
        animal(_, Type, _, Food) ->
        askhabitat(Type, Food);
        write("no"),
        askfood(Type)
    ).


askhabitat(Type, Food) :-
    write("habitat(domestic, forest, ocean, farm, antarctic, water): "),
    read(Habitat),
    (
        animal(_, Type, Habitat, Food);
        write('no')
    ).

guess(_) :-
    write("is it: "),
    animal(Animal, Type, Habitat, Food), write(Animal).

