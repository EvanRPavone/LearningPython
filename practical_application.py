from utils.utility_stuff import ListAndCharShortner, DictionaryShortner

myshortner = ListAndCharShortner([1,2,3,4,5,6])
myshortner.print_original_items()
myshortner.print_shortened_items()
# -> [1,2,3]

mydictshortner = DictionaryShortner({1: 'mike', 2: 'tom', 3: 'rebecca', 4: 'mike', 5: 'paul'})
mydictshortner.print_original_items()
mydictshortner.print_shortened_items()
# -> {1: 'mike', 2: 'tom', 3: 'rebecca'}