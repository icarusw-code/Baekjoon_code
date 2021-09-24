# from heapdict import heapdict
from collections import defaultdict
from heapq import *

def prim(start_node, edges):
    # 최소 신장트리 저장할 리스트
    mst = list()
    # 인접 간선리스트 -> defaultdict를 통해 default list()로 설정
    adjacent_edges = defaultdict(list)
    # 간선정보를 입력
    for weight, n1, n2 in edges:
        adjacent_edges[n1].append((weight, n1, n2))
        adjacent_edges[n2].append((weight, n2, n1))

    # 시작노드를 set()에 넣어줌 -> 사이클 여부 판별을 위해
    connected_nodes = set(start_node)
    # 시작노드의 간선리스트를 후보리스트에 등록
    candidate_edge_list = adjacent_edges[start_node]
    # 후보리스트를 heapq 구조화
    heapify(candidate_edge_list)

    # 후보 리스트를 순회
    while candidate_edge_list:
        # 후보리스트 중 가장 가중치가 작은 간선을 pop
        weight, n1, n2 = heappop(candidate_edge_list)
        # 연결 될 노드가 사이클에 포함되는지 확인
        if n2 not in connected_nodes:
            # 포함되지 않으면 set()에 추가
            connected_nodes.add(n2)
            # 해당 노드정보를 mst에 업데이트
            mst.append((weight, n1, n2))

            # 연결 확정된 다음 노드의 간선리스트들을 후보리스트에 heappush
            for edge in adjacent_edges[n2]:
                # 연결가능한 간선리스트들 중 n2가 이미  connected_nodes에 있다면 -> 사이클 존재 -> 후보리스트에 넣지 x
                if edge[2] not in connected_nodes:
                    heappush(candidate_edge_list, edge)

    return mst