import  matplotlib.pyplot as plt
import streamlit as st

fig, ax = plt.subplots()

data = list(range(-29, 30, 3))
print(data)

c1 = st.sidebar.radio ('선의 색을 선택하시오', ['red', 'green', 'purple', 'orange'])
s1 = st.sidebar.radio ('선의 스타일을 선택하시오', ['-', '--', ':', '-.'])
m1 = st.sidebar.radio ('마커의 스타일을 선택하시오', ['o', '^', 's', 'p'])

a = st.number_input('a의 값을 입력하시오', value=2.0, step=1.0)
b = st.number_input('b의 값을 입력하시오', value=-1.0, step=1.0)
c = st.number_input('c의 값을 입력하시오', value=15.0, step=1.0)
d = st.number_input('d의 값을 입력하시오', value=2000.0, step=100.0)



love = []
y = []
y1 = []
y2 = []


for i in range(-29, 30, 3):
    love.append(i)
    y.append(-2*i*i + 3*i + 5)
    # y1.append(y + ax + bx + c)
plt.plot(love, y, color = c1, linestyle = s1, marker = m1)



st.pyplot(fig)

import  matplotlib.pyplot as plt
import streamlit as st

fig, ax = plt.subplots()



# a = st.number_input('a의 값을 입력하시오', value=2.0, step=1.0)
# b = st.number_input('b의 값을 입력하시오', value=-1.0, step=1.0)
# c = st.number_input('c의 값을 입력하시오', value=15.0, step=1.0)
# d = st.number_input('d의 값을 입력하시오', value=2000.0, step=100.0)

# import matplotlib.pyplot as plt

# # numbers = []
# # for i in range():
# #     numbers

# y1 = []
# y2 = []

# y1 = ax* + bx + c



# # for i in range(-19, 30, 3):
# #     love.append(i)
# #     y.append(-2*i*i + 3*i + 5)
# # plt.plot(love, y, color = c1, linestyle = s1, marker = m1)



# st.pyplot(fig)






# print('y 데이터 생성')

# print(y1 = ax)


# def generate_data(n, a, b, c, d):
  
#     x = np.random.rand(n)
    
  
#     y1 = a * x**2 + b * x + c
    
 
#     y2 = x % d
    
   
#     y = y1 + y2
    
#     return x, y


# n = 100 
# a, b, c = 1, 2, 3  
# d = 5 
# x, y = generate_data(n, a, b, c, d)


# plt.scatter(x, y, label='Generated Data')
# plt.xlabel('x')
# plt.ylabel('y')
# plt.legend()
# plt.show()

