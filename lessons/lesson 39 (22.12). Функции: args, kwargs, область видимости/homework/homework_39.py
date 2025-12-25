def summarize_orders(*orders, **kwargs):
    if not orders:
        raise ValueError("Нет заказов для обработки")
    
    currency = kwargs.get("currency", "RUB")
    round_to = kwargs.get("round_to", 2)
    
    if not isinstance(round_to, int) or round_to < 0:
        raise ValueError("round_to должен быть неотрицательным целым числом")
    
    total_quantity = 0
    for order in orders:
        if not isinstance(order, tuple) or len(order) != 2:
            raise ValueError(f"Некорректный формат заказа: {order}")
        
        _, quantity = order 
        
        if not isinstance(quantity, (int, float)) or quantity < 0:
            raise ValueError(f"Некорректное количество в заказе: {order}")
        
        total_quantity += quantity
    
    orders_count = len(orders)
    average_quantity = total_quantity / orders_count
    average_quantity = round(average_quantity, round_to)

    result = {
        "заказов": orders_count,
        "общее количество": total_quantity,
        "среднее количество": average_quantity,
        "валюта": currency
    }
    return result
try:
    result1 = summarize_orders(("кофе", 2), ("чай", 1))
    print(f"Результат 1: {result1}")

except Exception as e:
    print(f"Ошибка: {type(e).__name__}: {e}")
try:
    result2 = summarize_orders(("пицца", 3), ("салат", 1), currency="USD", round_to=1)
    print(f"Результат 2: {result2}")
except Exception as e:
    print(f"Ошибка: {type(e).__name__}: {e}")
    
try:
    result3 = summarize_orders()
    print(f"Результат 3: {result3}")
except Exception as e:
    print(f"Ошибка: {type(e).__name__}: {e}")
    