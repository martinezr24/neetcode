class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        neighbors = defaultdict(list)

        for a, b in prerequisites:
            neighbors[a].append(b)

        visited = set()
            
        def dfs(course):
            if course in visited:
                return False
            
            if neighbors[course] == []:
                return True

            visited.add(course)
            
            for prereq in neighbors[course]:
                if not dfs(prereq): 
                    return False

            visited.remove(course)

            neighbors[course] = []
            return True
        
        for course in range(numCourses):
            if not dfs(course):
                return False
        return True


        
      