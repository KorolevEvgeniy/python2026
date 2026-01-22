from abc import ABC, abstractmethod

class NotificationChannel(ABC):
    def __init__(self, sender_name: str):
        self.sender_name = sender_name

    @abstractmethod
    def get_area(self):
        pass

    def format_message(self, message: str) -> str:
        return f"[{self.sender_name}] {message}"

class EmailChannel(NotificationChannel):
    def __init__(self, sender_name: str, sender_email: str):
        super().__init__(sender_name)
        self.sender_email = sender_email
    
    def send(self, recipient: str, message: str) -> None:
        formatted_message = super().format_message(message)
        print(f"EMAIL to {recipient}: {formatted_message} (from {self.sender_email})")

class SMSChannel(NotificationChannel):
    def __init__(self, sender_name: str, sender_phone: str):
        super().__init__(sender_name)
        self.sender_phone = sender_phone
    
    def send(self, recipient: str, message: str) -> None:
        formatted_message = super().format_message(message)
        print(f"SMS to {recipient}: {formatted_message} (from {self.sender_phone})")

class NotificationService:
    def __init__(self, channels: list[NotificationChannel]):
        self.channels = channels

    def notify_all(self, recipient: str, message: str) -> None:
        
        
