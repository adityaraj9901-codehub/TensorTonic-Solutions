import numpy as np

def expected_value_discrete(x: list, p: list) -> float:
    """
    Returns the expected value as a Python float.
    """
    # Write code here
    x_array = np.array(x)
    p_array = np.array(p)
    expected_value_discrete = sum(x*p for (x,p) in zip(x_array,p_array))
    return float(expected_value_discrete)
    pass