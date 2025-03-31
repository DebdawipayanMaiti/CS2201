import random
import matplotlib.pyplot as plt

# Number of trials
n = int(input("Enter the number of tosses: "))  # You can increase this for better estimation

# Variables to track the number of heads and estimated probability
heads_count = 0
estimated_probabilities = []

# Simulating the coin tosses
for i in range(1, n + 1):
    if random.random() < 0.5:  # If random number < 0.5, count it as heads
        heads_count += 1
    
    # Compute the fraction of heads (estimated probability)
    estimated_prob = heads_count / i
    estimated_probabilities.append(estimated_prob)

# Plot the estimated probability over trials
plt.plot(range(1, n + 1), estimated_probabilities, label='Estimated Probability')
plt.axhline(y=0.5, color='r', linestyle='--', label='Theoretical Probability')
plt.xlabel("Number of Trials")
plt.ylabel("Estimated Probability of Heads")
plt.title("Estimating Probability of Heads in a Coin Toss")
plt.legend()
plt.show()
