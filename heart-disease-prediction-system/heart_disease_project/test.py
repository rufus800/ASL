from sqlite3 import *
import pickle


d = [[80, 1, 120, 230, 65, 0.2, 10, 20]]
# d = [[age, cp, BP, CH, maxhr, STD, fluro, Th]]
print(d)
with open("heartdiseaseprediction.model", "rb") as f:
    model = pickle.load(f)	
res = model.predict(d)
print(res)