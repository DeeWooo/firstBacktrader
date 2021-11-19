import requests




def send_message(message):
    print(message)



# def _send_wx(message):



# 期望实现几种消息发送方式：
# 1。 邮件
# 2。 短信
# 3。 微信


if __name__ == '__main__':
    send_key = "SCT96212T55PKEt9YyCK1OYjsMPWoCehb"
    title = "测试标题"
    content = "消息内容"
    requests.get("https://sctapi.ftqq.com/{}.send?title={}&desp={}".format(send_key, title, content))