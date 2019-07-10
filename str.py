x,y=[i for i in input().split()]

for j in range(len(x)):
	if x[j] == y[j]:
		j=j+1
	else:
		break
print(len(y)-j)
