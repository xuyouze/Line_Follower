#!/usr/bin/python3
# coding: utf-8


from ev3dev.auto import *

# ------Input--------
tp = 50  # 电机正常码率

kp = float(16.6)  # 比例常量, Start value 10
ki = 0.01  # 积分常量, Start value 0
kd = 5.5  # 导数常量 , Start value 0

minRef = 2  # 最小光感值,当颜色传感器位于最暗位置的数值
maxRef = 18  # 最大光感值,当颜色传感器位于最亮位置的数值
dT = 0.003  # 运行一次循环的时间
pc = 1  # 振荡周期时间
kc = 30  # 临界值


# -------------------
def judge(args):
    temp = []
    for x in args:
        if x > 100:
            x = 100
        elif x < -100:
            x = -100
        temp.append(x)
    return temp


target = offset = (minRef + maxRef) / 2  # 线上的光感值
integral = 0
last_error = 0  # 用于存储最后一个误差值的变量
derivative = 0  # 用于存储导数的变量

# Connect two large motors on output ports D and A and check that
left_motor = LargeMotor(OUTPUT_D)
assert left_motor.connected
right_motor = LargeMotor(OUTPUT_A)
assert right_motor.connected
# Connect TouchSensor and ColorSensor and check that

ts = TouchSensor()

assert ts.connected
cs = ColorSensor()
assert cs.connected

# set color sensor mode
cs.mode = 'COL-REFLECT'

# Adding button so it would be possible to break the loop using
# one of the buttons on the brick
left_motor.run_direct()
right_motor.run_direct()

# when the touchSensor is pressed ,the loop will end

while not ts.value():

    refRead = cs.value()
    print("read:", refRead)

    error = refRead - offset
    integral = (2 / 3) * integral + error
    derivative = error - last_error
    last_error = error
    turn = kp * error + ki * integral + kd * derivative

    left_power = tp + turn
    right_power = tp - turn

    try:
        left_power, right_power = judge([left_power, right_power])
        left_motor.duty_cycle_sp = left_power
        right_motor.duty_cycle_sp = right_power
    except Exception as e:
        print(e)
        break
left_motor.stop()
right_motor.stop()
