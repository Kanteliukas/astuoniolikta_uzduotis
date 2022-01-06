from statistics import mean, median

def main():
    #   Sukurtų sąrašą iš skaičių nuo 0 iki 50
    numbers_list = range(0, 51)

    #   Padaugintų visus sąrašo skaičius iš 10 ir atspausdintų
    numbers_times_10 = [number * 10 for number in numbers_list]


    #   Atrinktų iš sąrašo skaičius, kurie dalinasi iš 7 ir atspausdintų
    numbers_divides_by_7 = [number for number in numbers_list if number % 7 == 0]


    #   Pakeltų visus sąrašo skaičius kvadratu ir atspausdintų
    numbers_raised_by_square = [number ** 2 for number in numbers_list]


    #Su kvadratų sąrašu atliktų šiuos veiksmus:
    #   atspausdintų sumą, mažiausią ir didžiausią skaičių,
    #   vidurkį, medianą
    #   Surūšiuotų ir atspausdintų kvadratų sąrašą atbulai
    amount = sum(numbers_raised_by_square)
    minimum_value = min(numbers_raised_by_square)
    maximum_value = max(numbers_raised_by_square)
    mean_number = mean(numbers_raised_by_square)
    median_number = median(numbers_raised_by_square)
    reverse_sort = sorted(numbers_raised_by_square, reverse=True)

    printable_list = []
    printable_list.extend([
        numbers_times_10,
        numbers_divides_by_7,
        numbers_raised_by_square,
        amount,
        minimum_value,
        maximum_value,
        mean_number,
        median_number,
        reverse_sort
    ])

    for numbers in printable_list:
        print(numbers)

main()