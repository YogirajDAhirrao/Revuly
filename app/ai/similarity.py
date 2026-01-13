import numpy as np

def cosine_similarity(vec1: list[float],vec2:list[float])->float:
    v1 = np.array(vec1)
    v2 = np.array(vec2)

    denom = (np.linalg.norm(v1)*np.linalg.norm(v2))
    if denom == 0:
        return 0.0
    return float(np.dot(v1,v2)/denom)