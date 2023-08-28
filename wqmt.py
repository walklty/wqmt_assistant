from utils import *
import random

def topquit():
    for i in range(6):
        adb_click_percent(0.429, 0.031, ran=1)
        time.sleep(0.5)
def homequit():
    adb_click_percent(0.133, 0.06)
    time.sleep(2)

def starttohome():# 启动到home
    adb_connect() # 连接MUMU模拟器
    [adb_click_percent(0.497656, 0.9, ran=1, sleepn=1) for i in range(3)]
    put_text("等待15秒->游戏完全进入主页面")
    time.sleep(15) 
    # 进入主界面
    for i in range(5):
        topquit()
        time.sleep(1)
    center = comparebackxy('./Target/wqmt/cancell.png') # 检查月卡提示
    if center:
        put_text("@@@@@@@已经取消月卡购买界面，请之后注意补充@@@@")
        x,y = center
        adb_click(x, y, sleepn=2)
        [topquit() for i in range(5)]
    center = comparebackxy('./Target/wqmt/confirm.png') # 检查公会战提示
    if center:
        put_text("@@@@@@@已经取消公会战提醒，请之后记得参加@@@@")
        x,y = center
        adb_click(x, y, sleepn=2)
        [adb_click_percent(0.274219, 0.03, ran=1) for i in range(5)]
    adb_click_percent(0.683, 0.53) # 展开面板 - 需要替换 面板展开()
    time.sleep(1)

def guild():# 公会收菜
    put_text("开始公会收菜")
    adb_click_percent(0.933, 0.365)
    time.sleep(2)
    adb_screenshot()
    ## 避免工会弹窗
    [adb_click_percent(0.513, 0.028, ran=1, sleepn=1) for i in range(3)]
    ## 开始捐赠
    adb_click_percent(0.374, 0.69, sleepn=1) 
    [adb_click_percent(0.169, 0.827, sleepn=1) for i in range(9)]
    adb_screenshot()
    homequit()
    put_text("公会收菜完毕")

def dailycheckin(): # 晨菜daily对话
    put_text("开始Check-in")
    adb_click_percent(0.825, 0.15)
    time.sleep(2)
    [adb_click_percent(0.807, 0.64, sleepn=0.8) for i in range(15)]
    for i in range(2):
        adb_click_percent(0.448, 0.752)
        adb_click_percent(0.558, 0.773)
        adb_click_percent(0.67, 0.752)
        adb_click_percent(0.792, 0.761)
        time.sleep(1)
    adb_screenshot()
    topquit()
    put_text("Check-in完成")

def getmail(): # 邮件
    put_text("开始收邮件")
    adb_click_percent(0.958, 0.146)
    time.sleep(2)
    [adb_click_percent(0.263, 0.942, sleepn=1) for i in range(9)]
    adb_screenshot()
    homequit()
    put_text("收完邮件")

def Bureau(): # 管理局领体力，派遣
    put_text("管理局领体力，派遣")
    center = comparebackxy('./Target/wqmt/glj1.png',0.95)
    if center:
        x,y = center
        adb_click(x, y, sleepn=2)
    ## 收体力
    adb_click_percent(0.143, 0.456,sleepn=2)
    for i in range(2):
        center = comparebackxy('./Target/wqmt/lingqu.png',0.95)
        if center:
            x,y = center
            [adb_click(x, y, sleepn=2) for i in range(2)]
    ### 退到管理局
    topquit()
    ## 派遣
    adb_click_percent(0.44, 0.742,sleepn=2)
    [adb_click_percent(0.105, 0.707, ran=1, sleepn=3) for i in range(3)]
    ## 退出
    adb_screenshot()
    homequit()
    put_text("完成管理局领体力，派遣")

def friends(): # 朋友
    center = comparebackxy('./Target/wqmt/friend1.png',0.95)
    if center is not None:
        x,y = center
        adb_click(x, y, sleepn=2)
    for i in range(3):
        ran = random.uniform(0.001, 0.005)
        adb_click_percent(0.869+ran, 0.855-ran)
        time.sleep(2)
    ## 退出
    homequit()

def construction(): # 基建
    adb_click_percent(0.844, 0.629, sleepn=3)
    [adb_click_percent(0.096, 0.373,sleepn=1) for i in range(3)]
    ## 退出
    homequit()
    adb_click_percent(0.074, 0.249, sleepn=2) # 开始聊天
    adb_click_percent(0.908, 0.612)
    [adb_click_percent(0.908, 0.889, ran=1) for i in range(50)]
    ## 退出
    homequit()

def purchase(): # 采购办领免费体力
    center = comparebackxy('./Target/wqmt/caigouban1.png',0.95)
    if center is not None:
        x,y = center
        adb_click(x, y, sleepn=2)
    adb_click_percent(0.091, 0.407, sleepn=2)
    for i in range(4):
        adb_swap_percent(0.965, 0.578, 0.27, 0.611, sleepn=1)
    adb_click_percent(0.587, 0.88, sleepn=2) # 收每日体力
    adb_click_percent(0.766, 0.733, sleepn=2) # 确认
    ## 退出
    homequit()
    homequit()

def raidriver(): # 秀河
    center = comparebackxy('./Target/wqmt/fuben1.png',0.95)
    if center is not None:
        x,y = center
        adb_click(x, y, sleepn=2)
    ## 秀河
    adb_click_percent(0.172, 0.926, sleepn=2)
    center = comparebackxy('./Target/wqmt/fuben2.png',0.95) # 记忆风暴
    if center is not None:
        x,y = center
        adb_click(x, y, sleepn=2)
    adb_click_percent(0.835, 0.682, sleepn=2)
    center = comparebackxy('./Target/wqmt/fubensaodang.png',0.95) # 开始扫荡
    if center is not None:
        x,y = center
        adb_click(x, y, sleepn=2)
        center = comparebackxy('./Target/wqmt/fubensaodangkaishi.png',0.95)
        if center is not None:
            x,y = center
            adb_click(x, y, sleepn=10)
            homequit()
            homequit()
    homequit()
    homequit()

def raid11(): # 刷11章
    center = comparebackxy('./Target/wqmt/fuben1.png',0.95) ## 回到副本界面
    if center is not None:
        x,y = center
        adb_click(x, y, sleepn=2)
    center = comparebackxy('./Target/wqmt/fuben3-11.png',0.95) ## 打开11章
    if center is not None:
        x,y = center
        adb_click(x, y, sleepn=2)
    for i in range(2):
        adb_swap_percent(0.965, 0.578, 0.27, 0.611, sleepn=1)
    adb_click_percent(0.078, 0.541, sleepn=2) # 打开11-6
    center = comparebackxy('./Target/wqmt/fubensaodang.png',0.95)
    if center is not None:
        x,y = center
        adb_click(x, y, sleepn=2)
        center = comparebackxy('./Target/wqmt/fubensaodangkaishi.png',0.95)
        if center is not None:
            x,y = center
            adb_click(x, y, sleepn=10)
            homequit()
            homequit()

def raiddark():## 深井
    center = comparebackxy('./Target/wqmt/fuben1.png',0.95) ## 回到副本界面
    if center is not None:
        x,y = center
        adb_click(x, y, sleepn=2)
    adb_click_percent(0.837, 0.891, 1) # 内海
    adb_click_percent(0.193, 0.523, 2) # 浊暗之井
    while True:
        center = comparebackxy('./Target/wqmt/fuben4.png', 0.95) ## 找乐园
        if center is not None:
            x, y = center
            adb_click(x, y, sleepn=2)
            adb_click_percent(0.587, 0.86) # 点击扫荡
            homequit()
            homequit()
            break
            center = comparebackxy('./Target/wqmt/fuben4-1.png', 0.85) ## 尝试切换
            if center is not None:
                x, y = center
                adb_click(x, y, sleepn=2)

def morning():
    starttohome()
    dailycheckin()
    guild()
    getmail()
    purchase()
    construction()
    raidriver()
    raid11()
    raiddark()

def night():
    starttohome()
    Bureau()
    friends()
    construction()
    raid11()