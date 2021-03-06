class ShippingContainer:

    next_serial = 1337 # Class attribute

    # @staticmethod
    # def _generate_serial():
    #     result = ShippingContainer.next_serial
    #     ShippingContainer.next_serial += 1
    #     return result

    @classmethod
    def _generate_serial(cls):
        result = cls.next_serial
        cls.next_serial += 1
        return result

    # Factory method
    @classmethod
    def create_empty(cls, owner_code):
        return cls(owner_code, contents=[])

    @classmethod
    def create_with_items(cls, owner_code, items):
        return cls(owner_code, contents=list(items))




    # TODO Check the differences between @classmethod and @staticmethod

    def __init__(self, owner_code, contents):
        self.owner_code = owner_code # Instance attributes...
        self.contents = contents
        # self.serial = ShippingContainer.next_serial
        # ShippingContainer.next_serial += 1
        # self.next_serial += 1 This has a similar affect, but could cause issues.
        
        # ShippingContainer.next_serial = ShippingContainer.next_serial + 1
        # self.next_serial = self.next_serial + 1
        # The above two are not the same. Second one will create a new instance attribute.
        self.serial = ShippingContainer._generate_serial()