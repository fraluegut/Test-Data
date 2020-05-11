"""
import mglearn
from matplotlib import pyplot as plt

# Generate dataset
x, y = mglearn.datasets.make_forge()

#plot dataset
mglearn.discret_scatter(x[:, 0], x[:,1], y)
plt.legend(["Class 0", "Class 1"], loc=4)
plt.xlabel("First feature")
plt.ylabel("Second feature")
print("x.shape: {}".format(x.shape))
"""



from sklearn.datasets import load_breast_cancer
cancer = load_breast_cancer()
x_train, x_test, y_train, y_test = train_test_split(cancer.data, cancer.target, stratify=cancer.target, random_state=66)
training_accuracy = []

print("cancer.keys(): \n{}".format(cancer.keys()))