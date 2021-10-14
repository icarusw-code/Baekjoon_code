# n = int(input())
# # 숫자 리스트
# num = list(map(int, input().split()))
# # 저장 공간
# path = [0 for _ in range(n)]
# used = [0 for _ in range(len(num))]
# # cnt = 0
# # lev 시작점
# def Permutation(lev):
#     if lev == n:
#         print(*path)
#         # global cnt
#         # cnt += 1
#         # print(cnt)
#         return
#     for i in range(len(num)):
#         if used[i] == 1:
#             continue
#         used[i] = 1
#         path[lev] = num[i]
#         Permutation(lev + 1)
#         used[i] = 0


# Permutation(0)


n = int(input())
# 숫자 리스트
num = list(map(int, input().split()))
# 저장 공간
path = [0 for _ in range(n)]
# 방문 처리
used = [0 for _ in range(len(num))]

def combination(lev, start):
    if lev == n:
        print(*path)
        return
    for i in range(start, len(num)):
        path[lev] = num[i]
        combination(lev + 1, i + 1)


combination(0, 0)
