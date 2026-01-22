def encrypt(text: str, shift: int) -> str:
    
    result = []
    
    for char in text:
        
        if 'A' <= char <= 'Z':
            base = ord('A')
            shifted_char = chr((ord(char) - base + shift) % 26 + base)
            result.append(shifted_char)
            
        elif 'a' <= char <= 'z':
            base = ord('a')
            shifted_char = chr((ord(char) - base + shift) % 26 + base)
            result.append(shifted_char)

        else:
            result.append(char)
    
    return ''.join(result)

def decrypt(text: str, shift: int) -> str:
   
    return encrypt(text, -shift)

def main():
   
    while True:
        mode = input("Выберите режим (e - шифрование, d - расшифровка, q - выход): ").lower()
        if mode in ['e', 'd', 'q']:
            break
        print("Некорректный ввод. Пожалуйста, введите 'e', 'd' или 'q'.")
    
    if mode == 'q':
        print("Выход из программы.")
        return
    
    while True:
        try:
            shift = int(input("Введите сдвиг (целое число): "))
            break
        except ValueError:
            print("Некорректный ввод. Пожалуйста, введите целое число.")
    
    text = input("Введите текст: ")
    
    if mode == 'e':
        result = encrypt(text, shift)
        print(f"\nЗашифрованный текст: {result}")
    elif mode == 'd':
        result = decrypt(text, shift)
        print(f"\nРасшифрованный текст: {result}")
    
    if mode == 'e':
        print(f"\nПроверка: decrypt(encrypt(text, {shift}), {shift}) == исходный текст")
        print(f"Результат проверки: {decrypt(result, shift) == text}")

if __name__ == "__main__":
    main()