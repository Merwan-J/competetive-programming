class TweetCounts:

    def __init__(self):
        self.tweetNames = defaultdict(list)
        

    def recordTweet(self, tweetName: str, time: int) -> None:
        self.tweetNames[tweetName].append(time)
        

    def getTweetCountsPerFrequency(self, freq: str, tweetName: str, startTime: int, endTime: int) -> List[int]:
        
        if freq=="minute":
            chunk_size = 60
        elif freq=="hour":
            chunk_size = 60 * 60
        else:
            chunk_size = 60 * 60 * 24
            
        chunk_count = int((endTime - startTime)/chunk_size) + 1
        
        bins = [0] * (chunk_count)
        
        for tweettime in self.tweetNames[tweetName]:
            if(startTime <= tweettime and tweettime <= endTime):
                chunk_number = int((tweettime-startTime)/chunk_size)
                bins[chunk_number] +=1

        return bins
        


# Your TweetCounts object will be instantiated and called as such:
# obj = TweetCounts()
# obj.recordTweet(tweetName,time)
# param_2 = obj.getTweetCountsPerFrequency(freq,tweetName,startTime,endTime)