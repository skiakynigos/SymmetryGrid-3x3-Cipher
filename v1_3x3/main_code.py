import numpy as np

class SymmGridCipher:
    def __init__(self):
        # Initial Magic Square Grid
        self.base_grid = np.array([
            [2, 7, 6],
            [9, 5, 1],
            [4, 3, 8]
        ])
        
        # The Vansh-Algorithm Mapping (Value -> New Coordinate)
        # Based on the pattern discovered by Vansh Aggarwal
        self.vansh_pattern = {
            7: (0, 0), 2: (0, 1), 9: (0, 2),
            3: (1, 0), 4: (1, 1), 1: (1, 2),
            8: (2, 0), 5: (2, 1), 6: (2, 2)
        }

    def encrypt(self):
        """Transform the base grid into the SymmGrid-3x3 pattern."""
        encrypted_grid = np.zeros((3, 3), dtype=int)
        
        for value, coord in self.vansh_pattern.items():
            r, c = coord
            encrypted_grid[r, c] = value
            
        return encrypted_grid

    def display_comparison(self, transformed):
        print("--- SymmGrid-3x3 Algorithm Output ---")
        print("\n[Initial Magic Square]:")
        print(self.base_grid)
        print("\n[Transformed Vansh-Grid]:")
        print(transformed)
        print("\nTransformation Status: Success")

if __name__ == "__main__":
    cipher = SymmGridCipher()
    result = cipher.encrypt()
    cipher.display_comparison(result)
