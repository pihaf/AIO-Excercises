import random
import math

def calculate_loss_function():
    # Get number of samples and validate the input if number
    num_samples = input("Input number of samples (integer number) which are generated: ")
    if not num_samples.isnumeric():
        print("number of samples must be an integer number")
        return 
    num_samples = int(num_samples)

    # Get user loss function and validate name
    loss_function = input("Input loss function name: ")
    if loss_function not in ("MAE", "MSE", "RMSE"):
        print(f'{loss_function} is not supported')
        return

    # Create a list to store loss value of each sample
    loss_values = []

    # Loop and calculate loss of each sample
    for i in range(0, num_samples):
        prediction = random.uniform(0,10)
        target = random.uniform(0,10)
        if loss_function == 'MAE':
            loss = abs(prediction - target)
        elif loss_function == 'MSE':
            loss = (prediction - target) ** 2
        elif loss_function == 'RMSE':
            loss = math.sqrt((prediction - target) ** 2)

        loss_values.append(loss)
        print(f'loss name: {loss_function}, sample: {i}, pred: {prediction}, target: {target},')
        print(f'    loss: {loss}')

    # Calculate final loss and print result
    final_loss = sum(loss_values) / num_samples
    print(f'final {loss_function}: {final_loss}')

calculate_loss_function()