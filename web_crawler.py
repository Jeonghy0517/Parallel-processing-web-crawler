#병렬처리 웹 크롤러 만들기
##진행 순서##
#1. 로깅(logging) 설정
#2. 시스템 정보 확인
#3. 웹 크롤러 만들기
#4. 병렬처리 세팅
#5. 실행 스케줄러 설정
#6. 매개변수를 입력 받는 시스켐 명령어 실행

#1. 로깅(logging) 설정
import logging

#로거 생성
logger = logging.getLogger()
#로그의 출력 기준 설정
logger.setLevel(logging.INFO)
#log 형식 지정
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
#log 출력
stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)
logger.addHandler(stream_handler)
#log 파일 생성
file_handler = logging.FileHandler('output.log')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

#2. 시스템 정보 확인
import platform, psutil
import os

def printSystemInfor():
    logger.info(f'''
        OS                   :\t {platform.system()}
        OS Version           :\t {platform.version()}
        OS                   :\t {platform.system()}
        OS Version           :\t {platform.version()}
        Process information  :\t {platform.processor()}
        Process Architecture :\t {platform.machine()}
        CPU Cores            :\t {os.cpu_count()}   
        RAM Size             :\t {str(round(psutil.virtual_memory().total / (1024.0 **3)))+"(GB)"} 
''')

printSystemInfor()

#3. 웹 크롤러 만들기
from bs4 import BeautifulSoup
import requests

#네이버 연합뉴스 URL
url1 = 'https://news.naver.com/main/list.naver?mode=LSD&mid=sec&sid1=100'
url2 = 'https://news.naver.com/main/list.naver?mode=LSD&mid=sec&sid1=101'
url3 = 'https://news.naver.com/main/list.naver?mode=LSD&mid=sec&sid1=102'
url4 = 'https://news.naver.com/main/list.naver?mode=LSD&mid=sec&sid1=103'
url5 = 'https://news.naver.com/main/list.naver?mode=LSD&mid=sec&sid1=104'
url6 = 'https://news.naver.com/main/list.naver?mode=LSD&mid=sec&sid1=105'

#헤더 정보 일람 사이트 : https://www.useragentstring.com/pages/useragentstring.php

def web_crawler(url):
    #헤더 설정
    headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36"}
    #서버 응답 확인
    response = requests.get(url, headers=headers)
    #BeautifulSoup 객체 생성
    beautifulSoup = BeautifulSoup(response.content, "html.parser")
    #페이지 제목 크롤링
    print(beautifulSoup.title.string)
    #기사 제목 크롤링
    print(beautifulSoup.find("ul", attrs={"class":"type06_headline"}).get_text())

#크롤러 실행 테스트
web_crawler(url1)


#4. 병렬처리 세팅
# import logging
#
# if __name__ == '__main__':
#     from multiprocessing import Pool
#     import time
#
#     url_list = [url1, url2, url3, url4, url5, url6]
#
#     logging.info(f''' 멀티 프로세스가 시작됩니다. ''')
#     start_time = time.time()
#
#     pool = Pool(processes=3)
#     result = pool.map(web_crawler, url_list)
#
#     pool.close()
#     pool.join()
#
#     logger.info(f''' 멀티 프로세스가 종료되었습니다. ''')
#     logger.info("--- %s seconds ---" % (time.time() - start_time))

#5. 실행 스케줄러 설정
# if __name__ =='__main__':
#     import schedule
#
#     #3초에 한번씩 메인 함수 실행
#     schedule.every(3).seconds.do(main) #이벤트 등록
#     #스케줄러 실행
#     while True:
#         schedule.run_pending()

#6. 매개변수를 입력받는 시스템 명령어 실행
import logging


def main(cpu=3):
    from multiprocessing import Pool
    import time

    url_list = [url1, url2, url3, url4, url5, url6]

    logging.info(f''' 멀티 프로세스가 시작됩니다. ''')
    start_time = time.time()

    pool = Pool(processes=3)
    result = pool.map(web_crawler, url_list)

    pool.close()
    pool.join()

    logger.info(f''' 멀티 프로세스가 종료되었습니다. ''')
    logger.info("--- %s seconds ---" % (time.time() - start_time))


if __name__ == '__main__':
    import argparse
    import schedule

    # 입력 매개변수 설정
    parser = argparse.ArgumentParser()
    parser.add_argument('--cpu', type=int, default=3, help="멀티프로세스 CPU 수")
    parser.add_argument('--run_interval', type=int, default=5, help="웹 크롤러 실행 주기(초)")
    args = parser.parse_args()  # 매개변수 파싱
    cpu = args.cpu
    interval = args.run_interval

    logger.info(f''' 
        CPU 사용                :\t {cpu} 코어
        프로그램 실행주기        :\t {interval} 초
    ''')
    parser = argparse.ArgumentParser()

    # n초에 한번씩 메인 함수 실행
    schedule.every(interval).seconds.do(main, cpu)
    while True:
        schedule.run_pending()
