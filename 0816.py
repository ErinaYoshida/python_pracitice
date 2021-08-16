# -*- coding: utf-8 -*-
"""
Created on Mon Aug 16 21:17:35 2021

@author: erina
"""

"""
numpy配列の作成
import numpy as np
a = np.array([1,2,3,4,5])
print(a) #[1 2 3 4 5]
print(type(a)) #<class 'numpy.ndarray'>

la = [1,2,3,4] #先にリストを変数に格納してもOK
a = np.array(la)
print(a) #[1 2 3 4]
"""

"""
numpy配列の四則演算
import numpy as np
a = np.array([1,2,3,4,5])
sa = a + 2
print(sa) #[3 4 5 6 7] 
#listで同じことをすると
a = [1,2,3,4,5]
sa = []
for i in a:
    sa.append(i + 2)
print(sa) #[3, 4, 5, 6, 7]
"""

"""
numpy配列とnumpy配列の計算
import numpy as np
a = np.array([1,2,3,4,5])
a2 = np.array([3,4,2,5,6])
print(a + a2) #[ 4  6  5  9 11]
"""

"""
import numpy as np
a = [[1,2,3,4,5],[2,3,7,3,6]]
aa = np.array(a)
print(a[1][2]) #listではリスト[行][列]で指定
print(aa[1,2]) #numpyではnumpy.ndarray[行,列]で指定
"""

"""
配列の変形
import numpy as np
a = [[1,2,3,4,5],[2,3,4,3,6]] #2行5列の配列
print(a) #[[1, 2, 3, 4, 5], [2, 3, 4, 3, 6]]
aa = np.array(a)
print(aa) #2行5列の配列
#[[1 2 3 4 5]
# [2 3 4 3 6]]
aa2 = aa.reshape(1,10) #1行10列の配列
print(aa2) #[[1 2 3 4 5 2 3 4 3 6]]
aa3 = aa.reshape(5,2) #5行2列の配列
print(aa3)
#[[1 2]
 #[3 4]
 #[5 2]
 #[3 4]
 #[3 6]]
 """