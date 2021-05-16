import csv
def sort_byapples(filename):
	apples=0
	num=0
	mapping=[]
	i=0
	with open(filename, 'r') as f, open('sorted_apples.txt' , 'w') as fw:
		reader = csv.reader(f)
		for line in reader:
			for item in line:
				num+=1
				if item == 'apple':
					apples +=1
			mapping.append([line,float(apples/num)])
		sorted_list=sorted(mapping, key=lambda x:x[1], reverse =True)
		print(sorted_list)
		for line, avg in sorted_list:
			fw.write(str(','.join(line)) +'\n')
sort_byapples('apple.txt')