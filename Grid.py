import numpy as np

class Grid:
    """Define a grid from the position of the faces"""

    def __init__(self, faces):

        self.faces = faces
        self.cell_position = np.zeros(len(faces)-1)
        self.cell_length = np.zeros(len(faces)-1)

        for i in range(len(self.cell_length)):
            self.cell_position[i] = (faces[i+1] + faces[i])/2
            self.cell_length[i]   =  faces[i+1] - faces[i]

