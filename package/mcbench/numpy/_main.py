import numpy

def get_state(
    initial_state: numpy.ndarray,
    delta: numpy.ndarray,
    transition: numpy.ndarray,
    n_iter: int) -> numpy.ndarray:
    """_summary_

    Args:
        initial_state (numpy.ndarray): _description_
        delta (numpy.ndarray): _description_
        transition (numpy.ndarray): _description_
        n_iter (int): _description_

    Returns:
        numpy.ndarray: _description_
    """
    for i in range(n_iter):
        initial_state = (initial_state + delta) @ transition
    return initial_state
