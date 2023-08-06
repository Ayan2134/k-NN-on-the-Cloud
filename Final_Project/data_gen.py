import numpy as np
m=10000
d=50
with open('./database.txt','w') as data :
    for i in range(m) :
        point_vector=np.random.randint(-10,10,(d,1))
        for point in point_vector :
            data.write(str(float(point)))
            data.write(" ")
        data.write("\n")
            