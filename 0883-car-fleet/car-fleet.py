class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []

        cars = [(position[i], speed[i]) for i in range(len(position))]
        cars.sort(key = lambda x : (-x[0]))
        
        for p, s in cars:
            if not stack or s == 0:
                stack.append((p, s))
            else:
                prev_p, prev_s = stack[-1]
                t_1 =  (target - p) / s
                t_2 = (target - prev_p) / prev_s  # further along
                if t_1 <= t_2: # they meet before target:
                    stack.pop()
                    if prev_s < s:
                        stack.append((prev_p, prev_s))
                    else:
                        stack.append((p, s))
                else:
                    stack.append((p, s))




                
                # dt * t_1 = s_1
                # t_1 = s_1 / dt


                # dt * t_2 = s_2
        return len(stack)