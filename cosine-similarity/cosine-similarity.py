import numpy as np

def cosine_similarity(a: list, b: list) -> float:
    """
    Returns the cosine similarity as a Python float.
    """
    dot_Product = np.dot(a,b)
    magnitude_a = np.linalg.norm(a)
    magnitude_b = np.linalg.norm(b)
    if magnitude_a==0 or magnitude_b ==0: return 0.0
    
    cosine_similarity =  (dot_Product)/(magnitude_a*magnitude_b)
    return float(cosine_similarity)   
    pass