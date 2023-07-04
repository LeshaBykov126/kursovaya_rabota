import json


class LocalStorage:
    """Класс для локального хранения и работы с данными"""

    @staticmethod
    def save_data(data, filename):
        """Сохранение данных в файл"""
        with open(filename, 'w', encoding='utf-8') as json_file:
            json.dump(data, json_file, sort_keys=False, indent=4, ensure_ascii=False)

    @staticmethod
    def load_data(filename):
        """Загрузка данных из файла"""
        with open(filename, 'r', encoding='utf-8') as json_file:
            data = json.load(json_file)
            return data
