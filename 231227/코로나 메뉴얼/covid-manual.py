cold, tem = input().split()
cold2, tem2 = input().split()
cold3, tem3 = input().split()

    
count = 0

if (cold == 'Y' and int(tem) >= 37):
    count = count + 1


if (cold2 == 'Y' and int(tem2) >= 37):
    count = count + 1


if (cold3 == 'Y' and int(tem3) >= 37):
    count = count + 1



if count >= 2:
    print('E')

else:
    print('N')