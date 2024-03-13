import random
import time

class Neuron:
    def __init__(self, id, inhibit=False, mimic=None):
        self.id = id
        self.connections = []
        self.inhibit = inhibit
        self.mimic = mimic if mimic else round(random.uniform(0.1, 9.9), 1)
        self.children = []

    def connect(self, neuron):
        if not self.inhibit:
            self.connections.append(neuron)

    def communicate(self, dataset, neurons):
        if not self.inhibit:
            # Generate a random number between 0 and 1
            random_number = random.random()
            # Calculate the weighted sum of the inputs
            weighted_sum = sum([connection.id * random_number for connection in self.connections])
            # Add the mimic factor to the weighted sum
            message = round(weighted_sum * self.mimic, 1)
            # Communicate the message to the connected neurons
            for connection in self.connections:
                # Add a random delay between messages
                time.sleep(random.uniform(0, 1))
                connection.receive(message, sender=self)

    def receive(self, message, sender=None):
        # Print the message received by the neuron and where it was received from
        print(f"Neuron {self.id} received message {message} from Neuron {sender.id if sender else 'Dataset'}")

    def mutate(self):
        # Randomly change the inhibit and mimic genes
        self.inhibit = not self.inhibit
        if random.random() < 0.5:
            self.mimic = round(random.uniform(0.1, 9.9), 1)

    def grow(self, neurons):
        # Randomly create a new neuron and add it to the list of neurons
        if random.random() < 0.1 and not self.inhibit:
            new_neuron = Neuron(len(neurons), inhibit=False, mimic=round(random.uniform(0.1, 9.9), 1))
            self.children.append(new_neuron)
            neurons.append(new_neuron)
            new_neuron.mutate()
            self.connect(new_neuron)

# Create a list of neurons
neurons = [Neuron(i) for i in range(20)]

# Connect the neurons randomly
for i in range(10):
    for j in range(i+1, 10):
        random_neuron1 = random.choice(neurons)
        random_neuron2 = random.choice(neurons)
        random_neuron1.connect(random_neuron2)

# Create a dataset
dataset = list(range(1, 101))

# Communicate the dataset to the neurons
for neuron in neurons:
    neuron.communicate(dataset, neurons)

# Make the neurons mutate and grow
for neuron in neurons:
    neuron.mutate()
    neuron.grow(neurons)

# Wait for a short time
time.sleep(1)