import pandas as pd
import matplotlib.pyplot as plt

iris_data = pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/iris/bezdekIris.data',
                        names=['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'class'])

plt.scatter(iris_data[ iris_data['class'] == 'Iris-setosa']['sepal_length'],
            iris_data[ iris_data['class'] == 'Iris-setosa']['sepal_width'],
            marker = 'x', color = 'b')

plt.scatter(iris_data[ iris_data['class'] == 'Iris-versicolor']['sepal_length'],
            iris_data[ iris_data['class'] == 'Iris-versicolor']['sepal_width'],
            marker = 'o', color = 'r')

plt.scatter(iris_data[ iris_data['class'] == 'Iris-virginica']['sepal_length'],
            iris_data[ iris_data['class'] == 'Iris-virginica']['sepal_width'],
            marker = '*', color = 'k')

plt.show()

plt.scatter(iris_data[ iris_data['class'] == 'Iris-setosa']['petal_length'],
            iris_data[ iris_data['class'] == 'Iris-setosa']['petal_width'],
            marker = 'x', color = 'b')

plt.scatter(iris_data[ iris_data['class'] == 'Iris-versicolor']['petal_length'],
            iris_data[ iris_data['class'] == 'Iris-versicolor']['petal_width'],
            marker = 'o', color = 'r')

plt.scatter(iris_data[ iris_data['class'] == 'Iris-virginica']['petal_length'],
            iris_data[ iris_data['class'] == 'Iris-virginica']['petal_width'],
            marker = '*', color = 'k')

plt.show()
