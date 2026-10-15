class Solution:
    def getImportance(self, employees: list['Employee'], id: int) -> int:
        emp_map = {e.id: e for e in employees}
        
        def dfs(emp_id):
            emp = emp_map[emp_id]
            total = emp.importance
            for sub_id in emp.subordinates:
                total += dfs(sub_id)
            return total
            
        return dfs(id)