from abc import ABC, abstractmethod


class AbstractJobPlatform(ABC):
    """Абстрактный класс для локального хранения вакансий"""

    @abstractmethod
    def save_vacancy(self, vacancy):
        """Метод для сохранения вакансии"""
        pass

    @abstractmethod
    def find_vacancy(self, keyword):
        """Метод для поиска вакансий по ключевому слову"""
        pass

    @abstractmethod
    def delete_vacancy(self, vacancy_id):
        """Метод для удаления вакансии по идентификатору"""
        pass


class LocalStorage(AbstractJobPlatform):
    """Класс для локального хранения вакансий"""

    def __init__(self):
        self.vacancies = []

    def save_vacancy(self, vacancy):
        """Метод для сохранения вакансии"""
        self.vacancies.append(vacancy)

    def find_vacancy(self, keyword):
        """Метод для поиска вакансий по ключевому слову"""
        result = []
        for vacancy in self.vacancies:
            if keyword.lower() in vacancy.title.lower() or keyword.lower() in vacancy.description.lower():
                result.append(vacancy)
        return result

    def delete_vacancy(self, vacancy_id):
        """Метод для удаления вакансии по идентификатору"""
        for vacancy in self.vacancies:
            if vacancy.id == vacancy_id:
                self.vacancies.remove(vacancy)
                break
