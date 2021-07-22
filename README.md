# myHASH
`myHASH`는 다음 기능을 수행한다.
1. 파일 1개의 해시값(MD5, SHA-1, SHA-256) 추출
2. 지정한 디렉터리 및 하위 디렉터리 내에 입력한 해시값을 가진 파일이 있는지 검사
  2-1. 존재한다면 발견 알림 +  해당 파일이 위치한 폴더 열기
  2-2. 존재하지 않는다면 미발견 알림
  
# Overview
![image](https://user-images.githubusercontent.com/49504937/126594589-abf77d5a-131c-4a2b-a69f-f163c6feca77.png)

## 1. HASHING FILE
1. `Select file to hash` 버튼을 눌러 파일 탐색기에서 해시값을 추출한 파일을 선택한다.
![image](https://user-images.githubusercontent.com/49504937/126594677-0001393b-4ba3-4a7e-8e82-b5f5a22175c5.png)

2. 지정한 파일에 대한 해시값을 확인한다.
![image](https://user-images.githubusercontent.com/49504937/126594712-8da8be55-e335-4ebe-b4f7-fc3deb282a49.png)

## 2. FINDING FILE WITH HASH
이 기능은 사용자가 이미 알고있는 해시값을 기반으로 지정한 디렉터리 내에 해당 해시값을 가지는 파일이 있는지의 여부를 알려준다.
1. Hash Type을 선택하고 Hash Value, Dir. Scope를 입력한 후 `ㅇㅇ`를 클릭하여 검색을 시작한다. 이 때 디렉터리 경로를 지정하면 그 하위 디렉터리도 포함하여 검색한다.

![image](https://user-images.githubusercontent.com/49504937/126594981-afcaa5e7-5b96-4799-ad27-9893585a9179.png)

2-1. 존재할 경우: 입력한 해시값에 매치되는 파일의 정보를 확인하고, `예`를 눌러 위치한 디렉터리를 열거나 `아니요`를 눌러 닫는다.

![image](https://user-images.githubusercontent.com/49504937/126595138-b1c93c11-a88b-4a42-a603-1946f143d5b4.png)

![image](https://user-images.githubusercontent.com/49504937/126595177-a691b707-8ed6-4b12-91cc-9191493653d2.png)

2-2. 존재하지 않을 경우: 정보 확인 후 닫는다.

![image](https://user-images.githubusercontent.com/49504937/126595194-e2ff0a7d-f2a2-4615-940a-e7aeb7870971.png)
