"""Fibonacci com memoização: exemplo clássico de DP top-down."""


def fib(n: int, memo: dict[int, int] | None = None) -> int:
    if memo is None:
        memo = {}
    if n <= 1:
        return n
    if n not in memo:
        memo[n] = fib(n - 1, memo) + fib(n - 2, memo)
    return memo[n]


if __name__ == "__main__":
    print(fib(40))  # 102334155
