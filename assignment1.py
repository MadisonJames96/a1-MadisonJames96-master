"""
Name: Madison James
Date started: 26/08/2018
GitHub URL: https://github.com/CP1404-2018-2/a1-MadisonJames96
"""


def main():
    print("Reading Tracker 1.0 - by Madison James")

    # counts number of lines in file
    count = 0
    for line in open("books.csv").readlines():
        count = count + 1

    # print number of books in file at the beginning of program
    print("{} books loaded from books.csv".format(count))


if __name__ == '__main__':
    main()
