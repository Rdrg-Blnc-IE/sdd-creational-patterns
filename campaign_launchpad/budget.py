class GlobalBudget:
    """
    One shared marketing budget across the system.
    """
    _instance = None

    def __new__(cls, initial_amount: float = 0.0):
        if cls._instance is None:
            instance = super().__new__(cls)
            instance._balance = initial_amount
            cls._instance = instance
        return cls._instance

    def allocate(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError('Allocation cant be negative')
        if self._balance - amount < 0:
            raise ValueError('Balance cant go below 0')
        self._balance -= amount

    def remaining(self) -> float:
        return self._balance

    def __repr__(self) -> str:
        return f"<GlobalBudget remaining={self._balance}>"
