def calculate_love_score(name1,name2):
    both = name1.upper() + name2.upper()
    value1= 'TRUE'
    value2 ='LOVE'
    total = 0
    total2 = 0
    for i in range(len(value1)):
        count = 0
        for j in range(len(both)):
            if value1[i] == both[j]:
                count += 1
            else:
                count += 0
        total += count
        print(f"{value1[i]} occurs {count} times\n")
    print(f"Total = {total}\n")

    for m in range(len(value2)):
        count1 = 0
        for n in range(len(both)):
            if value2[m] == both[n]:
                count1 += 1
            else:
                count1 += 0
        print(f"{value2[m]} occurs {count1} times \n")
        total2 += count1
    print(f"Total = {total2}")
    lovescore = str(total) + str(total2)
    print(f'\n\nLove Score = {lovescore}')
calculate_love_score('Angela Yu','Jack Bauer')
    
        
            