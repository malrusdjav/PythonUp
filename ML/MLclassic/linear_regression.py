import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

time_studied = np.array([70, 10, 60, 20, 50, 32, 65, 23, 43, 10, 5, 22, 35, 29, 5, 56]).reshape(-1, 1)
scores = np.array([92, 20, 78, 56, 83, 47, 93, 47, 82, 45, 38, 55, 67, 57, 15, 70]).reshape(-1, 1)

time_train, time_test, score_train, score_test = train_test_split(time_studied, scores, test_size=0.2)
model = LinearRegression()
model.fit(time_train, score_train)

print(model.score(time_test, score_test))

plt.scatter(time_studied, scores)

plt.plot(np.linspace(0, 70).reshape(-1, 1), model.predict(np.linspace(0, 70).reshape(-1, 1)), 'r')
plt.ylim(0, 100)
plt.show()
