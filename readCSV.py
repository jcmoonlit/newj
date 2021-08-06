import csv,time

file = 'testcsv.csv'

d = 6674
num = 5
start = 1
end = start + num + 1


def toMail(file,start,num,times=3):
	with open(file) as f:
		i = 1
		k = 1
		f_csv = csv.reader(f)
		for row in f_csv:
			if i>=start and i<=start+num-1:
				if i % 3 == 0:
					time.sleep(times)
				print(row[0],'i:',i)
				k+=1
			if k > num:
				print("ok")
				break
			print(i)
			i+=1


def toMail0(file):
	with open(file,'r') as f:
		reader = csv.DictReader(f)
		for row in reader:
			print(row)


if __name__ == '__main__':
	#toMail(file,start,num,2)
	toMail0(file)