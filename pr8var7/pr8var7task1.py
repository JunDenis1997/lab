n = int( input( 'Размер матрицы: ' ) )
k = (n*n - n)//2 + n
print( f'Введите {k} элементов матрицы: ' )
m = []
for i in range(n):
    m.append( [0]*n )
    for j in range(i,n):
        m[i][j] = int( input( '-> ' ) )
for i in range(n):
    for j in range(i,n):
        m[j][i] = m[i][j]
print ('Исходная матрица ')
for row in m:
    print(row, sep='\t' )