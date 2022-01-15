class Solution:
    def leastInterval(self, tasks, n) -> int:
        if n==0:
            return len(tasks)
        
        counter = dict()
        
        for task in tasks:
            counter[task] = counter.get(task,0) + 1
                
        counter = dict(sorted(counter.items(),key=lambda x: x[1]))
        row_num = max(counter.values())-1
        last_row_len = list(counter.values()).count(row_num+1) 
        row_length = n+1
        slots = row_length * row_num + last_row_len
        total = slots
        
        for task in counter:
            if slots ==0:
                total += counter[task]
                continue
            else:
                slots -= counter[task]
                if slots < 0:
                    total+= abs(slots)
                    slots = 0
        
        return total