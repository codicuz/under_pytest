class SomeClass():
    def greatings(self, name: str = None):
        if name:
            return f'Hello, {name}'
        else:
            return 'Hello'
