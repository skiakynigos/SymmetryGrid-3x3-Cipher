# The Universal Base Generator: Origins of SymmGrid
**Author:** Vansh Aggarwal

## 1. The Concept of "Relative Positioning"
The SymmGrid algorithm doesn't just scramble numbers; it manipulates a pre-existing state of perfect balance. That balance is the $3 \times 3$ Magic Square. 

During my research, I identified a universal method to construct a Magic Square from any 9 consecutive integers ($n, n+1, \dots, n+8$). This method ensures that no matter what the starting number is, the resulting grid will always satisfy the Magic Constant ($Sum = 3 \times \text{Middle Number}$).

## 2. The Universal Starting Coordinate
The key discovery is the **Middle-Row, 3rd-Column Start Rule**. By fixing the first number of the sequence at this specific coordinate, the rest of the numbers follow a deterministic spatial path.

### The Coordinate Mapping Path:
Let $n$ be the first number in your sequence.

| Sequence Order | Grid Coordinate (Row, Col) | Location Description |
| :--- | :--- | :--- |
| **$n$** | (1, 2) | Middle Row, Right |
| **$n+1$** | (0, 0) | Top Row, Left |
| **$n+2$** | (2, 1) | Bottom Row, Center |
| **$n+3$** | (2, 0) | Bottom Row, Left |
| **$n+4$** | (1, 1) | Dead Center |
| **$n+5$** | (0, 2) | Top Row, Right |
| **$n+6$** | (0, 1) | Top Row, Center |
| **$n+7$** | (2, 2) | Bottom Row, Right |
| **$n+8$** | (1, 0) | Middle Row, Left |



## 3. Practical Example: Sequence {67, 68, ..., 75}
When applying this rule to the sequence starting at 67:
* **67** is placed at (1, 2).
* **68** is placed at (0, 0).
* **69** is placed at (2, 1).
* ... and so on.

**The Generated Magic Square:**
```text
[ 68  73  72 ]
[ 75  71  67 ]
[ 70  69  74 ]
