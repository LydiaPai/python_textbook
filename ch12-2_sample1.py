import statistics
data=[8, 17, 0, 11, 6, 21, 16, 6,  17, 11, 
      7, 9, 6, 13, 12, 16, 3, 14, 13, 12]
# 平均數(mean)：將所有資料相加之後，再除以資料個數的值。
print("平均數為：", statistics.mean(data), "。")
# 中位數(median)：將資料「排序」後，位於中間的值。當資料的個數為偶數時，會取得兩個中位數的平均。
print("中位數為：", statistics.median(data), "。")
# 眾數(mode)：資料中重複次數最多的值。
print("眾數為：", statistics.mode(data), "。")
# 變異數(variance)：指個資料與平均數之間的差，其平方值的平均，表示資料與平均數之間分離的程度。
print("變異為：", statistics.pvariance(data), "。")
# 標準差(standard deviation)：變異數的正平方根，常用來做為表示資料離散程度的直觀指標。
print("標準差為：", statistics.pstdev(data), "。")