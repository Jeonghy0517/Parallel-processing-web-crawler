#1. 병렬처리 세팅
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

#2. 실행 스케줄러 설정
# if __name__ =='__main__':
#     import schedule
#
#     #3초에 한번씩 메인 함수 실행
#     schedule.every(3).seconds.do(main) #이벤트 등록
#     #스케줄러 실행
#     while True:
#         schedule.run_pending()

#3. 매개변수를 입력받는 시스템 명령어 실행
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

    #입력 매개변수 설정
    parser = argparse.ArgumentParser()
    parser.add_argument('--cpu', type=int, default=3, help="멀티프로세스 CPU 수")
    parser.add_argument('--run_interval', type=int, default=5, help="웹 크롤러 실행 주기(초)")
    args = parser.parse_args()  # 매개변수 파싱
    cpu = args.cpu
    interval = args.run_interval

    logger.info(f''' 
        CPU 사용                :\t {cpu} 코어
        프로그램 실행주기        :\t {interval} 초
    ''')    parser = argparse.ArgumentParser()

    #n초에 한번씩 메인 함수 실행
    schedule.every(interval).seconds.do(main.cpu)
    while True:
        schedule.run_pending()
