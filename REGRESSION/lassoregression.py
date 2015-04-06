import scipy.io as io
import scipy.sparse as sp
import scipy.linalg as la
import numpy as np

def l1_norm(x):
    return np.sum(np.abs(x))

def l2_norm(x):
    return np.dot(x.ravel().T, x.ravel())

def fast_threshold(x, threshold):
    return np.multiply(np.sign(x), np.fmax(abs(x) - threshold, 0))

def lasso_admm(X, A, gamma):
    c = X.shape[1]
    r = A.shape[1]

    C = io.loadmat("C.mat")["C"]

    L = np.zeros(X.shape)

    rho = 1e-4
    maxIter = 200
    I = sp.eye(r)
    maxRho = 5

    cost = []

    for n in range(maxIter):
        B = la.solve(np.dot(A.T, A) + rho * I, np.dot(A.T, X) + rho * C - L)

        C = fast_threshold(B + L / rho, gamma / rho)

        L = L + rho * (B - C);  

        rho = min(maxRho, rho * 1.1); 

        cost.append(0.5 * l2_norm(X - np.dot(A, B)) + gamma * l1_norm(B))

    cost = np.array(cost).ravel()

    return B, cost

data = io.loadmat("lasso.mat")
A = data["A"]
X = data["X"]    
B, cost = lasso_admm(X, A, gamma)
