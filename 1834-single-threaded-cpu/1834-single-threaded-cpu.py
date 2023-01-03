class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
    
#     two things 
#         put tasks into queue when they are available
        
#         process available tasks
    
#     track current time
    
    
#     sort tasks
#     put tasks with the same enque Time as the current Time into queue params:processTime and index
    
    
    
#     when to process?
#     how and when to increment the curTime?
#     what happens when queue is empty and the current time is less than the smalles enque time?
#     what happens in the end?


        tasks = [tasks[i]+[i] for i in range(len(tasks))]
        tasks.sort()
        heap = []
        ans = []
        curTime = 0

        for task in tasks:
            enqueTime,processTime,i = task
            while heap and curTime<enqueTime:
                currentProcessTime,idx = heappop(heap)
                ans.append(idx)
                curTime+=currentProcessTime

            if curTime<enqueTime:
                curTime = enqueTime
            heappush(heap,(processTime,i))

        while heap:
            currentProcessTime,idx = heappop(heap)
            ans.append(idx)

        return ans