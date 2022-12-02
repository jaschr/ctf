#pico2022 #webexploitation

## Challenge:
```md
Can you get the flag? Go to this [website](http://saturn.picoctf.net:54634/) and see what you can discover.
```

## Process:
First thing to do is visit the [website](http://saturn.picoctf.net:54634/).

Looking at the *style.css* I see this comment:
```css
/* picoCTF{1nclu51v17y_1of2_ *
```

And looking at the *script.js* I see another comment:
```js
// f7w_2of2_df589022}
```

Then concatenating them together we get the flag.
```bash
echo "picoCTF{1nclu51v17y_1of2_f7w_2of2_df589022}" > flag.txt
```
#echo 

**Flag: *picoCTF{1nclu51v17y_1of2_f7w_2of2_df589022}***
