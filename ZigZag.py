def z(a,n):
	flag=True
	for i in range(n-1):
	
		if flag is True:
			if a[i]>a[i+1]:
				a[i],a[i+1]=a[i+1],a[i]
		else:
			if a[i]<a[i+1]:
				a[i],a[i+1]=a[i+1],a[i]
		flag=bool(1-flag)
	print(a)
if __name__=='__main__':
	a=list(map(int,input().split()))
	z(a,len(a))

