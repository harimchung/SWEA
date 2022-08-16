T = int(input())

for t in range(1, T+1):
    N, K = map(int, input().split())
    homework_list = [0] * (N+1)
    done_people = list(map(int, input().split()))
    for people in done_people:
        homework_list[people] = 1
    print(f"#{t}", end=" ")
    for people_id in range(len(homework_list)):
        if people_id != 0 and homework_list[people_id] == 0:
            print(people_id, end=" ")
    print()
