started_vector = []
vector_aux = []
vector_with_results = []


def create_vector():
    for numerous in range(2, 8):
        started_vector.append(numerous)
    return started_vector


def division(start_vector):
    for number_fixed in start_vector:
        for index, number in enumerate(start_vector):
            if number % number_fixed == 0:
                start_vector[index] = number/number_fixed
        vector_aux.append(number_fixed)


created_vector = create_vector()
division(created_vector)

