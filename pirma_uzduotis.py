#Sukurti programą, kuri:
#Prie kiekvieno sakinio „The Zen of Python tekstu“ žodžio pridėtų šauktuką ir atspausdintų naują sakinį.
#Patarimai:
#Naudoti map (su lambda) arba comprehension, " ".join()

def main():
    sentence = "The Zen of Python tekstu"
    #List comprehension
    new_sentence_comprehension = [f"{word}!" for word in sentence.split()]
    print(" ".join(new_sentence_comprehension))

    #map
    new_sentence_map = map(lambda word: f"{word}!", sentence.split())
    print(" ".join(new_sentence_map))

main()
