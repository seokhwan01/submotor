import RPi.GPIO as GPIO  # RPi.GPIO 라이브러리를 GPIO로 사용
from time import sleep  # time 라이브러리의 sleep 함수 사용

# 서보모터 제어를 위한 설정
servoPin = 17  # 서보모터 제어 GPIO 핀 번호
SERVO_MAX_DUTY = 12  # 서보모터의 최대 위치 (180도) 주기
SERVO_MIN_DUTY = 3   # 서보모터의 최소 위치 (0도) 주기

# GPIO 핀 설정
GPIO.setmode(GPIO.BCM)  # GPIO 핀 모드를 BCM으로 설정
GPIO.setup(servoPin, GPIO.OUT)  # 서보핀을 출력으로 설정

# PWM 초기화
servo = GPIO.PWM(servoPin, 50)  # 서보핀을 50Hz PWM 모드로 설정
servo.start(0)  # PWM 시작, duty 0으로 시작 (동작하지 않음)

# 서보모터 위치 제어 함수
def setServoPos(degree):
    """
    각도를 입력받아 서보모터를 이동시키는 함수.
    :param degree: 서보모터 각도 (0~180도)
    """
    # 각도를 제한 (0~180도)
    if degree > 180:
        degree = 180
    if degree < 0:
        degree = 0

    # 각도를 Duty Cycle로 변환
    duty = SERVO_MIN_DUTY + (degree * (SERVO_MAX_DUTY - SERVO_MIN_DUTY) / 180.0)

    # Duty Cycle 값 출력 (디버깅용)
    print(f"Degree: {degree}, Duty: {duty}")

    # PWM Duty Cycle 변경
    servo.ChangeDutyCycle(duty)
    sleep(0.5)  # 서보모터가 움직일 시간을 줌

# 메인 동작
try:
    # 0도에서 90도까지 서보모터 이동
    setServoPos(0)   # 0도로 이동
    sleep(1)         # 1초 대기
    setServoPos(90)  # 90도로 이동
    sleep(1)         # 1초 대기

finally:
    # 프로그램 종료 시 PWM 및 GPIO 정리
    print("프로그램 종료")
    servo.stop()
    GPIO.cleanup()
