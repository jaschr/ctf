#pico2022 #webexploitation 

## Challenge:
```md
The developer of this website mistakenly left an important artifact in the website source, can you find it? The website is [here](http://saturn.picoctf.net:58133/)
```

## Process:
Step 1: Go to the [website](http://saturn.picoctf.net:58133/).
Step 2: Dig through the source files.

After looking at the *style.css* I find *picoCTF{1nsp3ti0n_0f_w3bpag3s_587d12b8}* as one of the comments.
```bash
echo "picoCTF{1nsp3ti0n_0f_w3bpag3s_587d12b8}" > flag.txt
```
#echo 

**Flag: *picoCTF{1nsp3ti0n_0f_w3bpag3s_587d12b8}***
