import re as re

if __name__ == '__main__':
    text = "555-1239Dr. Bernard Lander(636) 555-0113Hollingdorp, Donnatella555-6542Fitzgerald, F. Sco\
tt555 8904Rev. Martin Luther King636-555-3226Snodgrass, Theodore5553642Carlamina Scarfoni"
    #here we make a regex restraint on the text
    answer1 = re.findall('[0-9]+', text)
    print(answer1)
    #uses text as an input and tries to find patterns with characters a-z
    answer2=re.findall('[A-Za-z]{1,}', text)
    print(answer2)
    #uses compile to get title,first,last
    regex = re.compile("([A-Z]{1}[a-z]{1,2}\.)\s([A-za-z]+)\s([A-za-z]+)")
    answer3 = regex.findall(text)
    print(answer3)
    #boolean search returns true if pattern found
    if re.search("([A-Z]{1}[a-z]{1,2}\.)",text):
        print("title found")
    #boolean search returns true if pattern found
    if re.search("\s([A-za-z]+)\s([A-za-z]+)\s([A-za-z]+)",text):
        print("middle or second name found")

    #the issue here is that its matching every character when we only want title so to fix this we would make it only extract <title>
    texthtml="<title>+++BREAKING NEWS+++<title>"
    answer6= re.findall('<title>', texthtml)
    print(answer6)

    textmath="(5-3)^2=5^2-2*5*3+3^2"
    #Issue the ^0-9=+*()]+ doesnt work is becuase it only gets the signs to fix this we could simply just copy the pattern and escape the symbols that have a differnet meaning in regex
    answer7= re.findall(r"(\(5-3\)\^2=5\^2-2\*5\*3\+3\^2)",textmath)
    print(answer7)
