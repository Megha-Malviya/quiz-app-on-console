
#MEGHA MALVIYA 
#ENROLLMENT NO= 0176AL221078

import random  
 
questions_dbms = [  
     ("What does DBMS stand for? (A) Database Management System (B) Data Base Management Software (C) Document Base Management System", "A"),  
    ("Which of the following is a type of DBMS? (A) Network (B) Relational (C) Document", "B"),  
    ("SQL is used for? (A) Data Analysis (B) Querying databases (C) Web Development", "B"),  
    ("Which of the following is a popular DBMS? (A) MySQL (B) HTML (C) CSS", "A"),  
    ("In a relational DBMS, data is stored in? (A) Objects (B) Tables (C) Arrays", "B"),  
    ("Which language is primarily used for querying in databases? (A) C++ (B) SQL (C) Java", "B"),  
    ("What is the primary purpose of a DBMS? (A) Visualize data (B) Manage data (C) Secure data", "B"),  
    ("Which of these is not a type of DBMS? (A) Hierarchical (B) Sequential (C) Object-oriented", "B"),  
    ("What does normalization do in a database? (A) Increase redundancy (B) Reduce redundancy (C) Simplify queries", "B"),  
    ("Which of the following is an example of NoSQL DBMS? (A) Oracle (B) MongoDB (C) SQLite", "B"),  
]  

questions_python = [  
    ("What is the output of print(2 ** 3)? (A) 6 (B) 8 (C) 4", "B"),  
     ("What keyword is used to define a function in Python? (A) function (B) def (C) fun", "B"),  
    ("What is the correct file extension for Python files? (A) .py (B) .python (C) .pyt", "A"),  
    ("Which of the following is a mutable data type? (A) Tuple (B) String (C) List", "C"),  
    ("What is the output of print('Hello' + ' World')? (A) Hello World (B) HelloWorld (C) 'Hello World'", "A"),  
    ("Which of these is not a Python data type? (A) List (B) Set (C) Array", "C"),  
    ("What does PEP stand for? (A) Python Enhancement Proposal (B) Python Execution Process (C) Python Enhancement Project", "A"),  
    ("What is the correct way to create a list in Python? (A) list = [] (B) list = {} (C) list = ()", "A"),  
    ("Which built-in function can be used to iterate over a sequence? (A) after (B) for (C) loop", "B"),  
    ("How do you insert comments in Python? (A) // comment (B) # comment (C) /* comment */", "B"),  
]  

questions_java = [  
     ("What is the main method signature in Java? (A) public void main(String[] args) (B) public static void main(String[] args) (C) static void main(String args)", "B"),  
    ("Which of these is not a Java primitive type? (A) int (B) String (C) char", "B"),  
    ("What does JVM stand for? (A) Java Variable Machine (B) Java Virtual Machine (C) Java Version Manager", "B"),  
    ("Which keyword is used to inherit a class in Java? (A) implements (B) extends (C) inherits", "B"),  
    ("What is the default value of a boolean variable in Java? (A) true (B) false (C) 0", "B"),  
    ("What is the size of int in Java? (A) 16 bits (B) 32 bits (C) 64 bits", "B"),  
    ("Which of the following is a package in Java? (A) java.util (B) number (C) string", "A"),  
    ("What is the keyword for the main method in Java? (A) static (B) public (C) void", "B"),  
    ("Which collection allows duplicate elements? (A) Set (B) List (C) Map", "B"),  
    ("Which of the following is not a valid identifier in Java? (A) myVar (B) 2ndVar (C) _myVar", "B"),  
]  

accounts = {}  

def register():  
    username = input("Create a username: ")  
    if username in accounts:  
        print("Username already exists. Try again.")  
        return False  
    password = input("Create a password: ")  
    accounts[username] = password  
    print("Registration successful!")  
    return True  

def login():  
    username = input("Enter your username: ")  
    if username not in accounts:  
        print("Username does not exist.")  
        return False  
    password = input("Enter your password: ")  
    if accounts[username] != password:  
        print("Incorrect password.")  
        return False  
    print("Login successful!")  
    return True  

def select_quiz():  
    print("\nSelect a quiz:")  
    print("1. Python")  
    print("2. DBMS")  
    print("3. Java")  
    choice = input("Enter the choice number (1-3): ")  
    if choice == '1':  
        return random.sample(questions_python, 5)  
    elif choice == '2':  
        return random.sample(questions_dbms, 5)  
    elif choice == '3':  
        return random.sample(questions_java, 5)  
    else:  
        print("Invalid choice. Exiting.")  
        return None  

def take_quiz(questions):  
    score = 0  
    for question, answer in questions:  
        user_answer = input(f"{question} ")  
        if user_answer.strip().lower() == answer.strip().lower():  
            score += 1  
            print("Correct!")  
        else:  
            print(f"Wrong! The correct answer is: {answer}")  
    return score  

def main():  
    while True:  
        print("\nWelcome to the Quiz Application!")  
        print("1. Register")  
        print("2. Login")  
        print("3. Exit")  
        action = input("Select an option (1-3): ")  

        if action == '1':  
            register()  
        elif action == '2':  
            if login():  
                questions = select_quiz()  
                if questions:  
                    score = take_quiz(questions)  
                    print(f"You got {score} out of 5 correct!")  
            else:  
                print("Login failed.")  
        elif action == '3':  
            print("Thank you for using the Quiz Application!")  
            break  
        else:  
            print("Invalid option. Please try again.")  

if __name__ == "__main__":  
    main()
