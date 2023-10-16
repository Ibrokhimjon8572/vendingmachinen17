# import time

# # print

# # for i in range(10):
# #     pass
# # ('sleep boshlandi')
# # time.sleep(3)
# # print('sleep tugatildi')

# # def renge_custom(n):
# #     value = 0
# #     while value < n:
# #         yield value
# #         value += 1
# #     return 'ok'
# # for i in range(10):
# #     print(i)
# # x = [a for a in renge_custom(10)]
# # print(x)
# # for i in renge_custom(10):
# #     print(i)
# # print(a)


# def my_generator():
#     for i in range(10):
#         yield i
# a = my_generator()
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))


# class PowTwo:
#     def __init__(self, max):
#         self.n = 0
#         self.max = max

#     def __iter__(self):
#         return self

#     def __next__(self):
#         if self.n > self.max:
#             raise StopIteration

#         result = 2 ** self.n
#         self.n += 1
#         return result

# a = PowTwo(10)
# print(a.__next__())
# print(a.__next__())
# print(a.__next__())
# print(a.__next__())
# print(a.__next__())
# print(a.__next__())
# print(a.__next__())
# print(a.__next__())
# print(a.__next__())
# print(a.__next__())
# print(a.__next__())
# print(a.__next__())
# print(a.__next__())
# print(a.__next__())
# a = [12]
# print(dir(a))
# import time
# class Salom:
#     def salom(self):
#         print(time.time())
#     def __init__(self) -> None:
#         self.salom()

#     def __enter__(self):
#         print('in enter')
#     def __exit__(self):
#         print('in exit')
# print('a ---> ')
# a = Salom()
# time.sleep(3)
# print('b --> ')

# Python program showing
# file management using 
# context manager
# import time
# class FileManager():
#     def __init__(self, filename, mode):
#         print('file created')
#         self.filename = filename
#         self.mode = mode
#         self.file = None
#     def work(self):
#         pass
#     def __enter__(self):
        # time.sleep(3)
#         print('file yaratilish jarayonida')
#         self.file = open(self.filename, self.mode)
#         print('in enter')
#         return self.file
     
#     def __exit__(self, exc_type, exc_value, exc_traceback):
#         pass
#         print('uzur ishimiz tugatildi')
#         self.file.close()
 
# # # loading a file 
# with FileManager('test.txt', 'w') as f:
#     f.write('Test')
# file =  FileManager('test.txt', 'w')
# print(file)

 
# print(f.closed)