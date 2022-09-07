def find_avg_sum(str):
    sum = 0
    count = 0
    for ch in str:
        if ch.isdigit():
            sum += int(ch)
            count += 1
    return sum/count
if __name__ == "__main__":
    given_str = input("Anna merkkijono: ")
    print(find_avg_sum(given_str))
