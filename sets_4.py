alpha = {"a","b","c","d","e","f"}
bravo = {"z","y","x","w","v"}
charlie = alpha.union(bravo)
for x in charlie:
  print(x," ",end="c")
for i in range(len(charlie)):
  print("pop ",i," ",end="")
  thepop = charlie.pop()
  print (thepop)
