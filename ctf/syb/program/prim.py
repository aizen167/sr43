# -*- coding:utf-8 -*-

import gmpy2

# 节点，包含元素和步数


class Node:
    def __init__(self, element, step):
        element1 = element
        self.element = element1
        self.step = step

# 使用bfs(宽度优先搜索)


def foo():
    start = 1373
    end = 8017
    queue = [Node(start, 0)]
    visited = [start]
    while len(queue) != 0:
        now = queue[0]
        del queue[0]
        if now.element == end:
            return now.step
        for i in xrange(4):
            for j in xrange(10):
                if i == 0 and j == 0:
                    continue
                # 得到一个新的四位数
                tmp = int(str(now.element)[:i] +
                          str(j) + str(now.element)[i + 1:])
                # 判断是否素数，这里用gmpy2库来判断而已
                if gmpy2.is_prime(tmp):
                    # 该数是否被访问过
                    if tmp not in visited:
                        visited.append(tmp)
                        queue.append(Node(tmp, now.step + 1))
    return False


if __name__ == '__main__':
    print foo()
    print 'ok'
