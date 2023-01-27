with open('test.txt', 'r+') as f:
    Matrix = [[int(num) for num in line.split(',')] for line in f if line.strip() != " " ]
print(Matrix)
trans_Matrix = [[0 for j in range(len(Matrix))] for i in range(len(Matrix[0]))]
for i in range(len(Matrix)):
    for j in range(len(Matrix[0])):
        trans_Matrix[j][i] = Matrix[i][j]       
print(trans_Matrix)
with open('text.txt', 'r+') as f:
    for row in trans_Matrix:
        f.write(' '.join([str(a) for a in row]) + '\n')
f.close()

