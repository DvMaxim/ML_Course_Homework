# main.py
import os
import math
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from data_loader import DataLoader
from data_processing import DataProcessing
from visualization import DataVisualization
from sklearn.metrics import mean_squared_error

if __name__ == '__main__':
    # Загрузка данных
    cwd = os.getcwd()
    file_path = os.path.join(cwd, r'hw_2_data\train.csv')  # Замените на путь к вашему CSV файлу

    data = DataLoader.load_from_csv(file_path)

    # Print all columns with missing values and its counts

    print(f"Распределение пустых значений по столбцам:\n\n{DataProcessing.check_missing_values(data)}")
    print("\nУбираем пустые значения...")
    DataProcessing.fill_missing_values(data)
    print(f"Распределение пустых значений по столбцам:\n\n{DataProcessing.check_missing_values(data)}\n")

    # Предобработка данных
    target_column = 'SalePrice'

    X, y, preprocessor = DataProcessing.preprocess_data(data, target_column)

    # Разделение данных на тренировочную и тестовую выборки
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

    # Обучение модели
    model = DataProcessing.train_model(X_train, y_train)

    # Предсказание на тестовых данных
    y_pred = DataProcessing.predict(model, X_test)

    # Оценка модели
    rmse, r2 = DataProcessing.evaluate_model(y_test, y_pred)

    print(f"Среднеквадратичная ошибка: {rmse / data['SalePrice'].mean():.2f}")
    print(f"Коэффициент детерминации R^2: {r2:.2f}")

    DataVisualization.plot_predictions(y_test, y_pred)