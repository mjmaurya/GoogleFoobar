def solution(x,y):
	data={}
	for i in x:
		data[i]=data.get(i,0)+1
	for i in y:
		data[i]=data.get(i,0)-1
	for key in data:
		if (data[key]==1 or data[key]==-1):
			return key
	return None