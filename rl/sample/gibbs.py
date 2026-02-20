#gibbs sampling 

import numpy as np
import matplotlib.pyplot as plt

# Define correlated bi variate distribution
mean = np.array([0,0])
rho = 0.9 # Correlation coefcient

def sample_x_given_y(y):
    # P(X/Y)
    mu = rho * y
    sigma = np.sqrt(1-rho**2)
    return np.random.normal(mu, sigma)

def sample_y_given_x(x):
    #P(Y/X)
    mu = rho * x
    sigma = np.sqrt(1-rho**2)
    return np.random.normal(mu, sigma)

n_steps = 50
x_history = [4]
y_history = [4]

for i in range(n_steps):
    #Move horizontally
    new_x = sample_x_given_y(y_history[-1])
    x_history.append(new_x)
    y_history.append(y_history[-1]) # y stays same
    #move vertically
    new_y = sample_y_given_x(x_history[-1])
    x_history.append(x_history[-1])
    y_history.append(new_y)


plt.figure(figsize=(8,8))

x_grid, y_grid = np.mgrid[-5:5:.01, -5:5:.01]
pos = np.dstack((x_grid, y_grid))
from scipy.stats import multivariate_normal

rv = multivariate_normal([0,0], [[1, rho],[rho, 1]])
plt.contour(x_grid, y_grid, rv.pdf(pos), levels=5, colors='gray', alpha=0.5)

#plot
plt.plot(x_history, y_history, color='blue', alpha=0.6, label='Gibbs Path', lw=1)
plt.scatter(x_history, y_history, c=range(len(x_history)), cmap='viridis', s=10)
plt.title(f"Gibbs samplein visual trace (correlation={rho})")
plt.xlabel('X var')
plt.ylabel('Y var')
plt.grid(True, alpha=0.3)
plt.legend()
plt.show()