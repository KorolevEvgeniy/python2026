def analyze_purchases(items):

    total_price = 0
    items_count = 0
    max_price = 0
    most_expensive_item = None
    
    if not items:
        return {
            'total': 0,
            'count': 0,
            'avg_price': 0,
            'most_expensive': None
        }
    
    for item in items:
        current_price = item['price']
        current_name = item['name']
        
        total_price += current_price
        
        if current_price > max_price:
            max_price = current_price
            most_expensive_item = current_name
        
        items_count += 1
    
    average_price = total_price / items_count
    
    average_price = round(average_price, 2)
    
    return {
        'total': total_price,
        'count': items_count,
        'avg_price': average_price,
        'most_expensive': most_expensive_item
    }
if __name__ == "__main__":
    items = [
        {"name": "молоко", "price": 90},
        {"name": "хлеб", "price": 50},
        {"name": "яблоки", "price": 120}
    ]
    
    stats = analyze_purchases(items)
    print(stats)  
    
    empty_stats = analyze_purchases([])
    print(empty_stats) 