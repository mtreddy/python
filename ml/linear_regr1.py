import numpy as np
from sklearn.linear_model import LinearRegression

X = np.array([6, 8, 10, 14, 18]).reshape(-1, 1)
y = [7, 9, 13, 17.5, 18]

model = LinearRegression()
model.fit(X,y)
model.predict(12)[0]
#redidual sum of squares
# variance = sum(X-mean(X))/(n-1)
var = np.sum(np.square(X-np.mean(X)))/(np.shape(X)[0]-1)
# cov
cov = np.sum((X-np.mean(X))*((y - np.mean(y)).reshape(5,1)))/(np.shape(X)[0]-1)
# y = alpha + beta * x
beta = cov/var
alpha = np.mean(y) - beta * np.mean(X)

print(alpha, beta)

X_test = np.array([8, 9, 11, 16, 12]).reshape(-1, 1)
y_test = [11, 8.5, 15, 18, 11]

r_squared = model.score(X_test, y_test)

print(r_squared)
res_sum = np.sum((model.predict(X_test)-y_test)**2)
tot_sum = np.sum(np.square(y_test - np.mean(y_test)))

r_squared1 = 1 - (res_sum/tot_sum)
