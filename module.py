#sys模組，python內建模組存放系統相關的重要資訊
#載入sys模組
# import sys
# #使用sys模組
# print(sys.platform) #印出作業系統
# print(sys.maxsize) #印出整數型態的最大值
# print(sys.path) #印出搜尋模組的路徑

#載入sys模組
# import sys as s #s是別名，可以利用別名操作模組
# #使用sys模組
# print(s.platform) #印出作業系統
# print(s.maxsize) #印出整數型態的最大值
# print(s.path) #印出搜尋模組的路徑

#建立 geometry 模組，載入使用
import geometry2.point
result=geometry2.point.distance(1, 5)
print(result)
# result=geometry.slope(1,2,5,6)
# print(result)

#調整搜尋模組的路徑
# import sys
# # print(sys.path) #印出模組的搜尋路徑列表
# sys.path.append("modules")
# # print(sys.path)
# import geometry
# print(geometry.distance(1,1,5,5))