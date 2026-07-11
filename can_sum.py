"""
canSum(targetSum, numbers) -> bool

Return whether it is possible to generate targetSum using numbers from the
array. Elements may be reused. All numbers are non-negative.
"""

from __future__ import annotations

from typing import Dict, List, Optional


def can_sum_memo(
    target_sum: int,
    numbers: List[int],
    memo: Optional[Dict[int, bool]] = None,
) -> bool:
    """Memoized recursive solution. Time O(n*m), Space O(m)."""
    if memo is None:
        memo = {}
    if target_sum in memo:
        return memo[target_sum]
    if target_sum == 0:
        return True
    if target_sum < 0:
        return False

    for num in numbers:
        if can_sum_memo(target_sum - num, numbers, memo):
            memo[target_sum] = True
            return True

    memo[target_sum] = False
    return False


def can_sum_tab(target_sum: int, numbers: List[int]) -> bool:
    """Tabulated iterative solution. Time O(n*m), Space O(m)."""
    table = [False] * (target_sum + 1)
    table[0] = True

    for i in range(target_sum + 1):
        if not table[i]:
            continue
        for num in numbers:
            next_idx = i + num
            if next_idx <= target_sum:
                table[next_idx] = True

    return table[target_sum]


# Convenience alias matching the classic problem name.
can_sum = can_sum_memo
