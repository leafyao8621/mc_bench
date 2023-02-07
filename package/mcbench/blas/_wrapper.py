import numpy
import mcbench._blas

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
    out = numpy.empty_like(initial_state, dtype=numpy.double)
    mcbench._blas.get_state(
        initial_state,
        delta, transition,
        initial_state.shape[0],
        n_iter,
        out
    )
    return out
