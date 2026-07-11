"""
bestSum(targetSum, numbers) -> list | None

Return the shortest combination of numbers that add up to targetSum, or None
if impossible. Elements may be reused. All numbers are non-negative.
If there are multiple shortest combinations, any one is acceptable.
"""

from __future__ import annotations

from typing import Dict, List, Optional


def best_sum_memo(
    target_sum: int,
    numbers: List[int],
    memo: Optional[Dict[int, Optional[List[int]]]] = None,
) -> Optional[List[int]]:
    """Memoized recursive solution. Time O(n*m^2), Space O(m^2)."""
    if memo is None:
        memo = {}
    if target_sum in memo:
        return memo[target_sum]
    if target_sum == 0:
        return []
    if target_sum < 0:
        return None

    shortest: Optional[List[int]] = None

    for num in numbers:
        remainder_combo = best_sum_memo(target_sum - num, numbers, memo)
        if remainder_combo is not None:
            combo = remainder_combo + [num]
            if shortest is None or len(combo) < len(shortest):
                shortest = combo

    memo[target_sum] = shortest
    return shortest


def best_sum_tab(target_sum: int, numbers: List[int]) -> Optional[List[int]]:
    """Tabulated iterative solution. Time O(n*m^2), Space O(m^2)."""
    table: List[Optional[List[int]]] = [None] * (target_sum + 1)
    table[0] = []

    for i in range(target_sum + 1):
        if table[i] is None:
            continue
        for num in numbers:
            next_idx = i + num
            if next_idx <= target_sum:
                candidate = table[i] + [num]
                current = table[next_idx]
                if current is None or len(candidate) < len(current):
                    table[next_idx] = candidate

    return table[target_sum]


best_sum = best_sum_memo
