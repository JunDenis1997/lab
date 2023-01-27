mas= [1, 9, 2, 8, 3, 7, 4, 6, 5, 10]
sum_chetn=0
proizved=1
minim=min(mas)
maxim=max(mas)
i_minim=0
i_maxim=0
for i in range(len(mas)):
   if mas[i]%2!=0:
       proizved*=mas[i]
   else:
       sum_chetn+=mas[i]
print ('Исходный массив', mas)
print('Сумма', sum_chetn)
print('Произведение:', proizved)
for i in range(len(mas)):
   if mas[i]==minim:
       i_minim=i
   if mas[i]==maxim:
       i_maxim=i
mas[i_minim]=maxim
mas[i_maxim]=minim
print ('Массив после перестановки', mas)