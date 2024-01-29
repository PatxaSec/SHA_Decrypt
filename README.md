# Herramienta para descifrar hashes SHA1 mediante ataque de diccionario.
Herramienta para descifrar contraseñas que intenta encontrar la contraseña original a partir de un hash y una salt dados. Utiliza una lista de palabras para probar cada contraseña y aplicar el hash utilizando el algoritmo de hash especificado (SHA1 en este caso). Si el hash de una contraseña intentada coincide con el hash dado, la contraseña se considera encontrada y se muestra.
- La clase PasswordEncryptor se define con dos atributos: hash_type y pbkdf2_iterations. El atributo hash_type especifica el algoritmo hash que se utilizará, y el atributo pbkdf2_iterations especifica el número de iteraciones que se utilizarán en la función de derivación de claves PBKDF2.
- El método crypt_bytes de la clase PasswordEncryptor se utiliza para hacer hash de un valor dado utilizando el algoritmo hash especificado y una salt dada. Primero crea un nuevo objeto hash del tipo especificado. A continuación, actualiza el objeto hash con la salt y el valor. Finalmente, devuelve los bytes hash como una cadena codificada en base64.
- El método get_crypted_bytes es un método de ayuda que calcula el hash de un valor dado utilizando el algoritmo hash especificado y una salt dada. Primero crea un nuevo objeto hash del tipo especificado. A continuación, actualiza el objeto hash con la salt y el valor. Finalmente, devuelve los bytes hash como una cadena codificada en base64.
- El script comprueba primero si se ha proporcionado el número correcto de argumentos de línea de comandos. Si no es así, imprime un mensaje de error y sale.
- La variable hash_type se establece en "SHA1". Las variables salt, search y wordlist se establecen en el primer, segundo, tercer y cuarto argumento de la línea de comandos, respectivamente.
- La clase PasswordEncryptor se instancia con el tipo hash especificado.
- Se calcula el número total de líneas del archivo de lista de palabras y se almacena en la variable total_lines.
- A continuación, el script abre el archivo de lista de palabras en modo lectura y procesa cada línea del archivo. Para cada línea, primero elimina cualquier espacio en blanco inicial o final. A continuación, realiza el hash de la contraseña utilizando el método crypt_bytes de la clase PasswordEncryptor y la sal dada. - Si el hash de la contraseña intentada coincide con el hash dado, la contraseña se considera encontrada, y se muestra junto con su hash.
- El script se cierra.

---

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

---
## Require:
```
pip install tqdm
```
![Python](https://pypi-camo.freetls.fastly.net/6c7e16a4732b3e24d08c464d155bde3b89d95f80/68747470733a2f2f696d672e736869656c64732e696f2f707970692f707976657273696f6e732f7471646d2e7376673f6c6f676f3d707974686f6e266c6f676f436f6c6f723d7768697465)

---

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

---

## Example:
```bash
python3 sha1_dec.py 'd' '$SHA1$d$uP0_QaVBpDWFeo8-dRzDqRwXQ2I=' '/usr/share/wordlists/rockyou.txt'
```

---

## Output:
```bash
└─$ sha2text 'd' '$SHA1$d$uP0_QaVBpDWFeo8-dRzDqRwXQ2I=' '/usr/share/wordlists/rockyou.txt'
Processing:  10%|██████████████▉              | 1477066/14344392 [00:03<00:30, 418313.64it/s]
Found Password:monkeybizness, hash:$SHA1$d$uP0_QaVBpDWFeo8-dRzDqRwXQ2I=
Processing:  10%|██████████████▉              | 1478437/14344392 [00:03<00:31, 413593.99it/s]
```

