from abc import ABC, abstractmethod


# 1. Define the Notification interface
class Notification(ABC):
    @abstractmethod
    def send(self, title: str, message: str) -> None:
        pass


# 2. Implement EmailNotification class
class EmailNotification(Notification):
    def __init__(self, admin_email: str):
        self.admin_email = admin_email

    def send(self, title: str, message: str) -> None:
        print(
            f"Sent email with title '{title}' to '{self.admin_email}' that says '{message}'."
        )


# 3. Create SlackNotification adapter
class SlackNotification(Notification):
    def __init__(self, login: str, api_key: str, chat_id: str):
        self.login = login
        self.api_key = api_key
        self.chat_id = chat_id

    def _authorize(self):
        print(f'Authorizing Slack user {self.login} with API key {self.api_key}')

    def send(self, title: str, message: str) -> None:
        self._authorize()
        print(
            f"Sent Slack message with title '{title}' to chat '{self.chat_id}' that says '{message}'."
        )


# 4. Create SMSNotification adapter
class SMSNotification(Notification):
    def __init__(self, phone: str, sender: str):
        self.phone = phone
        self.sender = sender

    def send(self, title: str, message: str) -> None:
        print(
            f"Sent SMS from '{self.sender}' to '{self.phone}' with title '{title}' that says '{message}'."
        )


if __name__ == '__main__':
    email_notifier = EmailNotification('admin@example.com')
    email_notifier.send('Email Title', 'This is a test email message.')

    slack_notifier = SlackNotification('user_login', 'api_key', 'chat_id_123')
    slack_notifier.send('Slack Title', 'This is a test Slack message.')

    sms_notifier = SMSNotification('+1234567890', 'SenderName')
    sms_notifier.send('SMS Title', 'This is a test SMS message.')
