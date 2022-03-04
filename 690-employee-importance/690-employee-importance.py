"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        visited = dict()
        emps = dict()
        
        for emp in employees:
            emps[emp.id] = emp
        
        self.count = 0
        
        def count(employee):
            if employee.id not in visited:
                self.count += employee.importance
                visited[employee.id] = True
            for id in employee.subordinates:
                count(emps[id])
                
        count(emps[id])
        return self.count
            
        