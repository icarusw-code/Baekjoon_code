def is_available(candidate, current_col):
    current_row = len(candidate) # 선택된 queen list 의 길이, 개수 = 현재 행의 위치
    for queen_row in range(current_row): 
        # 세로 줄 탐색 , 대각선 탐색 만약 만족을 안하면 바로 break 
        # 핵심 코드
        if candidate[queen_row] == current_col or abs(candidate[queen_row] - current_col) == current_row - queen_row:
            return False
    return True

def DFS(N, current_row, current_candidate, final_result): # current_row: 현재 행/ current_candidate: 현재까지 놓여진 위치
    if current_row == N:
        final_result.append(current_candidate[:]) # 얇은 복사 사용: pop을 실행하면 값이 변하기 때문에 
        return

    for candidate_col in range(N): # current_row에서 한 칸씩 오른쪽으로 확인하며 놓을 queen 자리 확인
        if is_available(current_candidate, candidate_col): # 대각선, 세로 가능 여부 확인
            current_candidate.append(candidate_col) # 하나의 queen을 선택하고 넣어줌
            DFS(N, current_row + 1, current_candidate, final_result) # 다음 줄로 넘어감 (재귀)
            # 아직 남은 후보를 확인하기 위해 마지막 후보를 pop하고 나머지 확인
            current_candidate.pop() # 다시 공부하고 주석 채워 넣기


def solve_n_quuens(N): # N x N 크기의 체스판 
    final_result = []   # n-queen이 가능한 체스말의 위치
    DFS(N, 0, [], final_result)
    print(len(final_result))
    return final_result

n = int(input())
solve_n_quuens(n)