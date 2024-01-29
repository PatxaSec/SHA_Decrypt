# Tool to decrypt SHA1 hashes by dictionary attack.
## Usage:
- straight:
```
python3 sha1_dec.py <salt> <hash> <wordlist>
```
- By alias:
```
# into ~/.zshrc create a new alias.
alias sha1totext='python3 sha1_dec.py'
```

```
sha1totext <salt> <hash> <wordlist>
```

## Example:
```bash
python3 sha1_dec.py 'd' '$SHA1$d$uP0_QaVBpDWFeo8-dRzDqRwXQ2I=' '/usr/share/wordlists/rockyou.txt'
```

## Output:
```bash
└─$ sha1totext 'd' '$SHA1$d$uP0_QaVBpDWFeo8-dRzDqRwXQ2I=' '/usr/share/wordlists/rockyou.txt'
Processing:  10%|██████████████▉              | 1477066/14344392 [00:03<00:30, 418313.64it/s]
Found Password:monkeybizness, hash:$SHA1$d$uP0_QaVBpDWFeo8-dRzDqRwXQ2I=
Processing:  10%|██████████████▉              | 1478437/14344392 [00:03<00:31, 413593.99it/s]
```
## Install:
```
git clone https://github.com/PatxaSec/SHA1_Decrypt.git

```
