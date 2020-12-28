def madlib():
    adj1 = input("Adjective 1: ")
    adj2 = input("Adjective 2: ")
    adj3 = input("Adjective 3: ")
    adj4 = input("Adjective 4: ")
    adj5 = input("Adjective 5: ")
    adj6 = input("Adjective 6: ")
    adj7 = input("Adjective 7: ")
    adj8 = input("Adjective 8: ")
    adj9 = input("Adjective 9: ")
    adj10 = input("Adjective 10: ")
    adj11 = input("Adjective 11: ")
    noun1 = input("Noun 1: ")
    noun2 = input("Noun 2: ").capitalize
    place = input("Place: ")
    vehicle = input("Vehicle: ")
    plural_noun1 = input("Plural Noun 1: ")
    plural_noun2 = input("Plural Noun 2: ").capitalize 
    plural_noun3 = input("Plural Noun 3: ") 
    plural_noun4 = input("Plural Noun 4: ") 
    verb1 = input("Verb 1: ")
    verb2 = input("Verb 2: ")
    verb3 = input("Verb 3: ")
    pn_job = input("Plural Noun (type of job): ").capitalize
    
    madlib = f"Star Wats is a {adj1} {noun1} of {adj2} versus evil in a {place} far far away. \n\
There are {adj3} battles between {adj4} {vehicle} in {adj5} space and {adj6} duels with {plural_noun1} called {adj7} sabers. \n\
{plural_noun2} called 'droids' are helpers and {plural_noun3} to the heroes. \n\
A {adj8} power called The {noun2} {verb1}s people to do {adj9} things, like {verb2} {plural_noun4}. \n\
The Jedi {pn_job} use The Force for the {adj10} side and the Sith {verb3} it for the {adj11} side. \n"

    print(madlib)