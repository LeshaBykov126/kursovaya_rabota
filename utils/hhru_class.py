import json

import requests

from utils.abstract_class import AbstractJobPlatform


class HHJobPlatform(AbstractJobPlatform):
    """ Класс для работы с сайтом hh.ru """

    def __init__(self, count_vacancy):
        self.count_vacancy = count_vacancy

    def connect(self):
        """ Подключение к API hh.ru """
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0;Win64) AppleWebkit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36',
            'Accept': 'application/json'
        }
        params = {
            'per_page': self.count_vacancy
        }
        url = 'https://api.hh.ru/vacancies'
        response = requests.get(url, headers=headers, params=params)
        return response

    def get_jobs(self):
        """ Получение вакансий с hh.ru """
        if self.connect().status_code == 200:
            data = self.connect().json()
            list_job = []
            for item in data['items']:
                title = item['name']
                link = item['alternate_url']
                salary = item['salary']
                if salary:
                    salary_from = salary.get('from', 'Не указана')
                    salary_to = salary.get('to', 'Не указана')
                    salary_currency = salary.get('currency', 'Не указана')
                else:
                    salary_from = 'Не указана'
                    salary_to = 'Не указана'
                    salary_currency = 'Не указана'

                description = item['snippet']['requirement']
                jobs = {
                    'title': title,
                    'link': link,
                    'salary_from': salary_from,
                    'salary_to': salary_to,
                    'salary_currency': salary_currency,
                    'description': description
                }
                list_job.append(jobs)
            self.write_file_vacancy(list_job)
            return list_job
        else:
            print(f"Проблема с сетью, статус ошибки: {self.connect().status_code}")

    def write_file_vacancy(self, jobs):
        """ Создание файла для записи вакансий с сайта hh.ru """
        with open('vacancy_list_hhru.json', 'w', encoding='utf-8') as json_file:
            json.dump(jobs, json_file, sort_keys=False, indent=4, ensure_ascii=False)

    def save_vacancy(self, jobs):
        """ Сохранение вакансий в локальное хранилище """
        self.vacancies.extend(jobs)

    def find_vacancy(self, keyword):
        """ Поиск вакансий по ключевому слову """
        results = []
        for vacancy in self.vacancies:
            if keyword.lower() in vacancy['title'].lower() or keyword.lower() in vacancy['description'].lower():
                results.append(vacancy)
        return results

    def delete_vacancy(self, vacancy_id):
        """ Удаление вакансии по идентификатору """
        for vacancy in self.vacancies:
            if vacancy['id'] == vacancy_id:
                self.vacancies.remove(vacancy)
                break
