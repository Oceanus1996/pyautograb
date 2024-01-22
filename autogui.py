import random
import time
from datetime import datetime
import pyautogui
import os

#所有八个图标的固定position
POS1_X,POS1_Y=423,472
POS2_X,POS2_Y=746,474
POS3_X,POS3_Y=1057,469
POS4_X,POS4_Y=1362,474
POS5_X,POS5_Y=432,719
POS6_X,POS6_Y=747,709
POS7_X,POS7_Y=1057,715
POS8_X,POS8_Y=1359,708
button_dict=[(POS1_X,POS1_Y),(POS2_X,POS2_Y),(POS3_X,POS3_Y),(POS4_X,POS4_Y),(POS5_X,POS5_Y),(POS6_X,POS6_Y),
             (POS7_X,POS7_Y),(POS8_X,POS8_Y)]
back_x,back_y=20,88
plugin_x,plugin_y=479,146
store_x,store_y=445,118
so_x,so_y=445,194
all_x,all_y=455,357
next_x,next_y=626,893
last_x,last_y=590,889
pre_x,pre_y=306,889


ran_int = random.randint(2,12)

class search:

    def __init__(self):
         self.number = 1
         self.page = self.number // 8 + 1
         self.need_record_list=[]

    def detect_pos(self):
        time.sleep(5)
        return pyautogui.position()

    def if_turn_to_new(self):
        # 假设参考图像文件名
        time.sleep(2)
        region_to_search = (0, 300, 800, 500)
        try:
            location = pyautogui.locateOnScreen('/Users/icfem/PycharmProjects/pythonProject3/picture.png',region=region_to_search)
            if location:
                print("元素存在")
                return True
        except:
             print("元素不存在")
             return False

    def back(self):
        time.sleep(2)
        print('成功往回跳转')
        pyautogui.moveTo(back_x,back_y)
        pyautogui.click()
        time.sleep(3)

    def find_and_to_plugin(self):
        #打开store
        time.sleep(4)
        pyautogui.moveTo(plugin_x,plugin_y)
        time.sleep(2)
        pyautogui.doubleClick(plugin_x,plugin_y)
        try:
            location = pyautogui.locateOnScreen('/Users/icfem/PycharmProjects/pythonProject3/3.png')
            print("进来这里了？")
        except:
            pyautogui.click(plugin_x,plugin_y)
            print("还是这里")

        x,y=so_x,so_y
        for i in range(3):  # 尝试三次（第一行，第二行，第三行）
            print(x,y)
            pyautogui.click((x+30), y)
            try:
                location = pyautogui.locateOnScreen('/Users/icfem/PycharmProjects/pythonProject3/store.png')
                if location:
                    print("找到store图标")
                    break  # 如果找到了，就跳出循环
            except:
                print("在当前行未找到store图标")
                y += 50# 根据实际情况设置行间距#定位图标
            if i == 2:
                print("在所有行中都未找到store图标")
        pyautogui.click(all_x,all_y)


    def next_page(self):
        pyautogui.moveTo(next_x,next_y)
        time.sleep(random.randint(1,1))
        pyautogui.click()
        time.sleep(2)
        print('点击下一页')


    # def change_page(self,num:int):
    #     pyautogui.moveTo(last_x,last_y)
    #     time.sleep(1)
    #     pyautogui.click(last_x,last_y)
    #     pyautogui.doubleClick(last_x,last_y)
    #     time.sleep(1)
    #     if num==130:
    #         pass
    #     for i in range(130-num) :
    #         time.sleep(1)
    #         pyautogui.moveTo(pre_x,pre_y)
    #         pyautogui.click(pre_x,pre_y)
    #         print('切换到这一页',num)


    def change_page(self,num:int):
        if num==1:
            return
        pyautogui.moveTo(next_x,next_y)
        for i in range(num-1):
            time.sleep(random.randint(1,2))
            if i==0:
                pyautogui.click()
            else:
                pyautogui.click()
            time.sleep(1)
        print('切换到这一页',num)

    def clear(self):
        try:
            position= pyautogui.locateOnScreen('/Users/icfem/PycharmProjects/pythonProject3/installed.png',confidence=0.8)
            if position:
                print('有未uninstalled的插件')
            pyautogui.click(525,363)
            pyautogui.click(525,363)
            for i in range(8):
                pos = button_dict[i]
                pyautogui.doubleClick(pos)


            pyautogui.doubleClick(all_x,all_y)
            self.change_page(self.number//8 )
        except:
            print('没有uninstalled的插件')
            pass

    def change_default_num(self,num:int):
        self.number=num


    def timestamp(self):
        timestamp = int(time.time())

        # 将 Unix 时间戳转换为 datetime 对象
        dt_object = datetime.fromtimestamp(timestamp)

        # 格式化日期和时间
        # 例如: '2024-01-17 15:47:36'
        formatted_time = dt_object.strftime('%Y-%m-%d %H:%M:%S')
        return formatted_time

    def search(self):
        i = 1
        while i <= 8 :
            time.sleep(2)
            pos = button_dict[i-1]
            print("抓取了",i,pos,self.number)
            pyautogui.moveTo(pos)
            pyautogui.click(pos)
            pyautogui.doubleClick(pos)
            os.system('afplay /System/Library/Sounds/Glass.aiff')     
            time.sleep(random.randint(5,8))
            if self.if_turn_to_new():
                pyautogui.click(pos)
                pyautogui.doubleClick(pos)

                self.number+=1
            else:
                #获取时间戳
                timestamp = self.timestamp()
                # 创建包含时间戳的字符串
                record= (self.number,self.number//8 + 1,self.number%8,timestamp)
                self.need_record_list.append(record)
                filename='/Users/icfem/PycharmProjects/pythonProject3/recordauto'
                
                self.write_to_file(filename, str(record))

                print('在跳转前已经到这一页：',self.page)
                self.back()
                self.find_and_to_plugin()
                if i==8:
                    self.change_page(self.number//8)
                else:
                    self.change_page(self.number//8 + 1)

                self.number+=1
                os.system('afplay /System/Library/Sounds/Glass.aiff')
            i += 1
        time.sleep(6)
        #清除所有uninstall
        self.clear()

    def write_to_file(self,filename, line):
        with open(filename, 'a') as file:
            file.write(line + "\n")

    def search_pages(self,pages):
        self.find_and_to_plugin()
        self.change_page(self.number//8+1)
        for i in range(pages):
            print('开始抓取这一页',i,self.number,self.page)
            self.search()
            print(self.need_record_list)
            self.next_page()
            os.system('afplay /System/Library/Sounds/Glass.aiff')

            time.sleep(10)

if __name__=="__main__":

    a = search()

    a.change_default_num(113)
    #
    # # a.find_and_to_plugin()
    a.search_pages(55)
    #
    #



