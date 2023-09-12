T = int(input())

for i in range(T):
    N = int(input())
    K = int(input())
    print(int((N % K)+(N // K)))