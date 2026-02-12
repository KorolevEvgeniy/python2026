def is_balanced(s):
    if not s:
        return True
    
    pairs = ["()", "{}", "[]"]
    
    found_pair = False
    
    for pair in pairs:
        if pair in s:
            found_pair = True
    
    if found_pair:
        for pair in pairs:
            while pair in s:
                s = s.replace(pair, "")
        
        return is_balanced(s)
    else:
        return False

examples = ["([]{})", "([)]", "((()))"]
for example in examples:
    print(f"\nАнализ строки: '{example}'")
    result = is_balanced(example)
    print(f"ИТОГ: '{example}' -> {result}")