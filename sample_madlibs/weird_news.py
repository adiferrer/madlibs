def madlib():
    noun1 = input("Noun 1: ")
    noun2 = input("Noun 2: ")
    noun3 = input("Noun 3: ")
    noun4 = input("Noun 4: ")
    noun5 = input("Noun 5: ")
    noun6 = input("Noun 6: ")
    state = input("US State: ")
    verb1 = input("Verb 1: ")
    verb2 = input("Verb 2: ")  
    verb3 = input("Verb 3: ")
    verb4 = input("Verb 4: ")
    verb5 = input("Verb 5: ")
    proper_name = input("Proper Name: ")  
    body_part = input("Part of the Body: ")
    adj1 = input("Adjective 1: ")
    adj2 = input("Adjective 2: ")
    relative = input("Relative: ")
    act = input("Activity: ")
    chain_rest = input("Chain Restaurant: ")
    past_adj = input("Adjective (Past Tense): ")
    month = input("Month: ")  
    past_verb = input("Verb (Past Tense): ")
    plural_noun = input("Plural Noun: ")

    madlib = f"A {noun1} in {state} was arrested this morning after he {verb1} in front of {noun2}. \n\
{plural_noun}, had a history of {verb2}, but no one - not even his {noun3} - ever imagine he'd {verb3} with a {noun4} stuck in his {body_part}. \n\n\
'I always thought {adj1}, but I never thought he'd do something like this. Even his {relative} was surprised. \n\n\
After a brief {act}, cops followed him to a {chain_rest}, where he reportedly {past_adj} in the fry machine. \n\n\
In {month}, a woman was charged with a similar crime. \n\
But rather than {verb4} with a {noun5}, she {past_verb} with a {adj2} dog. \n\n\
Either way, we imagine that after witnessing him {verb5} with a {noun6}, there are probably a whole lot of {plural_noun} that are going to need some therapy. \n"

    print(madlib)