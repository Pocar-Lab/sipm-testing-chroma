

TefSpecRef=0.15
TefDiffRef=0.85
AlSpecRef=1.0
AlDiffRef=0
AlAbsorb=0.0
CuSpecRef=0.05
CuDiffRef=0.0
CuAbsorb=0
b=0.05 #step size of copper diffuse and spec reflection 
c=0.1  #step size of aluminum diffuse and absorption 


while TefDiffRef<=1.00 and TefDiffRef>=0.85 and TefSpecRef<=0.15 and TefSpecRef>=0.0:
	if float(TefDiffRef) + float(TefSpecRef) == 1.0:
		TefDiffRef+=float(0.05)
		TefSpecRef+=float(-0.05)
	else:
		break 
	CuDiffRef=0
	CuSpecRef=0
	CuAbsorb=1

	for j in range(3):
		if CuAbsorb!=1.0:
			CuDiffRef+=float(b)
			CuSpecRef+=float(-b) 
			AlAbsorb=0.0
			AlSpecRef=1.0
			for k in range(3):
				AlAbsorb+=float(c)
				AlSpecRef+=float(-c)
				print CuSpecRef, CuDiffRef, CuAbsorb, AlSpecRef, AlAbsorb, 'String' 
			
		if CuDiffRef==0 and CuSpecRef==0:
			CuAbsorb=1.0


			AlAbsorb=0.0
			AlSpecRef=1.0
			for k in range(3):
				AlAbsorb+=float(c)
				AlSpecRef+=float(-c)
				print CuSpecRef, CuDiffRef, CuAbsorb, AlSpecRef, AlAbsorb
			CuDiffRef=-0.05
			CuSpecRef=0.1
			CuAbsorb=0.95
		
				 
