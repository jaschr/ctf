#pico2022 #cryptography 

## Challenge:
```md
A type of transposition cipher is the rail fence cipher, which is described [here](https://en.wikipedia.org/wiki/Rail_fence_cipher). Here is one such cipher encrypted using the rail fence with 4 rails. Can you decrypt it? Download the message [here](https://artifacts.picoctf.net/c/272/message.txt). Put the decoded message in the picoCTF flag format, `picoCTF{decoded_message}`.
```

## Process:
Open the [link](https://en.wikipedia.org/wiki/Rail_fence_cipher) and ```wget``` the file.
```bash
wget -q https://artifacts.picoctf.net/c/272/message.txt
```
#wget 

According to the challenge it's encrypted using the rail fence with **4** rails.
#railfence #cipher

After reading the [wikipedia page](https://en.wikipedia.org/wiki/Rail_fence_cipher) I had some more understanding of the *rail fence* cipher (also known as *zigzag cipher*).

Print out the message:
```bash
cat message.txt
```
#cat 

I plugged the encrypted message into an [online decoder](https://www.boxentriq.com/code-breaking/rail-fence-cipher). I understood the cipher enough to draw it out, but for clarity, the online decoder worked better for showing the result.
![[019_rail-fence.png]]
#railfence 

And there is the flag.
```bash
echo "picoCTF{WH3R3_D035_7H3_F3NC3_8361N_4ND_3ND_4A76B997}" > flag.txt
```
#echo 

**Flag: *picoCTF{WH3R3_D035_7H3_F3NC3_8361N_4ND_3ND_4A76B997}***
