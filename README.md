## 데이터 분석, 웹 프로젝트 - 미대출 도서 추천 시스템
기간 : 2020.11.02 - 2020.11.16 / 2021.01.08 - 2021.01.13

깃허브 : https://github.com/dmswl0311/library-AI-web-project

웹 페이지 : [http://choeunji.pythonanywhere.com/](http://choeunji.pythonanywhere.com/)

### **서비스 소개 및 주제**

국내 공공도서관의 경우 내부적으로 편향된 도서 대출로 인해 도서관 이용 활성화가 저하되고 장서 포화의 문제가 발생하고 있습니다. 이와 같은 문제를 해결하기 위해 빅데이터와 인공지능에서 각광받고 있는 추천 시스템 알고리즘을 활용하여 기존의 인기 도서가 아닌 인기도서와 유사한 미대출 도서를 추천하는 시스템을 개발하였습니다.
![image](https://user-images.githubusercontent.com/48826021/148410413-8b5585a7-8276-44df-93c1-f95711ab2180.png)
![image](https://user-images.githubusercontent.com/48826021/148410467-214058ef-abd6-4971-a799-165928f316ca.png)

### **맡은 역할**

Open API를 이용한 데이터 수집, 파이썬을 이용한 데이터 전처리, 코사인 유사도를 이용해 인기 도서와 유사한 미대출 도서 추천 리스트 개발, 웹 개발 

### **사용 기술 스택**

Python, R, Django, HTML, CSS, Java Script

### **사용 API & 데이터**

- 도서관 정보나루 장서/대출 목록 데이터
- 대구디지털산업진흥원 대출 이력 데이터
- 대구디지털산업진흥원 회원 정보 데이터
- 도서관 정보나루 도서 상세 정보 Open API

### 분석 프로세스
![image](https://user-images.githubusercontent.com/48826021/148410482-2d0e0778-bc82-4132-a8f3-042f8c288721.png)

### 프로젝트 결과
![image](https://user-images.githubusercontent.com/48826021/148410534-027cf129-34e4-469c-9eb1-3667f9faa05a.png)
![image](https://user-images.githubusercontent.com/48826021/148410559-03956605-092a-4ba8-bab5-5aac367cffcb.png)

### 성과

도서관 빅데이터 우수 활용사례 및 아이디어 공모전 데이터 분석부문 최우수상 수상

‘공공도서관 미대출 도서 추천시스템 구현: 대구 D도서관을 중심으로’ 논문 작성 및 KCI 등재

### 설치
```
pip install django
pip install django-import-export
```
