with open(input()) as nums:
    num = nums.read()
    num = num.split()
num = [int(item) for item in num]
m = sorted(num)[len(num) // 2]
print(sum(abs(v - m) for v in num))