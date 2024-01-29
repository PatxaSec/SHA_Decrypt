# Tool to decrypt SHA1 hashes by dictionary attack.

## Usage:
```
python3 sha1_dec.py <salt> <hash> <wordlist>
```

- ejemplo
```bash
python3 sha1_dec.py 'd' '$SHA1$d$uP0_QaVBpDWFeo8-dRzDqRwXQ2I=' '/usr/share/wordlists/rockyou.txt'
```

- output

```bash
└─$ python3 sha1_dec.py 'd' '$SHA1$d$uP0_QaVBpDWFeo8-dRzDqRwXQ2I=' '/usr/share/wordlists/rockyou.txt'
Processing:  10%|██████████████▉                                                                                                                                  | 1477066/14344392 [00:03<00:30, 418313.64it/s]Found Password:monkeybizness, hash:$SHA1$d$uP0_QaVBpDWFeo8-dRzDqRwXQ2I=
Processing:  10%|██████████████▉                                                                                                                                  | 1478437/14344392 [00:03<00:31, 413593.99it/s]
```
## Install:

```

```
