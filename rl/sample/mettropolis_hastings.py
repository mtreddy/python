import numpy as np
import matplotlib.pyplot as plt

def target_distribution(x):
    # Two gausian  peaks
    peak1 = np.exp(-0.5 * (x+2)**2)
    peak2 = np.exp(-0.5 * (x-2)**2)
    return peak1 +  peak2
def metropolis_hastings(n_samples=5000, jump_size=1.0):
    samples = []
    current_x = 0 # start at 0

    for _ in range(n_samples):
        #Step1 - propose a move
        proposal_x = np.random.normal(current_x, jump_size)
        
        #step-2 caluclate heights of the peaks
        prob_current = target_distribution(current_x)
        prob_proposal = target_distribution(proposal_x)

        #Step-3 acceptance rule
        alpha = prob_proposal / prob_current
        #print(alpha)
        # if aplha > 1
        # if proposal random number < alpha
        if np.random.rand() < alpha:
            current_x = proposal_x

        samples.append(current_x)

    return np.array(samples)

samples = metropolis_hastings(n_samples=10000, jump_size=2.0)

plt.figure(figsize=(10, 6))

#plot histogram of samples
plt.hist(samples, bins=50, density=True, color='skyblue', alpha=0.7, laber='Sample Distribution')

#Plot the true math function for comparision
x_range = np.linspace(-6, 6, 500)
plt.plot(x_range, target_distribution(x_range)/3.5, color='red', lw=2, laber='True Function')

plt.title("Metroplois-hastings: Discovering Two peaks")
plt.xlabel("position (x)")
plt.ylabel("Prob density")
plt.legend()
plt.show()

