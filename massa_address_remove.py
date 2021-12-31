#!/usr/bin/env python3

import json
from os import system
import pathlib
from pathlib import Path

WALLET = Path(pathlib.Path.cwd(), 'massa', 'massa-client', 'wallet.dat')

# Удаляет из списка выбранные адреса из списка js
# Удалять можно как по индексу так и по адресу кошелька
# При ошибках возвращает пустой список None
def del_address(js, in_addr):
    try:
        if str(in_addr).isdigit():
            js.pop(int(in_addr) - 1)
        elif in_addr != '':
            js.remove(in_addr)
        else:
            return js[:1]
    except:
        print('Не верно введен адрес или индекс кошелька')
        return None

    return js

# Сохранить данные из списка в файл в формате JSON
# Файл при этом очищается, а данные записываются новые в пустой файл
def save_addr(js, WALLET):
    if js == None:
        return 

    with open(WALLET, 'w') as f:
        json.dump(js, f)
    
    
# Main
def main():
    with open(WALLET, 'r') as f:
        js = json.load(f)          
       
    if len(js) == 1:
        print("В кошельке только один адрес. Нечего удалять")
        return  
        
    print("Список адресов, которые были найдены в файле wallet.dat:\n")
    for i, j in enumerate(js):
        print(f"{i+1}) {j}")


    print("\nВведите индекс или адрес кошелька, который нужно удалить. (Если ничего не вводить, по умолчанию удалятся все, кроме первого)")
    save_addr(del_address(js, input()), WALLET)

if __name__ == "__main__":
    main()

        
