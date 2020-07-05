'''def soldier(p,f1,f2,fo):
    import os
    i=1
    os.chdir(p)
    print(os.getcwd())
    l=os.listdir(p)
    print(l)
    for x in l:
        if x.endswith(fo)!=True:
            if x == f1 or x == f2:
                pass
            else:
                os.rename(x,x.capitalize())
        else:
            os.rename(x,f'{i}{fo}')
            i+=1
    print(os.listdir(p))
soldier('f://',"$RECYCLE.BIN",'System Volume Information',".txt")
'''
import os
def removeFiles(filen):
    DNotDis = open(filen)
    l = (DNotDis.read())
    var = (l.split('\n'))
    DNotDis.close()
    return var

def soldier(pathn, filen, ext):
    filen=filen
    pathn=pathn
    os.chdir(pathn)
    count = 0
    var = removeFiles(filen)
    for f in os.listdir():
         f_name, f_ext = os.path.splitext(f)
         if f_ext == f'.{ext}':
             newName = f'{str(count)}{f_ext}'
             count += 1
             os.rename(f,newName)
             pass
         if f_name not in var:
             tn = f_name.title()
             new_name = f'{tn}{f_ext}'
         else:
             new_name = f'{f_name}{f_ext}'
         os.rename(f,new_name)

if _name_ == '__main__':
    pathn=input('Enter Path:')
    filen=input('Enter File Name Which Contain Name Of Files Not TO Alter: ')
    ext=input('Enter Extension/Formate: ')
    soldier(pathn,filen,ext)
