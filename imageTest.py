import requests

#####################################################################################
#################### Unique images URLs list ########################################
#####################################################################################

list_url = open('C:\Users\jash\Desktop\urls.txt').read().splitlines()
print list_url  #URLs with duplicates
list_furl = []  #final URL list

for url in list_url:
    if url not in list_furl:
        list_furl.append(url)
print list_furl #final list of URLs without duplicates

#####################################################################################
#################### TO find the URLs in ascending order ############################
#####################################################################################


####sudhanshu####
size_asc = []
for furl in list_furl:
    r = requests.get(furl)
    c = len(r.content)
    size_asc.append(c)
        
    
unsorted_list = size_asc[:]  #to make a copy of unsorted list
print unsorted_list
size_asc.sort()              
print size_asc


newList = []   
for i in range(0,len(size_asc)):
    a = unsorted_list.index(size_asc[i])
    newList.append(list_furl[a])
    
    
print newList  #sorted URL list (ascending order)
