
'''
N장의 카드가 바닥에 왼쪽에서 오른쪽으로 일렬로 놓여 있다. 
왼쪽에서 i번째에 위치한 카드의 앞면에는 정수 
A_i 가 쓰여 있다.

채완이는 희원이와 카드를 가지고 홀수와 짝수 게임을 하려고 한다. 

게임의 규칙은 다음과 같다.

게임은 두 사람이 번갈아 가며 진행하며, 채완이부터 시작한다.
각 플레이어는 자신의 차례가 될 때마다 바닥에 남아있는 카드 중 한 장을 골라 들고 간다. 
이때, 다음 조건을 만족하는 카드만 들고 갈 수 있다.

각 플레이어가 첫 번째로 들고 갈 수 있는 카드에는 제약이 없다.

! 이후 두 번째부터 들고 가는 카드는 반드시 자신이 첫 번째로 들고 간 카드와 홀짝 여부가 동일해야 한다.

만약 더 이상 카드를 들고 갈 수 없다면 그 플레이어가 패배한다.
채완이와 희원이가 각각 최선의 전략을 사용해 게임을 진행한다고 할 때, 

게임의 승자를 구해보자.
'''

from sys import stdin
for _ in range(int(stdin.readline())):
	N = int(stdin.readline())
	O = sum(i&1 for i in map(int, stdin.readline().split()))
	if (O == N-O) or not (max(O, N-O) & 1): print("heeda0528")
	else: print("amsminn")


