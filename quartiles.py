# 3-2
import numpy as np

def print_quartiles(data):
    # 데이터를 오름차순으로 정렬
    sorted_data = sorted(data)

    # 각 사분위수 계산
    q1 = np.percentile(sorted_data, 25); # 제1사분위수 (25%)
    q2 = np.percentile(sorted_data, 50); # 제2사분위수 (50%, 중앙값)
    q3 = np.percentile(sorted_data, 75); # 제3사분위수 (75%)

    print(f"정렬된 데이터: {sorted_data}")
    print(f"제1사분위수 (Q1): {q1}")
    print(f"제2사분위수 (Q2/중앙값): {q2}")
    print(f"제3사분위수 (Q3): {q3}")

# 실행 예시
numbers = [7, 15, 49, 40, 41, 36, 39, 78, 65, 89, 32, 24, 65]
print_quartiles(numbers)
