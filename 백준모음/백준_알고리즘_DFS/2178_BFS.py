import sys
from collections import deque

N,M = map(int,sys.stdin.readline().split())

board = [input() for _ in range(N)]

#방문한 칸은 chk[]로 이차원 배열을 만들어줌