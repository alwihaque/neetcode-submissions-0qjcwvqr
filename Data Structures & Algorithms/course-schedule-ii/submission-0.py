class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        preMap = {i:[] for i in range(numCourses)}

        for courses, pre_reqs in prerequisites:
            preMap[courses].append(pre_reqs)

        visited, visiting = set(), set()
        visiting = set()
        res = []

        def dfs(crs):
            if crs in visited:
                return False
            if crs in visiting:
                return True
            visited.add(crs)

            for pre_req in preMap[crs]:
                if dfs(pre_req) == False:
                    return False
            
            visited.remove(crs)
            visiting.add(crs)
            res.append(crs)
            return True
        
        for i in range(numCourses):
            if dfs(i) == False:
                return []
        return res


        