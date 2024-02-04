unyangTypingMaster   
==================

본 프로그램은 ChatGPT를 이용해 작성되었음.   

내가 제시한 프롬프트:

> Python을 이용해 ‘타이핑 웍스’ 웹 사이트에 접속하여 사용자의 타자 속도를 측정하고, 측정된 평균 타자 속도를 가져와 데이터베이스에 저장하고 랭킹 기능을 구현해주세요.   
> 
> 프로그램은 다음 조건을 따라서 만들어져야 합니다.   
> 
>   1.	Python을 실행했을 때 다음과 같이 표시되어야 합니다.   
>   a.	콘솔 창에 ‘운양고 타자왕’이 표시되어야 합니다.   
>   b.	콘솔 창에는 데이터베이스를 이용해 현재까지의 랭크가 표시되어야 합니다.   
>   c.	랭크는 가장 높은 10명만을 표시하되, 필요시 사용자의 입력을 받아 모든 랭크를 표시하는 기능을 구현해주세요.   
>   d.	데이터베이스에 자료가 없다면, ‘아무도 없음’을 표시해주세요.   
>   e.	랭크 표시 후, 사용자의 입력을 받아주세요.   
>   i.	‘도전하려면 Y를 누르세요’ 라고 표시한 후 사용자가 키를 누르면 아래 동작을 수행합니다.   
>   ii.	‘모든 랭크를 보려면 R을 누르세요’ 라고 표시한 후 사용자가 R을 입력하면 저장된 모든 랭크를 표시해야 합니다.   
>   2.	Python을 이용해 GUI를 구현해야 합니다.   
>   a.	프로그램은 학번을 입력받아 저장해야 합니다.  
>   i.	학번의 가장 첫번째 숫자는 학년을 의미합니다.  
>   ii.	학번의 두번째부터 세번째 숫자는 반을 의미합니다.  
>   iii.	학번의 네번째부터 다섯번째 숫자는 번호를 의미합니다.  
>   b.	프로그램은 이름을 입력받아 저장해야 합니다.  
>   c.	만약 학번이나 이름이 이미 데이터베이스에 저장된 값이라면, 사용자는 도전을 할 수 없습니다. 모든 사용자는 1번의 도전 기회만을 가집니다.  
>   3.	Python의 Selenium 라이브러리를 이용할 것.  
>   a.	Selenium은 Chrome web driver를 사용해야 합니다.  
>   b.	‘타이핑 웍스’ 웹 사이트의 주소는 ‘https://typing.works/’ 입니다.  
>   c.	웹 사이트에 접속합니다. 브라우저는 Chrome입니다.  
>   d.	사용자가 타자 속도 측정을 완료할 때까지 implicitly_wait()을 이용해 대기해주세요.  
>   e.	Implicitly_wait() 함수가 감시해야 하는 요소는 id 'tws-result’ 입니다.  
>   f.	위 요소가 나타나면 id ‘rstDate’ 요소의 text 값을 불러와 저장해야 합니다.  
>   g.	위 요소가 나타나면 id ‘rstMaxSpd’ 요소의 text 값을 불러와 저장해야 합니다.  
>   h.	위 요소가 나타나면 id ‘rstAvgSpd’ 요소의 text 값을 불러와 저장해야 합니다.  
>   i.	위 요소가 나타나면 id ‘rstAvgAcc’ 요소의 text 값을 불러와 저장해야 합니다.  
>   j.	‘rstAvgAcc’의 값은 90 이상이어야 합니다. 90 미만일 경우, 재 시도를 할 수 있는 버튼이 표시되어야 합니다.  
>   k.	값을 저장한 후 웹 브라우저를 종료하고, rstAvgSpd, rstAvgAcc 값을 볼 수 있는 GUI 창이 표시되어야 합니다.  
>   4.	Python의 sqlite3 라이브러리를 이용할 것.  
>   a.	데이터베이스에는 사용자의 학년, 반, 번호, 이름, rstDate, rstMaxSpd, rstAvgSpd, rstAvgAcc 값이 저장되어야 합니다.  
>   5.	랭킹 시스템이 구현되어야 합니다.  
>   a.	데이터베이스에 저장된 rstAvgSpd를 이용해 가장 높은 rstAvgSpd 순으로 순위를 매겨주세요.  
>   b.	매겨진 랭크를 1번의 콘솔 창에 출력해주세요.  
>   c.	이제 계속해서 여러 사용자들이 도전할 수 있도록 한 사용자가 측정을 완료했다면 1번으로 돌아가 대기해야 합니다.  

결과:  
>   이 프로젝트를 구현하기 위해서는 Python에서 Selenium 및 sqlite3 라이브러리를 사용하여 웹 스크래핑 및 데이터베이스 조작을 해야 합니다. 또한 GUI를 만들기 위해 tkinter 또는 다른 GUI 라이브러리를 사용해야 합니다.  
>   
>   아래는 전반적인 구현 아이디어를 제공하는 코드입니다. 이 코드는 특정 라이브러리와 모듈이 설치되어 있어야 하며, 실제로 동작하려면 몇 가지 세부사항을 조정해야 할 수 있습니다.  
>   
>   python  
>   Copy code  
>   import sqlite3  
>   from selenium import webdriver
>   from selenium.webdriver.common.keys import Keys  
>   from selenium.webdriver.common.by import By  
>   from selenium.webdriver.support.ui import WebDriverWait  
>   from selenium.webdriver.support import expected_conditions as EC  
>   import tkinter as tk  
>   from tkinter import simpledialog  
>     
>   # SQLite3 데이터베이스 연결  
>   conn = sqlite3.connect('ranking.db')  
>   cursor = conn.cursor()
>     
>   # 테이블 생성
>   cursor.execute('''  
>       CREATE TABLE IF NOT EXISTS users (
>           id INTEGER PRIMARY KEY AUTOINCREMENT,  
>           grade INTEGER,
>           class INTEGER,  
>           number INTEGER,  
>           name TEXT,  
>           rstDate TEXT,  
>           rstMaxSpd INTEG ER,  
>           rstAvgSpd INTEGER,  
>           rstAvgAcc INTEGER  
>       )  
>   ''')  
>   conn.commit()  
>   
>   # 웹 드라이버 설정
>   driver = webdriver.Chrome()  
>   
>   def challenge_typing():  
>       # 웹사이트로 이동  
>       driver.get('https://typing.works/')  
>   
>       # 사용자 정보 입력  
>       grade = int(input("학년을 입력하세요: "))  
>       class_num = int(input("반을 입력하세요: "))  
>       number = int(input("번호를 입력하세요: "))  
>       name = input("이름을 입력하세요: ")  
>   
>       # 중복 체크  
>       cursor.execute('''  
>           SELECT id FROM users  
>           WHERE grade = ? AND class = ? AND number = ?  
>       ''', (grade, class_num, number))  
>       existing_user = cursor.fetchone()  
>       if existing_user:  
>           print("이미 도전한 사용자입니다.")  
>           return  
>   
>       # 데이터베이스에 사용자 정보 저장  
>       cursor.execute('''  
>           INSERT INTO users (grade, class, number, name)  
>           VALUES (?, ?, ?, ?)  
>       ''', (grade, class_num, number, name))  
>       conn.commit()  
>   
>       # 웹페이지에서 타자 속도 측정  
>       # ... (Selenium을 사용하여 측정 및 결과 수집)  
>   
>       # 측정 결과를 데이터베이스에 저장  
>       # ... (rstDate, rstMaxSpd, rstAvgSpd, rstAvgAcc 값을 가져와서 데이터베이스에 저장)  
>   
>       # GUI로 결과 표시  
>       show_result_gui(rstAvgSpd, rstAvgAcc)  
>   
>   def show_ranking():  
>       # 랭킹 조회  
>       cursor.execute('''  
>           SELECT name, rstAvgSpd  
>           FROM users  
>           ORDER BY rstAvgSpd DESC  
>           LIMIT 10  
>       ''')  
>       ranking = cursor.fetchall()  
>     
>       if not ranking:  
>           print("아무도 없음")  
>       else:  
>           print("랭킹:")  
>           for i, (name, avg_spd) in enumerate(ranking, 1):  
>               print(f"{i}. {name} - {avg_spd} WPM")  
>   
>   def show_result_gui(avg_spd, avg_acc):  
>       # 결과를 GUI로 표시  
>       root = tk.Tk()  
>       root.title("타자 결과")  
>   
>       label1 = tk.Label(root, text="평균 속도: " + str(avg_spd) + " WPM")  
>       label1.pack()  
>   
>       label2 = tk.Label(root, text="평균 정확도: " + str(avg_acc) + "%")  
>       label2.pack()  
>   
>       root.mainloop()  
>   
>   # 메인 콘솔 창
>   while True:  
>       print("운양고 타자왕")  
>       show_ranking()  
>   
>       choice = input("도전하려면 Y를 누르세요. (종료하려면 다른 키 입력): ")  
>       
>       if choice.lower() == 'y':  
>           challenge_typing()  
>       elif choice.lower() == 'r':  
>           show_ranking()  
>       else:  
>           break  
>   
>   # 연결 종료
>   conn.close()  
>   driver.quit()  
>   이 코드는 간단한 예시일 뿐이며, 실제로 동작하려면 여러 가지 예외 처리 및 보안 조치가 필요할 것입니다. 또한 Selenium으로 웹 스크래핑을 수행하는 부분은 웹 사이트가 변경될 경우 수정이 필요할 수 있습니다.

위 스크립트를 통해 전체적인 프로그램의 개형을 GPT가 만들어주었고, 약간의 수정을 통해 프로그램을 완성할 수 있었다.  