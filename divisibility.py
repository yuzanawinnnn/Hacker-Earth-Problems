import sys
sys.set_int_max_str_digits(0)
N = int(input())
data = input().split()
num = ""
for i in range(N):
    num = num + data[-1]
    
if(int(num)% 10 == 0):
    ans = "Yes"
else:
    ans = "No"

print(ans)
