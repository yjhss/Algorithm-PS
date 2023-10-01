n = int(input())
members = []

for i in range(n):
    age, name = map(str, input().split())
    age = int(age)
    members.append((age, name)) #튜플로 저장 (나이,이름)

members.sort(key = lambda x : x[0])	# (age, name)에서 age만 비교

for i in members:
    print(i[0], i[1])