class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        

        # 0   1   2   3   4   5   6   7   8   9   10
        # 1   2           2           1


        cars = []
        for i in range(len(position)):
            cars.append((position[i], speed[i]))
        cars.sort()
        cars.reverse()

        times = []
        for car in cars:
            times.append((target - car[0]) / car[1])
        
        stack = []
        stack.append(times[0])

        for j in range(1, len(times)):
            if times[j] > stack[-1]:
                stack.append(times[j])
        return len(stack)


    # [8, 7, 6, 5, 4, 3]
    # [4, 4, 4, 4, 4, 4]
    
    # [1, 1, 1, 2, 2, 2]
            