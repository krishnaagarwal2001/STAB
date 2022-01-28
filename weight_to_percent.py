
def convert(entries,numSieves,pan):
    j = 0
    temp = 0
    sum = 0
    data=[]
    p_idx=0
    # print(len(entries))
    # print(numSieves.get())
    # print(len(pan))
    for i in range(len(entries)):
        # print("i",i)
        sum += float(entries[i].get())
        temp += 1
        if (temp == numSieves):
            td=[]
            sum+=float(pan[p_idx].get())
            p_idx+=1
            temp_sum = sum
            for k in range(numSieves):
                temp_sum -= float(entries[j].get())
                # print("temp_sum",temp_sum)
                # print("sum",sum)
                # print("value",float(temp_sum * 100) / float(sum))
                td.append(float(temp_sum * 100) / float(sum))
                j+=1
            # print(td)
            data.append(td)
            sum = 0
            temp=0

    return data