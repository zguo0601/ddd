import random
import time

class SF():
    def regiun(self):
        '''生成身份证前六位'''
        #列表里面的都是一些地区的前六位号码
        first_list = ['362402','362421','362422','362423','362424','362425','362426','362427','362428','362429','362430','362432','110100','110101','110102','110103','110104','110105','110106','110107','110108','110109','110111']
        first = random.choice(first_list)
        return first

    def year(self):
        '''生成年份'''
        now = time.strftime('%Y')
        #1948为第一代身份证执行年份,now-18直接过滤掉小于18岁出生的年份
        second = random.randint(1948,int(now)-18)
        age = int(now) - second
        return second


    def month(self):
        '''生成月份'''
        three = random.randint(1,12)
        #月份小于10以下，前面加上0填充
        if three < 10:
            three = '0' + str(three)
            return three
        else:
            return three


    def day(self):
        '''生成日期'''
        four = random.randint(1,31)
        # 日期小于10以下，前面加上0填充
        if four < 10:
            four = '0' + str(four)
            return four
        else:
            return four


    def randoms(self):
        '''生成身份证后四位'''
        # 后面序号低于相应位数，前面加上0填充
        five = random.randint(1,9999)
        if five < 10:
            five = '000' + str(five)
            return five
        elif 10 < five < 100:
            five = '00' + str(five)
            return five
        elif 100 < five < 1000:
            five = '0' + str(five)
            return five
        else:
            return five


    def sf(self):
        first = self.regiun()
        second = self.year()
        three = self.month()
        four = self.day()
        last = self.randoms()
        IDcard = str(first)+str(second)+str(three)+str(four)+str(last)
        return IDcard

    def name(self):
        xing = '赵钱孙李周吴郑王冯陈褚卫蒋沈韩杨朱秦尤许何吕施张孔曹严华金魏陶姜'
        ming = '豫章故郡洪都新府星分翼轸地接衡庐襟三江而带五湖'
        X = random.choice(xing)
        M = "".join(random.choice(ming) for i in range(2))
        return M


if __name__ == '__main__':
    a = SF()
    a.sf()