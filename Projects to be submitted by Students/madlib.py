def main(noun, verb, noun2, adverb, place):
    statement = f"{noun} is {verb} {noun2} {adverb} in {place}"
    print(statement)

inputted_noun = input("Noun1(Person):")
inputted_verb = input("Verb:")
inputted_noun2 = input("Noun2(Work being Done):")
inputted_adverb = input("Adverb:")
inputted_place = input("Place:")

if __name__ == "__main__":
    main(inputted_noun, inputted_verb, inputted_noun2, inputted_adverb, inputted_place)