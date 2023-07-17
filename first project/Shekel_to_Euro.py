from coins import EUR


def print_result(result):
    print(result)


def get_value_to_convert():
    try:
        value_to_convert = float(input('Please enter an amount to convert: '))
    except:
        print('Please enter only a number')
        return get_value_to_convert()
    return value_to_convert


# A Function displays the requested Euro value in comparing to the Shekel value
def convert_shekel_to_euro(value_to_convert):
    # object creation of EUR class
    euro_coin = EUR()
    converted_value = euro_coin.calculate(value_to_convert)
    return f'{value_to_convert} ILS = {converted_value} EUR'


def main():
    print('Welcome to currency converter Shekel to Euro')

    results_list = []

    continue_converting = 'Y'

    while continue_converting != 'N':
        value_to_convert = get_value_to_convert()
        result = convert_shekel_to_euro(value_to_convert)
        results_list.append(result)
        print_result(result)

        user_answer = input('Would you like to start over? (Y/N): Y = start over, N = finish')

        if user_answer == 'N':
            break
        elif user_answer != 'Y':
            while user_answer not in ['Y', 'N']:
                print('Invalid Choice, please try again')
                user_answer = input('Would you like to start over? (Y/N): Y = start over, N = finish')

        continue_converting = user_answer

    print('Thanks for using our currency converter')
    print(results_list)

    try:
        results_file = open('results.txt', 'a')
        content = '\n'.join(results_list)
        results_file.write(content)
        results_file.close()
    except:
        print("Error: can't find file or add data")


main()
