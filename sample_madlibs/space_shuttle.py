def madlib():
    noun1 = input("Noun: ")
    noun2 = input("Another Noun: ")
    noun3 = input("One More Noun: ")
    noun4 = input("Last Noun: ")
    plural_noun1 = input("Plural Noun: ")
    plural_noun2 = input("Another Plural Noun: ")
    plural_noun3 = input("One More Plural Noun: ")
    plural_noun4 = input("Last Plural Noun: ")
    verb_ing1 = input("Verb Ending in -ing: ")
    verb_ing2 = input("Another Verb Ending in -ing: ")
    city = input("City: ")
    adj1 = input("Adjective: ")
    adj2 = input("Another Adjective: ")
    adj3 = input("Last Adjective: ")
    num1 = input("Number (in words): ")
    num2 = input("Another Number (in words): ")
    verb1 = input("Verb: ")
    verb2 = input("Another Verb: ")
    adv = input("Adverb: ")
    
    madlib = f"In 1981, the U.S. launched the first real Space {noun1}. It was named 'Columbia' and was piloted by two brave {plural_noun1}. \n\
They had practiced {verb_ing1} for two years and were expert {plural_noun2}. 'Columbia' took off from {city} using its powerful first-stage {plural_noun3} 
and soared off into the {adj1} blue {noun2}. At an altitude of {num1} feet, it went into orbit around the {noun3}. \n\
For people watching from Earth, it was a/an {2} sight to {verb1}! Who could really {verb2} that there were two {plural_noun4} \n\
in space? It was mind {verb_ing2}. After {num2} orbits, the shuttle landed {adv} at an air force {noun4}. \n\
It was a/an {adj3} day for the U.S. Space Program."

    print(madlib)