import sys
from itertools import combinations

input = sys.stdin.readline
N, M = map(int, input().split())

city = []
house = []
chicken = []

for i in range(N):
    row = list(map(int, input().split()))
    city.append(row)
    for j in range(N):
        if row[j] == 1:
            house.append((i, j))
        elif row[j] == 2:
            chicken.append((i, j))

def calculate_city_chicken_distance(selected_chickens):
    total_distance = 0
    for hx, hy in house:
        min_dist = float('inf')
        for cx, cy in selected_chickens:
            dist = abs(hx - cx) + abs(hy - cy)
            min_dist = min(min_dist, dist)
        total_distance += min_dist
    return total_distance

min_chicken_distance = float('inf')
for selected in combinations(chicken, M):
    city_distance = calculate_city_chicken_distance(selected)
    min_chicken_distance = min(min_chicken_distance, city_distance)

print(min_chicken_distance)



'''

15686 치킨 배달

문제
크기가 N×N인 도시가 있다. 도시는 1×1크기의 칸으로 나누어져 있다. 도시의 각 칸은 빈 칸, 치킨집, 집 중 하나이다. 도시의 칸은 (r, c)와 같은 형태로 나타내고, r행 c열 또는 위에서부터 r번째 칸, 왼쪽에서부터 c번째 칸을 의미한다. r과 c는 1부터 시작한다.

이 도시에 사는 사람들은 치킨을 매우 좋아한다. 따라서, 사람들은 "치킨 거리"라는 말을 주로 사용한다. 치킨 거리는 집과 가장 가까운 치킨집 사이의 거리이다. 즉, 치킨 거리는 집을 기준으로 정해지며, 각각의 집은 치킨 거리를 가지고 있다. 도시의 치킨 거리는 모든 집의 치킨 거리의 합이다.

임의의 두 칸 (r1, c1)과 (r2, c2) 사이의 거리는 |r1-r2| + |c1-c2|로 구한다.

예를 들어, 아래와 같은 지도를 갖는 도시를 살펴보자.

0 2 0 1 0
1 0 1 0 0
0 0 0 0 0
0 0 0 1 1
0 0 0 1 2
0은 빈 칸, 1은 집, 2는 치킨집이다.

(2, 1)에 있는 집과 (1, 2)에 있는 치킨집과의 거리는 |2-1| + |1-2| = 2, (5, 5)에 있는 치킨집과의 거리는 |2-5| + |1-5| = 7이다. 따라서, (2, 1)에 있는 집의 치킨 거리는 2이다.

(5, 4)에 있는 집과 (1, 2)에 있는 치킨집과의 거리는 |5-1| + |4-2| = 6, (5, 5)에 있는 치킨집과의 거리는 |5-5| + |4-5| = 1이다. 따라서, (5, 4)에 있는 집의 치킨 거리는 1이다.

이 도시에 있는 치킨집은 모두 같은 프랜차이즈이다. 프렌차이즈 본사에서는 수익을 증가시키기 위해 일부 치킨집을 폐업시키려고 한다. 오랜 연구 끝에 이 도시에서 가장 수익을 많이 낼 수 있는  치킨집의 개수는 최대 M개라는 사실을 알아내었다.

도시에 있는 치킨집 중에서 최대 M개를 고르고, 나머지 치킨집은 모두 폐업시켜야 한다. 어떻게 고르면, 도시의 치킨 거리가 가장 작게 될지 구하는 프로그램을 작성하시오.

입력
첫째 줄에 N(2 ≤ N ≤ 50)과 M(1 ≤ M ≤ 13)이 주어진다.

둘째 줄부터 N개의 줄에는 도시의 정보가 주어진다.

도시의 정보는 0, 1, 2로 이루어져 있고, 0은 빈 칸, 1은 집, 2는 치킨집을 의미한다. 집의 개수는 2N개를 넘지 않으며, 적어도 1개는 존재한다. 치킨집의 개수는 M보다 크거나 같고, 13보다 작거나 같다.

출력
첫째 줄에 폐업시키지 않을 치킨집을 최대 M개를 골랐을 때, 도시의 치킨 거리의 최솟값을 출력한다.

'''

'''

조건
시간 제한: 1초
메모리 제한: 512MB

'''

'''
15686 치킨 배달 문제 설계

python으로 작성.

입력 처리:
입출력을 위해 sys를 import한다.
변수 N, M에 sys.stdin.readline()을 통해 입력을 받아 저장한다.
2중 for문을 통해 2차원 배열 city에 좌표 정보를 저장한다.

city는 불변이며, 이후 시뮬레이션에서는 맵 전체를 복사하지 않고
house, chicken 리스트를 기반으로 연산을 수행한다.
좌표값이 1이면 house 리스트에 해당 좌표(x,y)를 저장하고,
좌표값이 2면 chicken 리스트에 해당 좌표를 저장해서 사용한다.

시뮬레이션 처리:
for 문으로 치킨집을 선택하는 모든 M개 조합을 완전탐색한다.
1. 조합마다 선택된 치킨집 리스트(selected_chickens)를 구성한다.
2. house 리스트에 존재하는 모든 좌표에 대해, 선택된 치킨집들과의 맨해튼 거리(|hx - cx| + |hy - cy|)를 계산한다.
3. 각 집은 해당 거리 중 최솟값을 자신의 치킨 거리로 간주한다.
4. 모든 집의 치킨 거리를 더하여 도시의 치킨 거리(cityChickenDistance)를 계산한다.
5. 구한 도시 치킨 거리가 minChickenDistance보다 작다면 업데이트한다.
6. 시뮬레이션 반복이 끝나면 minChickenDistance 값을 출력한다.

Q1.
폐업할 치킨집을 어떻게 골라야 할까?
모든 경우의 수를 다뤄도 통과할 수 있나?

치킨집은 최대 13개이고, 선택할 수 있는 개수는 M ≤ 13이다.
전체 조합 수는 13 C M으로 최대 약 1,716개이며, 각 조합마다
집(최대 100개)과 치킨집(최대 13개) 간의 거리 계산을 수행해도
총 연산은 약 2,229,000번 수준이므로 완전탐색이 가능하다.

Q2.
chickenDistance를 어떻게 구할까? BFS가 나을까 DFS가 나을까?

이 문제는 장애물이나 벽이 없고, 단순히 두 좌표 사이의 최단 거리만 구하면 된다.
따라서 집 좌표(hx, hy)와 치킨집 좌표(cx, cy) 간의 거리 = |hx - cx| + |hy - cy|로 계산하면 되고, 
BFS나 DFS 탐색을 할 필요가 없다.

BFS는 맵의 상태 변화나 장애물 회피가 필요한 경우에 적합하며,
이 문제처럼 상태 변화 없이 거리만 계산하면 되는 경우에는
오히려 BFS는 비효율적이고 시간 초과를 유발할 수 있다.

이 문제는 거리 계산만 수행하면 되므로
맨해튼 거리 수식을 기반으로 효율적인 완전탐색을 수행하는 것이 정답이다.
'''
