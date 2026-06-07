import re
from tqdm import tqdm
import time, random
import os as sysOS
p_echo = re.compile(r"echo\s(.*)", re.DOTALL)
p_cls = re.compile("cls")
# TODO: 파일 시스템 기능 제작
class OS:
  @staticmethod
  def boot():
    steps = {
      "커널 로딩": {"count": 15, "speed": (0.03, 0.06)},
      "드라이버 초기화": {"count": 20, "speed": (0.02, 0.05)},
      "메모리 체크": {"count": 25, "speed": (0.01, 0.04)},
      "네트워크 연결": {"count": 18, "speed": (0.03, 0.07)},
      "UI 시작": {"count": 12, "speed": (0.02, 0.05)}
    }

    for step, config in steps.items():
      for i in tqdm(range(config["count"]), desc=step, leave=False): # 오류는 있는데 실제 실행 시에는 오류가 안 나니 괜찮음
        time.sleep(random.uniform(*config["speed"])) # 여기도 괜찮음

    print("부팅 완료!")
  @staticmethod
  def echo(text):
    print(text)
  @staticmethod
  def cls():
    sysOS.system("cls")
  @staticmethod
  def off():
    quit()
  #DONE: cal 메소드: 계산
  @staticmethod
  def cal(s):
    print(eval(s))
  #NOTE-P4: 참고, exec은 안전상 안 만들기로 함