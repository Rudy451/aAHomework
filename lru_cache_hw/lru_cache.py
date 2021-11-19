class LRUCache:

    def __init__(self, limit):
        self.limit = limit
        self.store = []

    def count(self):
        return len(self.store)

    def add(self, val):
        if self.__empty():
            pass
        else:
            if self.__limit_reached():
                self.__update_cache()
            self.__check_duplicate(val)
        self.store.append(val)

    def show(self):
        return self.store

    def __empty(self):
        return self.count() == 0

    def __limit_reached(self):
        return self.count() == self.limit

    def __update_cache(self):
        self.store.pop(0)

    def __check_duplicate(self, val):
        for spot in range(0, self.count()):
                if self.store[spot] == val:
                    self.store.pop(spot)
                    break

johnny_cache = LRUCache(4)

johnny_cache.add(5)

print(johnny_cache.count())

johnny_cache.add([1, 2, 3])
johnny_cache.add(5)
johnny_cache.add(-5)
johnny_cache.add({"a": 1, "b": 2, "c": 3})
johnny_cache.add([1, 2, 3, 4])
johnny_cache.add("rind_of_fire")
johnny_cache.add("I walk the line")
johnny_cache.add("I walk the line")
johnny_cache.add({"a": 1, "b": 2, "c": 3})

print(johnny_cache.show())
