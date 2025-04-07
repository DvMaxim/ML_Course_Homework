import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os


class DataVisualization:
    @staticmethod
    def plot_histogram(df, column, bins=30):
        """Строит гистограмму для указанного столбца."""
        plt.figure(figsize=(8, 5))
        sns.histplot(df[column], bins=bins, kde=True)
        plt.title(f'Гистограмма {column}')
        plt.xlabel(column)
        plt.ylabel('Частота')
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
    #DataVisualization.plot_histogram(df, 'SalePrice')
    #DataVisualization.plot_scatter(df, 'GrLivArea', 'SalePrice')
    DataVisualization.plot_line(df, 'YearBuilt', 'SalePrice')
