# print("hello world")
# N = int(input().strip())
# if N%2!=0:
#     print("weird")
# else:
#     if N>=2 and N<=5:
#         print("Not Weird")
#     elif N >= 6 and N <= 20:
#         print("Weird")
#     elif N > 20:
#         print("Not Weird")
n = int(input())
if n in range(1,21):
            for i in range(n): 
                    print(i*i)