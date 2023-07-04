class Vacancy:
    """ Класс для создания экземпляра класса вакансий """
    all_class_vacancy = []  # список экземпляров класса

    def __init__(self, id_vacancy, title, link, salary_min, salary_max, description):
        self.id = id_vacancy
        self.title = title
        self.link = link
        self.description = description
        self.salary_min = salary_min
        self.salary_max = salary_max

        Vacancy.all_class_vacancy.append(self)

    def __gt__(self, other):
        return int(self.salary_min) > int(other.salary_min)

    def __ge__(self, other):
        return int(self.salary_min) >= int(other.salary_min)

    def __lt__(self, other):
        return int(self.salary_min) < int(other.salary_min)

    def __le__(self, other):
        return int(self.salary_min) <= int(other.salary_min)

    def __eq__(self, other):
        return int(self.salary_min) == int(other.salary_min)

    def __str__(self):
        return f"id: {self.id}\n" \
               f"Название вакансии: {self.title}\n" \
               f"Ссылка на вакансию: {self.link}\n" \
               f"Зарплата от {self.salary_min} до {self.salary_max}\n" \
               f"Описание вакансии: {self.description}\n"

    @classmethod
    def class_vacancy_ex(cls, list_vacancy):
        """ Создание экземпляров класса из списка словарей """
        for row in list_vacancy:
            if 'id' in row:
                salary_min = row.get('salary_min')
                if salary_min is None:
                    salary_min = 'Не указан'
                salary_max = row.get('salary_max')
                if salary_max is None:
                    salary_max = 'Не указан'
                cls(row['id'], row['title'], row['link'], salary_min, salary_max, row['description'])
            else:
                cls('Не указан', row['title'], row['link'], 'Не указан', 'Не указан', row['description'])
