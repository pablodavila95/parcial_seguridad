import numpy as np
from perceptron import Perceptron

def generate_ciphertexts(key):
    ciphertexts = []
    with open('neuralnet/trainP.csv', 'r') as read_obj:
        csv_reader = reader(read_obj)
        for row in csv_reader:
            ciphertexts.append(encrypt(''.join(map(str, row)), key))
    return ciphertexts

training_inputs = []
training_inputs.append(np.array([1, 1]))
training_inputs.append(np.array([1, 0]))
training_inputs.append(np.array([0, 1]))
training_inputs.append(np.array([0, 0]))

labels = np.array([1, 0, 0, 0])

perceptron = Perceptron(2)
perceptron.train(training_inputs, labels)

inputs = np.array([1, 1])
perceptron.predict(inputs) 
#=> 1

inputs = np.array([0, 1])
perceptron.predict(inputs) 
#=> 0