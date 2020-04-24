# Flip the LSB of b.
# And check if the new number is in range(a < number < b) or not
# if the number greater than 'a' again flip lsb
# if it is not then that's the answer
class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        while (m < n):
            n -= (n & -n)  # -n is the 2s complement. We do bitwise AND with n. we get lsb. We subtract it from original
        return n
