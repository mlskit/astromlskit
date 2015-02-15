import pydtl
import csv

db = pydtl.LocalTable()
reader = csv.reader(open("smaller-dataset.csv"))
for row in reader:
	toDict={}	
	toDict["H"]=float(row[0]);
	toDict["Hmax"]=float(row[1]);
	toDict["UqVal"]=float(row[2]);
	toDict["Favg"]=float(row[3]);
	toDict["N"]=float(row[4]);
	toDict["Uval"]=float(row[5]);
	toDict["pairs"]=float(row[6]);
	toDict["log_pairs"]=float(row[7]);
	toDict["Target"]=float(row[8]);
	db.insert(toDict)

# target = variable to learn	
forest = pydtl.RandomForest(db, target='Target')

#passing no of trees to generate
forest.grow_trees(1)
print forest

#get mean square error
square_errors = []

#passing sample size
samples = db.sample_rows(100)
for inst in samples:
	#rounding off because allowed values for target is either 0 or 1
	y_pred = round(forest.predict(inst))
	y_real = inst['Target']
	square_errors.append((y_pred - y_real)**2)

print y_pred
mse = sum(square_errors) / len(square_errors)
print "Mean Square Error: %.3f" % mse
