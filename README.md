# CanSum

Dynamic programming solutions for the classic target-sum problems from the
[freeCodeCamp Dynamic Programming course](https://www.youtube.com/watch?v=oBt53YbR9Kk):

| Problem | Question | Return type |
|---------|----------|-------------|
| **canSum** | Can you make the target? | `bool` |
| **howSum** | How can you make it? (any combination) | `list` or `None` |
| **bestSum** | What is the shortest way? | `list` or `None` |

Numbers may be reused. All inputs are non-negative.

## Files

- `can_sum.py` — decision problem (memoization + tabulation)
- `how_sum.py` — combinatoric problem (memoization + tabulation)
- `best_sum.py` — optimization problem (memoization + tabulation)
- `test_sums.py` — unit tests

## Complexity

Where `m` = target sum and `n` = length of `numbers`:

| Approach | canSum | howSum / bestSum |
|----------|--------|------------------|
| Brute force | O(n^m) time, O(m) space | O(n^m * m) time |
| Memoization | O(n*m) time, O(m) space | O(n*m^2) time, O(m^2) space |
| Tabulation | O(n*m) time, O(m) space | O(n*m^2) time, O(m^2) space |

## Examples

```python
from can_sum import can_sum
from how_sum import how_sum
from best_sum import best_sum

can_sum(7, [5, 3, 4, 7])   # True
can_sum(7, [2, 4])         # False

how_sum(7, [5, 3, 4, 7])   # e.g. [3, 4] or [7]
how_sum(7, [2, 4])         # None

best_sum(8, [2, 3, 5])     # [3, 5]
best_sum(8, [1, 4, 5])     # [4, 4]
```

## Run tests

```bash
python3 -m unittest test_sums.py -v
```
