import json
from abc import ABC

import requests
from utils.abstract_class import AbstractJobPlatform


class HHJobPlatform(AbstractJobPlatform, ABC):
    """ Класс для работы с сайтом hh """

    def __init__(self, keyword, count_vacancy):
        self.count_vacancy = count_vacancy  # Кол-во вакансий для поиска
        self.keyword = keyword  # Ключевое слово для поиска
        self.salary_min = None  # Минимальная зарплата

    def connect(self, params=None):
        """ Подключение к API hh """
        url = 'https://api.hh.ru/vacancies'
        params = {'text': self.keyword,  # Ключевое слово для поиска вакансий
                  "per_page": self.count_vacancy  # Кол-во вакансий на странице
                  }
        headers = {
            "User-Agent": "50355527",  # User-Agent header
        }
        response = requests.get(url, params=params, headers=headers)
        return response

    def get_jobs(self, **kwargs):
        """ Создание словаря вакансий """
        if self.connect().status_code == 200:
            data = self.connect().json()
            list_job = []
            for item in data['items']:
                id_vacancy = item['id']
                title = item['name']
                link = item['alternate_url']

                if item['salary']:
                    salary_min = item['salary']['from']
                    salary_max = item['salary']['to']

                else:
                    salary_min = 'Не указана'
                    salary_max = 'Не указана'

                description = item['snippet']['requirement'] if item['snippet'] and 'requirement' in item[
                    'snippet'] else None
                #  Создание словарей из вакансий
                jobs = {
                    'id': id_vacancy,
                    'title': title,
                    'link': link,
                    'salary_min': salary_min,
                    'salary_max': salary_max,
                    'description': description
                }
                list_job.append(jobs)  # Добавление словаря в список
            self.write_file_vacancy(list_job)
            return list_job
        else:
            print(f"Проблема с сетью, статус ошибки: {self.connect().status_code}")

    def write_file_vacancy(self, jobs):
        """ Создание файла для записи вакансий с сайта hh """
        with open('vacancy_list_hhru.json', 'w', encoding='utf-8') as json_file:
            json.dump(jobs, json_file, sort_keys=False, indent=4, ensure_ascii=False)
