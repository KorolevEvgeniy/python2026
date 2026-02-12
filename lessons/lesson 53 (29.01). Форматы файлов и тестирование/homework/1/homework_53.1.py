import csv
import json
from collections import defaultdict

def read_csv_file(filename):
    sales_data = []
    with open('sales_data.csv', 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            row['Цена'] = float(row['Цена'])
            row['Количество'] = int(row['Количество'])
            sales_data.append(row)
    return sales_data

def analyze_sales_by_date(sales_data, target_date):
    daily_sales = []
    store_revenue = defaultdict(float)
    product_quantity = defaultdict(int)
    
    for sale in sales_data:
        if sale['Дата'] == target_date:
            daily_sales.append(sale)
            
            revenue = sale['Цена'] * sale['Количество']
            
            store_revenue[sale['Магазин']] += revenue
            
            product_quantity[sale['Продукт']] += sale['Количество']
    
    return daily_sales, store_revenue, product_quantity

def find_top_store(store_revenue):
    if not store_revenue:
        return None, 0
    
    top_store = max(store_revenue.items(), key=lambda x: x[1])
    return top_store

def generate_report(target_date, product_quantity):

    report = {
        target_date: []
    }
    
    for product, total_qty in product_quantity.items():
        report[target_date].append({
            "продукт": product,
            "общий объем продаж": total_qty
        })
    
    return report

def save_report_to_json(report, filename):
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(report, file, ensure_ascii=False, indent=2)

def main():
    csv_filename = 'sales_data.csv'
    
    print("Чтение данных из CSV-файла...")
    sales_data = read_csv_file(csv_filename)
    
    target_date = input("Введите дату для отчетности (формат YYYY-MM-DD): ")
    
    daily_sales, store_revenue, product_quantity = analyze_sales_by_date(
        sales_data, target_date
    )
    
    if not daily_sales:
        print(f"Нет данных о продажах за {target_date}")
        return
    
    top_store, top_revenue = find_top_store(store_revenue)
    
    if top_store:
        print(f"Наибольшие продажи за {target_date}: {top_store} с объёмом продаж {top_revenue:.0f}")
    else:
        print(f"Нет данных о продажах за {target_date}")
    
    report = generate_report(target_date, product_quantity)
    
    json_filename = f'sales_report_{target_date}.json'
    save_report_to_json(report, json_filename)
    print(f"Отчет сохранен в файл: {json_filename}")

if __name__ == "__main__":
    main()