from coins import USD, ILS

#A function to print the conversion result
def print_result(result):
    print(result)
# First screen
#A function prints the two choice options and a user can choose only integer value
def get_choice_option():
    choice_option = int(input('Please choose an option (1/2): Dollars to Shekels, 2. Shekels to Dollars'))
    return choice_option

#A function allows to user to choose only two choice options: 1 or 2
def get_user_value():
    choice_option = get_choice_option()

    if choice_option == 1:
        value_to_convert = get_value_to_convert()
        result = convert_dollar_to_shekel(value_to_convert)
        print_result(result)

    elif choice_option == 2:
        value_to_convert = get_value_to_convert()
        result = convert_shekel_to_dollar(value_to_convert)
        print_result(result)
# if the user chooses option not 1 or 2, prints 'Invalid Choice...'
    else:
        print('Invalid Choice, please try again')
        return get_user_value()

    return result
# Second screen, a function allows to user to choose float value as well
def get_value_to_convert():
    try:
        value_to_convert = float(input('Please enter an amount to convert'))
    except:
        print('Please enter only a number')
        return get_value_to_convert()
    return value_to_convert
# Third screen
# A Function displays the requested Shekel value in comparing to the Dollar value
def convert_dollar_to_shekel(value_to_convert):
# object creating of USD class
    dollar_coin = USD()
    converted_value = dollar_coin.calculate(value_to_convert)
    return f'{value_to_convert} USD = {converted_value} ILS'

# A Function displays the requested Dollar value in comparing to the Shekel value
def convert_shekel_to_dollar(value_to_convert):
# object creation of ILS class
    shekel_coin = ILS()
    converted_value = shekel_coin.calculate(value_to_convert)
    return f'{value_to_convert} ILS = {converted_value} USD'


def main():
# In the first screen, the program will open with a statement: ('Welcome to currency converter')
    print('Welcome to currency converter')
# In the third screen,a list of conversion result will be displayed
    results_list = []
# A creating a variable for 'Y' option (start over and continue to convert)
    continue_converting = 'Y'
# if the user chooses to finish and write 'N', all conversion results will be added to the list automatically
    while continue_converting != 'N':
        result = get_user_value()
        results_list.append(result)
# A question will be displayed for the user if he would like to stat over or finish
        user_answer = input('Would you like to start over? (Y/N): Y=start over, N=finish')

        if user_answer == 'N':
#if the user chooses to finish and write 'N', the loop will be stopped and the program will move to end screen
            break
# if the user chooses in option that not "Y" or "N", the program will print 'Invalid Choice' and print again the question
        elif user_answer != 'Y':
            while user_answer not in ['Y', 'N']:
                print('Invalid Choice, please try again')
                user_answer = input('Would you like to start over? (Y/N): Y=start over, N=finish')

        continue_converting = user_answer
#Fourth screen (end screen)
    print('Thanks for using our currency converter')
# all the conversion results will be printed
    print(results_list)
# all the conversion results will be added to 'results' file
    try:
        results_file = open('results.txt', 'a')
        file_content = '\n'.join(results_list)
        results_file.write(file_content)
        results_file.close()
# if there is IO error, the program will print: 'Error: can't find file or add data'
    except :
        print("Error: can't find file or add data")


main()
