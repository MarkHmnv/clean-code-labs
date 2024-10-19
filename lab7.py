from abc import ABC, abstractmethod


# Strategy Interface
class DeliveryStrategy(ABC):
    @abstractmethod
    def calculate_cost(self, order_amount: float) -> float:
        """Calculate the delivery cost based on the strategy."""
        ...


# Concrete Strategy: Pickup (No delivery cost)
class PickupStrategy(DeliveryStrategy):
    def calculate_cost(self, order_amount: float) -> float:
        return 0.0


# Concrete Strategy: External Delivery Service
class ExternalDeliveryStrategy(DeliveryStrategy):
    def calculate_cost(self, order_amount: float) -> float:
        return order_amount * 10.0


# Concrete Strategy: Own Delivery Service
class OwnDeliveryStrategy(DeliveryStrategy):
    def calculate_cost(self, order_amount: float) -> float:
        return order_amount * 5.0


# Context class to use the strategy
class DeliveryContext:
    def __init__(self, strategy: DeliveryStrategy):
        self._strategy = strategy

    def set_strategy(self, strategy: DeliveryStrategy):
        """Change the delivery strategy at runtime."""
        self._strategy = strategy

    def calculate_delivery_cost(self, order_amount: float) -> float:
        """Calculate the delivery cost using the selected strategy."""
        return self._strategy.calculate_cost(order_amount)


if __name__ == '__main__':
    pickup = PickupStrategy()
    external_delivery = ExternalDeliveryStrategy()
    own_delivery = OwnDeliveryStrategy()

    context = DeliveryContext(strategy=pickup)
    print('Pickup Cost:', context.calculate_delivery_cost(100.0))

    context.set_strategy(external_delivery)
    print('External Delivery Cost:', context.calculate_delivery_cost(100.0))

    context.set_strategy(own_delivery)
    print('Own Delivery Cost:', context.calculate_delivery_cost(100.0))
