import matplotlib.pyplot as plt
from scipy.spatial import ConvexHull
import numpy as np

# Зчитування датасету
data = np.loadtxt('DS8.txt')

# Знаходження опуклої оболонки
hull = ConvexHull(data)

# Збереження опуклої оболонки як окремого датасету
hull_points = data[hull.vertices]
np.savetxt('hull_dataset.txt', hull_points)

# Встановлення розмірів вікна
plt.figure(figsize=(960/100, 540/100), dpi=100)

# Відображення опуклої оболонки
for simplex in hull.simplices:
    plt.plot(data[simplex, 0], data[simplex, 1], 'b-')

# Відображення точок вихідного датасету
plt.plot(data[:, 0], data[:, 1], 'o')

# Збереження результатів у файл графічного формату
plt.savefig('convex_hull.png')

# Показати полотно
plt.show()
