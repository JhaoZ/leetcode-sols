class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        segments = 0

        chars = set(source)

        def match(ptr):
            src_ptr = 0
            dist = 0
            while ptr < len(target) and src_ptr < len(source):
                if target[ptr] not in chars:
                    return -1
                
                if target[ptr] == source[src_ptr]:
                    dist += 1
                    src_ptr += 1
                    ptr += 1
                else:
                    src_ptr += 1
            return dist


        ptr = 0
        while ptr < len(target):
            matched = match(ptr)
            if matched == -1:
                return -1
            segments += 1
            ptr += matched
        return segments


        
        