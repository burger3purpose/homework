from collections import deque

def solution(priorities, location):
    queue = deque([(idx, val) for idx, val in enumerate(priorities)])
    count = 0

    while True:
        front = queue.popleft()
        if any(front[1] < item[1] for item in queue):
            queue.append(front)
        else:
            count += 1
            if front[0] == location:
                return count

if __name__ == '__main__':
    priorities1 = [2, 1, 3, 2]
    location1 = 2
    print('priorities:' , priorities1)
    print('location:' , location1)
    print('인쇄 순서:' ,solution(priorities1, location1))

    priorities2 = [1, 1, 9, 2, 3, 4]
    location2 = 1
    print('priorities:' , priorities2)
    print('location:' , location2)
    print('인쇄 순서:' ,solution(priorities2, location2)) 

    priorities3 = [1, 1, 2, 1, 1, 1]
    location3 = 0
    print('priorities:' , priorities3)
    print('location:' , location3)
    print('인쇄 순서:' , solution(priorities3, location3)) 