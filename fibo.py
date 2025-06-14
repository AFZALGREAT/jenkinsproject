series = []
a, b = 0, 1
for _ in range(5):
 series.append(a)
 a, b = b, a + b
    
print(series)

