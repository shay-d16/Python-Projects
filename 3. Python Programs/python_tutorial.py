
def start():
    f_name = "Shay"
    l_name = "Davis"
    age = 26
    gender = "Female"
    get_info(f_name,l_name,age,gender)

def get_info(f_name,l_name,age,gender):
    print("My name is {} {}. I am a {} year-old {}.".format(f_name,l_name,age,gender))




if __name__ == "__main__":
    start()
