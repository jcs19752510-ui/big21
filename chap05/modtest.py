# import sys
# # sys.path.append(r"../modules/mod2") # 현재 디렉토리를 모듈 검색 경로에 추가
# import mod2 as mod2
import sys # 1회성으로 생성됨.
sys.path.append(r"C:\big21\python_dev\mymodules") # 현재 디렉토리를 모듈 검색 경로에 추가
import mod2 as mod2
result = mod2.sum(10, 20)
print(result)

