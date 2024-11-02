# Just for fun text Processing tool 
# Created By: Bright Amankwah
# Version: 1.0
# Requirements: none
# Description: This tool helps you perform basic and simple tasks that word processing tools such as finding and replacing texts, searching
# line of strings in a text, it's pretty awesome .


#FontStyle
bold = '\033[1m'
italics = '\033[3m'
underline = '\033[4m'
bright    = '\033[1m'
dim    = '\033[2m'
normal = '\033[22m'
end = '\033[0m'

#Colours foreground
black_fg = '\033[30m'
red_fg    = '\033[31m'
green_fg   = '\033[32m'
yellow_fg  = '\033[33m'
blue_fg   = '\033[34m'
magenta_fg = '\033[35m'
cyan_fg    = '\033[36m'
end_fg   = '\033[39m'

#Colours background
red     = '\033[41m'
green   = '\033[42m'
yellow  = '\033[43m'
blue    = '\033[44m'
magenta = '\033[45m'
cyan    = '\033[46m'
end_bg = '\033[49m'

#VARIOUS FUNCTIONS (MAIN CODE BLOCK)

def remove_special_char(test_string):  #Function to remove any special character from string
    bad_char = [':',';','.',',','\'','"','!','+','{','}','|','(',')','?','<','>','#','_','â€™']

#replace characters with nothing
    for i in bad_char:
        test_string = test_string.replace(i, '')
    return test_string.lower()    


     

def create_line ():  #Function to create line of text    
    lst = remove_special_char(txt).split() 
    new_lst = []
#extract every 11th word in list (lst) and add new line in front (\n), save it as new_lst      
    for i in lst[10:len(lst):11]: 
        add_line = "\n" + i
        new_lst.append(add_line)

#replace every 11th word in lst with every 11th word in new_lst 
    lst[10:len(lst):11] = new_lst
    processed_txt = " ".join(lst) #convert from list to string
    line_txt = processed_txt.lower().split("\n") #group into list for every newline character (\n)

    return line_txt
    

def enum_and_search(line_len): #Enumerate and search through text   
    line_res = []
    results = ""
    total_num = 0
    sentence_res = "" 

#iterate through and number every line i=line number and lines=line of text
    for i, lines in enumerate(line_len, 1):
        low_lines = lines.split()#lines converted to list 
        num_words = 0
        line_num = []

        #If search is sentence and appears in text
        if len(search.split()) > 1 and search in lines:
            if i not in line_num:    
                line_num.append(i)    
                line_res.append(cyan_fg+" line"+str(line_num)+end_fg)
                sentence_res = " ".join(line_res)
            

#iterate through every word on a line, if search word is the same, count number of words       
        for word in low_lines:          
            if search == word:
                num_words += 1
            if i not in line_num:    
                line_num.append(i)
                               

                    

#if number of words is not 0 add line_num and num_words to result                
        if num_words != 0:
           line_res.append(cyan_fg+"line"+str(line_num)+end_fg)
           line_res.append(f"{red_fg}("+str(num_words)+f"){end_fg} ")
           total_num += num_words

    if total_num != 0:     
        results += f"""\nHint: {cyan_fg}Line[line number]{end_fg} {red_fg}(word frequency){end_fg}
                    \nWord Found in: {" ".join(line_res)}                     
                    \ntotal number of words = {green_fg}{total_num}{end_fg}"""
    elif sentence_res != "":
        results += "\nYour sentence is likely to be in "+sentence_res    
        
    print(results)
    
 
def show_txt_line(): #Enumerate and show number of lines in text with special characters
    lst = txt.split() 
    new_lst = []
    #extract every 11th word in list (lst) and add new line in front (\n), save it as new_lst
    for i in lst[10:len(lst):11]:
        add_line = "\n" + i
        new_lst.append(add_line)

    #replace every 11th word in lst with every 11th word in new_lst
    lst[10:len(lst):11] = new_lst
    processed_txt = " ".join(lst)
    line_len = processed_txt.split("\n")

    print(f"\n========================{yellow}{black_fg}BEGIN TEXT{end_fg}{end_bg}=======================")
    for i , lines in enumerate(line_len, 1):
        print(i, lines)
    print(f"\n========================{yellow}{black_fg}END TEXT{end_fg}{end_bg}========================\n")
    print (f"\nNumber of lines: {green_fg}{i}{end_fg}")

def search_suggestion(string): #Show words in text
    word = [] 

    #search suggestion for words
    for i in string:
        if search in i:
            while i not in word:    
                word.append(i)
        try:    
            word.remove(search)
        except Exception:
            pass        
    if len(word) > 0:
        return f"Check: "+cyan_fg+italics+", ".join(word)+end+end_fg #convert to string e.g (word, search)
    else:
        return ""


def word_and_char_count(text): #word and character count function
    split_text = text.split() 
    print (f"Number of Words: {green_fg}{len(split_text)}{end_fg}")
    print (f"Number of characters: {green_fg}{len(text)}{end_fg}")
    counter = 0
    for i in range(0, len(text)):
        if text[i] == " ":
            counter = counter +1
    print (f"Number of spaces: {green_fg}{counter}{end_fg}")

def read_from_file(file_path):# Function to read from file
    with open (file_path,"r") as file:
        content = file.readlines()
        return ' '.join(content)

def find_and_replace(text, word_to_replace, replace_with, count):  #Function to find and replace
        lst_txt = text.split()
        if len(word_to_replace.split()) > 1 :
            if count == lst_txt.count(word_to_replace):
                count = -1
            if replace_with == '':
                replace_with = f'{italics}[removed]{end}'        
            text = text.replace(word_to_replace, cyan_fg+replace_with+end_fg, count)
                       
            
        else:   
            for index in range (len(lst_txt)):
                if lst_txt[index] == word_to_replace:
                    if replace_with == '':
                        replace_with = f'{italics}{cyan_fg}[removed]{end_fg}{end}'    
                    lst_txt[index] = cyan_fg+replace_with+end_fg
                    count -= 1
                    if count == 0:
                        break
                            
            text = " ".join(lst_txt)
        return text

        

    

    



print (f"\n====================={yellow}{black_fg}COMMANDLINE TEXT PROCESSING APP GROUP 3{end_fg}{end_bg}========================\n")
print(f"{italics}Hint: Use option 1, if your text in the file has not been grouped into lines{end}")

options = input("Choose your options \n(1) Paste text in terminal (2) Read text from file (:q to quit) \n")
if options == '1':
    txt = input("Enter text: \n")
    show_txt_line()
    word_and_char_count(txt)
elif options == '2':
    query = input(R'Enter file path e.g: C:\Users\(username)\Desktop\file.txt (:q to quit): ')
    file_query = query.replace('"', '')
    
    try:
        if file_query == ":q":
            exit()
        file = read_from_file(file_query)
        file_content = file
        file_content_list = file_content.split("\n")
        print(f"\n======================={yellow}{black_fg}BEGIN TEXT{end_fg}{end_bg}=========================\n")
        for i, lines in enumerate(file_content_list, 1):
            print (i,lines)
        print(f"\n========================{yellow}{black_fg}END TEXT{end_fg}{end_bg}==========================\n")    
        print(f"\nNumber of lines: {green_fg}{i}{end_fg}")    
        word_and_char_count(file_content)

    except Exception:
        print(f"{italics}{red_fg}\n[-] Make sure the file path is correct or the file exists")
        print("[-] Add the file extension to the file path e.g: .txt")
        print (f"[-] Only accepts .txt files{end_fg}{end}")        
    
else:
    print (f"{red_fg}Please select 1 or 2{end_fg}")
    exit()

      
while True:    
        try:
            if options == '1':
                input_txt = txt
            elif options == '2':
                input_txt = file_content 
            mode = input("Enter mode: find and replace(r) search_mode(s) (:q to quit) ")
            if mode == ':q':
                break   
            if mode != 's':
                if mode !='r':
                        continue

            while mode != ':q':
                if mode == 's':
                    search = input("\nEnter text to search (:q to exit mode): ").lower()
                    if search == ':q':
                        break
                    if search == "":
                        continue
                    if options == '1':
                        enum_and_search(create_line())
                        

                    elif options == '2':
                        del_spec_char = remove_special_char(input_txt).split('\n')
                        enum_and_search(del_spec_char)
                    print (search_suggestion(remove_special_char(input_txt).split()))



                if mode == 'r':
                    try: 
                        word_to_replace = input("Text to replace (case sensitive) (:q to quit:) ")
                        if word_to_replace == ":q":
                            break
                        elif word_to_replace == '':
                            continue

                        replace_word = input("Replace with (:q to quit): ")
                        if replace_word== ":q":
                            break

                        num_of_words = input("Press enter to replace all or enter the number to replace (:q to quit) ")
                        if num_of_words == ':q':
                            break
                        if num_of_words == '':
                            lst_txt = input_txt.split()
                            num_of_words = lst_txt.count(word_to_replace)
                        
                        #OUTPUT BLOCK --> highlight changes made while maintaining uncolored version of text
                        input_txt = find_and_replace(input_txt, word_to_replace, replace_word, int(num_of_words))
                        print(f'{yellow}{italics}{black_fg}HIGHLIGHTED CHANGES{end_fg}{end}{end_bg}')     
                        print('\n'+input_txt+'\n')
                        clean = [cyan_fg, end_fg, f'{italics}[removed]{end}']
                        for i in clean:
                            input_txt = input_txt.replace(i, '')
                        
                        print(f'{yellow}{italics}{black_fg}MAIN TEXT{end_fg}{end}{end_bg}')
                        print('\n'+input_txt+'\n')    

                        

                    except Exception as e :
                        print(f"{red_fg}Please enter number of words to replace, leave blank for all, :q to quit{end_fg}")
                        print (e)                   

        except Exception as e:
            print (f"\n{red_fg}Oops!! Something went wrong{end_fg}")
            break
        

    
