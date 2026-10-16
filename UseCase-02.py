import numpy as np
from sklearn.neural_network import MLPClassifier

# Input values for AND gate
X = np.array([
    [0, 0],
    [0, 1],
    [1, 0],
    [1, 1]
])

# Expected output values
y = np.array([0, 0, 0, 1])

# Create and train the neural network
model = MLPClassifier(
    hidden_layer_sizes=(4,),
    activation="relu",
    solver="lbfgs",
    max_iter=2000,
    random_state=1
)

model.fit(X, y)

# Predict output for each input
print("AND gate output:")

for inputs in X:
    output = model.predict([inputs])[0]
    print(f"{inputs[0]} AND {inputs[1]} = {output}")

print("Training completed")
"""
AND gate output:
0 AND 0 = 0
0 AND 1 = 0
1 AND 0 = 0
1 AND 1 = 1
Training completed
"""
