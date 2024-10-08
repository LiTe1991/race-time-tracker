"""
    Const for the program
"""
LIGHT_RED = (1, 0, 0)
LIGHT_GREEN = (0, 1, 0)
LIGHT_NO = (1, 1, 1)

MOTION_SENSOR_PIN = 22
MOTION_SENSOR_QUEUE_LENGTH = 5  # Set the queue length trigger something like sensitivity, value which we can increase to change behavior

LED_STRIP_RED_PIN = 23
LED_STRIP_GREEN_PIN = 24
LED_STRIP_BLUE_PIN = 25

BUTTON_TEXT_GO = "Ready"
BUTTON_TEXT_STOP = "Stop"
LABEL_TIMER_DEFAULT = "0:00:00.000000"
LABEL_ROUND_COUNTER = "Runde: {str}/{end}"
LABEL_ROUND_TIME = "Runde {rnd}: {time}"
