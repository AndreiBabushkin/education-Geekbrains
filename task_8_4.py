def val_checker(x):
   def checker(func):
      def func_cube(cube):
         if cube > 0:
            return func(cube)
         else:
            msg = 'wrong val ' + str(cube)
         raise ValueError(msg)

      return func_cube

   return checker


@val_checker(lambda x: x > 0)
def calc_cube(x):
   return x ** 3
a = calc_cube(10)
print(a)

