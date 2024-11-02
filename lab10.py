from abc import ABC, abstractmethod


# Abstract Mediator
class Mediator(ABC):
    @abstractmethod
    def notify(self, sender: object, event: str) -> None:
        pass


# Concrete Mediator
class FlowerDeliveryMediator(Mediator):
    def __init__(self):
        self.components = []

    def add_component(self, component: 'Component') -> None:
        self.components.append(component)
        component.set_mediator(self)

    def notify(self, sender: object, event: str) -> None:
        if event == 'date_selected':
            self.update_time_intervals(sender)
        elif event == 'recipient_checkbox_changed':
            self.update_recipient_fields(sender)
        elif event == 'pickup_checkbox_changed':
            self.update_delivery_fields(sender)

    def update_time_intervals(self, sender: object) -> None:
        print('Time intervals were updated')

    def update_recipient_fields(self, sender: object) -> None:
        print('Recipient fields were updated')

    def update_delivery_fields(self, sender: object) -> None:
        print('Delivery fields were updated')


# Abstract Component
class Component(ABC):
    def __init__(self):
        self.mediator = None

    def set_mediator(self, mediator: Mediator) -> None:
        self.mediator = mediator


# Concrete Components
class DateSelector(Component):
    def select_date(self, date: str) -> None:
        self.mediator.notify(self, 'date_selected')
        print('Date was selected')


class RecipientCheckbox(Component):
    def change_state(self, state: bool) -> None:
        self.mediator.notify(self, 'recipient_checkbox_changed')
        print('Recipient checkbox changed')


class PickupCheckbox(Component):
    def change_state(self, state: bool) -> None:
        self.mediator.notify(self, 'pickup_checkbox_changed')
        print('Pickup checkbox changed')


class RecipientNameField(Component):
    def set_value(self, name: str) -> None:
        print('Recipient name was set')


class RecipientPhoneField(Component):
    def set_value(self, phone: str) -> None:
        print('Recipient phone was set')


class DeliveryAddressField(Component):
    def set_value(self, address: str) -> None:
        print('Delivery address was set')


if __name__ == '__main__':
    mediator = FlowerDeliveryMediator()

    date_selector = DateSelector()
    recipient_checkbox = RecipientCheckbox()
    pickup_checkbox = PickupCheckbox()
    recipient_name_field = RecipientNameField()
    recipient_phone_field = RecipientPhoneField()
    delivery_address_field = DeliveryAddressField()

    mediator.add_component(date_selector)
    mediator.add_component(recipient_checkbox)
    mediator.add_component(pickup_checkbox)
    mediator.add_component(recipient_name_field)
    mediator.add_component(recipient_phone_field)
    mediator.add_component(delivery_address_field)

    # Simulate user interactions
    date_selector.select_date('2024-11-02')
    recipient_checkbox.change_state(True)
    pickup_checkbox.change_state(False)
