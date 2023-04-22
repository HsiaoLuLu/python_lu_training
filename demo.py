import demo_for_class.point as demo

# result = demo.distance(1, 5)
# print(result)

# -----------------

# 這是比較好的寫法

# 這裡是實體化
point = demo.Point(1, 5)

result = point.distance()
print(result)
result = point.minus()
print(result)

# -----------------

# 這是比較不好的寫法

# 這裡是實體化
point_old = demo.Point_old()

result = point_old.distance(1, 5)
print(result)
result = point_old.minus(2, 3)
print(result)