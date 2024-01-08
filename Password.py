class Password:
    def __init__(self,size):
        self.size = size
    
    def generate(self):
        import random
        import string
        chars = list(string.ascii_lowercase)

        password = ""
        i = 0
        while i<=self.size:
            index1 = random.randint(0,25)
            index2 = random.randint(0,25)
            index3 = random.randint(0,6)
            special_chars = ['!','@','#','$','%','&','*']
            random_characters = [chars[index1],chars[index2].upper(),str(random.randint(0,10)),special_chars[index3]]
            randomnum = random.randint(0,3)
            password += random_characters[randomnum]
            i = i+1
        print(f"Random Password is: {password}")

password_size = int(input("Enter the length of the password that you want: "))
p1 = Password(password_size)
p1.generate()




