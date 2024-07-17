import matplotlib.pyplot as plt

def fibonacci(n):
	fibonacci = [0, 1]
	for i in range(2, n):
		fibonacci.append(fibonacci[i-1] + fibonacci[i-2])
		print(f'{fibonacci[i-1]} + {fibonacci[i-2]} = {fibonacci[i]}')
	return fibonacci



def plotFibonacci(n):
	plt.plot(fibonacci(n))
	plt.show()
 
plotFibonacci(50)