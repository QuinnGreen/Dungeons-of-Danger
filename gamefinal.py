# Final_Program.py
import random
random.randint(1,2)
fire_spell = "ignis"
retreat = "escape"
cutting_spell = "sacare"
poison_spell = "plaga"
holy_spell = "sanctus"
count = 0
count1 = 30
count2 = 0
count3 = 120
count4 = 20
target = 4
print("""

╭━━━╮╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╭━╮╭━━━╮
╰╮╭╮┃╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱┃╭╯╰╮╭╮┃
╱┃┃┃┣╮╭┳━╮╭━━┳━━┳━━┳━╮╭━━╮╭━━┳╯╰╮╱┃┃┃┣━━┳━╮╭━━┳━━┳━╮
╱┃┃┃┃┃┃┃╭╮┫╭╮┃┃━┫╭╮┃╭╮┫━━┫┃╭╮┣╮╭╯╱┃┃┃┃╭╮┃╭╮┫╭╮┃┃━┫╭╯
╭╯╰╯┃╰╯┃┃┃┃╰╯┃┃━┫╰╯┃┃┃┣━━┃┃╰╯┃┃┃╱╭╯╰╯┃╭╮┃┃┃┃╰╯┃┃━┫┃
╰━━━┻━━┻╯╰┻━╮┣━━┻━━┻╯╰┻━━╯╰━━╯╰╯╱╰━━━┻╯╰┻╯╰┻━╮┣━━┻╯
╱╱╱╱╱╱╱╱╱╱╭━╯┃╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╭━╯┃
╱╱╱╱╱╱╱╱╱╱╰━━╯╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╰━━╯
    
    Welcome to the Dungeons of Danger, a text based adventure game made by Michael Bishop, Nathaniel Edwards, Pedro Osagiede, Olaolu Ladipo and Quinn Greenwood. 
      
    You are a wizard, a graduate of the most prestigious University in all of the lands. You are serching for the Staff of Power, said to belong to the Grand Warlock Ineritus. an item which makes all dreams come true.
      
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣠⣤⣤⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣶⠟⠛⠉⠉⠉⠛⠻⢿⣶⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡿⠁⠀⠀⠀⠀⠀⠀⠀⠀⣍⠻⢿⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢧⣄⠛⢿⣶⣄⣠⡾⣧⡀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣿⣷⣦⡉⠻⣫⣾⡽⣷⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠇⠀⠀⣀⣀⡀⠀⠀⠀⠀⣀⣀⡀⠀⠸⣿⠻⣿⣾⡿⠃⠹⣿⣷⡀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⣿⠟⠛⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⠻⣿⣇⠀⠉⠀⠀⠀⠈⠛⠛⠒⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⠃⢀⣀⣠⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣀⡀⠘⣿⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣴⣶⡿⠿⠟⠋⠉⠉⠁⠀⠀⠀⠀⠀⠀⠀⠈⠉⠉⠙⠛⠿⢿⣶⣦⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢀⣠⣴⣾⠿⠛⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⠿⣷⣦⣄⡀⠀⠀⠀⠀
⠀⣀⣴⣾⣿⣛⣁⣤⣤⣀⣀⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⣀⣀⣠⣤⣌⣛⣿⣷⣦⣀⠀
⣼⡿⣿⣿⣿⣿⣿⣿⠋⠉⢹⡿⠻⣿⣿⡶⠒⠒⠲⣶⣶⣶⣶⣶⣶⡶⠖⠒⠲⢾⣿⣿⠟⢿⡏⠉⠙⣿⣿⣿⣿⣿⣿⢿⣷
⢹⣷⡙⢿⣿⣿⠾⠍⠁⠀⣾⠇⠀⢻⠀⢈⣻⣷⣶⣤⣤⡽⠟⢯⣤⣤⣴⣾⣿⡁⠀⡟⠀⠘⣷⠀⠈⠩⠷⣿⣿⡿⢋⣾⡟
⠀⠙⢿⣶⣭⣛⡿⠷⠤⣼⠏⢠⢶⣾⠀⠀⠙⠓⢦⣼⣿⡇⠀⢸⣿⣧⣴⠟⠋⠀⠀⣿⡄⡄⠹⣧⠤⠾⠿⣛⣭⣴⡿⠋⠀
⠀⠀⠀⠈⠛⠻⠿⣷⣶⠟⢰⡏⢸⣇⠀⠀⠀⠈⠉⢉⣹⠇⠀⠘⣏⡉⠉⠁⠀⠀⠀⢸⡇⢹⡆⠻⣶⣾⠿⠟⠛⠉⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢠⡏⢠⡟⠀⣼⣿⣄⠀⠀⠀⡼⠋⠻⠀⠀⠀⠾⠉⢳⡀⠀⠀⣠⣿⣷⠀⢹⡄⢹⣆⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢀⣟⣠⡿⢀⣼⡇⢹⣝⡷⣤⣼⣳⠴⠛⠳⠤⠔⠛⠦⣞⣷⣤⢴⣫⡟⠸⣷⡀⢿⣄⣻⡀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠸⢋⣿⠁⣼⢹⣆⠀⠉⠛⠛⠉⠁⠀⠀⣀⣿⣄⠀⠀⠀⠉⠛⠛⠉⠀⢠⡏⢧⠀⢿⡝⠇⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣼⡇⣰⠃⠈⢿⣦⣄⣀⣀⣀⣤⡴⠞⠋⠉⠉⠳⢦⣤⣀⣀⣀⣠⣴⡿⠁⠘⣦⢸⣷⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢿⣿⡏⢠⠄⢸⣧⠉⠉⢻⣀⣠⡶⠞⠛⠉⠛⠳⢶⣤⣀⡟⠉⠉⢸⡇⠀⡄⢹⡿⠟⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢸⣡⡏⠀⡄⢿⡀⠀⠀⠛⠉⠀⠀⠀⠀⠀⠀⠀⠉⠛⠁⠀⢀⡿⢡⡀⢹⣬⡇⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠸⡿⣇⢸⣿⢸⣷⣼⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣧⣾⡇⣼⣧⣸⢻⡇⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣿⠹⣿⡏⡿⣧⣤⠀⠀⠀⠀⠀⠀⠀⠀⠀⣤⣾⣿⠻⣿⠏⢿⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠀⠀⠁⠀⠻⣿⣦⣾⠀⠀⠀⠀⠀⣶⣤⡟⠟⠀⠀⠀⠀⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⢻⣧⡀⠀⠀⣼⡿⡿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢷⣦⡾⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    Your quest has taken you all over the world, but now you near its end... 
      
    You stand at the edge of a mighty jungle. 
      """)

in_put = input("for more info, including the spells you can use and how you use them: type 'info', otherwise type 'next' ")

if in_put == "info":

    print("""

    you are a wizard, your name and details have been lost to time, but what the scholars do know is that you were a spellcasting prodigy,

    Many aspiring mages hope to master maybe two schools of magic and dabble in a third.

    You have mastered four.

           
    When asked 'What do you do?' you can cast spells by typing in the correct word, the word is always lower case, without any other characters like quotation marks. Be careful of spaces!
          

    The types of magic you can use are:


    Fire Magic: cast by typing 'ignis'
   
    Air Magic: cast by typing 'sacare'

    Poison Magic: cast by typing 'plaga'

    Divine Magic: cast by typing 'sanctus'  

    Retreat: while not a spell, you can run or avoid obstacles by typing 'escape'

   

    You may wish to make a note of these.
          

    """)

while count <4:
    if random.randint(1,2) == 1:
        if random.randint(1,2) == 1:
            in_put = input("Continue? y/n ")
            if in_put == "y":
                print("""
                As you walk through the oppressive heat of the jungle, spiky plants clutch at your hair and clothes. 
                  
                You suddenly break through into a clearing, a mighty fallen tree giving you a glimpse of a stark blue sky devoid of clouds.
                  
                You breath easier for a second, free of the muggy humidity of the forest floor.
                   
                It is then at once you notice a hushing of the general hubbub of the forest, no bird calls, no frog croaks or small mammal rustling.
                  
                With a flash of orange and a roar that chills your blood, a tiger bursts from the undergrowth, you have mere seconds before it is upon you.
                
                """)
            if in_put != "y":
                print("You leave and go home")
                exit()
            count += 1
            in_put = input("What do you want to do? ")
            if in_put == fire_spell:
                print("""
                The tiger flinches as the bolt of fire erupts from your hand, it tries to adjust course but the flame catches on its coat, igniting it. 
                
                Sending the creature yowling back into the jungle.
                
                """)
                if random.randint(1,10) == 1:
                    print("""
                          Growing on the rotten tree trunk you see some bright red mushrooms, known for their healing properties, add 5 health.
                          """)
                    count1 += 5
                else:
                    print("\nYou continue on your journey.")
            else:
                print("\n       The Tiger launches over you, its claws drawing bloody lines on your back. \nYou have lost 12 Health.")
                count1 -= 12
                if count1 > 0:
                    print(f"\nYou have {count1} health remaining.")
                if count1 == 0 or count1 < 0:
                    print("\nYou have died.")
                    exit()
                    
        else:
            in_put = input("Continue? y/n ")
            if in_put == "y":
                print("""
                You encounter a rocky cliff face, its surface slick with water and encumbered by moss, you stare upwards and spot a thick tree branch over hanging the cliff. 
                
                The remnants of rope you see up there indicating that this path has been used previously, but not in many years. 
                  
                You throw your rope and after a few tries you manage to get it over, securing it you start to abseil up. 
                
                Reaching the top, sweating and puffing, you take a minute to catch your breath, as you recover you are forced to jump backwards as a coal-black snake strikes at you from the tree.
                
                """)
            if in_put != "y":
                print("You leave and go home")
                exit()    
            count += 1
            if input("What do you want to do? ") == retreat:
                print("\n       You dodge left and sprint into the cover of the jungle, the snake hissing with displeasure at its lost meal. \n\n       You have escaped the Black Mamba.")
                if random.randint(1,10) == 1:
                    print("\nYou spot a small green frog that almost glows with life energy, you grind it up with herbs. \nAdd 5 health.")
                    count1 += 5
                else:
                    print("\nYou continue on your journey.")
            else:
                print("\n    Your spell misses the small target and the Black Mambas fangs sink with sickening ease into your shoulder. \n    While you are able to heal yourself of the poison, you have lost 9 Health")
                count1 -= 9
                if count1 > 0:
                    print(f"\nYou have {count1} health remaining.")
                if count1 == 0 or count1 < 0:
                    print("\nYou have died.")
                    exit()   
    else:
        
        if random.randint(1,2) == 1:
            in_put = input("Continue? y/n ")
            if in_put == "y": 
                print("""
                As you continue, beating back the bush along the ancient path, you are stuck by thirst. 
                  
                Finding your own water-skins to be empty, you start to search for a stream, spying an animal trail (and knowing these often lead to water) you decide to follow it. 
                  
                Ducking your head and weaving through the undergrowth you suddenly trip, something catching your ankle. You flail your hands out and catch a handful of vines, avoiding the fall. 
                
                You are now held suspended over a pit, only the slowly breaking lianas held in your hand impeding your fall into what you realise is a pit trap. 
                  
                It looks old, the points broken or rotted but still enough to end your journey.
                  
                """) 
                
            if in_put != "y":
                print("You leave and go home")
                exit()
            count += 1
            if input("What do you want to do? ") == cutting_spell:
                print("\n       Your spell scatters the spikes, providing you with a safe landing.")
                if random.randint(1,10) == 1:
                    print("\n       You spot a skeleton impaled on one of the spikes, in the decayed ruins of its bag You find a only slighty out of date healing potion. \n\n    Add 5 health.")
                    count1 += 5
                else:
                        print("\nYou continue on your journey.")
            else:
                print("\n       The lianas finally give way, Despite your efforts you fall headfirst into the pit, a sliver of wood sunk deep into your thigh. \nyou have lost 7 Health")
                count1 -= 7
                if count1 > 0:
                    print(f"\nYou have {count1} health remaining")
                if count1 == 0 or count1 < 0:
                    print("\nYou have died.")
                    exit()
        else:
            in_put = input("Continue? y/n ")
            if in_put == "y":
                print("""
                As you trek through the forest you notice you are not alone in your voyage. 
                  
                Beside your path you notice a thin, unbroken line of ants 
                  
                Their slim silver bodies carrying disproportionately large loads of leaves and other plant parts in a show of strength and efficiency. 
                  
                So enamoured are you with the little creatures, you forget to watch your step, then *crunch!* your foot buries itself deep into the anthill 
                  
                The serene atmosphere vanishes as the ants swarm up your leg, their mandibles clattering into aggressive buzzing.
                  
                """)
            if in_put != "y":
                    print("You leave and go home")
                    exit()
            count += 1
            if input("What do you want to do? ") == poison_spell:
                print("\n       You watch with a tinge of sadness as the poison spreads out in a wave, the ants writing in pain as the spell relentlessly advances, eventually wiping out the whole colony.")
                if random.randint(1,10) == 1:
                    print("\nYou spot a small bush of golden berries, their flesh is tart but bolstering. Add 5 health")
                    count1 += 5
                else:
                    print("\nYou continue on your journey.")
            else:
                print("\nYou flee away from the hill, frantically brushing away the stinging ants, you escape but your legs are swollen and oozing. \nYou have lost 10 Health>")
                count1 -= 10
                if count1 > 0:
                    print(f"\nYou have {count1} health remaining")
                if count1 == 0 or count1 < 0:
                    print("\nYou have died.")
                    exit()    
                else:
                    print("\nYou continue on your journey.")
if count1 == 0 or count1 < 0:
    print("\nYou have died")
else:
    in_put = input("Continue? y/n ")
    if in_put == "y":
        print("""
            Just as you think the jungle would go on forever, you hack through one final thorny bush and your machete meets ancient stone.
           
            Pulling back the vegetation, you discover a wall of worked stone. 
          
            Cleaning off the growth, you notice the arcane sigils of the Lich and you know you have found the place that you seek. 
          
            Clearing away more vegetation, you uncover a stone door. 
              
            Pulling with all your might, the door gives way, opening wide.
           
            A gust of foul smelling air rushes out to greet you. You detect hints of graveyard, with a solid helping of rotten seaweed.
        
        """)
    if in_put != "y":
            print("You leave and go home")
            exit()

print("""
      
        You walk down the steps, your footfalls sinking deep into the dust of ages, no-one has used these steps in an age. 
      
        Casting a small light spell you summon an orb of white light that playfully orbits your head, revealing an elaborately carved chamber. 
      
      
        Two elegant statues lounge playfully on stone couches in the spaces between 3 doors, the door on the right is set apart from the others. 
      
        It is taller, wider and gothic, framed by bones, in place of a knocker there is a human skull, partially embedded in the stone. 
      
        In one of the eye sockets a a dark purple umbral gem glows darkly, the other is empty.
      
      
        The 2 other doors are identical to each other, masterfully carved creations of stone inlaid with gold. 
      
        As you examine the doors the statues move with a grinding sound, you notice the stone melting into flesh as they look to you, their faces splitting into wide, wicked grins, you notice the sharp incisor fangs, Vampires! 
      
        You hurriedly back up and prepare to defend yourself, but after a long moment, instead of leaping, they settle back on their seats and say together, 
      

        "There are 3 doors here, one leads to your goal, (indicating the skull door) but the key to that door is behind one of the others, but beware, one of the doors leads to instant doom"

        Another voice, a booming rattle that you can feel in your bones which seems to come from the walls themselves cuts over
      

        "You may ask a single yes or no question, and both will answer it, but know that one can only lie, whereas the other speaks the truth, fail and they will kill you"
""")
in_put = input("""
        Select a question to ask. 
        
        1. You ask the vampires "Would the other vampire tell me that your door leads to the key?"

        2.  You ask the vampires "is the left door is the correct one?"
               
	3.  You ask the vampires "Which of you is the liar?"
               
        4.  You ask the vampires "would the other vampire lie to me?"  
               
    (1/2/3/4)
                """)
if in_put == "1":
        print("""
            The vampires look crestfallen as they reply, the left vampire says, 

            "The right vampire would say the right door is correct." 

            The right vampire says
  
            "The left vampire would say the right door is correct."

            Using logic you realise that the opposite of these statements is the truth, you set your mind to open the left door,
              
            as you do, the vampire on the left hands you an elaboratly carved enchanted mask, its visage that of some aquatic monstrosity.
        """)
if in_put != "1":
        print("""
            The vampires look at each other with widening grins, they face you and say together in a mocking tone,

            "That's not the right question."

            In a flash they launch themselves towards you, claws extended.
            """)
        in_put = input("what do you want to do? ")
        if in_put == fire_spell:
            print("\n    You summon a roaring torrent of flame, engulfing the vampires, when the smoke clears, all that is left is scorched rubble.\n\n    Amongst the rubble you spot an elaborately carved enchanted mask, its visage that of some aquatic monstrosity.")
        if in_put != fire_spell:
               print("\n   Your spell blasts one of the vampires, but the second evades and rushes towards you, sinking its teeth into your neck, draining your blood. \n\n2   You try to cast, but with your lifeforce fading the spell sputters out, and you follow shortly after. \n\n   You have died.  ")
               exit()
print("""
      
        You open the left door, revealing a wall of clear water, improbably suspended in the door frame, you place the mask over your face and enter the water

""")
while count2 <4:
    if random.randint(1,2) == 1:
        count3 -= 10
        if random.randint(1,2) == 1:
            in_put = input("Continue? y/n ")
            if in_put == "y":
                print("""
                You swim through the dark, murky water, your only light the brave little orb you cast earlier, causing a slow strobe effect.
                 
                You feel the water become colder as you continue, then you notice a small graceful form swimming fast towards you. 
                
                After a moments thought you recognise the creature from your long past zoology lectures, what in all the hells is a penguin doing here? 
                  
                As you examine the small creature during its graceful loops and twists you realise the creature looks unwell. 
                  
                Its hide is patchy, its eyes milky white and its limbs are twisted and skeletal. 
                
                Then it bites you sharply in the arm, easily tearing through your robe, your skin and the muscle beneath. 
                  
                This is no ordinary bird you think, just as the rest of the colony rounds the corner, churning the water into a frenzy as they speed towards you.
                  """)
            count2 += 1
            if in_put != "y":
                print("You leave and go home")
                exit()
            if input("What do you want to do? ") == holy_spell:
                print("\n       With a quick prayer you call upon divine force, the penguins shriek as the golden light you summon unstiches them leaving no remains.")
                if random.randint(1,10) == 1:
                    print("/n   You have found a pocket of air add 5 miniutes of air")
                    count3 += 5
                else:
                    print("\nYou continue on your journey.")
            else:
                print("Due to the undead penguins' attacks you have lost 7 miniutes of air")
                count3 -= 7
                if count3 > 0:
                    print(f"You have {count3} miniutes of air left")
        else:
            in_put = input("Continue? y/n ")
            if in_put == "y":
                print("""
                You swim further and leave the tight corridor into an open area, the water is clearer here but not by much, enough to notice a light overhead. 
                
                From the furniture remnants you figure this must have been a dining room of some kind.
                  
                You swim out into the open and see on the far side of this open chamber an open doorway, its stone door broken and in pieces around the frame.
                
                You head towards it, as you do so a shadow passes over you and you look up instinctively, straight into the dead eyes of a shark. 
                  
                It watches you hungrily for a second before snapping into action, racing towards you. 
                  
                As it nears you see the eyes roll back in its head, preparing for its strike.
                """)
            count2 += 1
            if input("What do you want to do? ") == fire_spell:
                print("\n   You strike out with fire, sending a missile of hissing spitting water, you boil the shark in its own skin.")
                if random.randint(1,10) == 1:
                    print("\n   You have found a pocket of air add 5 miniutes of air.")
                    count3 += 5
                else:
                    print("\nYou continue on your journey.")
            else:
                print("\n   The shark hits you hard in the shoulder, knocking the mask off in a spray of bubbles, \n\nyou grab it and fix it back on your face but you have lost 10 minutes of air.")
                count3 -= 10
                if count3 > 0:
                    print(f"\n  You have {count3} miniutes of air left.")
    else:
        count3 -= 10
        if random.randint(1,2) == 1:
            in_put = input("Continue? y/n ")
            if in_put == "y":
                print("""
                Looming shapes fill the passage, in the light of the spell you see spiky looking balls, cloaked in vegetation and floating, chained to brackets on the wall. 
                
                You've seen these sea mines before, but never ones so ancient in design. 
                  
                You don't know if they are still functional, but if so, you know that one errant jostle will set them off and probably kill everything within a large radius.
                  
                """)
            count2 += 1
            if input("What do you want to do? ") == retreat:
                print("\n   Careful not to disturb any of the mines you swim back and take a different route.")
                if random.randint(1,10) == 1:
                    print("You have found a pocket of air add 5 miniutes of air.")
                    count3 += 5
                else:
                    print("\nYou continue on your journey.")
            else:
                print("\n   Your spell goes off and you hear a dread ticking as the mines start their countdown, you swim away with all your speed as the mines detonate.\n\nWhile you are not hurt you have wasted 5 minutes of air.")
                count3 -= 5
                if count3 > 0:
                    print(f"\nYou have {count3} miniutes of air left.")
        else:
            in_put = input("Continue? y/n ")
            if in_put == "y":
                print("""
                You swim further down the twisting shadowed corridors until you come upon what seems to be a dead end, 
                  
                However further investigation reveals that a dense mass of underwater plants and vines has grown, almost fully blocking your path, 
                  
                You spot a gap and begin working the plants out of the way, you do not notice the plants growing around your legs till you try to move. 
      
                Feeling the tight grasp and a stab of pain from the thorny weeds. 
                  
                You notice them growing quickly, if you don't act now you are sunk.
                  
                """)
            count2 += 1
            if input("What do you want to do? ") == cutting_spell:
                print("\n   Your spell slices out with precision and speed, cleaving through the underwater plants like a surgeons scalpel.")
                if random.randint(1,10) == 1:
                    print("\n   You have found a pocket of air add 5 miniutes of air.")
                    count3 += 5
                else:
                    print("\nYou continue on your journey.")
            else:
                print("\n   Your action is ineffective, and causes you to drift into the plants, entagling you, you wriggle free but lose 3 minutes of air.")
                count3 -= 3
                if count3 > 0:
                    print(f"You have {count3} miniutes of air left.")
if count3 == 0:
    print(f"You have died.")
else:
    count3 -= 10
    in_put = input("Continue? y/n ")
    if in_put == "y":
        print("""
    You come to a great door, wide enough for 20 people to walk side by side, barred by what must have been a whole tree. 
          
    You know no spell that would be effective verses an object that size, so you search for an alternative.
    
    After a few minutes you find the outline of a smaller wicket gate, set into the grand door, 
          
    a few minutes of scraping and pulling and you manage to open it enough to slip through. 
          
    You enter what must have once been an ornate throne room before the flooding and muddying, 
          
    schools of plump silver fish flit in and around the soiled dais.
           
          
    As you explore, a presence, no, *two* presences assault your mind and you hear their deep reverberating voices in your head,
          
    “Oh what a pretty little shiny thing you are, sun ripened.”
          
    The other voice, darker and more cruel echoes.
          
    “Sun ripened, fresh and wriggling.”
          
    “Sweet and tasty.” the first agrees.
          
    “But not enough for both of us.” the second interjects.
          
    “And we are soooo hungry.” they chorus.
              
          
    At this point you see the origins of the voices, two huge aquatic forms, 
    
    their bodies like the great leviathans of the sea, but twisted by some foul sorcery, their craniums bulging and transparent, 
          
    their teeth are so long they couldn't possibly close their elongated jaws, 
              
    they loom impossibly large over you. 
              
          
    You think feverishly, your spells could probably deal with one, but a second monster? then you have an idea.
          
    “What about the fish? why don't you eat those?” you think to the abyssal monstrosities.
          
    “Too small.” the first one replies haughtily.
          
    “Too slidey and slippery.” the colder second voice agrees.
          
    “But not too small for me.” you respond “if I can feed you will you let me pass?”
          
    For a painfully long moment, the leviathans consider, you see dark energy rippling over their cortexes as they think. 
          
    With your heart pounding you hear both voices reply,
          
    “We agree, though if we are not satisfied soon, we will take the remainder from your flesh.”
""")

fish_count = 0
fish_reward = 0
max_fish = range(20)
keyword = "fish"
intro = ["\nThe Orcas Watch hungrily as you prepare to chase the fish.", "\nDon't underestimate them. These are very large creatures and they look hungry.", "\nCatch as many fish as you can to stop them from killing you.", "\nYou need to be quick.", "\nThe faster you work, the more air you'll have remaining.\n"]
result = ["\n You didn't catch enough fish, with a swift motion, they launch at you tearing you into chum.", "\nYou caught enough fish and you are safe from the orcas...\n\nFor now! You quickly exit. \n\n You still have plenty of air left.", "\n\nYou caught enough fish and you are safe from the orcas...\nfor quite a while, good job!\n\n You quickly exit, you still have plenty of air left.", "\n\nYou caught all the fish, great job! The orcas magic renews your mask."]

# print("Location - Cape Town. Reports vary but Up to 20 shark carcasses washed up on a beach.\nSharks the predators have now become the prey!")
scene_continue = input("Continue? y/n ")
# print("\nThe sharks were found with their livers missing!\nThe rest of their organs intact and a clean tear in their shoulders.\nRemoved with near surgical precision!\n\nWhat could this be! *thinking*")
# scene_continue = input("Press any button to continue...")
# print("\nMeet Port & Starboard the Orcas!")

import time

time.sleep(2)
print(intro[0])
time.sleep(2)
print(intro[1])
time.sleep(2)
print(intro[2])
time.sleep(2)
print(intro[3])
time.sleep(2)
print(intro[4])
scene_continue = input("Continue? y/n ")



def catch_fish(fish_count,max_fish):
    for n in max_fish:
            is_fish = input("Catch the fish by typing fish + [ENT] ")
            if is_fish == "fish":
                fish_count += 1
                print("You caught", fish_count, "fish.")
            else:
                break
    def fish_result():
        x = fish_count
        return x
    fish_result()
    y = fish_result()
    if y <=5:
         print("\n You didn't catch enough fish, with a swift motion, they launch at you tearing you into chum.")
         exit()
    if y > 5 and y <= 10:
        print(result[1])
    if y > 10 and y <= 15:
        print(result[2])
    if y > 15 and y <= 20:
        print(result[3])
catch_fish(fish_count,max_fish)

print("\n    The orcas, full from their feast, drift lazily half in slumber. \n    Carefully, as to not to disturb them, you swim past and fit yourself through the slightly open double doors past the rotten throne, its gold leaf peeling and sparkling in the water.")


target = 8

while count2 <8:
    if random.randint(1,2) == 1:
        count3 -= 10
        if random.randint(1,2) == 1:
            in_put = input("Continue? y/n ")
            if in_put == "y":
                print("""
                You swim through the dark, murky water, your only light the brave little orb you cast earlier, causing a slow strobe effect.
                 
                You feel the water become colder as you continue, then you notice a small graceful form swimming fast towards you. 
                
                After a moments thought you recognise the creature from your long past zoology lectures, what in all the hells is a penguin doing here? 
                  
                As you examine the small creature during its graceful loops and twists you realise the creature looks unwell. 
                  
                Its hide is patchy, its eyes milky white and its limbs are twisted and skeletal. 
                
                Then it bites you sharply in the arm, easily tearing through your robe, your skin and the muscle beneath. 
                  
                This is no ordinary bird you think, just as the rest of the colony rounds the corner, churning the water into a frenzy as they speed towards you.
                  """)
            count2 += 1
            if in_put != "y":
                print("You leave and go home.")
                exit()
            if input("What do you want to do? ") == holy_spell:
                print("\n       With a quick prayer you call upon divine force, the penguins shriek as the golden light you summon unstiches them leaving no remains.")
                if random.randint(1,10) == 1:
                    print("/n   You have found a pocket of air add 5 miniutes of air.")
                    count3 += 5
                else:
                    print("\nYou continue on your journey.")
            else:
                print("Due to the undead penguins' attacks you have lost 7 miniutes of air.")
                count3 -= 7
                if count3 > 0:
                    print(f"You have {count3} miniutes of air left.")
        else:
            in_put = input("Continue? y/n ")
            if in_put == "y":
                print("""
                You swim further and leave the tight corridor into an open area, the water is clearer here but not by much, enough to notice a light overhead. 
                
                From the furniture remnants you figure this must have been a dining room of some kind.
                  
                You swim out into the open and see on the far side of this open chamber an open doorway, its stone door broken and in pieces around the frame.
                
                You head towards it, as you do so a shadow passes over you and you look up instinctively, straight into the dead eyes of a shark. 
                  
                It watches you hungrily for a second before snapping into action, racing towards you. 
                  
                As it nears you see the eyes roll back in its head, preparing for its strike.
                """)
            count2 += 1
            if input("What do you want to do? ") == fire_spell:
                print("\n   You strike out with fire, sending a missile of hissing spitting water you boil the shark in its own skin.")
                if random.randint(1,10) == 1:
                    print("\n   You have found a pocket of air add 5 miniutes of air.")
                    count3 += 5
                else:
                    print("\nYou continue on your journey.")
            else:
                print("\n   The shark hits you hard in the shoulder, knocking the mask off in a spray of bubbles. \n\nYou grab it and fix it back on your face but you have lost 10 minutes of air.")
                count3 -= 10
                if count3 > 0:
                    print(f"\n  You have {count3} miniutes of air left.")
    else:
        count3 -= 10
        if random.randint(1,2) == 1:
            in_put = input("Continue? y/n ")
            if in_put == "y":
                print("""
                Looming shapes fill the passage, in the light of the spell you see spiky looking balls, cloaked in vegetation and floating, chained to brackets on the wall. 
                
                You've seen these sea mines before, but never ones so ancient in design. 
                  
                You don't know if they are still functional, but if so, you know that one errant jostle will set them off and probably kill everything within a large radius.
                  
                """)
            count2 += 1
            if input("What do you want to do? ") == retreat:
                print("\n   Careful not to disturb any of the mines you swim back and take a different route.")
                if random.randint(1,10) == 1:
                    print("You have found a pocket of air add 5 miniutes of air.")
                    count3 += 5
                else:
                    print("\nYou continue on your journey.")
            else:
                print("\n   Your spell goes off and you hear a dread ticking as the mines start their countdown, you swim away with all your speed as the mines detonate.\n\nWhile you are not hurt you have wasted 5 minutes of air.")
                count3 -= 5
                if count3 > 0:
                    print(f"\nYou have {count3} miniutes of air left.")
        else:
            in_put = input("Continue? y/n ")
            if in_put == "y":
                print("""
                You swim further down the twisting shadowed corridors until you come upon what seems to be a dead end, 
                  
                However further investigation reveals that a dense mass of underwater plants and vines has grown, almost fully blocking your path, 
                  
                You spot a gap and begin working the plants out of the way, you do not notice the plants growing around your legs till you try to move. 
      
                Feeling the tight grasp and a stab of pain from the thorny weeds. 
                  
                You notice them growing quickly, if you don't act now you are sunk.
                  
                """)
            count2 += 1
            if input("What do you want to do? ") == cutting_spell:
                print("\n   Your spell slices out with precision and speed, cleaving through the underwater plants like a surgeons scalpel.")
                if random.randint(1,10) == 1:
                    print("\n   You have found a pocket of air add 5 miniutes of air.")
                    count3 += 5
                else:
                    print("\nYou continue on your journey.")
            else:
                print("\n   Your action is ineffective, and causes you to drift into the plants, entagling you, you wriggle free but lose 3 minutes of air.")
                count3 -= 3
                if count3 > 0:
                    print(f"You have {count3} miniutes of air left.")
if count3 == 0:
    print(f"You have died.")
else:
    count3 -= 10
    in_put = input("Continue? y/n ")
    if in_put == "y":
        print("""
        The corridor past the throne room curves upwards, the now slimy stairs made useless by the water. 
        
        At the top, you notice the passageway half blocked by some obstacle of hard, smooth material, free from any vegetation. 
              
        You squeeze through and looking up once more and instead of more flooded stone roof, you see the rippling surface, ‘fresh’ air! 
              
        You swiftly ascend and slip off the mask.
              
              
        You manage to take a few great lungfuls of air before something powerful wraps itself around your waist and sharply yanks you downwards. 
              
        You almost lose hold of the mask as you plummet downwards, bubbles streaming from you as the shock robs you of your hard fought breath. 
              
        Somehow you keep hold of the mask and fit it over your face. 

        As the tentacle pulls you further down, towards the murky depths you see the shape of a great beast. 
              
        A truly massive, dire looking octopus, crouched over and around a pedestal, a darkly glowing gem winking. 
              
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⣀⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣶⣿⣿⣿⣿⣿⣿⣿⣿⣷⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⠀⠀⠀⢠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢠⣾⡿⠿⢿⣿⣷⣠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡆⣷⣠⣴⣶⣶⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠻⢿⡄⠀⠀⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⣿⣿⣟⠉⢹⣿⣷⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠛⠿⠿⠿⠋⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣾⣿⡿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠉⣿⣿⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⢀⣀⣀⠀⠀⠀⠀⠀⣰⣿⣿⡟⠁⠘⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠃⠀⠈⢿⣿⣷⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⣴⣾⣿⣿⣿⣿⣶⡀⢀⣾⣿⣿⠋⠀⠀⠀⠈⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠃⠀⠀⠀⠀⠹⣿⣿⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀
⢸⣿⡁⠀⠀⢀⣿⣿⢇⣾⣿⣿⠃⠀⠀⠀⠀⠀⠀⣿⡈⠙⢿⣿⣿⣿⠿⠋⢩⡇⠀⠀⠀⠀⠀⠀⠙⣿⣿⣇⠀⠀⠀⠀⠀⠀⠀⠀
⠈⠛⠛⣠⣴⣿⡿⠋⢸⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⣿⣿⣶⣾⣿⣿⣿⣷⣶⣿⡇⠀⠀⠀⠀⠀⠀⠀⣻⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀
⠀⣠⣾⣿⡿⠋⠀⠀⢻⣿⣿⣷⡀⠀⠀⠀⠀⣠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⡀⠀⠀⠀⠀⢠⣿⣿⣏⣠⣤⣶⣤⠀⠀⠀⠀
⢰⣿⣿⣟⠀⠀⠀⠀⠘⢿⣿⣿⣿⣷⣶⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣤⣤⣴⣿⣿⣿⣿⠋⠀⠀⠀⠀⠀⠀⠀
⢸⣿⣿⣿⣦⣄⣀⠀⠀⠀⠉⠙⠛⠛⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⠛⠉⢻⣿⣄⠀⠀⠀⠀⠀⠀⠀
⠀⠙⠿⣿⣿⣿⣿⣿⣿⣿⣶⣶⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⡀⠀⠀⠀⠈⢿⣿⣶⣄⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠈⠉⠉⠙⠛⠛⠛⠛⠛⣿⣿⣿⣿⠟⢋⣿⣿⣿⡿⠋⠙⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣆⠀⠀⠀⠀⠙⢿⣿⣧⡀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣾⣿⣿⠟⠁⠀⣿⣿⣿⠟⠀⠀⢀⣿⣿⣿⡿⢿⣿⣿⣿⣿⣿⣿⣆⠀⠀⠀⠀⠈⢿⣿⣷⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⣿⣿⠏⠀⠀⢸⣿⣿⣿⠀⠀⠀⢸⣿⣿⣿⠀⠈⢻⣿⣿⣿⢿⣿⣿⣦⡀⠀⠀⠀⣸⣿⣿⠀⣀⡄
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⣿⣿⡟⠀⠀⠀⠸⣿⣿⣿⠀⠀⠀⢻⣿⣿⣿⠀⠀⠀⢻⣿⣿⡆⠹⢿⣿⣿⣶⣶⣾⣿⣿⣿⣿⠋⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⣿⡿⠁⠀⠀⠀⠀⢿⣿⣿⡆⠀⠀⠸⣿⣿⣿⡄⠀⠀⠀⢿⣿⣿⠀⠀⠙⠛⠿⠿⠿⠛⠋⢸⣿⠀⠀
⠀⠀⠀⠀⠀⠀⣠⣴⣿⣿⡿⠛⠁⠀⠀⠀⠀⠀⠘⣿⣿⣿⠀⠀⠀⣿⣿⣿⡇⠀⠀⠀⢸⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⠀⠀
⠀⠀⠀⢠⣶⣿⣿⠿⠋⠁⠒⠛⢻⣷⠀⠀⠀⠀⠀⢹⣿⣿⡇⠀⣠⣿⣿⣿⢃⣴⣿⠟⠛⢿⣿⣿⡄⠀⠀⠀⠀⠀⠀⢠⣿⣿⠀⠀
⠀⠀⢰⣿⣿⠟⠁⠀⠀⠀⠀⢀⣾⡟⠀⠀⠀⠀⠀⠘⣿⣿⣧⣾⣿⣿⠟⠁⣾⣿⡇⠀⠀⠘⢿⣿⣿⣦⡀⠀⠀⣀⣴⣿⣿⠃⠀⠀
⠀⠀⣿⣿⡇⠀⠀⢀⡄⠀⢠⣿⣿⠀⠀⠀⠀⠀⠀⢰⣿⣿⣿⣿⠟⠁⠀⠀⢿⣿⣇⠀⠀⠀⠈⠻⣿⣿⣿⣿⣿⣿⡿⠟⠁⠀⠀⠀
⠀⠀⠹⣿⣷⣄⣀⣼⡇⠀⢸⣿⣿⡀⠀⠀⠀⠀⣠⣿⣿⣿⡿⠋⠀⠀⠀⠀⢸⣿⣿⡀⠀⠀⠀⠀⠀⠉⠉⠉⠉⠁⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠈⠛⠛⠛⠋⠀⠀⠀⢻⣿⣿⣶⣶⣶⣿⣿⣿⣿⣿⠁⠀⠀⠀⠀⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⠛⠛⠛⠛⠉⣿⣿⣿⡀⠀⠀⠀⠀⠀⠀⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣿⣿⣷⣄⣀⠀⢀⣀⣴⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢿⣿⣿⣿⣿⣿⣿⣿⡿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠉⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀

              
        Seeing you caught in its tentacle, the monsters fearsome beak lunges towards you.
              """)

def deadend():
    print("Game over!")
         
def main():
    print("""
          
        You twist your body with all your might, sliding out from the beasts slippery grasp,  
          
        Casting a blast of air at your feet you rocket away as the beast thrashes at the room, causing debris to rain down around you. 
          
          
        Hiding from the beast's fury behind some loose rocks you plan your next move. 
          
        You see a corridor nearby that looks like it comes out behind the Kraken, maybe allowing you to steal the gem without notice, 
          
          
        Or if you felt brave you could conjure wings and attempt to move with speed through the air and use superior agility to dive down and grab the gem before the kraken grabs you.
                 
""")
    
def flippers():
    print("""
    You decide to swim, making your way towards the corridor you notice it guarded by a smaller octopus, just smaller than yourself. 
          
    Your magic makes short work of the creature, and you swim quickly into the corridor before the big one spots you.

    Too quickly you suddenly find, as you smack headfirst into another brace of mines. 
    
    That same dreadful ticking ringing in your ears as you paddle desperately away, but not fast enough, it explodes, forcing you through the water to impact painfully on the wall.
""")   
    in_put = input("Do you want to try the flying route? y/n ")
    if in_put == "y":
        wings()
    else:
        print("You cant escape from the room and eventually die")
        exit()    

def wings():
    print("""
You conjure delicate, almost invisible wings of air, and with a swoosh you take to the air, avoiding the tangling plants on the ceiling. 
          
You hover for a second, searching for that purple glimmer, finding it you dive down hard, extending your arms to break the water. 
          
The Kraken spots you and lashes out, but you are too quick, grabbing the gem and making for the exit. 
          """)

main()    
in_put = input("\n Do you want to swim or fly? 'swim' or 'fly' ")
if in_put == "swim":
        flippers()
elif in_put == "fly":
         wings()
else: 
        deadend()
        main()

in_put = input("continue? y/n ")
if in_put == "y":
    print("""
    You clamber through the broken roof, jumping climbing and scrambling up the jagged rocks and crumbling earth, using the now exposed roots of those great jungle trees. 
          
      
    It takes you well over an hour to navigate the tight and difficult route, but finally you emerge, dirty and sweating but clutching the umbral key-gem, into the foyer you first arrived into earlier. 
          
      
    The room is now in complete disarray from the Krakens' fury, the stone vampires lie broken, only the dark gothic door remains untouched, you approach and with a shaking hand you place the key-gem into its waiting socket. 
          
      
    With a hiss the door opens by itself, gliding smoothly around as if freshly oiled, as it opens an avalanche of bones comes with it, 
      
    Knocking you back and stunning you momentarily as you receive a posthumous flying headbutt from some unfortunate soul. 
      
      
    As your vision clears you realise that many of the skeletons' rotted apparel looks very similar to yours, you wonder how many folk have followed your same path… 
      
    But resolving to not become like them, you steel yourself and plunge fearlessly on, your boots crunching over the carpet of bones. 
          
      
    Inside the door is deep, inky blackness, you cast your light, but as it starts to orbit it flickers like a dying candle and a second later winks out entirely. 
      
    You try to feel out for the wall but find nothing but air, in fact you almost fall as the bone floor abruptly ends, only impenetrable darkness and this thin path of bones remain.
          
    
    You hear a bone dry, rasp of a chuckle behind you and you wheel around to the door in time to see it close, the last glimmer of light extinguished. 
      
    “No going back now” you think to yourself as you sink to your knees and feel your way along this thin and uneven path as it weaves through this dark void.
          
    
    As you slowly travel, you start to lose track of time, all you dont know how long you've been here, could be seconds, could have been a month, 
      
    Your provisions are long gone but you've stopped being hungry, or thirsty come to think of it, all that remains is putting one foot in front of another.
""")
in_put = input("What do you want to do? ")
if in_put == holy_spell:
    print("""
        You cast a glorious blast of holy radiance and the darkness around you melts like snow in a furnace, 
          
        You are back in the dungeon, the floor still scattered with bones, but you are almost pathetically grateful for the solid walls and floor below you.
          """)
else:
    print("""
        The darkness scourges your flesh, like hundreds of whips, then slowly start to disperse, 
        
        you are back in the dungeon, the floor still scattered with bones, but you are almost pathetically grateful for the solid walls and floor below you.
          """)
    count4 -= 10
print("""
    With your footfalls rattling the bones beneath you, you walk on till you spy a doorway, beyond it you can see flickering moving lights in purple green and black, 
      
    As you inch closer the smell of death rises till you can almost taste it like bile in the back of your throat, passing through the door you look out into an arcane workshop.

    Bubbling cauldrons and esoteric devices line the walls, a heady chemical smoke fills the air with the smell of formaldehyde and you hear a tortured buzzing from a large mesh cage of locust-like creatures. 
      
    As the inhabitants smell the life you carry they heedlessly drum the cage wall, desperate for blood.

    At the far end you spot a figure by a great stone altar, tattered robes cloaking preserved flesh, wrapped impossibly tightly around spindly bones.
      
    The head snaps in your direction, empty eye sockets staring deep into your fragile white orbs, and you hear that same bone dry rasp that sets your body to tense and the heart hammer in your chest.

    “Many have come before you to claim the Staff of Power, their bones litter your path… what makes you different? What makes you … worthy?”

    "You feel the icy tendrils of their spell before they even cast it, as they chant, a fearsome wraith composed of ice rips its way from the void, you have a split second to counter.
""")
in_put = input("What do you want to do? ")
if in_put == fire_spell:
    print("\n    Launching a scorching and unrefined wave of fire, you melt the icy claws of the lich's spell, water striking hard and drenching you. The air clears for a moment \n")
else:
    print("\n   The icy claws of the lich's spell tear into your flesh.\n")
    count4 -= 10
if count4 > 0:
    print("\n    As the phantasm fades you have a window of opportunity. You can use this to strike.\n")
    in_put = input("What do you want to do? ")
    if in_put  == cutting_spell:
        print("""
            You slice out with invisible super-sharp blades of air, the projectiles screaming as they cut through the muggy air. 
              
            The lich jerks his arms roughly to the air like a puppet master, and as if pulled by invisible strings, skeletal minions arise and are instantly scattered as the slicing spell hits them.
            """)
        if count4 > 0:
            print("\n    As the Skeletons hit the floor, their bones clattering like dice, the lich turns and with a crack of bone on metal, breaks the latch on the large mesh cage beside him and begins to chant. \n\n    The inhabitants, free at last, swarm towards you.\n")
            in_put = input("What do you want to do? ")
            if in_put  == poison_spell:
                print("\n   The swarm writhes in the remnants of your poison.")
                if count4 > 0:
                    print(" \n    The lich launches himself into the air, borne by purple and black lightning that swat away any further spells from you. \n\n    You hear them continue to chant, dire words from a language so ancient and vile that only they know their meaning. \n\n    You feel vomit rise in your throat and a tearing buzzing pain in your head as the lich threatens to tear your soul from your flesh.\n    With your life about to end and your vision fading...\n")
                    in_put = input("What do you want to do? ")
                    if in_put  == holy_spell:
                        
                        print("Only life can defeat death, with your hands numb and your voice less than a wisper you fumble through the casting and with your final breath you fire a single intense burst of holy light. \n\nYour vision fades and you collapse to the floor.")
                        if count4 > 0:
                            print("""
                                You awake some time later, half buried in bones, Staring straight into a grinning skull. 
                                
                                You sit up and see the ravaged remains of the lich, the chest still smouldering with embers of holy fire. 
                                  
                                As you watch, the bones start to disintegrate, the cinders slowly consuming the wretched form. 
                                  
                                Brushing off grave dust you limp to the altar, the Staff glowing gold as if it knew its liberation was at hand.")
                                  
                                You have conquered the dungeon and claimed the Staff of Power. Well done!
                                  """) 
                    else:
                        print("As the lich launches their final attack, your life flashes before your eyes, your vision fades and you collapse to the floor.")
                        count4 -= 20
                        if count4 > 0:
                            print("""
                                You awake some time later, half buried in bones, Staring straight into a grinning skull. 
                                
                                You sit up and see the ravaged remains of the lich, the chest still smouldering with embers of holy fire. 
                                  
                                As you watch, the bones start to disintegrate, the cinders slowly consuming the wretched form. 
                                  
                                Brushing off grave dust you limp to the altar, the Staff glowing gold as if it knew its liberation was at hand.")
                                  
                                You have conquered the dungeon and claimed the Staff of Power. Well done!
                                  """) 
            else:
                print("\n   The swarm suround and attack, you feel tiny probisci penetrate your skin and gorge themselves on your blood.")
                count4 -= 10
                if count4 > 0:
                    print("\n    \n\n    The lich launches himself into the air, borne by purple and black lightning that swat away any further spells from you. \n\n    You hear them continue to chant, dire words from a language so ancient and vile that only they know their meaning. \n\n    You feel vomit rise in your throat and a tearing buzzing pain in your head as the lich threatens to tear your soul from your flesh.\n    With your life about to end and your vision fading...")
                    in_put = input("what do you want to do? ")
                    if in_put  == holy_spell:
                        print("\n   Only life can defeat death, with your hands numb and your voice less than a wisper you fumble through the casting and with your final breath you fire a single intense burst of holy light. \n\nYour vision fades and you collapse to the floor.\n")
                    else:
                        print("\n   As the lich launches their final attack, your life flashes before your eyes, your vision fades and you collapse to the floor.")
                        count4 -= 20
                        if count4 > 0:
                            print("""
                                You awake some time later, half buried in bones, Staring straight into a grinning skull. 
                                
                                You sit up and see the ravaged remains of the lich, the chest still smouldering with embers of holy fire. 
                                  
                                As you watch, the bones start to disintegrate, the cinders slowly consuming the wretched form. 
                                  
                                Brushing off grave dust you limp to the altar, the Staff glowing gold as if it knew its liberation was at hand.")
                                  
                                You have conquered the dungeon and claimed the Staff of Power. Well done!
                                  """)
                        else:
                            print("You soul and very being is reduced to ash as the lich laughs at your folly.")
                else:
                    print("You have been fully consumed by the swarm.")
    else:
        print("\n    The lich creates a barrier to deflect your spell then jerks his arms roughly to the air like a puppet master. \n\nAs if pulled by invisible strings, skeletal minions arise and lurch towards you, their rusted weapons sink into your flesh.\n")
        count4 -= 10
        if count4 > 0:
            print("\n    As the Skeletons hit the floor, their bones clattering like dice, the lich turns and with a crack of bone on metal, breaks the latch on the large mesh cage beside him and begins to chat. \n\nThe inhabitants, free at last, swarm towards you.")
            in_put = input("what do you want to do? ")
            if in_put  == poison_spell:
                print("\n    The swarm writhes in the remnants of your poison.")
            else:
                print("\n    The swarm suround and attack, you feel tiny probisci penetrate your skin and gorge themselves on your blood.")
                count4 -= 10
                if count4 > 0:
                    print(" \n\nThe lich launches himself into the air, borne by purple and black lightning that swat away any further spells from you. \n\You hear them continue to chant, dire words from a language so ancient and vile that only they know their meaning. \n\nYou feel vomit rise in your throat and a tearing buzzing pain in your head as the lich threatens to tear your soul from your flesh.\nWith your life about to end and your vision fading...\n")
                    in_put = input("what do you want to do? ")
                    if in_put  == holy_spell:
                        print("\nOnly life can defeat death, with your hands numb and your voice less than a wisper you fumble through the casting and with your final breath you fire a single intense burst of holy light. \n\nYour vision fades and you collapse to the floor.\n")
                    else:
                        print("\nAs the lich launches their final attack, your life flashes before your eyes, your vision fades and you collapse to the floor.\n")
                        count4 -= 20
                        if count4 > 0:
                            print("""
                                You awake some time later, half buried in bones, Staring straight into a grinning skull. 
                                
                                You sit up and see the ravaged remains of the lich, the chest still smouldering with embers of holy fire. 
                                  
                                As you watch, the bones start to disintegrate, the cinders slowly consuming the wretched form. 
                                  
                                Brushing off grave dust you limp to the altar, the Staff glowing gold as if it knew its liberation was at hand.")
                                  
                                You have conquered the dungeon and claimed the Staff of Power. Well done!
                                  """)
                        else:
                            print("You soul and very being is reduced to ash as the lich laughs at your folly.")  
                else:
                    print("You have been fully consumed by the swarm.")
        else:
            print("You scream in agony as you are torn limb for limb by the liches minions only to eventually join them.")
else:
    print("You perish as your very soul freezes and shatters.")