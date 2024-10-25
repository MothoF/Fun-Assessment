def dog_years():
    
    """
    Create a program that counts a dog's age in dog's years. The program should only calculate dog years until 20 human years.
    Note: For the first two years, a dog year is equal to 10.5 human years. After that, each dog year equals 4 human years.

    Expected Output:
    ```
    Input a dog's age in human years: 15
    The dog's age in dog's years is 73
    ```
    """

    #enter your code here
    human_years = input("Input human years here: ")
    human_years = int(human_years)
    dogyears = 0

    if human_years <= 20:
        for year in range(1,human_years+1):
            if year < 3:
                dogyears += 10.5
            else:
                dogyears += 4
        print(f"The dog's age in dog's years is {int(dogyears)}")
    else:
        print('\nHuman years must not exceed 20\n')
        dog_years()
#print(dog_years())

def fizzbuzz(num):
    """
    Create a program that returns the numbers as a string from 1 to num. 
    But for multiples of three print “Fizz” instead of the number, 
    and for multiples of five print “Buzz”. For numbers which are 
    multiples of both three and five, print “FizzBuzz”.

    Expected Output:
    fizzbuzz(15) => "1 2 Fizz 4 Buzz Fizz 7 8 Fizz Buzz 11 Fizz 13 14 FizzBuzz"
    """

    #enter your code here
    output = ''

    for number in range(1,num+1):
        if number%3 == 0 and number%5 == 0:
            output += 'FizzBuzz '
        elif number%3 == 0:
            output += 'Fizz '
        elif number%5 == 0:
            output += 'Buzz '
        else:
            output += str(number)+' '
    return output.strip()
print(fizzbuzz(15))
    

def word_lengths(sentence):
    """
    Create a program that takes a sentence and returns a dictionary with each unique word
    as the key and the length of the word as the value.

    Expected Output:
    ```
    Input a sentence: "Aunty Yankho is amazing"
    Output: {'Aunty': 5, 'Yankho': 6, 'is': 2, 'amazing': 7}
    ```
    """
    
    #enter your code here
    sentence_components = sentence.split()
    output = {}

    for component in sentence_components:
        output[component] = len(component)
    
    return output
print(word_lengths('Aunty Yankho is amazing'))

def cube_sum(number):
    """
    Create a program that calculates the sum of the cubes of each digit in a number.
    
    Expected Output:
    ```
    cube_sum(123) => 1^3 + 2^3 + 3^3 = 1 + 8 + 27 = 36
    ```
    """
    
    #enter your code here
    string_number = str(number)
    list_string_numbers = []
    for string_num in string_number:
        list_string_numbers.append(string_num)
    cube__sum = 0

    for num in list_string_numbers:
        num = int(num)
        cube__sum += num**3

    return cube__sum
print(cube_sum(123))