class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        bits=max(x,y)
        count=0
        sx=0
        sy=0
        rang=0
        num=0
        while(num<bits):
            num=int(math.pow(2,rang))
            rang+=1
        numy=num
        for i in range(rang):
            checkx=checky=0
            if(sx+num<=x):
                checkx=1
                sx+=num
            num=num/2
            if(sy+numy<=y):
                checky=1
                sy+=numy
            numy=numy/2
            if(checkx!=checky):
                count+=1
               
        return count
