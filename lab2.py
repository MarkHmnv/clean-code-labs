from abc import ABC, abstractmethod


# 1. Define the abstract class (SocialNetwork)
class SocialNetwork(ABC):
    def __init__(self, username: str, password: str) -> None:
        self.username = username
        self.password = password

    @abstractmethod
    def publish_message(self, message: str) -> None:
        """Abstract method to publish a message to a social network."""
        pass


# 2. Define concrete classes for Facebook and LinkedIn
class Facebook(SocialNetwork):
    def __init__(self, login: str, password: str) -> None:
        super().__init__(login, password)

    def publish_message(self, message: str) -> None:
        """Simulate publishing a message to Facebook."""
        print(f"Publishing message to Facebook: {message}")


class LinkedIn(SocialNetwork):
    def __init__(self, email: str, password: str) -> None:
        # LinkedIn uses email instead of username
        super().__init__(email, password)

    def publish_message(self, message: str) -> None:
        """Simulate publishing a message to LinkedIn."""
        print(f"Publishing message to LinkedIn: {message}")


# 3. Define a factory interface to create social network connections
class SocialNetworkFactory(ABC):
    @abstractmethod
    def create_social_network(self, username: str, password: str) -> SocialNetwork:
        """Factory method to create a social network instance."""
        pass


# 4. Implement the concrete factories for Facebook and LinkedIn
class FacebookFactory(SocialNetworkFactory):
    def create_social_network(self, login: str, password: str) -> Facebook:
        """Create a Facebook instance."""
        return Facebook(login, password)


class LinkedInFactory:
    def create_social_network(self, email: str, password: str) -> LinkedIn:
        """Create a LinkedIn instance."""
        return LinkedIn(email, password)


if __name__ == "__main__":
    # Facebook example
    facebook_factory = FacebookFactory()
    facebook = facebook_factory.create_social_network(login="facebook_user", password="facebook_pass")
    facebook.publish_message("Hello, Facebook!")

    # LinkedIn example
    linkedin_factory = LinkedInFactory()
    linkedin = linkedin_factory.create_social_network(email="linkedin_user@example.com", password="linkedin_pass")
    linkedin.publish_message("Hello, LinkedIn!")
