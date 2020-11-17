def my_fun(data,str,num):
    data = data[:num]+tuple(str)+data[num+1:]
    print(data)
    return data
