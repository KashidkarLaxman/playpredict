from sklearn.metrics import accuracy_score
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
import pandas as pd
def knn() :
	data=pd.read_csv(r'\python\notes\MarvellousInfosystems_PlayPredictor.csv')
	df=pd.DataFrame(data,columns=['Wether','Temperature','Play'])

	wether={'Sunny':1,'Rainy':2,'Overcast':3}
	temperature={'Hot':1,'Mild':2,'Cool':3}
	play={'No':0,'Yes':1}
	df.Wether=[wether[item] for item in df.Wether]
	df.Temperature=[temperature[item] for item in df.Temperature]
	df.Play=[play[item] for item in df.Play]
	data=df[['Wether','Temperature']]

	target=df[['Play']]

	train_data,test_data,train_target,test_target =train_test_split(data,target,test_size=0.7)
	clf=KNeighborsClassifier(n_neighbors=3)
	clf.fit(data,target)
	prediction=clf.predict(test_data)

	accuracy=accuracy_score(test_target,prediction)
	print(accuracy*100)
	for i  in prediction :
		
		if i == 1 :
			print("play ")
		else :
			print("cant play")
		
		

def main() :
	knn()


if __name__ == "__main__" :
	main()