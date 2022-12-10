#pico2022 #webexploitation 

## Challenge:
```md
Connect to this PostgreSQL server and find the flag!
```

This challenge launches an instance.
```md
Connect to this PostgreSQL server and find the flag! `psql -h saturn.picoctf.net -p 64427 -U postgres pico` Password is `postgres`
```

## Process:
Start by connecting to the database.
```bash
psql -h saturn.picoctf.net -p 64427 -U postgres pico
```
#psql #postgres

```
postgres
```

And look at the tables.
```
pico-# \dt
         List of relations
 Schema | Name  | Type  |  Owner
--------+-------+-------+----------
 public | flags | table | postgres
(1 row)
```
#postgres 

And lets look at the flags.
```
pico=# select * from public.flags;
 id | firstname | lastname  |                address
----+-----------+-----------+----------------------------------------
  1 | Luke      | Skywalker | picoCTF{L3arN_S0m3_5qL_t0d4Y_31fd14c0}
  2 | Leia      | Organa    | Alderaan
  3 | Han       | Solo      | Corellia
(3 rows)
```
#postgres 

And there's the flag.
```bash
echo "picoCTF{L3arN_S0m3_5qL_t0d4Y_31fd14c0}" > flag.txt
```
#echo 

**Flag: *picoCTF{L3arN_S0m3_5qL_t0d4Y_31fd14c0}***



