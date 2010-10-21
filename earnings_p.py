import sys

def calculate_interest():
    print 'how much money do you have?'
    money = float(sys.stdin.readline())
    print '%s' % money
    print 'how much interest do you get?'
    interest = float(sys.stdin.readline())
    print 'how long is the period?'
    period = int(sys.stdin.readline())
    for year in range(period + 1):
        money = money + (money * interest)
        print 'Year %s = %s' % (year, money)

#calculate_interest(100, 0.03, 15)
