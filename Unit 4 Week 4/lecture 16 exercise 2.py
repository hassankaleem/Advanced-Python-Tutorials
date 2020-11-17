def look_up(stg,pas_dic):
    for key in pas_dic.keys():
        if pas_dic[key]==stg:
            print(key)
    
look_up('uno',{'one':'uno','two':'duo','three':'trio'})
