def aggregate_data(*args, **kwargs):
    
    operation = kwargs.get('operation', 'sum')
    valid_operations = {'sum', 'max', 'min'}
    result = None
    
    if args:
        if operation == 'sum':
            result = sum(args)
        elif operation == 'max':
            result = max(args)
        elif operation == 'min':
            result = min(args)
        else:
            result = None
    
    response = {'result': result, 'count': len(args)}
    
    response.update(kwargs)
    
    return response


if __name__ == "__main__":
    summa = aggregate_data(10, 20, 30, operation='sum')
    print(f"Сумма чисел: {summa}")

    maximum = aggregate_data(5, 7, 9, 1, operation='max', source='sensor_A', unit='Celsius')
    print(f"Максимум: {maximum}")
    
    minimum = aggregate_data(operation='min')
    print(f"Минимум: {minimum}")