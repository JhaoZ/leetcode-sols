class Solution:
    def ambiguousCoordinates(self, s: str) -> List[str]:
        ans = []

        def convert(arr, s1):


            for i in range(1, len(s1) + 1):
                if i == len(s1):
                    curr = s1
                else:
                    first = s1[0:i]
                    last = s1[i:len(s1)]
                    curr = first + "." + last

                converted = "{:.10f}".format(float(curr)).rstrip("0").rstrip(".")
                if float(int(float(curr))) == float(curr):
                    if len(str(int(float(curr)))) == len(curr):
                        arr.append(curr)
                elif len(converted) == len(curr) or len(str(float(curr))) == len(curr):
                    arr.append(curr) 



        for i in range(2, len(s) - 1):
            first = s[1:i]
            last = s[i:len(s)-1]
            arr1 = []
            arr2 = []

            convert(arr1, first)
            convert(arr2, last)

            for i in arr1:
                for j in arr2:
                    ans.append("(" + i + ", " + j + ")")
        return ans
        
