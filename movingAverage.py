x, y = map(int, input().split())
n = int(input())
p = list(map(float, input().split()))[:n]
sum_x = 0.0
sum_y = 0.0
for i in range(x):
    sum_x += p[i]
for i in range(y):
    sum_y += p[i]
ma_x = 20 * [0]
ma_y = 20 * [0]
ma_x[0] = sum_x / x
ma_y[0] = sum_y / y
j = 1
for i in range(x, n):
    j += 1
    sum_x += (p[i - x] + p[i])
    ma_x[j] = sum_x / x
j = 1
for i in range(y, n):
    j += 1
    sum_y += (-p[i - y] + p[i])
    ma_y[j] = sum_y / y

above = 0
count = 0
if(ma_x[y - x] > ma_y[0] and above == 0):
    above = 1
if(maxadc==adc[0]):
    for i in range(100):
        if(minadc > adc[i]):
            minadc = adc[i]

            (ans1)=4 * pow((maxabc+maxadc), 2)
            (ans2)=4 * pow((minabc+minadc), 2)
print(round(ans1))
print(round(ans2))
