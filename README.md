# Random_numbers
 Details on how to run the program on MacOS and Linux

1. Install Python: If you haven't already, start by installing Python on your computer. You can download the latest version of Python for your operating system from the official Python website: https://www.python.org/downloads/

2. Open a text editor: In my own case i used Visual Studio Code. Next, open a text editor on your computer. You can use a built-in text editor like Notepad on Windows or TextEdit on macOS, or you can download a more advanced text editor like Sublime Text or Visual Studio Code 

3. Write the program: In the text editor, write the Python code to print numbers from 1 to 10 in a random order. Here's is what i have in my random_number.py :

   python
   import random
   
   numbers = list(range(1, 11))  # create a list of numbers from 1 to 10
   random.shuffle(numbers)  # shuffle the list in place
   
   for num in numbers:
       print(num, end=" ")  # print each number in the shuffled list
   

4. Save the program: Save the program with a .py extension (e.g., `random_number.py`) in a directory on your computer where you can easily find it.

5. Open a terminal: Open a terminal (command prompt on Windows or terminal on macOS or Linux) on your computer.

6. Navigate to the directory where the program is saved: Use the `cd` command to navigate to the directory where you saved the program. For example, if you saved the program in a folder called `python_programs` on your desktop, you would type `cd ~/Desktop/python_programs` in the terminal and in my case this is where i have it on my system  Users/debolek/Documents/GitHub/Random_numbers


7. Run the program: Finally, run the Python program by typing `python random_number.py` in the terminal, where `random_number.py` is the name of the file you saved in step 4.

   You should see the program output randomized numbers from 1 to 10 in the terminal. Each time you run the program, you'll get a different random order of the numbers.


This was my output when i run mine 

usr/local/bin/python3 /Users/debolek/Documents/GitHub/Random_numbers/random_number.py
➜  Random_numbers git:(main) ✗ /usr/local/bin/python3 /Users/debolek/Documents/GitHub/Random_numbers/random_number.p
y
64510723819%                                                                                                        
➜  Random_numbers git:(main) ✗ ll
total 16
-rw-r--r--  1 debolek  staff    63B 18 Apr 02:49 README.md
-rw-r--r--  1 debolek  staff   226B 18 Apr 02:58 random_number.py
➜  Random_numbers git:(main) ✗ 
                                                                                                                    
➜  Random_numbers git:(main) ✗ 
➜  Random_numbers git:(main) pwd
/Users/debolek/Documents/GitHub/Random_numbers
➜  Random_numbers git:(main)
