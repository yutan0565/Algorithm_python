def solution(tickets):
    routes = dict()
    answer = []

    # 각각의 시잠점에서 갈 수 있는 장소를 정리 해주기
    for (start, end) in tickets:
        routes[start] = routes.get(start, []) + [end]
    print(routes)

    #각각의 시작 경로에서,   도착하는 지점들을   정렬 해주기
    for r in routes.keys():
        routes[r].sort(reverse=True)

    current_list = ["ICN"]

    while current_list:
        current = current_list[-1]
        if current in routes and routes[current]:
            current_list.append(routes[current].pop())
        else:
            answer.append(current_list.pop())
    answer.reverse()
    return answer
    # 내가 총 가진 티켓의 개수



print(solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]))