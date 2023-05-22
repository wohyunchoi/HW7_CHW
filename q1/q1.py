import numpy as np

if __name__ == "__main__":
    eig = np.linalg.eig
    matrix = np.array([[1,2],[3,4]])

    value = eig(matrix)[0]
    vector = eig(matrix)[1]
    determinant = np.linalg.det(matrix)

    print('Eigenvalue :',value)
    print('Eigenvector :\n', vector)
    print('Determinant :', determinant)

    vec1 = [1,2,3]
    vec2 = [4,5,6]

    print("\ncrossproduct: ",np.cross(vec1,vec2))

    a = np.array([[1,2,-2],[2,1,-5],[1,-4,1]])
    b = np.array([-15,-21,18])
    print("\nsolution: ",np.linalg.solve(a,b))
