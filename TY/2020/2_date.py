# 윤년인지 확인
def isLeapYear(year):
    if year%400==0: 
        return True
    if year%100==0:
        return False
    if year%4==0:
        return True
    return False

def today(date):
    result=0
    day=date%100
    month=((date/100)%100)
    year=(date/10000)
    
    #월별로 날짜 갯수
    result+=(year-1)*365
    result+= #올해 지난 달의 날짜 갯수 (윤년, 2월, 30일인 달 31일인 달 고려) 


def subDate(date1,date2):
    if date1==date2:
        return 0

    if date1>date2:
        date1,date2 = date2,date1

    if date1//100 == date2//100:
        return date2%100 - date1%100
    
    else:
        return today(date2)-today(date1)


date1,date2=list(map(int,input().strip().split(' ')))
