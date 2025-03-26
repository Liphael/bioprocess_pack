# coeffcient_std 多项式回归模型的系数标准化
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures, StandardScaler

# 生成示例数据
np.random.seed(0)
X = 2 - 3 * np.random.normal(0, 1, 20)
Y = X - 2 * (X ** 2) + 0.5 * (X ** 3) + np.random.normal(-3, 3, 20)
X = X.reshape(-1, 1)

# 标准化原始特征
scaler = StandardScaler()
X_std = scaler.fit_transform(X)

# 生成多项式特征（标准化后的X）
poly = PolynomialFeatures(degree=3)
X_poly_std = poly.fit_transform(X_std)

# 拟合模型
model = LinearRegression()
model.fit(X_poly_std, Y)

# 输出标准化系数（排除截距项β0）
coefficients_std = model.coef_[1:]  # β1, β2, β3
print("标准化系数:", coefficients_std)