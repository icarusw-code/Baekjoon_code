t = int(input())

for i in range(t):
    n = int(input())
    stocks = list(map(int, input().split()))
    
    stocks.reverse()
    max_stock = stocks[0]
    profit = 0

    for j in range(len(stocks)):
        if max_stock >= stocks[j]:
            profit += max_stock - stocks[j]
        
        else: 
            max_stock = stocks[j]
    
    print(profit)
    