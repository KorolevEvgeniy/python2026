from abc import ABC, abstractmethod
from typing import List

class DiscountPolicy(ABC):
    
    def __init__(self, name: str):
        self.name = name
    
    @abstractmethod
    def apply(self, price: float) -> float:
        pass
    
    def clamp_price(self, price: float) -> float:
        if price < 0:
            return 0.0
        return price

class PercentDiscount(DiscountPolicy):
    
    def __init__(self, name: str, percent: float):
        super().__init__(name)
        self.percent = percent
    
    def apply(self, price: float) -> float:
        normalized_price = super().clamp_price(price)
        
        discount = normalized_price * (self.percent / 100)
        return normalized_price - discount


class FixedDiscount(DiscountPolicy):
    
    def __init__(self, name: str, amount: float):
        super().__init__(name)
        self.amount = amount
    
    def apply(self, price: float) -> float:
        normalized_price = super().clamp_price(price)
        
        discounted_price = normalized_price - self.amount
        return max(discounted_price, 0.0)


class PriceCalculator:
    
    def __init__(self, policies: List[DiscountPolicy]):
        self.policies = policies
    
    def calculate(self, price: float) -> float:
        result = price
        
        for policy in self.policies:
            result = policy.apply(result)
            
        return result
    
percent_discount = PercentDiscount("Скидка 10%", 10)
print(f"   Создана процентная скидка: {percent_discount.name}")
    
fixed_discount = FixedDiscount("Скидка 150 руб.", 150)
print(f"   Создана фиксированная скидка: {fixed_discount.name}")


class MinPriceDiscount(DiscountPolicy):
    
    def __init__(self, name: str, min_price: float, percent: float):
        super().__init__(name)
        self.min_price = min_price
        self.percent = percent
    
    def apply(self, price: float) -> float:
        normalized_price = super().clamp_price(price)
        
        if normalized_price < self.min_price:
            return normalized_price
        
        discount = normalized_price * (self.percent / 100)
        return normalized_price - discount

test_prices = [500.0, 1200.0, -150.0]
    
for price in test_prices:
    print(f"\nИсходная цена: {price} руб.")
    print(f"  После {percent_discount.name}: {percent_discount.apply(price):.2f} руб.")
    print(f"  После {fixed_discount.name}: {fixed_discount.apply(price):.2f} руб.")
