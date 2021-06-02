## import modules here 
import pandas as pd
import numpy as np
import helper


################### Question 1 ###################

def buc(df):
    if len(df.columns.values) == 1:
        return [[sum(df.iloc[:, -1])]]

    if df.shape[0] == 1:
        result = buc_single_tuple(df)
        result = pd.DataFrame(result, columns=df.columns.values)
        return result

    # dims = [dim1, rest_of_dims]
    result = []
    dim1_value = sorted(set([x for x in df.iloc[:, 0]]))
    for v in dim1_value:
        list_v = []
        slice_v = helper.slice_data_dim0(df, v)
        if slice_v.shape[0] == 1:
            v_result = buc_single_tuple(slice_v)
        else:
            v_result = buc(slice_v)
        # 遍历result中每一种可能 加上 dim1的v
        for l in v_result:
            l.insert(0, v)
            list_v.append(l)
        result.extend(list_v)

    # ALL 那一行加入result中
    All_df = helper.remove_first_dim(df)
    if All_df.shape == 1:
        all_result = buc_single_tuple(All_df)
    else:
        all_result = buc(All_df)
    for e in all_result:
        e.insert(0, "ALL")
        result.append(e)
    return result

def buc_rec_optimized(df):
    if df.empty:
        return df
    result_list = buc(df)
    result_pd = pd.DataFrame(result_list, columns = df.columns.values)
    return result_pd

def buc_single_tuple(df):
    if df.empty:
        return df
    result = []
    head = df.iloc[0].tolist()
    epoch = 2**(df.shape[1]-1)
    length = df.shape[1]
    test = helper.project_data(df,0)
    for i in range(0, epoch):
        bin = '{0:0b}'.format(i)
        bin = '0'*(length-1-len(bin))+bin
        temp = head[:]
        for j in range(len(bin)):
            if bin[j] == "1":
                temp[j] = 'ALL'
        result.append(temp[:])
    return result

if __name__ == "__main__":
    d = {'A':[1,2], 'B':[2,1],'M':[100,20]}
    df = pd.DataFrame(data=d)
    print(buc_rec_optimized(df))