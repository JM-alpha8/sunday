import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


print('1번째 zeros()실수형태 0. 숫자발생')
print(np.zeros(10)) # 1행 10열
print()

print(np.zeros( (3,6) )) #  3행 * 6열
print('- ' * 40)
print()

data = [ 6, 7, 8, 9,  1.2] 
A = np.array(data)
print(A) 
print(np.zeros(A) ) 
print()






print()
print()