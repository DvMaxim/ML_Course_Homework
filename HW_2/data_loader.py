import pandas as pd
import json
import requests
import os


class DataLoader:
    @staticmethod
    def load_from_csv(file_path):
        """Загружает данные из CSV файла."""
        try:
            return pd.read_csv(file_path)
        except Exception as e:
            print(f"Ошибка загрузки CSV: {e}")
            return None

    @staticmethod
    def load_from_json(file_path):
        """Загружает данные из JSON файла."""
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                data = json.load(file)
            return pd.DataFrame(data)
        except Exception as e:
            print(f"Ошибка загрузки JSON: {e}")
            return None

    @staticmethod
    def load_from_api(url, params=None):
        """Загружает данные из API."""
        try:
            response = requests.get(url, params=params)
            response.raise_for_status()
            data = response.json()
            return pd.DataFrame(data)
        except Exception as e:
            print(f"Ошибка загрузки данных из API: {e}")
            return None


# Пример использования
if __name__ == "__main__":
    # Загрузка данных
    cwd = os.getcwd()
    file_path = os.path.join(cwd, r'hw_2_data\train.csv')  # Замените на путь к вашему CSV файлу
    data = DataLoader.load_from_csv(file_path)
    print(data.head())
