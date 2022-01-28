
def convert(entries,numSieves,pan):
    j = 0
    temp = 0
    sum = 0
    data=[]
    p_idx=0

    for i in range(len(entries)):
        sum += float(entries[i].get())
        temp += 1
        if (temp == numSieves):
            td=[]
            sum+=float(pan[p_idx].get())
            p_idx+=1
            temp_sum = sum
            for k in range(numSieves):
                temp_sum -= float(entries[j].get())
                td.append(round(float(temp_sum * 100) / float(sum),6))
                j+=1
            data.append(td)
            sum = 0
            temp=0

    return data