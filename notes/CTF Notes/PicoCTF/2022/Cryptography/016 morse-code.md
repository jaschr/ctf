#pico2022 #cryptography 

## Challenge:
```md
Morse code is well known. Can you decrypt this? Download the file [here](https://artifacts.picoctf.net/c/235/morse_chal.wav). Wrap your answer with picoCTF{}, put underscores in place of pauses, and use all lowercase.
```

## Process:
Start by using ```wget``` the  get the file.
```bash
wget -q https://artifacts.picoctf.net/c/235/morse_chal.wav
```
#wget 

And I used ```aplay``` to play the file within the terminal.
```bash
aplay morse_chal.wav
```
#aplay

And I used [MorseCode.world](https://morsecode.world/international/decoder/audio-decoder-adaptive.html) to decrypt the message.
```
W H 4 7 H 4 7 H 9 0 D W 2 0 U 9 H 7
```

And following the instructions of the challenge we get the flag.
```bash
echo "picoCTF{wh47_h47h_90d_w20u9h7}" > flag.txt
```
#echo 

**Flag: *picoCTF{wh47_h47h_90d_w20u9h7}***
