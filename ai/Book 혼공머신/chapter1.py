bream_length = [25.4, 26.3, 26.5, 29.0, 29.0, 29.7, 29.7, 30.0, 30.0, 30.7, 31.0, 31.0, 
                31.5, 32.0, 32.0, 32.0, 33.0, 33.0, 33.5, 33.5, 34.0, 34.0, 34.5, 35.0, 
                35.0, 35.0, 35.0, 36.0, 36.0, 37.0, 38.5, 38.5, 39.5, 41.0, 41.0]
bream_weight = [242.0, 290.0, 340.0, 363.0, 430.0, 450.0, 500.0, 390.0, 450.0, 500.0, 475.0, 500.0, 
                500.0, 340.0, 600.0, 600.0, 700.0, 700.0, 610.0, 650.0, 575.0, 685.0, 620.0, 680.0, 
                700.0, 725.0, 720.0, 714.0, 850.0, 1000.0, 920.0, 955.0, 925.0, 975.0, 950.0]

smelt_length = [9.8, 10.5, 10.6, 11.0, 11.2, 11.3, 11.8, 11.8, 12.0, 12.2, 12.4, 13.0, 14.3, 15.0]
smelt_weight = [6.7, 7.5, 7.0, 9.7, 9.8, 8.7, 10.0, 9.9, 9.8, 12.2, 13.4, 12.2, 19.7, 19.9]

import matplotlib.pyplot as plt

plt.scatter(bream_length,bream_weight)
plt.scatter(smelt_length,smelt_weight)
plt.xlabel('length')
plt.ylabel('weight')
# plt.show()

length = bream_length + smelt_length
weight = bream_weight + smelt_weight

fish_data = [[l,w] for l,w in zip(length, weight)]

fish_target = [1] * 35 + [0] * 14
# print(fish_target)

from sklearn.neighbors import KNeighborsClassifier

kn = KNeighborsClassifier() # 어떤 알고리즘을 사용할건지 정하고 해당 클래스를 객체화 하는 것
kn.fit(fish_data,fish_target) # 사이킷런 클래스로 만든 kn 객체를 학습하여 모델화 시키는 과정
print(kn.score(fish_data, fish_target)) # 학습된 모델의 정확도 점수를 0~1 사이의 백분율로 산출하는 과정
print(kn.predict([[30,600]])) # 임의의 값을 넣어서 예측하는 과정

kn49 = KNeighborsClassifier(n_neighbors=49) # 참고하는 주변 데이터를 49개로 한 kn49 모델

kn49.fit(fish_data,fish_target)
print(kn49.score(fish_data, fish_target))



