Person(dave, 25, male).
person(emma, 25, female).
person(john, 32, male).
person(sally, 25, female).

"""
OUTPUT: 


?- person(Name, 25, _).
Name = dave .

?- person(Name, 25, Gender).
Name = dave,
Gender = male .

?- person(dave, _, _).
true.

?- person(_, 25, _).
true .
"""
