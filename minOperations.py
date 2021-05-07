class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        if len(boxes) == 0:
            return []
        # init
        answer = [0 for _ in range(len(boxes))]
        # forward pass
        for i in range(len(boxes)):
            if boxes[i] == '1':
                for j in range(i+1, len(boxes)):
                    answer[j] += (j - i)
        
        # backward pass
        for i in range(len(boxes)-1, -1, -1):
            if boxes[i] == '1':
                for j in range(i-1, -1, -1):
                    answer[j] += (i - j)
        return answer
