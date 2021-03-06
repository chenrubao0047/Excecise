# Problem 12
# Highly divisible triangular number
# The sequence of triangle numbers is generated by adding the natural numbers. So the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28. The first ten terms would be:
#
# 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, …
# Let us list the factors of the first seven triangle numbers:
#
#  1: 1
#  3: 1,3
#  6: 1,2,3,6
# 10: 1,2,5,10
# 15: 1,3,5,15
# 21: 1,3,7,21
# 28: 1,2,4,7,14,28
# We can see that 28 is the first triangle number to have over five divisors.
#
# What is the value of the first triangle number to have over five hundred divisors?
#
# 高度可约的三角形数
# 三角形数数列是通过逐个加上自然数来生成的。例如，第7个三角形数是 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28。三角形数数列的前十项分别是：
#
# 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, …
# 让我们列举出前七个三角形数的所有约数：
#
#  1: 1
#  3: 1,3
#  6: 1,2,3,6
# 10: 1,2,5,10
# 15: 1,3,5,15
# 21: 1,3,7,21
# 28: 1,2,4,7,14,28
# 我们可以看出，28是第一个拥有超过5个约数的三角形数。
#
# 第一个拥有超过500个约数的三角形数是多少？

# 第n个三角形数为：

n = 1
x = 1
lis = []
s = []
def countDivisors(num):
    cnt = 0
    sqrt = int(num ** 0.5)
    for x in range(1, sqrt + 1):
        if num % x == 0:
            cnt += 1
    return cnt * 2 - (sqrt ** 2 == num)

while True:
	# for i in range(1, int(x/2)+1):
	# 	if x % i == 0 and i not in lis:
	# 		lis.append(i)
	cnt = countDivisors(x)
	if cnt >= 500:
		break
	else:
		n += 1
		x = x + n
print(x)

