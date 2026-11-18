from collections import Counter
import numpy as np
import statistics

def mean_median_mode(x: list) -> dict:
    """
    Returns a dictionary with mean, median, and mode.
    """
    # Write code here
    mean = sum(x)/len(x)
    median = statistics.median(x)
    mode = statistics.mode(x)
    return {
        "mean":mean,
        "median":float(median),
        "mode": float(mode)
    }
    pass