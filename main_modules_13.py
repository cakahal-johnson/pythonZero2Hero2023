#import modules_13  # main calling
import modules_13 as md
# built-in modules
import platform as pl

# modules_13.greetings("cakahal") #  main calling

md.greetings("cakahal")

# main calling
# a = modules_13.person1['country']
# print(a)

# calling with as keyword
a = md.person1['country']
print(a)

# built-in modules
b = pl.system()
print(b)


# built-in modules using dir() Function
c = dir(pl)
print(c)

# our own modules using dir() Function
c = dir(md)
print(c)


