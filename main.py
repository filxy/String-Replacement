# Mistyped lyrics of Journey - Don't Stop Believin' assigned to variable journey
journey = """Just a small tone girl
Leaving in a lonely whirl
She took the midnight tray going anywhere
Just a seedy boy
Bored and raised in South Detroit or something
He took the midnight tray going anywhere"""
# Assigning correct words in lyrics to variables
T = "town" 
L = 'Livin'
Tr = 'train goin'
C = 'city'
B = 'Born' 
s = " "
# Assigning correct words in lyrics to variable dsbWords & replacing mistyped words with correct words
dsbWords = journey.replace('tone',T) and journey.replace('Leaving',L) and journey.replace('tray',Tr) and journey.replace('seedy',C) and journey.replace('Bored',B) and journey.replace('or something',s)
#Printing correct lyrics of Journey - Don't Stop Believin'
print(dsbWords)
