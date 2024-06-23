""" Making Decisions """

# Exercise 31 (Study Question 2)- Making Decisions

print(
    """The Genetic and Biomech Olympic 100m race is about to start.
You need to make a decision on which augmentation you will choose.
Do you use:\n\t(1) - Genetically Enhanced Heamoglobin (GEH)
    \t(2) - Carbon struts (CS)
    \t(3) - Good old fashioned Cocaine (aka. Speed)??
    """
)

door = input("> ")

if door == "1":
    print(
        "Genetically Enhanced Heamoglobion (GEH) is highly volatile and Experimental."
    )
    print("How much do you administer?")
    print("(1) 250ml Take the cake.")
    print("(2) A full blood transfusion.")

    geh = input("> ")

    if geh == "1":
        print(
            "You decide to take a calculated risk. Your organism comes 3rd! Good job!"
        )
    elif geh == "2":
        print("We're not here to make friends. The first 30m is incredible, then")
        print(
            "the organism internally combusts. Spraying biological ooze everywhere. Good job!"
        )
    else:
        print(f"Well, doing {geh} is probably a bad idea.")
        print("You are disqualified.")

elif door == "2":
    print("The Carbon Struts(CS) provide high tensile strength and greater leverage.")
    print("(1) 2 metre carbon struts?")
    print("(2) 1 metre carbon struts?")

    cs = input("> ")

    if cs == "1":
        print(
            "The 2 Metre struts.... well you vault in two strides out of the field and are"
        )
        print("seen passing traffic down the highway 6 km away. Whoops :-/ ")
    elif cs == "2":
        print("The 1 Metre struts is an excellent choice! The slightly extra leverage")
        print("provides a balance of stride length and strength. You WON!!!!")
    else:
        print("This insanity is a very bad idea. You're disqualified.")
        print("Good job!")
else:
    print("You are an evil and diabolical scientist with not respect for the Olympics!")
    print("Good day to you sir/madam.")
