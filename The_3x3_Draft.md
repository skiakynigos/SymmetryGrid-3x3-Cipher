# The Vansh-Cipher (SymmGrid-3x3)
### A Personal Discovery in Discrete Grid Permutations

## The Origin Story
This isn't your standard textbook algorithm. It started on a torn piece of notebook paper (Reference: original_sketch.jpg). While most people see a 3x3 box as a static set of numbers, I saw a system of interconnected positions. I wanted to see if I could "break" the symmetry of a Magic Square and turn it into a deterministic encryption engine. 

## The Core Philosophy: "Spatial Disturbance"
The logic follows a simple rule: Movement over Value. In the SymmGrid-3x3, a number's identity is secondary to its coordinates. By using modular arithmetic (wrapping) and non-linear swaps, we create a transformation that looks random but is 100% reversible if you hold the "Key."

## How the Algorithm "Thinks"
To scramble a grid, the system executes these core phases:

### Phase 1: The Binary Swap (Pivot Interchange)
* Operation: Interchange(2, 7)
* Logic: This breaks the primary diagonal symmetry.

### Phase 2: The Gravity Shift (Modular Wrapping)
* Operation: Shift(5) Down by 1 unit.
* Result: Since the grid is a 3x3 torus, shifting 5 down wraps it back to the top.

### Phase 3: The Positional Replacement
* Operation: Pos(9) takes the place of Pos(6).
* Outcome: Forces other numbers to find their "Opposite" homes.

### Phase 4: The Boundary Flips
* 8 moves horizontally to the opposite side.
* 6 moves vertically to the bottom.
* 3 and 4 undergo a cross-multiplication swap.

## Security Analysis
1. Non-Linearity: Because of the wrapping (Modular 3), you can't use simple linear logic to guess the next position.
2. Deterministic Chaos: To an outsider, it looks like a random shuffle, but it’s a calculated dance where every number knows its partner's new address.   
