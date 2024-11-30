import json
 

def output_all_records(flowers):
 with open('flowers.json', 'r', encoding='utf-8') as file:
            data = json.load(file)
            for flower in data:
                print(f"№: {flower['id']}, Название: {flower['name']}, Латинское название: {flower['latin_name']}, Является краснокнижным: {flower['is_red_book_flower']}, Цена: {flower['price']}")
                
def output_for_recording_by_id(flowers):
        num=input("Введите номер записи по которой вы хотите сделать вывод информации:\n")
        with open('flowers.json', 'r', encoding='utf-8') as file:
            data = json.load(file)
            found = False
            for flower in data:
                if flower['id'] == num:
                    print(f"\n=============== Найдено ===============")
                    print(f"{flower['id']} >> Название {flower['name']}, Латинское название: {flower['latin_name']}")
                    print(f"Является краснокнижным: {flower['is_red_book_flower']}, Цена: {flower['tank_volume']}")
                    found = True
                    break
            if not found:
                print("\n=============== Не найдено ===============")

def adding_a_record(flowers):
    new_id=input("Введите номер записи:")
    new_name=input("Введите название цветка:")
    new_latin_name=input("Введите полное латинское название:")
    new_is_red_book_flower=input("Является краснокнижным?(True/False):")=='True'
    new_price = int(input("Введите цену: ")) 
           
    new_flower = {
        "id": new_id,
        "name": new_name,
        "latin_name": new_latin_name,
        "is_red_book_flower": new_is_red_book_flower,
        "price": new_price
        }
    with open('Flowers.json', 'r+', encoding='utf-8') as file:
        data = json.load(file)
        data.append(new_flower)
        file.seek(0)
        json.dump(data, file, ensure_ascii=False, indent=4)
    
def delete_record():
     deletе = input("Введите номер записи которую вы хотите удалить: ")
     with open('flowers.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
        found = False
        for flower in data:
                if flower['id'] == deletе:
                    data.remove(flower)
                    found = True
                    break
        if not found:
                print("\n=============== Не найдено ===============")
        else:
                file.seek(0)
                file.truncate()
                json.dump(data, file, ensure_ascii=False, indent=4)

def main():
     count=0

     flowers = [
    {"id": "1", "name": "French Rose", "latin_name": "Rosa gallica", "is_red_book_flower": False, "price": 70},
    {"id": "2", "name": "Madonna Lily", "latin_name": "Lilium candidum", "is_red_book_flower": False, "price": 60},
    {"id": "3", "name": "Common Peony", "latin_name": "Paeonia officinalis", "is_red_book_flower": False, "price": 50},
    {"id": "4", "name": "White Water Lily", "latin_name": "", "is_red_book_flower": False, "price": 55},
    {"id": "5", "name": "Lady's Slipper Orchid", "latin_name": "", "is_red_book_flower": True, "price": 500}
    ]
     with open('flowers.json', 'w', encoding='utf-8') as file:
      json.dump(flowers, file, ensure_ascii=False, indent=4)


     while True:
      print("\nЧто вы хотите сделать?")
      print("1. Вывести все записи")
      print("2. Вывести запись по цветку")
      print("3. Добавить запись")
      print("4. Удалить запись по цветку")
      print("5. Выйти из программы")

      res = input("\nВыберите пункт из предложенного списка: ")

      if res=="1":
           output_all_records(flowers)
           count+=1
      elif res=="2":
           output_for_recording_by_id(flowers)
           count+=1
      elif res=="3":
           adding_a_record(flowers)
           count+=1
      elif res=="4":
           delete_record(flowers)
           count+=1
      elif res=="5":
           print(f"\nКоличество выполненных операций с записями: {count}")
           break
      else:
       print("Неправильный ввод, попробуйте снова.")  
       
if __name__ == "__main__":#выполнение проверки того, что скрипт выполняется как основной модуль
     main()
