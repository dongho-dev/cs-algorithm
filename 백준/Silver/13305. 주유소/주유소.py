N = int(input())  # 도시 개수 입력
roadLength = list(map(int, input().split()))  # 각 도로 길이 저장
oilPrice = list(map(int, input().split()))  # 각 도시 유류비 저장

minOilPrice = oilPrice[0] # 최소 유류비, 최소 유류비에 첫번째 도시 기름값 저장
resultOilPrice = 0 # 최소 유류비

# 탐색
for i in range(0, N - 1):
  if (minOilPrice > oilPrice[i]):
    minOilPrice = oilPrice[i]
    
  resultOilPrice += minOilPrice * roadLength[i]
  
print(resultOilPrice)