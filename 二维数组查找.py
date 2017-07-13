# -*- coding:utf-8 -*-
class Solution:
    # array 二维列表
    # write code here
    # 从右上角开始搜索
    def Find(self, target, array):
        if array is None:
            return False
        max_x = len(array[0]) - 1
        max_y = len(array) - 1
        cur_x = max_x
        cur_y = 0
        found = False
        while cur_x >= 0 and cur_y <= max_y:
            # print (cur_x)
            # print (cur_y)
            if array[cur_y][cur_x] > target:
                cur_x -= 1
            elif array[cur_y][cur_x] == target:
                found = True
                break
            else:
                cur_y += 1
        return found


solu = Solution()
array = [[1, 2, 8, 9], [2, 4, 9, 12], [4, 7, 10, 13], [6, 8, 11, 15]]
print(solu.Find(7, array))
