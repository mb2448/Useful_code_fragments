def divide(x, y):
    return float(x)/y

if __name__ == "__main__":
    point_foo = (3, 4)
    point_bar = {'y': 3, 'x': 2}
    
    print(divide(*point_foo))
    print(divide(**point_bar))
    

