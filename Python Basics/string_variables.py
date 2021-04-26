
favBook = "My favorite book is Women Who Run With the Wolves \nby Clarissa Pinkola Estes."
print(favBook)


b = len(favBook)
print("\nThe length of the above string is {} characters.".format(b))



quote = """ \n\"It is worse to stay
    where one does not belong at all
    than to wander about lost for a while
    and looking for the psychic
    and soulful kinship one requires\"
    ― Clarissa Pinkola Estés\n """
print(quote)




goddesses = ("Aphrodite", "Athena", "Artemis", "Hera", "Persephone", "Demeter", "Hestia")
    
s = slice(3)

print(goddesses[s])

if "Hestia" in goddesses:
    print("\nSome may not be familiar with the Greek Goddesses Hestia, but she is very important among the other Goddesses.\n")




favGoddess = "    Aphrodite    "

x = favGoddess.strip()

print("\nMy favorite Greek Goddess is", x)


love = ("\nI love her soooo much!!").upper()
print(love)



goddessStr = "\nMy second favorite Greek Goddess is "

secondFav = "Persephone"

print(goddessStr + secondFav)

