# Tool for cracking SHA1 hashes by dictionary attack.
Password cracking tool that attempts to find the original password from a given hash and salt. It uses a wordlist to try each password and hash it using the specified hash algorithm (SHA1 in this case). If the hash of a tried password matches the given hash, the password is considered found and displayed.
- The PasswordEncryptor class is defined with two attributes: hash_type and pbkdf2_iterations. The hash_type attribute specifies the hash algorithm to be used, and the pbkdf2_iterations attribute specifies the number of iterations to be used in the PBKDF2 key derivation function.
- The crypt_bytes method of the PasswordEncryptor class is used to hash a given value using the specified hash algorithm and a given salt. It first creates a new hash object of the specified type. Then, it updates the hash object with the salt and the value. Finally, it returns the hashed bytes as a base64-encoded string.
- The get_crypted_bytes method is a helper method that computes the hash of a given value using the specified hash algorithm and a given salt. It first creates a new hash object of the specified type. Then, it updates the hash object with the salt and the value. Finally, it returns the hashed bytes as a base64-encoded string.
- The script first checks if the correct number of command-line arguments is provided. If not, it prints an error message and exits.
- The hash_type variable is set to "SHA1". The salt, search, and wordlist variables are set to the first, second, third, and fourth command-line arguments, respectively.
- The PasswordEncryptor class is instantiated with the specified hash type.
- The total number of lines in the wordlist file is calculated and stored in the total_lines variable.
- The script then opens the wordlist file in read mode and processes each line in the file. For each line, it first removes any leading or trailing whitespace. Then, it hashes the password using the crypt_bytes method of the PasswordEncryptor class and the given salt. - If the hash of the tried password matches the given hash, the password is considered found, and it is displayed along with its hash.
- The script then exits.
## Usage:
- straight:
```
python3 /full/file/path/to/sha1_dec.py <salt> <hash> <wordlist>
```
- By alias:
```
# into ~/.zshrc create a new alias.
alias sha2text='python3 /full/file/path/to/sha1_dec.py'
```

```
sha2text <salt> <hash> <wordlist>
```

## Example:
```bash
python3 sha1_dec.py 'd' '$SHA1$d$uP0_QaVBpDWFeo8-dRzDqRwXQ2I=' '/usr/share/wordlists/rockyou.txt'
```

## Output:
```bash
└─$ sha2text 'd' '$SHA1$d$uP0_QaVBpDWFeo8-dRzDqRwXQ2I=' '/usr/share/wordlists/rockyou.txt'
Processing:  10%|██████████████▉              | 1477066/14344392 [00:03<00:30, 418313.64it/s]
Found Password:monkeybizness, hash:$SHA1$d$uP0_QaVBpDWFeo8-dRzDqRwXQ2I=
Processing:  10%|██████████████▉              | 1478437/14344392 [00:03<00:31, 413593.99it/s]
```
## Install:
```
git clone https://github.com/PatxaSec/SHA1_Decrypt.git

```
