def madlib():
    verb_ing1 = input("Verb (ending with -ing) 1: ")
    verb_ing2 = input("Verb (ending with -ing) 2: ")
    adj1 = input("Adjective 1: ")
    adj2 = input("Adjective 2: ").capitalize
    adj3 = input("Adjective 3: ")
    adj4 = input("Adjective 4: ")
    adj5 = input("Adjective 5: ")
    adj6 = input("Adjective 6: ")
    adv = input("Adverb: ")
    fam_memb = input("Family Member: ")
    num = input("Number: ")
    past_verb1 = input("Verb (in past tense) 1: ")
    past_verb2 = input("Verb (in past tense) 2: ")
    past_verb3 = input("Verb (in past tense) 3: ")
    noun1 = input("Noun 1: ").capitalize
    noun2 = input("Noun 2: ")
    noun3 = input("Noun 3: ")
    mil_rank = input("Military Rank: ").capitalize
    award = input("Award: ")
    adj_er = input("Adjective (with -er): ")
    pronoun = input("Pronoun: ")
    plural_noun1 = input("Plural Noun 1: ")
    plural_noun2 = input("Plural Noun 2: ")
    verb1 = input("Verb 1: ") 
    verb2 = input("Verb 2: ")
    feeling = input("Feeling: ").capitalize

    madlibs = f"If you are {verb_ing1} this, it means I am {adj1}. I am sure you are all {adv} grieved, especially my {fam_memb} and our {num} children. \n\
In my life, I {past_verb1} for many popular {noun1} shows, including {mil_rank} Bilko and Get {adj2}. I led a {adj3} life, with {adj4} {noun2} and even better memories. \n\
I'll never forget the day I won my {award}, and showed it to my wife. She remarked, It's so much {adj_er} than I thought!. \n\
To which I replied, That's what {pronoun} said. We laughed and {past_verb2}. \n\
When I {past_verb3} Mad Libs, I never imagined it would be as {adj5} as the Bible, but I guess {plural_noun1} really prefer filing in the {plural_noun2}. \n\
I hope to be remembered as a {noun3} who loved to make people {verb1}, but more importantly, as a(n) {adj6} man. \n\
Thank you all for {verb_ing2}, I promise not to {verb2} you while you sleep. {feeling} forever, Leonard B. Stern." 

    print(madlibs)