import pandas as pd
import math
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import os
from data_loader import DataLoader


class DataProcessing:

    @staticmethod
    def preprocess_data(df, target_column):
        """
        Предобработка данных: разделение на признаки и целевую переменную, масштабирование признаков.
        :param df: DataFrame с данными.
        :param target_column: Имя столбца с целевой переменной.
        :return: Обработанные признаки, целевая переменная, препроцессор.
        """
        X = df.drop(columns=[target_column])
        y = df[target_column]

        # Определение числовых и категориальных признаков
        numeric_features = ['1stFlrSF', '2ndFlrSF', 'BedroomAbvGr', 'KitchenAbvGr']
        categorical_features = ['OverallQual', 'OverallCond', 'MSZoning', 'KitchenQual']

        # Создание препроцессора
        numeric_transformer = StandardScaler()
        categorical_transformer = OneHotEncoder(drop='first')

        preprocessor = ColumnTransformer(
            transformers=[
                ('num', numeric_transformer, numeric_features),
                ('cat', categorical_transformer, categorical_features)
            ])

        # Применение препроцессора к данным
        X_processed = preprocessor.fit_transform(X)
        return X_processed, y, preprocessor

    @staticmethod
    def train_model(X, y):
        """
        Обучение модели линейной регрессии.
        :param X: Признаки.
        :param y: Целевая переменная.
        :return: Обученная модель.
        """
        model = LinearRegression()
        model.fit(X, y)
        return model

    @staticmethod
    def predict(model, X):
        """
        Предсказание на новых данных.
        :param model: Обученная модель.
        :param X: Признаки.
        :return: Предсказанные значения.
        """
        return model.predict(X)

    @staticmethod
    def evaluate_model(y_true, y_pred):
        """
        Оценка модели с использованием метрик MSE и R^2.
        :param y_true: Истинные значения.
        :param y_pred: Предсказанные значения.
        :return: MSE, R^2.
        """
        mse = mean_squared_error(y_true, y_pred)
        rmse = math.sqrt(mse)
        r2 = r2_score(y_true, y_pred)
        return rmse, r2

    @staticmethod
    def check_missing_values(df):
        """Возвращает столбцы с пропусками значений и их количеством."""
        missing_values = df.isnull().sum()
        print("\nОбщее кол-во пустых значений: ", missing_values.sum(), "\n")
        return missing_values[missing_values > 0]

    @staticmethod
    def fill_missing_values(df):
        """Заполняет пропущенные значения в DataFrame в зависимости от типа данных."""
        for column in df.columns:
            if pd.api.types.is_object_dtype(df[column]):
                df.fillna({column: df[column].mode()[0]}, inplace=True)  # Заполняем самым частым значением
            else:
                df.fillna({column: df[column].median()}, inplace=True)  # Заполняем медианой

        return df

    @staticmethod
    def describe_data(df):
        """Возвращает общую информацию и статистику по DataFrame."""
        return df.describe()


if __name__ == "__main__":
    # data = {'A': [1, 2, None, 4], 'B': [None, 2, 3, 4], 'C': [1, 2, 3, 4]}
    # df = pd.DataFrame(data)
    # print(DataProcessing.check_missing_values(df))
    cwd = os.getcwd()
    file_path = os.path.join(cwd, r'hw_2_data\train.csv')  # Замените на путь к вашему CSV файлу

    data = DataLoader.load_from_csv(file_path)
    # Print all columns with missing values and its counts
    print(f"\nBefore:\n\n{DataProcessing.check_missing_values(data)}\n---------------------\n")
    DataProcessing.fill_missing_values(data)
    print(f"\nAfter:\n\n{DataProcessing.check_missing_values(data)}\n")
