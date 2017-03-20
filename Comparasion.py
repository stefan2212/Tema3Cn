import numpy as np
class Comparasion:
    def __init__(self):
        return

    def compareDiag(self, diag_a, diag_b):
        diag_a=np.array(diag_a)
        diag_b=np.array(diag_b)
        return (diag_a == diag_b).all()
