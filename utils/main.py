from utils.abstract_class import LocalStorage
from utils.work_function import hh_function, sj_function


def main():
    """ Основная функция программы """
    local_storage = LocalStorage()  # Создаем экземпляр класса LocalStorage

    while True:
        while True:
            first_question = input('Выберите платформу:\n'
                                   '1 - hh\n'
                                   '2 - super job\n')
            if first_question == '1' or first_question == '2':
                break
            else:
                print('Некорректный ввод')
                continue

        while True:
            keyword = input('Введите интересующую должность\n')
            if len(keyword.lower()) <= 2:
                print("Слишком короткий запрос")
                continue
            else:
                break

        while True:
            count_vacancy = input('Укажите количество вакансий, не более 100\n')
            try:
                count_vacancy = int(count_vacancy)
                if count_vacancy > 0 and count_vacancy <= 100:
                    break
                else:
                    print("Некорректное количество вакансий")
                    continue

            except ValueError:
                print("Пустой ввод или некорректное значение")
                continue

        while True:
            city = input('В каком городе искать вакансии?\n')
            if len(city.lower()) <= 2:
                print("Указано мало символов")
                continue
            else:
                break

        keyword_end = keyword + ' ' + city

        if first_question == '1':
            hh_function(keyword_end, int(count_vacancy))
            keyword_local = input('Введите ключевое слово для поиска в локальном хранилище: ')
            results = local_storage.find_vacancy(keyword_local)  # Используем экземпляр класса LocalStorage
            print(f"Результаты поиска в локальном хранилище для ключевого слова '{keyword_local}':")
            for result in results:
                print(result)
            vacancy_id = input("Введите идентификатор вакансии для удаления: ")
            local_storage.delete_vacancy(vacancy_id)  # Используем экземпляр класса LocalStorage

        elif first_question == '2':
            sj_function(keyword_end, count_vacancy)
            keyword_local = input('Введите ключевое слово для поиска в локальном хранилище: ')
            results = local_storage.find_vacancy(keyword_local)  # Используем экземпляр класса LocalStorage
            print(f"Результаты поиска в локальном хранилище для ключевого слова '{keyword_local}':")
            for result in results:
                print(result)
            vacancy_id = input("Введите идентификатор вакансии для удаления: ")
            local_storage.delete_vacancy(vacancy_id)  # Используем экземпляр класса LocalStorage

        while True:
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
