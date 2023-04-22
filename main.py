#主程式
# import geometry2.point
# result=geometry2.point.distance(3,4)
# print("距離",result)

# import geometry2.line
# result=geometry2.line.slope(1,1,3,3)
# print("斜率",result)

import geometry2.line
import geometry2.line as linee #如果覺得名字太長，可以使用別名，但下一行就需要使用一樣的名稱，程式才有辦法跑
result=linee.slope(1,1,3,3)
print("斜率",result)