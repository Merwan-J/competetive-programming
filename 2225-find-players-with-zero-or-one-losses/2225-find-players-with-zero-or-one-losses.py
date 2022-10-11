class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        
        
        wins = defaultdict(int)
        losses = defaultdict(int)
        players = set()
        for winner,loser in matches:
            players.add(winner)
            players.add(loser)
            
            wins[winner]+=1
            losses[loser]+=1
        
        losers = []
        winners = []
        
        for player in players:
            if losses[player] == 1:
                losers.append(player)
            if losses[player] == 0:
                winners.append(player)
        
        winners.sort()
        losers.sort()
        
        return [winners,losers]
        
        
        