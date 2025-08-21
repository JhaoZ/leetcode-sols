from typing import List

class Solution:
    def ipToCIDR(self, ip: str, n: int) -> List[str]:
        def ip_to_int(s: str) -> int:
            x = 0
            for part in s.split("."):
                x = (x << 8) + int(part)
            return x

        def int_to_ip(x: int) -> str:
            return ".".join(str((x >> (8 * i)) & 255) for i in range(3, -1, -1))

        curr = ip_to_int(ip)
        ans: List[str] = []

        while n > 0:
            lowbit = curr & -curr                 # 0 only when curr == 0
            # align exponent (k). If lowbit == 0, pretend it's 2^32 so k=32.
            align_exp = (lowbit.bit_length() - 1) if lowbit else 32
            rem_exp = n.bit_length() - 1          # m = floor(log2(n))
            exp = min(align_exp, rem_exp)

            block_size = 1 << exp                 # 2^exp
            mask_len = 32 - exp                   # since 2^(32-mask) = block_size

            ans.append(f"{int_to_ip(curr)}/{mask_len}")
            curr += block_size
            n -= block_size

        return ans
