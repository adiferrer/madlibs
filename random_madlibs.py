from sample_madlibs import space_shuttle, star_wars, weird_news, my_eulogy
import random

if __name__ == "__main__":
    m = random.choice([space_shuttle, star_wars, weird_news, my_eulogy])
    m.madlib()