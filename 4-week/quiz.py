money = int(input("용돈: "))
ame = int(input("아메리카노(3,000원) 몇 잔?: "))
ratte = int(input("카페라떼(5,000원) 몇 잔?: "))
chooco = int(input("아이스 초코(500원) 몇 잔?: "))

all_money=3000 * ame + 5000 * ratte + 500 * chooco

print("총 얼마?: ", all_money, "원")

def order(a, b):
    giv_money = money - all_money
    while True:
        if b < a:
            money_1000 = giv_money //1000
            giv_money %= 1000 

            money_500 = giv_money //500 
            giv_money %= 500 

            money_100 = giv_money //100
            giv_money %= 100 

            money_50 = giv_money //50 
            giv_money %= 50

            money_10 = giv_money //10
            giv_money %= 10
            
            all_giv_money = 1000 * money_1000 + 500 * money_500 + 100 * money_100 + 50 * money_50 + 10 * money_10
            
            print("1000원: ", money_1000, "개")
            print("500원: ", money_500, "개")
            print("100원: ", money_100, "개")
            print("50원: ", money_50, "개")
            print("10원: ", money_10, "개")
            
            return all_giv_money
        
        else:
            continue;


print("거스름돈: ", order(money, all_money), "원")