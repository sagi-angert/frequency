import sys



def main():
    if (len(sys.argv) != 2):
        print("N not provided, run again")
        exit
    try:
        N = int(sys.argv[1])
        file_path = input("enter file path to read: ")
        open_file = open(file_path, "r")
        words_list = open_file.read().split(" ")
        word_list = set(words_list)
        word_dict = {x: words_list.count(x) for x in word_list}
        word_dict = dict(sorted(word_dict.items(), key = lambda item: item[1], reverse = True))
        items = list(word_dict.items())
        for i in range (N):
            print(f"The word {items[i][0]} appeared {items[i][1]} times in the file")
    except ValueError as val_err:
        print(f"Given a string and not and integer for N, try again. full error: {val_err}")
    except FileNotFoundError as file_err:
        print(f"Error with file provided not existing, try again. full error: {file_err}")



if __name__ == "__main__":
    main()