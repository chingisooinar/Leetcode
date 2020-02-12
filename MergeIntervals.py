class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        if len(intervals)==0:
            return []
        res=[]
        merged=[]
        intervals=sorted(intervals,key= lambda x:x[0])
        for lis in intervals:
            if lis in merged:
                continue
            end=lis[1]
            toadd=[lis[0],lis[1]]
            index=intervals.index(lis)
            for i in range(index+1,len(intervals)):
                tomerge=[toadd[0],toadd[1],intervals[i][0],intervals[i][1]]
                tomerge.sort()
                if(((toadd[0]==tomerge[0] and toadd[1]==tomerge[1]) or (toadd[0]==tomerge[2] and toadd[1]==tomerge[3])) and tomerge[2]!=tomerge[1]):
                    continue
                else:
                    toadd=[tomerge[0],tomerge[3]]
                    merged.append(intervals[i])
            res.append(toadd)
        return(res)
