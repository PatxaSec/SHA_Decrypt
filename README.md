# Herramienta para descifrar hashes SHA mediante ataque de diccionario.
Herramienta para descifrar contraseñas que intenta encontrar la contraseña original a partir de un hash y una salt dados. Utiliza una lista de palabras para probar cada contraseña y aplicar el hash utilizando el algoritmo de hash especificado (SHA1 en este caso). Si el hash de una contraseña intentada coincide con el hash dado, la contraseña se considera encontrada y se muestra.

---

# Tool for cracking SHA hashes by dictionary attack.
Password cracking tool that attempts to find the original password from a given hash and salt. It uses a wordlist to try each password and hash it using the specified hash algorithm (SHA1 in this case). If the hash of a tried password matches the given hash, the password is considered found and displayed.

---
## Require:
- TQDM Librarie.
```
pip install tqdm
```
![python](https://pypi-camo.freetls.fastly.net/6c7e16a4732b3e24d08c464d155bde3b89d95f80/68747470733a2f2f696d672e736869656c64732e696f2f707970692f707976657273696f6e732f7471646d2e7376673f6c6f676f3d707974686f6e266c6f676f436f6c6f723d7768697465)

---

## Usage:
- straight:
```
python3 /full/file/path/to/sha2text.py <salt> <hash> <wordlist>
```
- By alias:
```
# into ~/.zshrc create a new alias.
alias sha2text='python3 /full/file/path/to/sha2text.py'
```

```
sha2text <salt> <hash> <wordlist>
```

---

## Example:
```bash
python3 sha2text.py 'd' '$SHA1$d$uP0_QaVBpDWFeo8-dRzDqRwXQ2I=' '/usr/share/wordlists/rockyou.txt'
```

---

## Output:
```bash
└─$ sha2text 'd' '$SHA1$d$uP0_QaVBpDWFeo8-dRzDqRwXQ2I=' '/usr/share/wordlists/rockyou.txt'
Processing:  10%|██████████████████████▎                                                                                                                                                                     | 1478437/14344392 [00:04<00:34, 369078.27it/s]

 [+] Pwnd !!! $SHA1$d$uP0_QaVBpDWFeo8-dRzDqRwXQ2I=::::monkeybizness
```

