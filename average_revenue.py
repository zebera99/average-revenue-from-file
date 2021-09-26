with open ('data/chicken.txt', 'r') as f:

    total_days = 0
    total_revenue = 0


    for list in f:
        data = list.strip().split(': ')
        revenue = int((data[1]))

        total_revenue += revenue
        total_days += 1

    print(total_revenue / total_days)
