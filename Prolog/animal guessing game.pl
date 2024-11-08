% Facts about animals with yes/no questions about characteristics
animal(tiger) :- mammal, fur, carnivore, 4.
animal(dolphin) :- mammal, aquatic, carnivore, 0.
animal(lion) :- mammal, fur, carnivore, 4.
animal(eagle) :- bird, feather, carnivore, 2.
animal(salmon) :- fish, aquatic, carnivore, 0.
animal(frog) :- amphibian, aquatic, herbivore, 4.

% Animal types with key characteristics
mammal :- ask("Is it a mammal?").
bird :- ask("Is it a bird?").
fish :- ask("Is it a fish?").
amphibian :- ask("Is it an amphibian?").
aquatic :- ask("Is it aquatic?").
fur :- ask("Does it have fur?").
feather :- ask("Does it have feathers?").
carnivore :- ask("Is it a carnivore?").
herbivore :- ask("Is it a herbivore?").
four_legs :- ask("Does it have four legs?").

% Asking yes/no questions
ask(Question) :-
    write(Question), nl,
    read(Response),
    (   Response == yes -> true
    ;   Response == no -> fail
    ;   write('Please answer yes or no.\n'), ask(Question)
    ).

% Start the guessing game
start_game :-
    write('Think of an animal and I will try to guess it.\n'),
    guess(Animal),
    write('I guessed your animal: '), write(Animal), nl.

% Guess the animal based on the questions
guess(Animal) :-
    (   animal(Animal) ->
        true
    ;   write('I am not sure. Please answer more questions.\n'),
        ask_more_questions
    ).

% If more questions are needed, ask
ask_more_questions :-
    animal(Animal),
    write('I guessed your animal: '), write(Animal), nl.
