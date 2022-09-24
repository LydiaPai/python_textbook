from sklearn import datasets # 利用產生資料的模組
from sklearn import linear_model # 能夠進行線性回歸的模組
from sklearn.model_selection import train_test_split
import numpy as np
import matplotlib.pyplot as plt
# 設定亂數種子
np.random.seed(0) 
# 事先準備線性回歸的資料
x, y = datasets.make_regression(n_samples=100, n_features=1, noise=30)
# 區分學習與測試資料
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3)
# 取得用於回歸的實體物件
e=linear_model.LinearRegression()
# 取得適合的模型
e.fit(x_train, y_train)
# 取得回歸模型
print("迴歸係數為：", e.coef_, "。")
print("截距為：", e.intercept_, "。")
# 用測試資料進行預測
y_pred=e.predict(x_test)
# 評估模型對學習資料的適合度
print("根據學習資料所得到的決定係數為：", e.score(x_train, y_train),"。")
print("根據測試資料所得到的決定係數為：", e.score(x_test, y_test),"。")
plt.scatter(x_train, y_train, label="train")
plt.scatter(x_test, y_test, label="test")
plt.plot(x_test, y_pred, color="magenta")
plt.legend()
plt.show()