class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        n = len(asteroids)
        stack = []
        def is_negative(n):
            return n < 0
        def is_positive(n):
            return n > 0
        def opposite(a, b):
            return (is_negative(a) and is_positive(b)) or (is_negative(b) and is_positive(a)) 
        def same(a, b):
            return (is_positive(a) and is_positive(b)) or (is_negative(b) and is_negative(a)) 
        
        while asteroids:
            asteroid = asteroids.pop(0)
            if stack and same(stack[-1], asteroid):
                stack.append(asteroid)
                continue
            while stack and (is_positive(stack[-1]) and is_negative(asteroid)) and abs(asteroid) > abs(stack[-1]):
                stack.pop()
            if stack and abs(asteroid) <= abs(stack[-1]) and (is_positive(stack[-1]) and is_negative(asteroid)):
                if abs(asteroid) == abs(stack[-1]):
                    stack.pop()
                continue
            stack.append(asteroid)
        return stack
