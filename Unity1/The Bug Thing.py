def input_bug_counts(bug_type):
    count = int(input(f"Enter the count of {bug_type} bugs: "))
    return count

def calculate_percent(total, count):
    percentage = (count / total) * 100
    return percentage

def input_bug_type_and_count():
    bug_type = input("Enter the type of bug: ")
    count = input_bug_counts(bug_type)
    return bug_type, count

def display_table(bug1, count1, bug2, count2, bug3, count3):
    total = count1 + count2 + count3
    percent1 = calculate_percent(total, count1)
    percent2 = calculate_percent(total, count2)
    percent3 = calculate_percent(total, count3)

    print("Bug Type\tCount\tPercentage")
    print("---------------------------------")
    print(f"{bug1}\t\t{count1}\t{percent1:.2f}%")
    print(f"{bug2}\t\t{count2}\t{percent2:.2f}%")
    print(f"{bug3}\t\t{count3}\t{percent3:.2f}%")
    
def main():
    bug1, count1 = input_bug_type_and_count()
    bug2, count2 = input_bug_type_and_count()
    bug3, count3 = input_bug_type_and_count()

    display_table(bug1, count1, bug2, count2, bug3, count3)

main()