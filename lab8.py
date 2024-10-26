from abc import ABC, abstractmethod
from typing import Optional


# Base abstract class with the template method
class BaseEntityUpdater(ABC):
    def update(
        self, entity_id: int, new_data: dict[str, any]
    ) -> tuple[int, str, Optional[dict[str, any]]]:
        """Template method defining the steps for updating an entity."""
        original_data = self.get_entity(entity_id)
        if not self.validate(original_data, new_data):
            self.on_validation_failure(entity_id, original_data, new_data)
            return 400, 'Validation Failed', None

        save_status = self.save_entity(entity_id, new_data)
        response = self.generate_response(entity_id, save_status)

        return response

    @abstractmethod
    def get_entity(self, entity_id: int) -> dict[str, any]:
        """Retrieve the entity from the database or API."""
        ...

    @abstractmethod
    def validate(self, original_data: dict[str, any], new_data: dict[str, any]) -> bool:
        """Validate the entity before saving."""
        ...

    @abstractmethod
    def save_entity(self, entity_id: int, new_data: dict[str, any]) -> bool:
        """Save the updated entity."""
        ...

    @abstractmethod
    def generate_response(
        self, entity_id: int, save_status: bool
    ) -> tuple[int, str, Optional[dict[str, any]]]:
        """Generate the response after updating."""
        ...

    def on_validation_failure(
        self, entity_id: int, original_data: dict[str, any], new_data: dict[str, any]
    ) -> None:
        """Optional hook: Called when validation fails."""
        ...


# Product Updater class with specific behavior
class ProductUpdater(BaseEntityUpdater):
    def validate(self, original_data: dict[str, any], new_data: dict[str, any]) -> bool:
        # Custom validation logic for Product
        return new_data.get('validated', False)

    def on_validation_failure(
        self, entity_id: int, original_data: dict[str, any], new_data: dict[str, any]
    ) -> None:
        # Notify administrator on validation failure
        print(f'Notification to admin: Product {entity_id} failed validation.')

    def get_entity(self, entity_id: int) -> dict[str, any]:
        return {'id': entity_id, 'name': 'Sample Product', 'validated': False}

    def save_entity(self, entity_id: int, new_data: dict[str, any]) -> bool:
        return True  # Simulate save success

    def generate_response(
        self, entity_id: int, save_status: bool
    ) -> tuple[int, str, Optional[dict[str, any]]]:
        return 200, 'Product Updated', None


# User Updater class with restricted email change logic
class UserUpdater(BaseEntityUpdater):
    def validate(self, original_data: dict[str, any], new_data: dict[str, any]) -> bool:
        # Prevent changing the email field
        if 'email' in new_data and new_data['email'] != original_data['email']:
            return False
        return True

    def get_entity(self, entity_id: int) -> dict[str, any]:
        return {'id': entity_id, 'name': 'John Doe', 'email': 'john.doe@example.com'}

    def save_entity(self, entity_id: int, new_data: dict[str, any]) -> bool:
        return True  # Simulate save success

    def generate_response(
        self, entity_id: int, save_status: bool
    ) -> tuple[int, str, Optional[dict[str, any]]]:
        return 200, 'User Updated', None


# Order Updater class with JSON response
class OrderUpdater(BaseEntityUpdater):
    def validate(self, original_data: dict[str, any], new_data: dict[str, any]) -> bool:
        return True  # Assume all orders are valid

    def get_entity(self, entity_id: int) -> dict[str, any]:
        return {'id': entity_id, 'items': ['item1', 'item2'], 'status': 'pending'}

    def save_entity(self, entity_id: int, new_data: dict[str, any]) -> bool:
        return True  # Simulate save success

    def generate_response(
        self, entity_id: int, save_status: bool
    ) -> tuple[int, str, Optional[dict[str, any]]]:
        order_data = self.get_entity(entity_id)
        return 200, 'Order Updated', order_data


if __name__ == '__main__':
    product_updater = ProductUpdater()
    user_updater = UserUpdater()
    order_updater = OrderUpdater()

    print(product_updater.update(1, {'validated': True}))  # Product update
    print(
        user_updater.update(2, {'name': 'Jane Doe', 'email': 'jane.doe@example.com'})
    )  # User update with email change attempt
    print(
        order_updater.update(3, {'status': 'shipped'})
    )  # Order update with JSON response
