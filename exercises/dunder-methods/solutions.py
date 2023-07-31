class EmailAddress:
    def __init__(self, address):
        if address.count('@') != 1:
            raise ValueError()
        self.__address = address

    def __str__(self):
        return self.__address

    def __repr__(self):
        return f'EmailAddress({self.__address!r})'

    def __eq__(self, other):
        if isinstance(other, EmailAddress):
            return str(self).lower() == str(other).lower()
