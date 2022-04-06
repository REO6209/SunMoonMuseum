'''
파일명 변경
'''

import os
 
def changeName(path, cName):
    i = 1
    for filename in os.listdir(path):
        print(path+filename, '=>', path+str(cName)+str(i)+'.jpg')
        os.rename(path+filename, path+str(cName)+str(i)+'.jpg')
        i += 1
 
# param(경로, 변경할 이름)
changeName(r'파일 경로','test')
