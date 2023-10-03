class Solution:
    def reorganizeString(self, s: str) -> str:        
        c = Counter(s)
        hq = [(-cnt, ch) for ch, cnt in c.items()]
        
        heapq.heapify(hq)
        
        print(hq)
        
        ret = ""
        last_cnt = 0
        last_ch = ""
        
        while hq:
            cnt, ch = heapq.heappop(hq)
            
            if last_cnt < 0:
                heapq.heappush(hq, (last_cnt, last_ch))
                
            
            ret += ch
            last_cnt = cnt + 1
            last_ch = ch
        
        # print(ret)
        # print(hq)
        return ret if len(ret) == len(s) else ""
            