from main import sum

def testsum(a,b):
    assert sum(5,6) == 11
    print("the sum func works correctly")


if __name__ == "__main__":
    testsum()

