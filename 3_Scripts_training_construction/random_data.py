import sys
import random
import os

if __name__ == '__main__':
    test = input("""Choose the test you want for your dataset: 
                    test_15.txt for a test dataset of 15 pages (5 of each documents types)
                    test_30.txt for a test dataset of 30 pages (10 of each documents types)
                    test_20_CatExpo.txt for a test dataset of 20 exhibition catalogs' pages
                    """)
    train = open("train.txt", "w")
    val = open("val.txt", "w")
    random.seed('1214')

   with open(test.txt) as f:
       files = (os.path.basename(filepath) for file in f.readlines())

    for i in sys.argv[1:]:
        with open('test.txt') as f:
            if os.path.basename(1) in files:
                pass
            else:
                i = os.path.abspath(i)
                monRand = random.random()
                if monRand <= 0.1:
                    val.write(i+"\n")
                else:
                    train.write(i+"\n")

    val.close()
    train.close()
    print("Dataset created")
