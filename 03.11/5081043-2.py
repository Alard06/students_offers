def main():
    num = 1
    while num <= 20:
        if num == 5:
            num += 1
            continue
        print(num)
        if num == 10:
            break
        num += 1


if __name__ == '__main__':
    main()