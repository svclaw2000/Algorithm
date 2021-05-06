# 00:10 / 00:30 unsolved

N = int(input())
unselect = list(map(int, input().split()))
select = []


while True:
    cur_sum = sum(select)
    if 1 in unselect:
        select.append(1)
        unselect.remove(1)
    elif cur_sum+1 in unselect:
        unselect.extend(select)
        select = [cur_sum + 1]
        unselect.remove(cur_sum + 1)
    else:
        has_num = False
        for n in select:
            if n+1 in select:
                pass

