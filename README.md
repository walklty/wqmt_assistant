# wqmt_assistant

本项目由ChatGPT 3.5编写，Codeium复审代码，用于无期迷途每日收菜

程序完全自用，只在MUMU12上使用，只在720P下开发，本人啥也不懂，有问题问AI。

为了减少报错，程序相当低效和冗余，有问题问AI。

---

程序使用Python语言，PyWebIO提供简单的选项和log查看， OpenCV识别图像。

功能包括：

- 从登录界面进入主界面，干掉活动提示、工会战提示、月卡到期提示

- 收取邮件，公会捐赠，采购部免费日礼包，戳好友

- 管理局派遣，领取中午晚上的体力

- 扫荡锈河记忆副本第一个

- 扫荡副本11-6， 扫荡深井

缺点包括：

- 我是个躺平的闲鱼，不缺材料，因此没有换副本刷不同材料的需求

- 自用方式为每天早晚点一次，因此不考虑特殊情况比如明明没有体力你却让软件去刷11-6这种

安装相关依赖

```
pip install -r requirements.txt
```

先打开无期迷途，然后如下启动程序

```
start.bat
```

Todo:

1. 面板展开检测

2. 限制log小数点 ——done

3. APP启动检测

4. 副本界面检查（切换副本第一页、第二页界面）

5. 多个副本供选择（什么时候我有刷其他本的动力了）

6. 自带ADB ——done

7. OCR识别

8. 兑换采购部商品（每月一次）