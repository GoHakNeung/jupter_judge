# 상호작용형 프로그램 자동 평가 시스템
**상호작용형 프로그램 자동 평가 시스템은** 주피터 노트북에서 설명, 실습, 평가를 할 수 있는 모듈입니다.
- 설명 : Text cell을 이용한 설명  
- 실습 : Code cell을 이용한 코드 작성 및 결과 확인
- 평가 : Code cell을 이용해서 문제 제시, 코드 작성, 코드 평가 실시  
(주피터 노트북에서 활용할 수 있으나, 모듈에서 파일 경로는 **Colab**을 기준으로 작성하였으므로, **Colab**에서 사용하는 것을 추천합니다.)  

## 사용 방법
상호작용형 프로그램 자동 평가 시스템은 중앙 서버에서 평가하는 것이 아닌 개별 **주피터 노트북(Kernel)**에서 평가합니다.  

- **초기 설정** : Code cell에서 **Git**에 공개한 자동 평가 모듈을 다운로드 받고 실행합니다.
``` python
!git clone https://github.com/GoHakNeung/jupyter_judge.git
%run /content/jupyter_judge/code_check.py 
```

- **문제 출력** :  
  - Code cell에서 **Question('문제번호','문제유형')** 함수를 통해 작동됩니다.
  - Code cell Output에서 문제, 코드 작성을 위한 공간, 결과를 확인하는 버튼이 출력됩니다.  

  ``` python
Question('6201', 'code')
```
![문제 출력 예시](https://github.com/GoHakNeung/python/blob/main/python/%EC%88%98%EC%A0%95_%EB%AC%B8%EC%A0%9C.png?raw=true)
- **문제 해결하기** : 
  - **코드 작성** 공간에 코드를 작성한 후 **제출** 버튼을 클릭합니다.  
  - 평가 결과(정답, 오답, 오류)는 제출 버튼 하단에 출력됩니다.  
    
  ![문자숫자예시](https://github.com/GoHakNeung/python/blob/main/python/%EB%AC%B8%EC%9E%90%20%EC%88%AB%EC%9E%90%20%EC%98%88%EC%8B%9C.png?raw=true)
___
___

## 평가 유형
평가할 수 있는 유형은 문자·숫자 데이터, turtle 라이브러리, matplotlib, pandas 입니다.  
매개변수에 대한 값으로 'code', 'turtle', 'plot','pandas'를 입력합니다.   
- 'code' : 기본값이며 문자, 숫자 데이터를 평가합니다.  
  (문제 : 1000~7000번대 문제이며 5000번대에 있는 일부 반복 문제 제외)
  ```python
Question('6201', 'code')
```
  ![문자숫자예시](https://github.com/GoHakNeung/python/blob/main/python/%EB%AC%B8%EC%9E%90%20%EC%88%AB%EC%9E%90%20%EC%98%88%EC%8B%9C.png?raw=true)
- 'turtle' : 터틀 라이브러리를 활용한 평가입니다.  
  (문제 : 5201~5206)  
```python
Question('5203', 'turtle')
```
  ![turtle예시](https://github.com/GoHakNeung/python/blob/main/python/turtle%20%EC%98%88%EC%8B%9C.png?raw=true)
- 'plot' :  matplotlib를 활용한 데이터 시각화 평가입니다.  
  (문제 : 8501~8583)    
```python
Question('8572', 'plot')
```
  ![plot예시](https://github.com/GoHakNeung/python/blob/main/python/plot%20%EB%AC%B8%EC%A0%9C%20%EC%98%88%EC%8B%9C1.png?raw=true)
- 'pandas' : pandas 라이브러리를 활용한 데이터 전처리 평가입니다.  
  (문제 : 8601~8621)
```python
Question('8614', 'pandas')
```
  ![pandas예시](https://github.com/GoHakNeung/python/blob/main/python/pandas%20%EB%AC%B8%EC%A0%9C%20%EC%98%88%EC%8B%9C.png?raw=true)

