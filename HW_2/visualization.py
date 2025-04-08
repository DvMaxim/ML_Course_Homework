import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os


class DataVisualization:
    @staticmethod
    def plot_histogram(df, column, bins='auto'):
        """Строит гистограмму для указанного столбца."""
        plt.figure(figsize=(8, 5))
        sns.histplot(df[column], bins=bins, kde=True)
        plt.title(f'Гистограмма {column}')
        plt.xlabel(column)
        plt.ylabel('Частота')
        plt.show()

    @staticmethod
    def plot_price_by_year_built(df):
        """Строит график зависимости средней цены от года постройки."""
        plt.figure(figsize=(10, 6))
        sns.lineplot(data=df, x='yearbuilt', y='avg_sale_price', marker='o')
        plt.title('Средняя цена продажи по году постройки')
        plt.xlabel('Год постройки')
        plt.ylabel('Средняя цена продажи')
        plt.grid(True)
        plt.tight_layout()
        plt.show()

    @staticmethod
    def plot_boxplot(df, x_column, y_column):
        plt.figure(figsize=(10, 6))
        sns.boxplot(data=df, x=x_column, y=y_column)
        plt.title(f"Распределение {y_column} по {x_column}")
        plt.xlabel(x_column)
        plt.ylabel(y_column)
        plt.grid(True)
        plt.tight_layout()
        plt.show()

    @staticmethod
    def plot_predictions(y_true, y_pred, num_points=50):
        plt.figure(figsize=(10, 6))
        plt.scatter(range(num_points), y_true[:num_points], color='blue', label='Истинные значения')
        plt.scatter(range(num_points), y_pred[:num_points], color='red', label='Предсказанные значения')
        plt.xlabel('Индекс')
        plt.ylabel('Значение charges')
        plt.title(f'Истинные и предсказанные значения charges (первые {num_points} точек)')
        plt.legend()
        plt.show()


if __name__ == "__main__":
    # Загрузка данных
    cwd = os.getcwd()
    file_path = os.path.join(cwd, r'hw_2_data\train.csv')  # Замените на путь к вашему CSV файлу
    df = pd.read_csv(file_path)
    DataVisualization.plot_histogram(df, 'SalePrice')
    #DataVisualization.plot_scatter(df, 'GrLivArea', 'SalePrice')
    #DataVisualization.plot_line(df, 'YearBuilt', 'SalePrice')
