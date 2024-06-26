class LinearFx:
    def __init__(self, m: float, c: float, interval: range = None) -> None:
        self.m = m
        self.c = c
        self.interval = interval

    def __str__(self) -> str:
        return f"LinearFx( {str(self.m)}x {'+ ' + str(self.c) if self.c > 0 else '- ' + abs(self.c)} ) [{self.interval.start}, {self.interval.stop}]"
    
    def calc(self, x: int):
        return self.m * x + self.c
        