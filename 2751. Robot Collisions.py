class Solution:
    def survivedRobotsHealths(self, positions: list[int], healths: list[int], directions: str) -> list[int]:
        n = len(positions)
        robots = [[i, positions[i], healths[i], directions[i]] for i in range(n)]
        robots.sort(key=lambda x: x[1])

        stack = []

        for robot in robots:
            if robot[3] == 'R':
                stack.append(robot)
                continue

            survived = True
            while stack and stack[-1][3] == 'R' and survived:
                top_robot = stack[-1]

                if robot[2] > top_robot[2]:
                    stack.pop()
                    robot[2] -= 1
                elif robot[2] < top_robot[2]:
                    top_robot[2] -= 1
                    survived = False
                else:
                    stack.pop()
                    survived = False

            if survived:
                stack.append(robot)

        stack.sort(key=lambda x: x[0])
        return [robot[2] for robot in stack]
