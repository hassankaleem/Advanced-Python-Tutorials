def cout(n):
    if n<=0:
        print('Just kill the processe')
    else:
        print(n)
        cout(n-1)
