import RPi.GPIO as GPIO
import time

# GPIO 핀 번호 설정
SERVO_PIN = 17  # 서보모터 핀 번호

# GPIO 모드 설정
GPIO.setmode(GPIO.BCM)
GPIO.setup(SERVO_PIN, GPIO.OUT)

# PWM 초기화
pwm = GPIO.PWM(SERVO_PIN, 50)  # 50Hz 주파수
pwm.start(0)

def set_angle(pwm, angle):
    """
    서보모터를 특정 각도로 회전시키는 함수.
    :param pwm: PWM 객체
    :param angle: 목표 각도 (0~180)
    """
    duty = 2.5 + (angle / 18)  # 각도를 Duty Cycle로 변환
    pwm.ChangeDutyCycle(duty)
    time.sleep(0.5)  # 서보모터가 움직일 시간을 줌
    pwm.ChangeDutyCycle(0)  # 신호 제거 (서보모터가 떨리지 않도록)

try:
    # 0도에서 90도까지 움직임
    for angle in range(0, 91, 10):  # 10도 간격으로 움직임
        set_angle(pwm, angle)

    # 서보모터 초기 위치로 복귀 (옵션)
    set_angle(pwm, 0)

finally:
    print("종료합니다.")
    pwm.stop()
    GPIO.cleanup()
