
while True:
    price=int(input("물건 값: "))
    get_money=int(input("받은 돈: "))
    give_money=get_money-price

    print("물건 값:", price, "원")
    print("받은 돈:", get_money, "원")
    print("거스름돈:", give_money, "원")

    if price<get_money:
        money_1000=give_money //1000
        give_money%=1000 
        
        money_500=give_money //500 
        give_money%=500 

        money_100=give_money //100
        give_money%=100 

        money_50=give_money //50 
        give_money%=50

        money_10=give_money //10
        give_money%=10
        break;

    else:
        continue;

print("1000원: ", money_1000, "개")
print("500원: ", money_500, "개")
print("100원: ", money_100, "개")
print("50원: ", money_50, "개")
print("10원: ", money_10, "개")
