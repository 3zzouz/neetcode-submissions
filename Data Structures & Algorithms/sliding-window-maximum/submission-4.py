from collections import deque

class IndexedHeap:
    def __init__(self):
        self.heap = []          # (priority, key)
        self.pos = {}           # key -> index

    def swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]
        self.pos[self.heap[i][1]] = i
        self.pos[self.heap[j][1]] = j

    def sift_up(self, i):
        while i > 0:
            p = (i - 1) // 2
            if self.heap[p][0] <= self.heap[i][0]:
                break
            self.swap(i, p)
            i = p

    def sift_down(self, i):
        n = len(self.heap)

        while True:
            smallest = i
            l = 2 * i + 1
            r = 2 * i + 2

            if l < n and self.heap[l][0] < self.heap[smallest][0]:
                smallest = l

            if r < n and self.heap[r][0] < self.heap[smallest][0]:
                smallest = r

            if smallest == i:
                break

            self.swap(i, smallest)
            i = smallest

    def push(self, priority, key):
        self.heap.append((priority, key))
        idx = len(self.heap) - 1
        self.pos[key] = idx
        self.sift_up(idx)

    def erase(self, key):
        i = self.pos[key]

        self.swap(i, len(self.heap) - 1)

        self.heap.pop()
        del self.pos[key]

        if i < len(self.heap):
            p = (i - 1) // 2

            if i > 0 and self.heap[i][0] < self.heap[p][0]:
                self.sift_up(i)
            else:
                self.sift_down(i)

    def top(self):
        return self.heap[0]


class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        heap = IndexedHeap()

        # build first window
        for i in range(k):
            heap.push(-nums[i], i)

        res = deque()

        left = 0

        while left + k <= len(nums):

            res.append(-heap.top()[0])

            heap.erase(left)

            right = left + k

            if right < len(nums):
                heap.push(-nums[right], right)

            left += 1

        return list(res)