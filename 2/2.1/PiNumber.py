# Function implementation
def Get(n = 1_000_000)->float:
    n = int(n)
    radius = 1
    horizontalSide = radius / n

    def GetVerticalSide(sideNumber: int)->float:
        return (radius ** 2 - ((sideNumber - 0.5) / n) ** 2) ** 0.5

    return 4 * sum([horizontalSide * GetVerticalSide(i) for i in range(1, n + 1)])

# Lambda function implementation
GetPi = lambda n: 4 * sum(list(map(lambda i: 1/n * (1 - ((i - 0.5) / n) ** 2) ** 0.5, range(1, n + 1))))