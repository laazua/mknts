#!/usr/bin/env python3
#coding:utf-8
# 在0-9中,找出k个数之和为n的序列,序列中对数字不能重复
# 如输入: 3, 7
# 输出: [[1,2,4]]

class Solution:

    def combinetion(self, k: int, n: int) -> list:
        result = []
        candidates = [1,2,3,4,5,6,7,8,9]
        def auxiliary(counter, start, tmp,remain):
            if remain < 0 or counter > k:
                return
            elif remain == 0 and counter == k:
                result.append(tmp)
            else:
                for index in range(start, len(candidates) + 1):
                    if index > remain:
                        break
                    else:
                        auxiliary(counter + 1, index + 1, tmp + [index], remain - index)
        auxiliary(0, 1, [], n)

        return result


if __name__ == "__main__":
   a = Solution()
   b = a.combinetion(2,12)
   print(b)