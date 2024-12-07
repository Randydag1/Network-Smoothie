import numpy as np
import torch
import torch.nn as nn
import torch.optim as optim

class DynamicNeuralNetwork(nn.Module):
    def __init__(self, input_size, output_size):
        """
        Initializes a dynamic neural network with adjustable layers.
        
        :param input_size: Number of input features.
        :param output_size: Number of output features.
        """
        super(DynamicNeuralNetwork, self).__init__()
        self.layers = nn.ModuleList([
            nn.Linear(input_size, 64),
            nn.ReLU(),
            nn.Linear(64, output_size)
        ])

    def forward(self, x):
        """
        Forward pass through the network.
        """
        for layer in self.layers:
            x = layer(x)
        return x

    def add_layer(self, input_size, output_size):
        """
        Dynamically adds a new layer to the network.
        
        :param input_size: Number of input features for the new layer.
        :param output_size: Number of output features for the new layer.
        """
        self.layers.append(nn.Linear(input_size, output_size))
        self.layers.append(nn.ReLU())

    def remove_layer(self):
        """
        Removes the last two layers (Linear and ReLU) to adjust the network structure.
        """
        if len(self.layers) > 2:
            self.layers = self.layers[:-2]

def train_network(model, data, target, epochs=100, lr=0.01):
    """
    Trains the neural network using a given dataset.
    
    :param model: The dynamic neural network.
    :param data: Training data (features).
    :param target: Training labels.
    :param epochs: Number of epochs to train.
    :param lr: Learning rate.
    """
    criterion = nn.MSELoss()
    optimizer = optim.Adam(model.parameters(), lr=lr)

    for epoch in range(epochs):
        model.train()
        optimizer.zero_grad()
        output = model(data)
        loss = criterion(output, target)
        loss.backward()
        optimizer.step()

        if epoch % 10 == 0:
            print(f"Epoch {epoch}/{epochs}, Loss: {loss.item()}")

# Example usage
if __name__ == "__main__":
    # Example: Input data and target values
    input_data = torch.tensor([[1.0, 2.0], [3.0, 4.0]], dtype=torch.float32)
    target_data = torch.tensor([[5.0], [7.0]], dtype=torch.float32)

    # Initialize and train the network
    model = DynamicNeuralNetwork(input_size=2, output_size=1)
    train_network(model, input_data, target_data)