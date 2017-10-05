import pandas as pd
import matplotlib.pyplot as plt

iris_data = pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/iris/bezdekIris.data',
                        names=['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'class'])

shuffled_data = iris_data.sample(frac=1)

train_data_size = 30
training_data = shuffled_data[:30]

plt.scatter(training_data[ training_data['class'] == 'Iris-setosa']['sepal_length'],
            training_data[ training_data['class'] == 'Iris-setosa']['sepal_width'],
            marker = 'x', color = 'b')

plt.scatter(training_data[ training_data['class'] == 'Iris-versicolor']['sepal_length'],
            training_data[ training_data['class'] == 'Iris-versicolor']['sepal_width'],
            marker = 'o', color = 'r')

plt.scatter(training_data[ training_data['class'] == 'Iris-virginica']['sepal_length'],
            training_data[ training_data['class'] == 'Iris-virginica']['sepal_width'],
            marker = '*', color = 'k')

plt.show()

