#1比较运算符可以连用
c00 = 5
print(1<c00<6)

#2位操作
c01 = 0b11001
c02 = 0b01000
c03 = c01|c02  # "|" 按位或 "^" 按异位或  "&" 按位与
print(bin(c03))


#3保留n位小数
print(f'{2.5:.2f}')

