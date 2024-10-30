from random import randint
import MergeSort

if __name__ == "__main__":
    T = [randint(1, 100) for _ in range(100)]
    print("Przed sortem:")
    print(T)
    MergeSort.Sort(T)
    print("Po sortowaniu:")
    print(T)
