import sys
import requests
import re
from bs4 import  BeautifulSoup
from collections import Counter

def get_body_txt(url):
    response = requests.get(url, verify=False)
    soup = BeautifulSoup(response.text, "html.parser")
    
    if soup.body:
        return soup.body.get_text()
    
    return ""

def freq_of_words(text):
    words = text.lower().split()
    return Counter(words)


def hash_value(word):
    a = 53
    b = 2**64
    h= 0
    pow = 1

    for i in word:
        h = (h + ord(i) * pow) % b
        pow = (pow * a) % b

    return h



def simhash(word_fr):
    bit_v = [0]* 64

    for w, f  in word_fr.items():
        h = hash_value(w)

        for j in range(64):
            bit = (h>>j) & 1
            if bit == 1:
                bit_v[j] += f
            else:
                bit_v[j] -= f
    
    simhash_v =0
    for i in range(64):
        if bit_v[i]>0:
            simhash_v = simhash_v + (1<<i)
    return simhash_v


def common_bits_count(h1, h2):
    a  = h1 ^ h2
    count = 0
    
    while a>0:
        if a%2 ==1:
            count +=1
        a=a//2
    return 64- count



if len(sys.argv) < 3:
    print("Please provide TWO URLs")
    sys.exit()


url1 = sys.argv[1]
url2 = sys.argv[2]

text1 = get_body_txt(url1)
text2 = get_body_txt(url2)

freq1 = freq_of_words(text1)
freq2 = freq_of_words(text2)

hash1 = simhash(freq1)
hash2 = simhash(freq2)

common = common_bits_count(hash1, hash2)

print("Simhash 1:", hash1)
print("Simhash 2:", hash2)
print("Common Bits:", common)
