
# List of questions, options, and correct answers
questions_data = [
    ["Bharat ke pratham Rashtrapati kaun the?", # Question
     "Dr. Rajendra Prasad", "Dr. S. Radhakrishnan", "Jawaharlal Nehru", "Mahatma Gandhi", 1], # Options and correct answer index

    ["Taj Mahal kis shahar mein sthit hai?",
     "Mumbai", "Agra", "Delhi", "Jaipur", 1],

    ["Kaun sa planet 'Red Planet' ke roop mein jana jata hai?",
     "Mercury", "Jupiter", "Mars", "Venus", 3],

    ["Ramayana ke lekhak kaun hain?",
     "Tulsidas", "Ved Vyas", "Valmiki", "Kalidas", 3],

    ["Google kis cheez ke liye jana jata hai?",
     "Operating System", "Search Engine", "Database", "Browser", 2],

    ["Mahatma Gandhi ka janm kab hua tha?",
     "1869", "1879", "1889", "1899", 1],

    ["Olympic Games har kitne saal mein hote hain?",
     "2", "3", "4", "5", 3],

    ["Pehla computer ka naam kya tha?",
     "ENIAC", "UNIVAC", "IBM", "MICRO", 1],

    ["World War 2 kis varsh khatam hua?",
     "1940", "1945", "1950", "1939", 2],

    ["Python kya hai?",
     "Snake", "Language", "Car", "App", 1]
]
# List of prizes for each correct answer
prize = [1000,2000,3000,4000,5000,6000,7000,8000,9000,100000]
# Initialize question index
i = 0
# Iterate through each question
for quation in questions_data:
    # Print the current question
    print(quation[0])
    # Print the options with labels
    print(f'a {quation[1]}')
    print(f'b {quation[2]}')
    print(f'c {quation[3]}')
    print(f'd {quation[4]}')
    # Get user input for the answer
    a = int(input('enter a answer 1 for a , 2 for b , 3 for c , 4 for d :\n'))
    # Check if the answer is correct
    if(quation[5] == a):
        print('your ansewer is the correct ')
    else:
        print(f'your ansewer is the wrong')
        print('better luck next time')
        # Exit the loop if the answer is wrong
        break
    # Print the prize for the current correct answer
    print(f'your prize is {prize[i]}')
    # Increment question index
    i+=1

else:
    print("\n🎉 Congrats! Aapne saare sawaalon ke sahi jawab diye!")
    print("🏆 Aap jeet gaye ₹100000!")