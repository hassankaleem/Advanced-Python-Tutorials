##We have coded the transpose of 3 by 3 matrix 

new_matrix= [[],[],[]]
def t_mat(mat):
    for i in range(3):
        for j in range(3):
            new_matrix[j][i]= mat[i][j]
            print(j,i,'=',i,j)
    return new_matrix
        
print(t_mat([[1,2,3],[4,5,6],[7,8,9]]))
