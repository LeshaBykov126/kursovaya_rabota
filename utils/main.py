from utils.work_function import hh_function, sj_function


def main():
    """ Основная функция программы """
    while True:  # Цикл для проверки ответа
        while True:
            first_question = input('Выберите платформу:\n'
                                   '1 - hh\n'
                                   '2 - super job\n')
            if first_question == '1' or first_question == '2':
                break

            else:
                print('Некорректный ввод')
                continue

        while True:  # Цикл для проверки ответа
            keyword = input('Введите интересующую должность\n')
            if len(keyword.lower()) <= 2:
                print("Слишком короткий запрос")
                continue
            else:
                break

        while True:  # Цикл для проверки ответа
            count_vacancy = input('Укажите количество вакансий, не более 100\n')
            try:
                if int(count_vacancy) > 1:
                    break
                else:
                    print("Указано мало символов")
                continue

            except ValueError:
                print("Пустой ввод")
                continue

        while True:  # Цикл для проверки ответа
            city = input('В каком городе искать вакансии?\n')
            if len(city.lower()) <= 2:
                print("Указано мало символов")
                continue
            else:
                break

        keyword_end = keyword + ' ' + city  # составление запроса для поиска вакансий

        if first_question == '1':
            hh_function(keyword_end, count_vacancy)  # вызываем функцию для поиска на hh

        elif first_question == '2':
            sj_function(keyword_end, count_vacancy)  # вызываем функцию для поиска на superjob

        while True:  # проверка ответа
            answer_end = input('Выбрать другую вакансию? Да/нет\n')
            if answer_end.lower() == 'да' or answer_end.lower() == 'lf':
                break
            elif answer_end.lower() == 'нет' or answer_end.lower() == 'ytn':
                print('До скорой встречи!')
                exit()

            else:
                print('Невалидный ответ')
                continue


if __name__ == '__main__':
    main()
