import numpy as np

# Activation functions
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def sigmoid_derivative(x):
    return x * (1 - x)

# Training data (XOR problem)
X = np.array([[0,0],
              [0,1],
              [1,0],
              [1,1]])

y = np.array([[0],
              [1],
              [1],
              [0]])

# Hyperparameters
epochs = 10000
lr = 0.1
input_dim = 2
hidden_dim = 2
output_dim = 1

# Initialize weights and biases
np.random.seed(42)
W1 = np.random.uniform(-1, 1, (input_dim, hidden_dim))
b1 = np.zeros((1, hidden_dim))
W2 = np.random.uniform(-1, 1, (hidden_dim, output_dim))
b2 = np.zeros((1, output_dim))

# Training
for epoch in range(epochs):
    # Forward pass
    z1 = np.dot(X, W1) + b1
    a1 = sigmoid(z1)
    z2 = np.dot(a1, W2) + b2
    a2 = sigmoid(z2)
    
    # Compute error
    error = y - a2
    
    # Backpropagation
    d_a2 = error * sigmoid_derivative(a2)
    d_a1 = np.dot(d_a2, W2.T) * sigmoid_derivative(a1)
    
    # Update weights and biases
    W2 += np.dot(a1.T, d_a2) * lr
    b2 += np.sum(d_a2, axis=0, keepdims=True) * lr
    W1 += np.dot(X.T, d_a1) * lr
    b1 += np.sum(d_a1, axis=0, keepdims=True) * lr
    
    # Print loss occasionally
    if epoch % 2000 == 0:
        loss = np.mean(np.square(error))
        print(f"Epoch {epoch}, Loss: {loss:.4f}")

# Final predictions
print("\nPredictions after training:")
print(a2)
