nkg=input()
att1=list(map(int,npit.split()))
kit1=att1[1]
hit=input()
flag1=0
svs=list(map(int,hit.split()))
for i in range(0,len(svs)-1):
	for j in range(i+1,len(svs)):
		if svs[i]+svs[j]==kit1:
			print("yes")
			flag1=1
			break
	if flag1==1:
		break
if flag1!=1:
	print("no")
