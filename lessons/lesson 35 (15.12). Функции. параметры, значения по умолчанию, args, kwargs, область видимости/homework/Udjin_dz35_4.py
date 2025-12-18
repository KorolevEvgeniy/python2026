def create_counter(start=0, step=1):
 
    current_value = start
    
    def increment():
        nonlocal current_value
        
        current_value += step
        
        return current_value
    
    return increment

if __name__ == "__main__":
        
    counter1 = create_counter()
    print("create_counter (start=0, step=1)")
    print(f"counter1(): {counter1()}") 
    print(f"counter1(): {counter1()}")
    print(f"counter1(): {counter1()}")
    counter2 = create_counter(start=10, step=5)
    print("create_counter() (start=10, step=5)")
    print(f"counter2(): {counter2()}")
    print(f"counter2(): {counter2()}")
    print(f"counter2(): {counter2()}")
    print(f"counter1(): {counter1()}", '(счетчики независимы)')