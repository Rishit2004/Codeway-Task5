import csv
import time

print("Initiallizing game....")

i=0

def loading_animation(duration):
    animation = "loading.."
    start_time = time.time()
    while time.time() - start_time < duration:
        for char in animation:
            print('\r' + char, end='', flush=True)
            time.sleep(0.1)

loading_animation(5)  # Display the loading animation for 5 seconds
print("\nLoading complete!")


while True:
    #Q1
    print("Q1.What is the fastest land animal? \n")
    print("(a)Cheetah (b)Giraffe (c)Tiger (d)Wolf\n")
    a=input("enter your choice:")
    print("Fectching answer...")
    time.sleep(1)
    if(a=="a" or a=="Cheetah"):
        i+=1
        print("You got it right\n")
        print("┌────────────────────┐")
        print("│                    │")
        print("│     Respect++      │")
        print("│                    │")
        print("└────────────────────┘")
    else:
        print("Oops wrong answer\n")
        print("The correct option was (a)Cheetah\n")

    #Q2
    print("Q2.Which of these is the fastest fish? \n")
    print("(a) Shark (b)Flying Fish (c)Tuna (d)Sailfish\n")
    b=input("enter your choice:")
    print("Fectching answer...")
    time.sleep(1)
    if(b=="d" or b=="Sailfish" or b=="sailfish"):
        i+=1
        print("You got it right\n")
        print("┌────────────────────┐")
        print("│                    │")
        print("│     Respect++      │")
        print("│                    │")
        print("└────────────────────┘")
    else:
        print("Oops wrong answer\n")
        print("The correct option was (d)Sailfish")

    #Q3
    print("Q3.What is the fastest bird? \n")
    print("(a)Peregrine Falcon (b)Hawk (c)Eagle (d)Stork\n")
    c=input("enter your choice:")

    print("Fectching answer...")
    time.sleep(1)
    if(c=="a" or c=="Peregrine Falcon" or c=="peregrine falcon"):
        i+=1
        print("You got it right\n")
        print("┌────────────────────┐")
        print("│                    │")
        print("│     Respect++      │")
        print("│                    │")
        print("└────────────────────┘")

    else:
        print("Oops wrong answer\n")
        print("The correct option was (a)peregrine")


    #Q4
    print("Q4.Which of these is the shortest time span? \n")
    print("(a)Century (b)A dozen years (c)Millennium (d)Decade\n")
    d=input("enter your choice:")
    print("Fectching answer...")
    time.sleep(1)
    if(d=="d" or d=="Decade" or d=="decade"):
        i+=1
        print("You got it right\n")
        print("┌────────────────────┐")
        print("│                    │")
        print("│     Respect++      │")
        print("│                    │")
        print("└────────────────────┘")
    else:
        print("Oops wrong answer\n")
        print("The correct option was (d)Decade")
        
    #Q5
    print("Q5.Which of these is the shortest measurement of length? \n")
    print("(a)Inch (b)Centimetre (c)Metre (d)Gramme\n")
    f=input("enter your choice:")
    print("Fectching answer...")
    time.sleep(1)
    
    if(f=="b" or f=="Centimetre" or f=="centimetre"):
        i+=1
        print("You got it right\n")
        print("┌────────────────────┐")
        print("│                    │")
        print("│     Respect++      │")
        print("│                    │")
        print("└────────────────────┘")
 
    else:
        print("Oops wrong answer\n")
        print("The correct option was (b)Centimetre")

    #Q6
    print("Q6. Which of these words best completes this sentence grammatically: He _______ dodged the speeding car. \n")
    print(" (a)neither of these (b)fastly (c)quickly (d)either of these\n")
    e=input("enter your choice:")
    print("Fectching answer...")
    time.sleep(1)
    if(e=="c" or e=="quickly" or e=="Quickly"):
        i+=1
        print("You got it right\n")
        print("┌────────────────────┐")
        print("│                    │")
        print("│     Respect++      │")
        print("│                    │")
        print("└────────────────────┘")

    else:
        print("Oops wrong answer\n")
        print("The correct option was (c)quickly")


    #Q7
    print("Q7.Which of these things most likely takes up the least time? \n")
    print(" (a)Reading a novel with at least 300 pages (b)Taking a shower (c)Driving from Los Angeles to New York (d)Watching a movie \n")
    g=input("enter your choice:")
    print("Fectching answer...")
    time.sleep(1)
    if(g=="b" or g=="Taking a shower" or g=="taking a shower"):
        i+=1
        print("You got it right\n")
        print("┌────────────────────┐")
        print("│                    │")
        print("│     Respect++      │")
        print("│                    │")
        print("└────────────────────┘")

    else:
        print("Oops wrong answer\n")
        print("The correct option was (b)Taking a shower")


    #Q8
    print("Q8.What is the shortest sentence in the English language? \n")
    print(" (a)Go! (b)A. (c)I am. (d)None of these\n")
    h=input("enter your choice:")
    print("Fectching answer...")
    time.sleep(1)
    if(h=="a" or h=="Go!" or h=="go!" or h=="go" or h=="GO"):
        i+=1
        print("You got it right\n")
        print("┌────────────────────┐")
        print("│                    │")
        print("│     Respect++      │")
        print("│                    │")
        print("└────────────────────┘")

    else:
        print("Oops wrong answer\n")
        print("The correct option was (a)Go!")

    #Q9
    print("Q9.The Central Rice Research Station is situated in? \n")
    print(" (a)Chennai (b)Cuttack (c)Bangalore (d)Quilon\n")
    j=input("enter your choice:")
    print("Fectching answer...")
    time.sleep(1)
    if(j=="b" or j=="Cuttack" or j=="cuttack"):
        i+=1
        print("You got it right\n")
        print("┌────────────────────┐")
        print("│                    │")
        print("│     Respect++      │")
        print("│                    │")
        print("└────────────────────┘")

    else:
        print("Oops wrong answer\n")
        print("The correct option was  (b)Cuttack!")

    #Q10
    print("Q10.Who among the following wrote Sanskrit grammar? \n")
    print("(a)Kalidasa (b)Charak (c)Panini (d)Aryabhatt\n")
    k=input("enter your choice:")
    print("Fectching answer...")
    time.sleep(1)
    if(k=="c" or k=="Panini" or k=="panini"):
        i+=1
        print("You got it right\n")
        print("┌────────────────────┐")
        print("│                    │")
        print("│     Respect++      │")
        print("│                    │")
        print("└────────────────────┘")

    else:
        print("Oops wrong answer\n")
        print("The correct option was  (c)Panini\n")
    print("XXXX END XXXX")
    print("Your final score is:",i)
    ch=input("Do you want to play again?(y/n):")
    if(ch=="y" or ch=="yes" or ch=="Y"):
        continue
    else:
        print("Exiting quizzz....")
        break

