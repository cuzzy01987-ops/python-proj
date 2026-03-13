
   






def main():

    while True:

        password = input("Enter a password to test (or q to quit): ")

        if password.lower() == "q":
            print("Goodbye.")
            break

        strength = password_strength(password)

        print("Password strength score:", strength)

        # Enhancement label
        labels = {
            0: "Very Weak",
            1: "Weak",
            2: "Fair",
            3: "Medium",
            4: "Strong",
            5: "Very Strong"
        }

        print("Strength level:", labels.get(strength, "Unknown"))
        print()
        
# Enhancement:
# This program also prints a descriptive label for the password strength
# (Very Weak, Weak, Medium, Strong, Very Strong) in addition to the numeric score.

# Character type constants
LOWER=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
UPPER=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
DIGITS=["0","1","2","3","4","5","6","7","8","9"]
SPECIAL=["!","@","#","$","%","^","&","*","(",")","-","_","=","+","[","]","{","}","|",";",":","'","\"",",",".","<",">","?","/","\\","`","~"]


def word_in_file(word, toppasswords,wordlist, case_sensitive=False):
     with open("toppasswords.txt", "r", encoding="utf-8") as file1, open("wordlist.txt","r", encoding="utf-8") as file2:
         toppasswords = set(file1.readline())
         wordlist = set(file2.readline())
         
         for line in file1 or line in file2:
             file_word = line.strip()
             if case_sensitive:
                 if word == file_word:
                     return True
                 else:
                     if word.lower() == file_word.lower():
                         return True
     return False
             
         
        
                       

        
                    

                
                
     




def word_has_character(word, character_list):
    for char in word:
        if char in character_list:
            return True
    return False


def word_complexity(word):
    complexity = 0

    if word_has_character(word, LOWER):
        complexity += 1

    if word_has_character(word, UPPER):
        complexity += 1

    if word_has_character(word, DIGITS):
        complexity += 1

    if word_has_character(word, SPECIAL):
        complexity += 1

    return complexity




    # Dictionary check (case insensitive)
def password_strength(password, min_length=10, strong_length=16):
   
        
    # Dictionary check
    if word_in_file(password,"wordlist.txt", case_sensitive=False):
        wordlist = file1.readline()
        print("Password is a dictionary word and is not secure.")
        return 0

    # Common password check
    if word_in_file(password, "toppasswords.txt", case_sensitive=True):
        print("Password is a commonly used password and is not secure.")
        return 0

    # Length check
    if len(password) < min_length:
        print("Password is too short and is not secure.")
        return 1

    # Strong length rule
    if len(password) >= strong_length:
        print("Password is long, length trumps complexity this is a good password.")
        return 5

    # Complexity calculation
    complexity = word_complexity(password)

    strength = 1 + complexity

    return strength
    


if __name__ == "__main__":
    main()