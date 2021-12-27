import json
from os import system
import pathlib
from pathlib import Path

WALLET = Path(pathlib.Path.cwd(), 'massa', 'massa-client', 'wallet.dat')

# Удаляет из списка выбранные адреса из списка js
# Удалять можно как по индексу так и по адресу кошелька
# При ошибках возвращает пустой список None
def del_address(js, idx = None, addr=None):
    if addr == None and idx == None:
        return js[:1]
    
    try:
        js.pop(idx) if addr == None else js.remove(addr)
        print('Выбранный адрес кошелька удален!')
    except Exception:
        print('Индекс или адрес кошелька указаны неверно\n')
   
    return js

# Сохранить данные из списка в файл в формате JSON
# Файл при этом очищается, а данные записываются новые в пустой файл
def save_addr(js, WALLET):
    with open(WALLET, 'w') as f:
        json.dump(js, f)
    
    
# Main
if __name__ == "__main__":
    with open(WALLET, 'r') as f:
        js = json.load(f)          
       
    if len(js) == 1:
        print("В кошельке только один адрес. Нечего удалять")
        exit(0)    
        
    print("Список адресов, которые были найдены в файле wallet.dat:\n")
    for i, j in enumerate(js):
        print(f"{i+1}) {j}")
    print("\nВведите индекс или адрес кошелька, который нужно удалить. (Если ничего не вводить, по умолчанию удалятся все, кроме первого)")
    addr = input();

    if addr == '':
        js_ = del_address(js)
    elif addr.isdigit():
        js_ = del_address(js, idx = int(addr) - 1)
    else:
        js_ = del_address(js, addr = addr)


    if js_ != js:
        save_addr(js_, WALLET)

        
