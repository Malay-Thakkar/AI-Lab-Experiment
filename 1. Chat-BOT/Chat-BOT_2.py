print("1. Hello")
print("2. What is your name?")
print("3. How are you?")
print("4. How was your day?")
print("5. How are you doing?")
print("6. Nice to see you!")
print("7. Good Morning")
print("8. Good Afternoon")
print("9. Do aliens exist?")
print("10. do you have any pets?")
print("11. do you believe in ghosts?")
print("12. how much do you weigh?")
print("13. how old are you?")
print("14. what is your favorite color?")
print("15. Good night!")
print("16. who is your owner?")
print("17. what is your age?")
print("18. what do you like?")
print("19. Thank you!")
print("20. bye")


while(True):
    
    Q="";
    Q = input("Enter your question: ")
    Q = Q.lower()
    specific_char= ["?","!","@","#","$","%","&","^","-","_","=","+","  "]
    for i in specific_char:
        Q=Q.replace(i,"")
    print(Q)
   
    if Q in ["hello","hi","hey"]:
        print("Hello! How may i help you");
    elif(Q == "what is your name"):
        print("My name is Chat-bot. I like to help you!");
    elif(Q=="how are you"):
        print("I am Fine");
    elif(Q=="how was your day"):
        print("such a great day");
    elif(Q=="how are you doing"):
        print("I'm fine, thanks");
    elif(Q=="nice to see you"):
        print("It's a pleasure to meet you as well");
    elif(Q=="good morning"):
        print("Good Morning! have a grate day.");
    elif(Q=="good afternoon"):
        print("Good afternoon!");
    elif(Q=="do aliens exist"):
        print("No, I don't think so");
    elif(Q=="do you have any pets"):
        print("No, i don't have but i like pets");
    elif(Q=="do you believe in ghosts"):
        print("nNo, i don't belive in ghosts.");
    elif(Q=="how much do you weigh"):
        print("i am a program so i don't have any weight i have time and space complexity.");
    elif(Q=="how old are you"):
        print("sorry i don't have any idea for that");
    elif(Q=="what is your favorite color"):
        print("Blue");
    elif(Q=="good night"):
        print("Good night! sweet dream");
    elif(Q=="who is your owner"):
        print("Malay Thakkar");
    elif(Q=="what is your age"):
        print("sorry i don't have any idea for that");
    elif(Q=="what do you like"):
        print("I like answer to you!");
    elif(Q=="thank you"):
        print("welcome, visit again");
    elif Q in ["bye","quit","brack"]:
        print("bye")
        break;
    else:
        print("I don't understand! sorry!");