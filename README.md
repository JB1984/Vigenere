# Vigenere
Program to decrypt/encrypt a passage using Vigenere cipher technique. 

Just run the file and it will prompt you to make a choice betweeen encrypting or decrypting

In both the encrypting or decrypting choice you will see the following input questions:

<b>The first keyword</b>, which creates the alphabet "top" line of the matrix. The keyword here currently must contain only one instance of each letter of the alphabet. For example you can use "Help" but not "Helper" since "Helper" has two e's. 

<b>The second keyword</b>, which creates the lines undeaneath the top line. This finishes the "matrix" used for encoding/decoding. You can use any word here, it can contain more than one instance of a letter. So you could use "Hello" here.

<b>The passage to encrypt/decrypt</b>.

You can take a look at this rather quick YouTube video to see the basics of how Vigenere ciphers work.

https://www.youtube.com/watch?v=0Pm2PrxmU38

<hr>

I would suggest you try first doing something where you know the keys, as well as the encrypted/decrypted passages just to test that it is working. Something like the first Kryptos passage (K1) from the CIA Kryptos sculpture which is listed below. Please note that "illusion" in the text below is intentionally misspelled:

<H4> ENCRYPT </H4>

First Key: KRYPTOS <br>
Second Key: PALIMPSEST <br>
Enter passage you wish to encrypt: Between subtle shading and the absence of light lies the nuance of iqlusion

Encrypted passage you should get returned: EMUFPHZLRFAXYUSDJKZLDKRNSHGNFIVJYQTQUXQBQVYUVLLTREVJYQTMKYRDMFD <br>


<H4> DECRYPT </H4>

First Key: KRYPTOS <br>
Second Key: PALIMPSEST <br>
Enter passage you wish to decrypt: EMUFPHZLRFAXYUSDJKZLDKRNSHGNFIVJYQTQUXQBQVYUVLLTREVJYQTMKYRDMFD

Decrypted passage you should get returned: <br>Betweensubtleshadingandtheabsenceoflightliesthenuanceofiqlusion

