import json

from utils.hhru_class import HHJobPlatform
from utils.sj_class import SuperJobPlatform
from utils.vacancy_class import Vacancy


def hh_function(keyword, count_vacancy):
    """ Функция вызова класса для работы с hh ру """
    get_list = HHJobPlatform(keyword, count_vacancy)  # Создаем экземпляр класса с параметрами пользователя
    list_job = get_list.get_jobs()  # Получаем список вакансий из класса
    print(f'Нашлось {len(list_job)} вакансий.')
    Vacancy.all_class_vacancy = []
    Vacancy.class_vacancy_ex(list_job)
    for item in Vacancy.all_class_vacancy:  # Перебираем и выводим список
        print(str(item))
    print('Чтобы перейти на вакансию, нажми на ссылку')


def sj_function(keyword, count_vacancy):
    """ Функция вызова класса для работы с superjob """
    get_list = SuperJobPlatform(keyword, count_vacancy)  # Создаем экземпляр класса с параметрами пользователя
    list_job = get_list.get_jobs()  # Получаем список вакансий из класса
    print(f'Нашлось {len(list_job)} вакансий!')
    Vacancy.all_class_vacancy = []
    Vacancy.class_vacancy_ex(list_job)
    for item in Vacancy.all_class_vacancy:  # Перебираем и выводим список
        print(str(item))
    print('Чтобы перейти на вакансию, нажми на ссылку')
    # Даём возможность вывести данные в уменьшенном варианте, т.к. в superjob длинное описание
    short_answer = input('Вывести только наименование вакансии, зарплату и ссылку? да/нет\n')
    if short_answer.lower() == 'да' or short_answer.lower() == 'lf':
        with open('vacancy_list_sjru.json', 'r', encoding='utf-8') as file:  # Получаем список из файла
            data = json.load(file)
            for i in data:  # Перебираем список и выводим нужные параметры
                print('Вакансия:', i['title'])
                print('Ссылка:', i['link'])
                print('Зарплата: от', i['salary_min'], ' до', i['salary_max'], '\n')
                print('Чтобы перейти на вакансию, нажми на ссылку')
