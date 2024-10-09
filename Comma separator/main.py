text = input("Text: ")

subjects = text.split(",")
for subject in subjects:
    if "French" in subject:
        print(subject.strip() + " - Grade 8")
    else:
        print(subject.strip() + " - Grade 9")




