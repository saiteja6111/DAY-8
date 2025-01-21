alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l',
            'm','n','o','p','q','r','s','t','u','w','x','y','z']
print(''' ________      _______       ________      ________       _______       ________     
|\   ____\    |\  ___ \     |\   __  \    |\   ____\     |\  ___ \     |\   __  \    
\ \  \___|    \ \   __/|    \ \  \|\  \   \ \  \___|_    \ \   __/|    \ \  \|\  \   
 \ \  \        \ \  \_|/__   \ \   __  \   \ \_____  \    \ \  \_|/__   \ \   _  _\  
  \ \  \____    \ \  \_|\ \   \ \  \ \  \   \|____|\  \    \ \  \_|\ \   \ \  \\  \| 
   \ \_______\   \ \_______\   \ \__\ \__\    ____\_\  \    \ \_______\   \ \__\\ _\ 
    \|_______|    \|_______|    \|__|\|__|   |\_________\    \|_______|    \|__|\|__|
                                             \|_________|                            
                                                                                     
                                                                                     
 ________       ___    ___  ________    ___  ___      _______       ________         
|\   ____\     |\  \  /  /||\   __  \  |\  \|\  \    |\  ___ \     |\   __  \        
\ \  \___|     \ \  \/  / /\ \  \|\  \ \ \  \\\  \   \ \   __/|    \ \  \|\  \       
 \ \  \         \ \    / /  \ \   ____\ \ \   __  \   \ \  \_|/__   \ \   _  _\      
  \ \  \____     \/  /  /    \ \  \___|  \ \  \ \  \   \ \  \_|\ \   \ \  \\  \|     
   \ \_______\ __/  / /       \ \__\      \ \__\ \__\   \ \_______\   \ \__\\ _\     
    \|_______||\___/ /         \|__|       \|__|\|__|    \|_______|    \|__|\|__|    
              \|___|/                                                                
''')
again = True
while again:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: \n").lower()
    original_text = input('enter a message : \n').lower()
    shift_amount = int(input("type the shift number 'or' (decoded code): \n"))

    def encrypt(original_text,shift_amount):
        again2 = True
        while again2:
            if direction == 'encode':
                encoded_value =''
                for i in range(len(original_text)):
                    index = alphabet.index(original_text[i])
                    index += shift_amount
                    encoded_value += alphabet[index]
                print(f'Your Encoded message : {encoded_value}')
                again2 = False
            elif direction == 'decode':
                decoded_value= ''
                for j in range(len(original_text)):
                    index1 = alphabet.index(original_text[j])
                    index1 -= shift_amount
                    decoded_value += alphabet[index1]
                print(f'Your Decoded Message : {decoded_value}')
                again2 = False
            else:
                print('Enter choic correctly!!!')
    encrypt(original_text ,shift_amount)
    choice = input('Type \'yes\' if you want to go again. Otherwise type \'no\' : ').lower()
    if choice == 'yes':
        again = True
    elif choice == 'no':
        again = False
