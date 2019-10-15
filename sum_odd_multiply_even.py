

def recieve():
    recieved = []
    for numbers in range(2):
        recieved.append(int(input(f"Digite o {numbers+1}º número do intervalo: ")))
    return recieved

def make_list(numbers_recieved):
    list_of_numbers = []
    for numbers_recieved in range(numbers_recieved[0],numbers_recieved[1]+1):
        list_of_numbers.append(numbers_recieved)
    return list_of_numbers


def sum_even(ready_list):
    accumulator = 0
    for number in ready_list:
        if number % 2 == 0:
            accumulator += number
    return accumulator


def multiply_odd(ready_list):
    accumulator = 1
    for number in ready_list:
        if number % 2 != 0:
            accumulator *= number
    return accumulator


if __name__ == '__main__':
    numbers_recieved = recieve()
    ready_list = make_list(numbers_recieved)
    sum_of_even = sum_even(ready_list)
    print(sum_of_even)
    odd_multiplication = multiply_odd(ready_list)
    print(odd_multiplication)

