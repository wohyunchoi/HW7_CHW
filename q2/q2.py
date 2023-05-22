import numpy as np

def cos_sim(A,B):
    return np.dot(A,B)/(np.linalg.norm(A)*np.linalg.norm(B))

if __name__ == "__main__":

    docs = np.array([[1,1,0,1,0,1],[1,1,1,0,1,0],[1,1,0,1,0,0]])

    query = np.array([1,1,0,0,1,0])


    print("doc1=%0.2f" %cos_sim(docs[0],query))
    print("doc2=%0.2f" %cos_sim(docs[1],query))
    print("doc3=%0.2f" %cos_sim(docs[2],query))
