# # names =('nile praj', 'dil praj', 'mil praj')
# # i = 0
# # total_names = len(names)
# # print('user:')
# # while i < total_names:
# #     end='and\n' if i==total_names -2 else'\n'
# #     print(' - %s' % names[i], end=end)
# #     i +=1

# #loop over a list of number
for num in[1,2,3,4,5,6,7,8,9,10]:
    print(num)
print('--')

#do the same using range
for num in range(10):
    print(num + 1)


#list and the for loop

# names =('nile praj', 'dil praj', 'mil praj')
# print('user:')
# for name in names:
#    end =' \n and\n' if name == names[-2] else'\n' 
#    print(' - %s' % name, end=end)

names =['nile praj', 'dil praj', 'mil praj']
for (index,value) in enumerate(names):
   
   print(' %d \t %s' %(index,value))
