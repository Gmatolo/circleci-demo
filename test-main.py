from main import sum

def testsum(a,b):
    assert sum(2,5) == 7 
    print("the sum func works correctly")


if __name__ == "__main__":
    testsum()

