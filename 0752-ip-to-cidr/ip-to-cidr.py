class Solution:
    def ipToCIDR(self, ip: str, n: int) -> List[str]:
        ans = []

        curr_ip = 0
        for num in ip.split("."):
            curr_ip = curr_ip * 256 + int(num)

        def ip_to_str(ip_addr):
            return ".".join(str((ip_addr >> (8 * i)) & 255) for i in range(3, -1, -1))

       

        while n > 0:
            # fill next block
            max_range = curr_ip & -curr_ip   # alignment constraint

            if max_range == 0:   # special case for 0.0.0.0
                max_range = 1 << 32
            while max_range > n:             # don’t exceed what’s left
                max_range //= 2
            block_size = max_range

            
            mask_len = 32 - (block_size.bit_length() - 1)

           
            ans.append(f'{ip_to_str(curr_ip)}/{mask_len}')

            n -= block_size
            curr_ip += block_size
        return ans
