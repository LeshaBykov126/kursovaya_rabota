import json

import requests

from utils.abstract_class import AbstractJobPlatform


class SuperJobPlatform(AbstractJobPlatform):
    """ Класс для работы с сайтом superjob.ru """

    def __init__(self, keyword, count_vacancy):
        self.keyword = keyword
        self.count_vacancy = count_vacancy

    def connect(self):
        """ Подключение к API superjob.ru """
        headers = {
            'X-Api-App-Id': 'your_app_id'
        }
        params = {
            'keyword': self.keyword,
            'count': self.count_vacancy
        }
        url = 'https://api.superjob.ru/2.0/vacancies/'
        response = requests.get(url, headers=headers, params=params)
        return response

    def get_jobs(self):
        """ Получение вакансий с superjob.ru """
        if self.connect().status_code == 200:
            data = self.connect().json()
            list_job = []
            for item in data['objects']:
                title = item['profession']
                link = item['link']
                salary_from = item['payment_from']
                salary_to = item['payment_to']
                salary_currency = item['currency']
                description = item['description']
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
        """ Создание файла для записи вакансий с сайта superjob.ru """
        with open('vacancy_list_sjru.json', 'w', encoding='utf-8') as json_file:
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
