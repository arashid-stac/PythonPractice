class Buyer:
    """Buyer class for APO"""

    key_access = "test"
    buyer_id = 1

    def __init__(self, member_key=None):
        self.status = None
        if member_key is None:
            self.buyer_id = 0
            self.set_status("NONMEMBER")
        else:
            if member_key == Buyer.key_access:
                self.set_status("MEMBER")
                self.buyer_id = Buyer.buyer_id
                Buyer.buyer_id = Buyer.buyer_id + 1
            else:
                self.buyer_id = 0
                self.set_status("NONMEMBER")
                
    def set_status(self, status):
        self.status = status

    def get_status(self):
        return self.status

    def get_id(self):
        return self.buyer_id

    def __str__(self):
        return "Buyer {}: {}".format(self.get_id(), self.get_status())


b1 = Buyer()
b2 = Buyer("test")
b3 = Buyer("test")
b4 = Buyer("nope")
print(b1)
print(b2)
print(b3)
print(b4)
