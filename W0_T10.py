# search_term_in_word.py

word = input("Insert word: ")
search_term = input("Insert search term: ")

if search_term in word:
    print(f"Search term '{search_term}' do appear in word '{word}'")
else:
    print(f"Search term '{search_term}' doesn't appears in word '{word}'")
