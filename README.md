# 通过Lego Mindstorms , python3, ev3dev, pycharm 来创建PID控制器来完成机器人巡线任务

1. 搭建机器人
机器人必须要有两个履带并且每个都连接到了一个大型电机,
以及一个离地面10mm的颜色传感器
例如: robot.jpg

2. 在SD卡里面下载并编译ev3dev
参考https://github.com/rhempel/ev3dev-lang-python 里面的内容

3. 找出最暗以及最亮位置的光感值
运行max_find_finder.py 或者手动查看

4. 运行巡线程序
需要有 ev3dev库
kp、ki、kd 参数 需要手动不断调整以适应环境及机器

## 这个程序参考自http://bbs.cmnxt.com/thread-5688-1-1.html