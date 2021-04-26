class FruitCountInsufficientException(Exception):
    def __init__(self, fruit_count, message="Fruit count insufficient error"):
        self.fruit_count = fruit_count
        self.message = message
        super().__init__(self.message)

fruit_count = int(input("Enter Fruit Count: "))
if not 10 < fruit_count:
    raise FruitCountInsufficientException(fruit_count)
else:
    print("Fruit count is " , fruit_count)