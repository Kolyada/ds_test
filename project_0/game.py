import numpy as np

def random_predict(number:int) -> int:

    count = 0

    while True:
        count += 1
        predict_number = np.random.randint(1, 101) # предполагаемое число
        if number == predict_number:
            break # выход из цикла, если угадали
    return(count)


def binary_predict(number:int,min_value:int=1,max_value:int=100) -> int:
    """Функция ищет заданное число из интервале методом бинарного поиска, полагаясь на результаты сравнения

    Args:
        number (int, optional): Искомое чисо. Defaults to 1.
        min_value (int, optional): Начало интервала (включительно). Defaults to 1.
        max_value (int, optional): Конец интервала (включительно). Defaults to 100.

    Raises:
        ValueError: Возникает при поиске число, находящегося вне заданного интервала

    Returns:
        int: Число сравнений
    """
    count = 0

    if number < min_value or number > max_value:
        raise ValueError('Number is out of interval')
    
    count += 1
    if number == min_value:
        return count

    count += 1
    if number == max_value:
        return count

    while True:
        count += 1
        current_number = min_value + round((max_value - min_value)/2)
        if number < current_number:
            max_value = current_number
        elif number > current_number:
            min_value = current_number
        else:
            break
    return count

def score_game(predict_function) -> int:
    """За какое количество попыток в среднем за 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """

    count_ls = [] # список для сохранения количества попыток
    np.random.seed(1) # фиксируем сид для вопроизводимости
    random_array = np.random.randint(1, 101, size=(1000)) # загадали список чисел

    for number in random_array:
        count_ls.append(predict_function(number))

    score = int(np.mean(count_ls)) # находим среднее количество попыток

    print(f'Ваш алгоритм угадывает число в среднем за: {score} попыток')
    return(score)

def main():
    score_game(binary_predict)

if __name__=='__main__':
    main()