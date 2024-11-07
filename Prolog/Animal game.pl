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
    write("\nEnter the type of animal (e.g., mammal, bird, fish, amphibian): "),
    read(Type),
    (
        animal(_, Type, _, _) ->
        askfood(Type);
        write("no"),
        asktype
    ).



askfood(Type) :-
    write("\nIs it a (herbivore, carnivore or omnivore): "),
    read(Food),
    (
        animal(_, Type, _, Food) ->
        askhabitat(Type, Food);
        write("no"),
        askfood(Type)
    ).


askhabitat(Type, Food) :-
    write("\nhabitat(domestic, forest, ocean, farm, antarctic, water): "),
    read(Habitat),
    (
        animal(X, Type, Habitat, Food) ->
        write(X)
    ).
