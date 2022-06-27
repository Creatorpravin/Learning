from re import A
import threading




class __calc:
    def __init__(self, num):
        self.__num = num
        self.__cub = 0
    
    def print_cube(self):
        """
        function to print cube of given num
        """
        self.__cub = self.__num * self.__num * self.__num
        print("Cube: {}".format(self.__cub))
        
    def print_square(self):
        """
        function to print square of given num
        """
        print(self.__cub)
        print("Square: {}".format(self.__cub * self.__cub))


if __name__ == "__main__":
    # creating thread
    p1 = __calc(45)
    t1 = threading.Thread(target=p1.print_cube)
    t2 = threading.Thread(target=p1.print_square)

    # starting thread 1
    t1.start()
    # starting thread 2
    t2.start()

    # wait until thread 1 is completely executed
    t1.join()
    # wait until thread 2 is completely executed
    t2.join()

    # both threads completely executed

    print("Done!")
