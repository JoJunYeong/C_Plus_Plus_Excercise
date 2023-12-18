# 특성공학과 규제
import pandas as pd # 데이터 분석 라이브러리
df = pd.read_csv('https://bit.ly/perch_csv_data') # 데이터 불러오기
perch_full = df.to_numpy() # 넘파이 배열로 변환
print(perch_full)

import numpy as np # 넘파이 라이브러리
perch_weight = np.array([5.9, 32.0, 40.0, 51.5, 70.0, 100.0, 78.0, 80.0, 85.0, 85.0, 110.0,
       115.0, 125.0, 130.0, 120.0, 120.0, 130.0, 135.0, 110.0, 130.0,
       150.0, 145.0, 150.0, 170.0, 225.0, 145.0, 188.0, 180.0, 197.0,
       218.0, 300.0, 260.0, 265.0, 250.0, 250.0, 300.0, 320.0, 514.0,
       556.0, 840.0, 685.0, 700.0, 700.0, 690.0, 900.0, 650.0, 820.0,
       850.0, 900.0, 1015.0, 820.0, 1100.0, 1000.0, 1100.0, 1000.0,
       1000.0])

from sklearn.model_selection import train_test_split # 훈련 세트와 테스트 세트로 나누기
train_input, test_input, train_target, test_target = train_test_split(perch_full, perch_weight, random_state=42) # 훈련 세트와 테스트 세트로 나누기

from sklearn.preprocessing import PolynomialFeatures # 특성 공학
poly = PolynomialFeatures(include_bias=False) # 객체 생성
poly.fit([[2,3]]) # 2와 3을 각각 제곱한 값과 2와 3을 곱한 값을 구함
print(poly.transform([[2,3]])) # 특성을 새롭게 만듦

poly = PolynomialFeatures(include_bias=False) # 객체 생성
poly.fit(train_input) # 훈련 세트에 적용
train_poly = poly.transform(train_input) # 훈련 세트를 변환
print(train_poly.shape) # 훈련 세트의 크기 확인
print(poly.get_feature_names_out()) # 특성 이름 확인

from sklearn.linear_model import LinearRegression # 선형 회귀 모델
lr = LinearRegression() # 객체 생성
lr.fit(train_poly, train_target) # 훈련
print(lr.score(train_poly, train_target)) # 훈련 세트 점수 출력
print(lr.score(poly.transform(test_input), test_target)) # 테스트 세트 점수 출력

poly = PolynomialFeatures(degree=5, include_bias=False) # 5제곱 특성을 만듦
poly.fit(train_input) # 훈련 세트에 적용
train_poly = poly.transform(train_input) # 훈련 세트를 변환
test_poly = poly.transform(test_input) # 테스트 세트를 변환
print(train_poly.shape) # 훈련 세트의 크기 확인

lr.fit(train_poly, train_target) # 훈련
print(lr.score(train_poly, train_target)) # 훈련 세트 점수 출력
print(lr.score(test_poly, test_target)) # 테스트 세트 점수 출력

from sklearn.preprocessing import StandardScaler # 표준화 전처리
ss = StandardScaler() # 객체 생성
ss.fit(train_poly) # 훈련 세트에 적용
train_scaled = ss.transform(train_poly) # 훈련 세트를 변환
test_scaled = ss.transform(test_poly) # 테스트 세트를 변환

from sklearn.linear_model import Ridge # 릿지 회귀 모델
ridge = Ridge() # 객체 생성
ridge.fit(train_scaled, train_target) # 훈련
print(ridge.score(train_scaled, train_target)) # 훈련 세트 점수 출력
print(ridge.score(test_scaled, test_target)) # 테스트 세트 점수 출력

import matplotlib.pyplot as plt # 그래프 그리기
train_score=[]
test_score=[]

# alpha_list = [0.001, 0.01, 0.1, 1, 10, 100] # alpha 값의 범위
# for alpha in alpha_list: # alpha 값의 범위를 반복
#     ridge = Ridge(alpha=alpha) # 릿지 모델 생성
#     ridge.fit(train_scaled, train_target) # 훈련
#     train_score.append(ridge.score(train_scaled, train_target)) # 훈련 점수 저장
#     test_score.append(ridge.score(test_scaled, test_target)) # 테스트 점수 저장

# plt.plot(np.log10(alpha_list), train_score) # 훈련 점수 그래프
# plt.plot(np.log10(alpha_list), test_score) # 테스트 점수 그래프
# plt.xlabel('alpha') # x축 레이블
# plt.ylabel('R^2') # y축 레이블
# plt.show() # 그래프 출력


ridge = Ridge(alpha=0.1) # alpha 값을 0.1로 설정
ridge.fit(train_scaled, train_target) # 훈련
print(ridge.score(train_scaled, train_target)) # 훈련 점수 출력
print(ridge.score(test_scaled, test_target)) # 테스트 점수 출력


from sklearn.linear_model import Lasso # 라쏘 회귀 모델
lasso = Lasso() # 객체 생성
lasso.fit(train_scaled, train_target) # 훈련
print(lasso.score(train_scaled, train_target)) # 훈련 점수 출력
print(lasso.score(test_scaled, test_target)) # 테스트 점수 출력

alpha_list = [0.001, 0.01, 0.1, 1, 10, 100] # alpha 값의 범위
for alpha in alpha_list: # alpha 값의 범위를 반복
    lasso = Lasso(alpha=alpha, max_iter=10000) # 릿지 모델 생성
    lasso.fit(train_scaled, train_target) # 훈련
    train_score.append(lasso.score(train_scaled, train_target)) # 훈련 점수 저장
    test_score.append(lasso.score(test_scaled, test_target)) # 테스트 점수 저장

plt.plot(np.log10(alpha_list), train_score) # 훈련 점수 그래프
plt.plot(np.log10(alpha_list), test_score) # 테스트 점수 그래프
plt.xlabel('alpha') # x축 레이블
plt.ylabel('R^2') # y축 레이블
# plt.show() # 그래프 출력

lasso = Lasso(alpha=10) # alpha 값을 10으로 설정
lasso.fit(train_scaled, train_target) # 훈련
print(lasso.score(train_scaled, train_target)) # 훈련 점수 출력
print(lasso.score(test_scaled, test_target)) # 테스트 점수 출력
