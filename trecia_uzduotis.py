def get_amount(sarasas):
    numbers_list = [number for number in sarasas if type(number) is int or type(number) is float]
    amount = sum(numbers_list)
    return amount

def get_sentence(sarasas):
    words_list = [word for word in sarasas if type(word) == str]
    sentence = " ".join(words_list)
    return sentence

def count_amount_true_booleans(sarasas):
    true_booleans_count = sum(boolean is True for boolean in sarasas)
    return true_booleans_count

def main():
    sarasas = [2.5, 2, "Labas", True, 5, 7, 8, 2.8, "Vakaras", False, None, True]
    printable_list = []

    printable_list.extend([
        get_amount(sarasas),
        get_sentence(sarasas),
        count_amount_true_booleans(sarasas)
    ])

    for result in printable_list:
        print(result)

main()