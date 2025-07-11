def main():
    source_file = 'SPORT.DAT'
    target_file = 'BASKET.DAT'
    sport_name = "Basket Ball"
    source=open('Sport.dat', 'r')
    target=open('Basket.dat', 'w')
    copied_records = 0
    for line in source:
        data = line.strip().split(',')
        if data[0] == sport_name:
            target.write(line)
            copied_records += 1
    a='hello world'
    target.write(a)
    print(f"Copied {copied_records} records to {target_file}")

if __name__ == "__main__":
  main()
