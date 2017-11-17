import numpy as np
import matplotlib.pyplot as plt

def computeCost(X, y, theta):
    # Length of samples(X)
    m = np.shape(X)[0]
    pred = np.dot(X, theta)
    err = (pred - y)
    # element wise squre
    errsq = np.square(err)
    J = np.sum(errsq)
    J = J/(2*m)
    return J

def gradientDescent(X, y, theta, alpha, iter_n):
    m = np.shape(X)[0]
    J_hist = np.zeros((iter_n, 1))

    for ind in range(1,iter_n):
        pred = np.dot(X, theta)
        err = pred - y
        ttheta = np.dot(np.transpose(X), err) * alpha * (1/m)
        theta = theta - ttheta
        J_hist[ind] = computeCost(X, y, theta)
    return theta

fd = open('ex1data1.txt')
data = np.genfromtxt('ex1data1.txt',delimiter=",")
X = data[:,0] #first column
y = data[:,1] # second column
plt.scatter(X,y, marker="x")
# plotting
#plt.show()
# Cost and Gradient decent
# Add column of ones y = mx+b form. Where 1 is b and m is slope
m = np.shape(X)[0]
tmp = np.ones((m,1))
X = X.reshape(m,1)
y = y.reshape(m,1)
tmp = np.append(tmp,X,axis=1)
# theta is for m and b
theta = np.zeros((2,1))
J = computeCost(tmp, y, theta)
print(J)
theta = ([-1], [2])
J = computeCost(tmp, y,np.array(theta))
print(J)
theta = np.zeros((2,1))
ttheta = gradientDescent(tmp, y, theta, 0.01, 1500)
print(ttheta)
