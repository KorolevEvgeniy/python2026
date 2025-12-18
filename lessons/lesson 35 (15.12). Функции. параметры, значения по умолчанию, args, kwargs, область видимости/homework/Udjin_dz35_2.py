def generate_prices(base, count, markup=0.0, discount=0.0):
    result = []

    final_price = base * (1 + markup) * (1 - discount)
    rounded_price = round(final_price, 2)
    
    for _ in range(count):
        result.append(rounded_price)
        
    return result

if __name__ == "__main__":

    prices1 = generate_prices(base=100, count=3)
    print(f"Тест 1: {prices1}") 
    
    prices2 = generate_prices(base=100, count=2, markup=0.1)
    print(f"Тест 2: {prices2}") 
    
    prices3 = generate_prices(base=200, count=2, markup=0.2, discount=0.05)
    print(f"Тест 3: {prices3}")  
    
    prices4 = generate_prices(base=50, count=0)
    print(f"Тест 4: {prices4}")  