
car = ['bugati','ferrari','lamborgini','audi']
num_car = [1,2,3,4]
print(dict(zip(car,num_car)))

lst =[1,2,3,4,5,6,6,4,3]

nk = [str(i) for i in lst]
nm = '-'.join(nk)
# print('-'.join(nk))
print(nm)

from colorama import Fore,Style
print(Fore.MAGENTA + 'this is a new output'.center(40)+ Style.RESET_ALL)
ks = '-'.join(map(str,lst))
print(ks)