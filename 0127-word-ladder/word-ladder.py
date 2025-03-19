class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:

        wordList.append(beginWord)
        everything = set(wordList)

        graph = defaultdict(set)
        for w in wordList:
            temp = [ch for ch in w]
            for i in range(len(w)):
                curr_ascii = ord(temp[i]) - ord('a')
                for j in range(0, 26):
                    if j == curr_ascii:
                        continue
                    temp[i] = chr(ord('a') + j)
                    curr = ''.join(temp)
                    if curr in everything:
                        graph[w].add(curr)
                        graph[curr].add(w)
                    temp[i] =chr(ord('a') + curr_ascii)

 
        
        queue = deque()
        dist = {}
        dist[beginWord] = 1
        queue.append(beginWord)

        while queue:
            curr = queue.popleft()

            for n in graph[curr]:
                if n in dist:
                    continue
                dist[n] = dist[curr] + 1
                if n == endWord:
                    return dist[n]
                queue.append(n)
        if endWord in dist:
            return dist[endWord]
        else:
            return 0
