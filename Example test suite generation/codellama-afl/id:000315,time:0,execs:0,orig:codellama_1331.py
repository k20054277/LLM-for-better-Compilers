def main():
    x = 5
    y = 10
    
    # Using assert with range
    for i in range(x, y):
        assert i > 0, "i must be greater than 0"
        print(i)

if __name__ == "__main__":
    main()