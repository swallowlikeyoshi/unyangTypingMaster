import os
import sqlite3
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import tkinter as tk
import time

# SQLite3 데이터베이스 연결
conn = sqlite3.connect('ranking.db')
cursor = conn.cursor()

# 테이블 생성
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        grade INTEGER,
        class_num INTEGER,
        number INTEGER,
        name TEXT,
        rstDate TEXT,
        rstMaxSpd INTEGER,
        rstAvgSpd INTEGER,
        rstAvgAcc INTEGER
    )
''')
conn.commit()

# 웹 드라이버 설정
driver = webdriver.Chrome()

def challenge_typing():
    os.system('cls')
    # 사용자 정보 입력
    grade = int(input("학년을 입력하세요: "))
    class_num = int(input("반을 입력하세요: "))
    number = int(input("번호를 입력하세요: "))
    name = input("이름을 입력하세요: ")

    # 중복 체크
    cursor.execute('''
        SELECT id FROM users
        WHERE grade = ? AND class_num = ? AND number = ?
    ''', (grade, class_num, number))
    existing_user = cursor.fetchone()
    if existing_user:
        print("이미 도전한 사용자입니다.")
        return
    
    os.system('cls')
    print('도전 기회는 오직 1번 뿐입니다.')
    print('화면에 표시된 문장을 5번 입력하면 평균 타자 속도가 측정됩니다.')
    print('정확도 90% 미만 달성 시 실패 처리됩니다.')
    print()
    input('시작하려면 엔터: ')

    # 웹사이트로 이동
    driver.implicitly_wait(3000)
    driver.get('https://typing.works/')
    tws_result = driver.find_element(By.CLASS_NAME, "tws-result-on")

    rstDate = driver.find_element(By.ID, "rstDate").text

    rstSpd = driver.find_element(By.ID, "rstAvgSpd").text
    idx = rstSpd.index('/')
    rstMaxSpd = rstSpd[0:idx]
    rstAvgSpd = rstSpd[idx + 1:]

    rstAvgAcc = driver.find_element(By.ID, "rstAvgAcc").text

    driver.close()

    if int(rstAvgAcc) < 90:
        print(f"정확도 {rstAvgAcc}% 로, 실패입니다.")
        input("재시도하려면 엔터: ")
        return
    
    # 데이터베이스에 사용자 정보 저장
    cursor.execute('''
        INSERT INTO users (grade, class_num, number, name, rstDate, rstMaxSpd, rstAvgSpd, rstAvgAcc)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    ''', (grade, class_num, number, name, rstDate, rstMaxSpd, rstAvgSpd, rstAvgAcc))
    conn.commit()

    # GUI로 결과 표시
    show_result_gui(name, rstAvgSpd, rstAvgAcc)

def show_ranking():
    # 랭킹 조회
    cursor.execute('''
        SELECT grade, class_num, number, name, rstAvgSpd, rstAvgAcc
        FROM users
        ORDER BY rstAvgSpd DESC
        LIMIT 10
    ''')
    ranking = cursor.fetchall()

    if not ranking:
        print("아무도 없음")
    else:
        print("랭킹:")
        for i, (grade, class_num, number, name, rstAvgSpd, rstAvgAcc) in enumerate(ranking, 1):
            print(f"{i}. {grade}{str(class_num).zfill(2)}{str(number).zfill(2)} - {name} - 평균: {rstAvgSpd} WPM, 정확도: {rstAvgAcc}%")

def show_result_gui(name, rstAvgSpd, avg_acc):
    # 결과를 GUI로 표시
    root = tk.Tk()
    root.title("타자 결과")

    root.geometry("400x300")
    root.lift()
    root.attributes('-topmost', True)

    label1 = tk.Label(root, text="평균 속도: " + str(rstAvgSpd) + " WPM")

    label2 = tk.Label(root, text="평균 정확도: " + str(avg_acc) + "%")

    
    label1.place(relx=0.5, rely=0.4, anchor='center')
    label2.place(relx=0.5, rely=0.5, anchor='center')

    confirm_button = tk.Button(root, text="확인", command=root.destroy)
    confirm_button.place(relx=0.5, rely=0.8, anchor='center')

    root.mainloop()

def show_fail_gui(rstAvgAcc):
    root = tk.Tk()
    root.title("타자 결과")

    root.geometry("400x300")
    root.lift()
    root.attributes('-topmost', True)

    label1 = tk.Label(root, text="실패. 정확도: " + str(rstAvgAcc))

    label1.place(relx=0.5, rely=0.4, anchor='center')

    confirm_button = tk.Button(root, text="확인", command=root.destroy)
    confirm_button.place(relx=0.5, rely=0.8, anchor='center')

    root.mainloop()

def close():
    # 연결 종료
    print('프로그램을 종료합니다.')
    conn.close()
    driver.quit()
    exit()

# 메인 콘솔 창
while True:
    os.system('cls')
    print("----------운양고 타자왕----------")
    show_ranking()

    choice = input("도전하려면 Y를 누르세요: ")
    
    if choice.lower() == 'y':
        challenge_typing()
    elif choice.lower() == 'rrrrrr':
        show_ranking()
    elif choice.lower() == 'qqqqqq':
        close()
    else:
        continue