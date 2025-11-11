import numpy as np
company,datejoined,country,valuation,industry = np.genfromtxt('Startups in 2021 end.csv', delimiter=',' , usecols=(1,3,4,2,6), unpack=True , dtype=None,skip_header=1)
print(company)
print(datejoined)
print(country)
print(valuation)
print(industry)


int_X = valuation.astype(str)
int_X = np.char.replace(int_X,'$','')
int_X = int_X.astype(float)
print("means: " , np.mean(int_X))

#statics operations
print(np.mean(int_X))
print(np.average(int_X))
print(np.std(int_X))
print(np.median(int_X))
print(np.percentile(int_X,67))
print(np.percentile(int_X,75))
print(np.percentile(int_X,3))
print(np.min(int_X))
print(np.max(int_X))


# maths operations
print("square: " , np.square(int_X))
print("sqrt: " , np.sqrt(int_X))
print("pow: " , np.power(int_X,int_X))
print("abs: " , np.abs(int_X))

#Trigonometric Functions

int_XPie = (int_X/np.pi) +1
# Calculate sine, cosine, and tangent
sine_values = np.sin(int_XPie)
cosine_values = np.cos(int_XPie)
tangent_values = np.tan(int_XPie)

print("Zameen.com int_X - div - pie  - Sine values:", sine_values)
print("Zameen.com int_X - div - pie Cosine values:", cosine_values)
print("Zameen.com int_X - div - pie Tangent values:", tangent_values)

print("Zameen.com int_X - div - pie  - Exponential values:", np.exp(int_XPie))
