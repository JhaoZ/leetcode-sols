class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = {i: [] for i in range(numCourses)}
        indegrees = {i: 0 for i in range(numCourses)}
        for course, prereq in prerequisites:
            graph[prereq].append(course)
            indegrees[course] += 1

        
        queue = deque([])
        for course in range(numCourses):
            if indegrees[course] == 0:
                queue.append(course)

        ans = []
        visited = set()
        while queue:
            curr = queue.popleft()
            ans.append(curr)
            visited.add(curr)
            for n in graph[curr]:
                indegrees[n] -= 1
                if indegrees[n] == 0 and n not in visited:
                    queue.append(n)
        return ans if len(visited) == numCourses else []
        

        
        

