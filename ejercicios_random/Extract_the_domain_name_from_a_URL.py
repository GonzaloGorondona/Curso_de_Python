#Write a function that when given a URL as a string, 
# parses out just the domain name and returns it as a string. 

def domain_name(url):
    sobrantes = ("http://","https://","www.")
    url = url.replace((sobrantes[0]),"")
    url = url.replace((sobrantes[1]),"")
    url = url.replace((sobrantes[2]),"")
    url = url.split("/")[0]
    parts = url.split(".")
    return parts[0]
    
print(domain_name("http://www.zombie-bites.com"))