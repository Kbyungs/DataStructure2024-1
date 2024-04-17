def quickSort(a):
  # 길이가 1보다 작거나 같을 경우에는 배열을 그대로 반환
  if len(a) <= 1: return a
  # pivot은 가운데 위치한 값으로 해봄
  pivot = a[len(a)//2]
  temp_low = []
  temp_high = []
  for i in range(len(a)):
    # pivot값은 건너뛰고
    if i != len(a)//2:
      # pivot 중심으로 작은 값은 temp_low, 큰 값은 temp_high
      if a[i] >= pivot: temp_high.append(a[i])
      else: temp_low.append(a[i])
  # 재귀로 각각 temp_low, temp_high를 정렬
  temp_low = quickSort(temp_low)
  temp_high = quickSort(temp_high)
  # 3개를 모두 합쳐서 반환
  return temp_low + [pivot] + temp_high

n = [6, 4, 2, 1, 22, 9, 17]
print(quickSort(n))
