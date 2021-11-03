class ShippingContainer:

    next_serial = 1337 # Class attribute

    def __init__(self, owner_code, contents):
        self.owner_code = owner_code # Instance attributes...
        self.contents = contents
        self.serial = ShippingContainer.next_serial
        ShippingContainer.next_serial += 1
        # self.next_serial += 1 This has a similar affect, but could cause issues.
        
        # ShippingContainer.next_serial = ShippingContainer.next_serial + 1
        # self.next_serial = self.next_serial + 1
        # The above two are not the same. Second one will create a new instance attribute.