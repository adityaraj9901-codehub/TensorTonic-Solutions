import numpy as np
import statistics

def sample_var_std(x: list) -> dict:
    """
    Returns a dictionary with variance and standard_deviation.
    """
    # Write code here
    variance = statistics.variance(x)
    standard_deviation = statistics.stdev(x)
    return {
        "variance":float(variance),
        "standard_deviation":standard_deviation
    }
    pass