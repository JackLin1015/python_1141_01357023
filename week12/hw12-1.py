from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# 1. 載入 Iris 資料集
iris = load_iris()
X = iris.data
y = iris.target

# 2. 切分訓練資料與測試資料
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

# 3. 特徵標準化（對 KNN、Logistic Regression 都有幫助）
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# -------------------------
# 方法一：K-Nearest Neighbors
# -------------------------
knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(X_train, y_train)
y_pred_knn = knn.predict(X_test)
acc_knn = accuracy_score(y_test, y_pred_knn)

# -------------------------
# 方法二：Logistic Regression
# -------------------------
logreg = LogisticRegression(max_iter=200)
logreg.fit(X_train, y_train)
y_pred_logreg = logreg.predict(X_test)
acc_logreg = accuracy_score(y_test, y_pred_logreg)

# 4. 輸出結果
print("KNN Accuracy:", acc_knn)
print("Logistic Regression Accuracy:", acc_logreg)
