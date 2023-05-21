# Function to calculate gravitational attraction
# Matthew Gordon
# 24840416
# 07/11/21

def compute_attraction(m1: float,m2: float,r: float) -> float:
    """
    Compute gravitational attraction.

    :m1: Mass of ship 1 (Kg)

    :m2: Mass of ship 2 (Kg)

    :r: Distance between ship 1 and ship 2 (m)

    :return: Gravitaional attraction (N)
    """ 
    G = 6.6743e-11
    F = (G * m1 * m2) / (r * r) 
    return F 
