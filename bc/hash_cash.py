import md5


string = "Hello world"

n = 0;

found = False


while found == False:
   cstr = string + str(n)
   chash = md5.new(cstr).hexdigest()
   n = n + 1
   
   if chash.startswith('0000'):
	print(chash)
        print(cstr)
	found = True
