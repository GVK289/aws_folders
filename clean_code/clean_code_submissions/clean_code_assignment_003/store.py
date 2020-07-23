class Item:
    def __init__(self, name, price, category):
        self._name = name
        self._price = price
        self._category = category

        if bool(isinstance(price, str) or price <= 0):
            raise ValueError('Invalid value for price, got {}'.format(price))

        if not isinstance(category, str):
            raise 'Invalid value for category, got {}'.format(category)

        if not isinstance(name, str):
            raise 'Invalid value for name, got {}'.format(name)
    @property
    def name(self):
        return self._name

    @property
    def price(self):
        return self._price
    @property
    def category(self):
        return self._category

    def __str__(self):
        return '{}@{}-{}'.format(self._name, self._price, self._category)

class Query:
    def __init__(self, field, operation, value):
        self._field = field
        list_of_operations = ['IN', 'EQ', 'GT', 'GTE', 'LT',
                              'LTE', 'STARTS_WITH', 'ENDS_WITH', 'CONTAINS']

        if operation not in list_of_operations:
            raise ValueError('Invalid value for operation, got '+(operation))
        if not isinstance(field, str):
            raise ValueError('Invalid value for field')
        if not isinstance(operation, str):
            raise ValueError('Invalid value for price')
        self._operation = operation
        self._value = value
    @property
    def field(self):
        return self._field
    @property
    def operation(self):
        return self._operation
    @property
    def value(self):
        return self._value

    def __str__(self):
        return '{} {} {}'.format(self._field, self._operation, self._value)

class Store:
    def __init__(self, item_list=None):
        if item_list:
            self.item_list = item_list
        else:
            self.item_list = []

    def add_item(self, item):
        self.item_list.append(item)

    def count(self):
        return len(self.item_list)

    @staticmethod
    def filtering_items(query, items_list):
        filtered_list = []
        for item in items_list:
            attribute = getattr(item, query.field)
            Store.arthematic_operations(attribute, query, filtered_list, item)
            Store.string_operations(attribute, query, filtered_list, item)
        return filtered_list

    @staticmethod
    def arthematic_operations(attribute, query, filtered_list, item):
        if query.operation == 'EQ':
            if attribute == query.value:
                filtered_list.append(item)
        elif query.operation == 'GTE':
            if attribute >= query.value:
                filtered_list.append(item)
        elif query.operation == 'GT':
            if attribute > query.value:
                filtered_list.append(item)
        elif query.operation == 'LTE':
            if attribute <= query.value:
                filtered_list.append(item)
        elif query.operation == 'LT':
            if attribute < query.value:
                filtered_list.append(item)

    @staticmethod
    def string_operations(attribute, query, filtered_list, item):
        if query.operation == 'IN':
            if attribute in query.value:
                filtered_list.append(item)
        if query.operation == 'STARTS_WITH':
            if attribute.startswith(query.value):
                filtered_list.append(item)
        if query.operation == 'ENDS_WITH':
            if attribute.endswith(query.value):
                filtered_list.append(item)
        if query.operation == 'CONTAINS':
            if attribute.find(query.value) != -1:
                filtered_list.append(item)

    def filter(self, query):
        filtered_list = self.filtering_items(query, self.item_list)
        store = Store(filtered_list)
        return store

    def exclude(self, query):
        excluded_list = []
        filtered_list = self.filtering_items(query, self.item_list)
        for item in self.item_list:
            if item not in filtered_list:
                excluded_list.append(item)
        store = Store(excluded_list)
        return store

    def __str__(self):
        item_str = ""
        for item in self.item_list:
            item_str += str(item) + '\n'
        store_items = item_str[:-1]
        length = len(item_str)
        if length:
            return store_items
        return 'No items'
