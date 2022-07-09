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
	a=[4, 3, 7, 8, 6, 2, 1]
	n=len(a)
	z(a,n)

