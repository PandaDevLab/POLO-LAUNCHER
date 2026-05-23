import time
import os
from pathlib import Path

LOG_DIR = "logs"

# 3분보다 오래된 로그 파일 삭제
def delete_old_logs():
    log_dir = Path(LOG_DIR)

    # logs 디렉토리가 없으면 생성
    log_dir.mkdir(exist_ok=True)

    current_time = time.time()

    for log_file in log_dir.iterdir():
        # 파일만 처리
        if log_file.is_file():
            # 파일 수정 시간 기준
            file_age = current_time - log_file.stat().st_mtime

            # 3분(180초) 초과 시 삭제
            if file_age > 180:
                os.remove(log_file)
                print(f"Deleted old log file: {log_file.name}")

# 주기적으로 로그 파일 정리
while True:
    delete_old_logs()
    time.sleep(60)  # 1분마다 확인