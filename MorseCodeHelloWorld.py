import RPi.GPIO as GPIO
import time

CODE= {' ': ' ',
        'A': '.-',
        'B': '-...',      
        'C': '-.-.',
        'D': '-..',
        'E': '.',
        'F': '..-.',
        'G': '--.',
        'H': '....',
        'I': '..',
        'J': '.---',
        'K': '-.-',
        'L': '.-..',
        'M': '--',
        'N': '-.',
        'O': '---',
        'P': '.--.',
        'Q': '--.-',
        'R': '.-.',
        'S': '...',
        'T': '-',
        'U': '..-',
        'V': '...-',
        'W': '.--',
        'X': '-..-',
        'Y': '-.--',
        'Z': '--..'}

LED=11       
GPIO.setmode(GPIO.BOARD)
GPIO.setup(LED, GPIO.OUT)

def dot():
    GPIO.output(LED,1)
    time.sleep(0.2)
    GPIO.output(LED,0)
    time.sleep(0.2)

def dash():
    GPIO.output(LED,1)
    time.sleep(0.5)
    GPIO.output(LED,0)
    time.sleep(0.2)

while True:
    input = input('Please enter your message in all caps:')
    for letter in input:
        for symbol in CODE[letter.upper()]:
            
            if symbol == '-':
                dash()
            elif symbol == '.':
                dot()
        
    GPIO.output(11,True)
    time.sleep(2)
    GPIO.output(11,False)
    time.sleep(2)
