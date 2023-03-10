#시스템 정보 확인
#platform : 실행하고자하는 프로그램이 시스템 요구사항을 만족하는지 사양 정보를 확인할 때 사용하는 모듈
import platform

#1. 운영 체제 확인
def printOsInfo():
    print('OS                   :\t', platform.system())
    print('OS Version           :\t', platform.version())

printOsInfo()

#튜플 객체형으로 확인
info = platform.uname()
info

#2. CPU/메모리(RAM) 확인
print(info.processor) #CPU

import os
os.cpu_count() #CPU 코어 개수 확인

import platform, psutil

def printSystemInfor():
    print('Process information  :\t', platform.processor())
    print('Process Architecture :\t', platform.machine())
    print('CPU Cores          :\t', os.cpu_count())
    print('RAM Size             :\t', str(round(psutil.virtual_memory().total / (1024.0 ** 3))) + "(GB)")
printSystemInfor()
#----------------------------------------------------------------------------------------------------------------------
#매개변수 입력 받기
#매개변수 : 프로그램 명령행에서 사용자로부터 입력 받는 값 (혹은 인자)
#외부에서 입력받는 값에 따라 프로그램 동작이 달라져야 할 경우 주로 사용

#sys.argv
#파이썬 스크립트로 전달한 명령행 매개변수를 처리할 대 사용하는 모듈
#list() 형식의 반환값을 사용하기 때문에 여러개의 인자를 다룰때 편함

#sys.py 파일로 실습 진행
#터미널에서 >> python 'sys.py' 매개변수1, 매개변수2 << 실행

'''
import sys

if __name__ == "__main__":
    print(sys.argv)

    val1 = int(sys.argv[1])
    val2 = int(sys.argv[2])

    print(val1, ' 곱하기 ', val2, ' 은? ', (val1 * val2))
'''

#argparse
#sys.argv 모듈과 마찬가지로 명령행 매개변수를 다룰 대 사용
#sys.argv는 인자를 파싱(parsing)하는 과정이 필요하며, 이는 인자 별 예외처리가 필요함을 의미
#인자를 입력받고, 파싱하고, 예외처리, 사용법 작성까지 자동으로 수행해주는 편리한 모듈

#argparse_1.py 파일로 실습 진행
'''
import argparse

#1. 객체 생성
parser = argparse.ArgumentParser()

#2. 매개변수 추가
parser.add_argument('X', type=int, help="첫번째 숫자는 ?")
parser.add_argument('Y', type=int, help="첫번째 숫자는 ?")

#3. 매개변수 파싱
args = parser.parse_args()
X = args.X
Y = args.Y

#4. 사용법 확인
argparse_1.py --help
'''

#argparse_2.py 파일로 실습 진행
'''
from __future__ import print_function
import argparse

def main():
    parser = argparse.ArgumentParser(description='This Code is Written for Practice about argparse')
    parser.add_argument('X', type=float,
                        metavar='First_number',
                        help='첫번째 숫자는?')
    parser.add_argument('Y', type=float,
                        metavar='Second_number',
                        help='두번째 숫자는?')
    parser.add_argument('--op', type=str, default=덧셈,
                        choices=['덧셈','뺄셈','곱하기','나누기'],
                        help='연산 방법을 선택해 주세요')
    args = parser.parse_args()

    X = args.X
    Y = args.Y
    op = args.op
    print(calc(X, Y, op))

def calc(x, y, op):
    if op == '덧셈':
        return x+y
    elif op == '뺄셈':
        return x-y
    elif op == '곱셈':
        return x*y
    elif op == '나누기':
        return x/y

if __name__ = "__main__" :
    main()
'''
#----------------------------------------------------------------------------------------------------------------------
#프로그램 실행 로그 남기기
#logging : 프로그램이 실행되는 동안 일어나는 정보를 기록하고 관리하는 로깅 모듈
#로그는 파일뿐만 아니라 소켓, 이메일, 콘솔 등 다양한 방법으로 출력이 가능

#print 문 사용
#프린트문은 실행 기록을 관리하거나 분석시에는 활용이 어려움
def myfunc():
    print("함수가 시작되었습니다.")

#logging 사용
#로깅은 프로그램 진행 상황에 따라 로그를 레벨 별로 관리하거나 모듈 별 별도의 기록을 남기는 등의 작업이 가능
import logging

#1. 로그생성
logger = logging.getLogger()
#2. 로그의 출력 기준 설정
logger.setLevel(logging.INFO)
#3. 로그 형식 지정
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
#4. 로그 출력
stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)
logger.addHandler(stream_handler)
#5. 로그 파일 생성
file_handler = logging.FileHandler('sample1.log')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

def myfunc():
    logger.info("함수가 시작되었습니다.")

myfunc()

#로그 레벨 5단계
#로그는 설정한 레벨 이상만 출력됨
#예를 들어 핸들러나 로거의 로그 레벨을 'INFO'로 설정하면 DEBUG 로그는 출력되지 않고 INFO 이상의 로그만 출력

#DEBUG < INFO < WARNING < ERROR < CRITICAL

#1단계 DEBUG : 디버깅 목적으로 사용
#2단계 INFO : 일반 정보를 출력할 목적으로 사용
#3단계 WARNING : 경고 정보를 출력할 목적으로(작은 문제) 사용
#4단계 ERROR : 오류 정보를 출력할 목적으로(큰 문제) 사용
#5단계 CRITICAL : 아주 심각한 문제를 출력할 목적으로 사용

import logging

#1. 로그 생성
logger = logging.getLogger()
#2. 로그의 출력 기준 설정
logger.setLevel(logging.WARNING)
#3. log 형식 지정
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
#4. log 출력
stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)
logger.addHandler(stream_handler)
#5. log 파일 생성
file_handler = logging.FileHandler('sample2.log')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

def myfunc():
    logger.debug("DEBUG 로그입니다.")
    logger.info("INFO 로그입니다.")
    logger.warning("WARNING 로그입니다.")
    logger.error("ERROR 로그입니다.")
    logger.critical("CRITICAL 로그입니다.")

myfunc()
#----------------------------------------------------------------------------------------------------------------------
#원하는 시간에 작업 실행
#sched : 지정된 시간 간격으로 원하는 이벤트를 실행하게 하는 이벤트 스케줄러 표준 라이브러리
#사용 순서
'''
1. 스케줄러 객체 생성
2. enter(실행 간격(초), 우선 순위, 실행 할 함수, 함수에 전달할 인자)를 사용해 실행 할 이벤트 등록
3. run() 스케줄러 실행
'''

#sched 예제
#1. 프로그램 실행 후 5초 후에 print_a() 호출
#1. 프로그램 실행 후 3초 후에 print_a() 호출
#1. 프로그램 실행 후 7초 후에 print_a() 호출
import sched
import time

start = time.time()

def print_a(a):
    print(round(time.time() - start, 2), ' 초 경과')
    print(a)
def print_b(b):
    print(round(time.time() - start, 2), ' 초 경과')
    print(b)
def print_c(c):
    print(round(time.time() - start, 2), ' 초 경과')
    print(c)

s = sched.scheduler()
s.enter(5, 1, print_a, ('print_a 함수 실행됨',)) #5초 후에 실행
s.enter(3, 1, print_b, ('print_b 함수 실행됨',)) #3초 후에 실행
s.enter(7, 1, print_c, ('print_c 함수 실행됨',)) #7초 후에 실행
s.run()

#schedule : sched와 마찬가지로 일정한 시간 간격으로 프로그램을 실행시켜주는 외장 라이브러리
#파이썬의 함수들의 원하는 실행 주기를 (초, 분, 시간, 요일, 특정 시각) 손쉽게 설정이 가능
#시간 관련 내장 라이브러리인 time과 주로 함꼐 사용됨
import schedule
import time

def message(interval):
    print(f"{interval}간격 스케줄 실행중...")
#
# schedule.every(5).seconds.do(message, '5초') #이벤트 등록
#
# while True:
#     schedule.run_pending() #스케줄러 실행
#
# #1. 1분에 한번씩 함수 실행
# schedule.clear() #스케줄러 초기화
#
# schedule.every(1).minutes.do(message, '1분') #이벤트 등록
#
# while True:
#     schedule.run_pending() #스케줄러 실행
#
# #2. 1시간에 한번씩 함수 실행
# schedule.clear() #스케줄러 초기화
#
# schedule.every(1).hour.do(message, '1시간')
#
# while True:
#     schedule.run_pending()
#
# #3. 일, 주 단위 실행
# schedule.clear() #스케줄러 초기화
#
# #1일에 한번씩 함수 실행
# schedule.every(1).days.do(message, '1일')
# #1주에 한번씩 함수 실행
# schedule.every(1).weeks.do(message, '1주')
#
# while True:
#     schedule.run_pending() #스케줄러 실행
#
# #4. 매일 정해진 시각에 실행
# schedule.clear() #스케줄러 초기화
#
# #매일 13시 30분에 함수 실행
# schedule.every().day.at("13:30").do(message, '1일')
# #매일 "11:11:11"에 함수 실행
# schedule.every().day.at("11:11:11").do(message, '1일')
#
# while True:
#     schedule.run_pending() #스케줄러 실행
#
# #5. 매주 정해진 시각에 실행
# schedule.clear() #스케줄러 초기화
#
# #매주 월요일 13시 30분에 함수 실행
# schedule.every().monday.at("13:30").do(message, '1주')
#
# while True:
#     schedule.run_pending() #스케줄러 실행

#6. 스케줄러 중지
schedule.clear() #스케줄러 초기화

#job 설정
job = schedule.every(1).seconds.do(message, '1초') #이벤트 등록

#스케줄러 실행
count = 0

while True:
    schedule.run_pending()
    time.sleep(1)

    count = count + 1

    if count > 5: #5회 실행 후 스케줄러 중지
        schedule.cancel_job(job)
        print('스케줄러가 종료되었습니다 !')
        break

#----------------------------------------------------------------------------------------------------------------------
#병렬처리 1
#스레드(thread) : 프로세스 내부에 있는 CPU 수행 단위를 말함
#프로세스 : 운영체제로부터 자원을 할당받아 실행되는 작업(어플리케이션)의 단위

#스레드는 사전적 의미로 한 가닥의 실이란 의미
#한 프로세스 내에 스레드가 두개라면 코드가 실행되는 흐름이 두 개 생긴다는 의미

#threading : 스레드를 이용하여 한 프로세스에서 2가지 이상의 일을 동시에 실행할 수 있게 하는 표준 모듈
#병렬 처리를 위해서는 별도 작업이 필요함 (파이썬은 기본적으로 싱글 스레드에서 순차적으로 동작)
#활용 분야
'''
1. 대용량 데이터의 처리시간을 줄이기 위해 데이터를 분할하여 병렬로 처리
2. 애플리케이션에서 다중 네트워크 통신을 할 때
3. 여러 클라이언트의 요청을 동시에 처리하는 서버를 개발할 때
'''
from threading import Thread
import time

#0부터 10,000,000 까지의 합을 구하는 프로그램
#1. threading을 사용하지 않을 경우
def work(id, start, end, result):
    total = 0
    for i in range(start, end):
        total += i
    result.append(total)
    return

if __name__ == "__main__":
    start = time.time()

    START, END = 0, 10000000
    result = list()
    th1 = Thread(target=work, args=(1, START, END, result))

    th1.start()
    th1.join()

    th1_elapsed = round(time.time() - start, 2)
    print(th1_elapsed, ' 초 경과')
    print(f"합계 결과: {sum(result)}")

#2. threading을 사용할 경우
if __name__ == "__main__":
    start = time.time()

    START, END = 0, 10000000
    result = list()
    th2 = Thread(target=work, args=(2, START, END, result)) #멀티스레드

    th2.start()
    th2.join()

    th2_elapsed = round(time.time() - start, 2)
    speed_up = round(th1_elapsed/th2_elapsed, 1)
    print(th2_elapsed, ' 초 경과')
    print(speed_up, ' 배 속도 향상')
    print(f"합계 결과: {sum(result)}")

#----------------------------------------------------------------------------------------------------------------------
#병렬처리 2
#파이썬에서 병렬처리를 구현하는 방식은 멀티 쓰레드를 사용하거나 멀티 프로세스를 사용하는 두가지 방법이 있음

#스레드 특징
#1. 스레드는 가볍지만 cpu 계산 처리를 하는 작업에는 한번에 하나의 쓰레드에서만 작동함
#2. cpu 작업이 적고 네트워크 통신 또는 파일 읽고 쓰기와 같은 작업 (I/O)이 많은 병렬 처리 프로그램에서 효과적

#멀티프로세싱 특징
#1. 멀티 프로세서와 별개의 메모리를 사용하여 완전히 독립하여 병렬 프로그래밍이 가능
#2. 여러 개의 CPU가 있는 멀티코어 환경에서 CPU 수 만큼 작업을 나누어 실행 가능
#3. 프로세스는 각자가 고유한 메모리 영역을 가지기 때문에 더 많은 메모리를 필요로 하지만,
#각각 프로세스에서 병렬로 CPU 작업을 할 수 있고 이를 이용해 여러 장비에서 동작하는 분산 처리 프로그래밍도 구현이 가능

#multiprocessing : 멀티 프로세스를 활용하여 2가지 또는 그 이상의 일을 동시에 실행할 수 있게 하는 표준 모듈
#쓰레드 대신 다중 프로세스를 만들어 병렬로 동작
import multiprocessing
import time

#0부터 50,000,000 까지의 합을 구하는 프로그램
#1. multiprocessiong을 사용하지 않을 경우
def work(id, start, end, result):
    total = 0
    for i in range(start, end):
        total += i
    result.append(total)
    return

if __name__ == "__main__":
    start = time.time()

    START, END = 0, 50000000
    result = list()

    #싱글 프로세스 2번 실행
    for i in range(2):
        work(1, START, END, result)
        print(f'{i+1} 번째 실행')

    time_elapsed1 = round(time.time() - start, 2)
    print(time_elapsed1, ' 초 경과')
    print(f"합계 결과: {sum(result)}")

#2. multiprocessiong을 사용 할 경우
if __name__ == "__main__":
    start = time.time()

    START, END = 0, 50000000
    result = list()

    procs = []
    for i in range(2):
        #프로세스 수만큼 코어 할당
        p = multiprocessing.Process(target=work, args=(i, START, END, result))
        p.start()
        procs.append(p)
        print(f'{i+1} 번째 실행')

    for p in procs:
        p.join() #프로세스가 모두 종료될 때까지 대기

    time_elapsed2 = round(time.time() - start, 2)
    speed_up = round(time_elapsed1/time_elapsed2, 1)
    print(time_elapsed2, ' 초 경과')
    print(speed_up, '배 속도 향상')
    print(f"합계 결과: {sum(result)}")
#----------------------------------------------------------------------------------------------------------------------
#시스템 명령어 실행
#subprocess : 파이썬 스크립트 상에서 외부 프로세스 시스템 명령어를 실행할 때 사용하는 표준 모듈
#새로운 프로세스를 실행하도록 도와주며, 프로세서의 입/출력 및 에러 결과겡 대한 리턴 값을 사용자가 직접 제어할 수 있게 도와줄 수 있음

#파이썬 코드를 subprocess로 실행하기
import subprocess
subprocess.run(['python', 'test.py'])

#출력된 결과를 txt파일로 저장하기
f = open('output.txt', 'w')
out = subprocess.check_output(['python', 'test.py'], encoding='utf-8')
f.write(out)
f.close()

