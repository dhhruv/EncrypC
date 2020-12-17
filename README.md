<p align="center">
  <img src="https://user-images.githubusercontent.com/72680045/102007940-19d68080-3d53-11eb-8518-d681586666e6.png">
  <h2 align="center" style="margin-top: -4px !important;">File Encryption Application using Python</h2>
  <p align="center">
    <a href="https://github.com/dhhruv/EncrypC/blob/master/LICENSE">
      <img src="https://img.shields.io/github/license/dhhruv/EncrypC?color=informational">
    </a>
    <a href="https://www.python.org/">
    	<img src="https://img.shields.io/badge/python-v3.8-informational">
    </a>
    <img src="https://img.shields.io/badge/maintainer-dhhruv-informational">
    <a href="https://github.com/dhhruv/EncrypC">
    	<img src="https://img.shields.io/github/v/release/dhhruv/EncrypC">
    </a>
    <a href="https://github.com/dhhruv/EncrypC">
      <img src="https://img.shields.io/badge/managed%20since-dec%202019-informational">
    </a>
    <img src="https://img.shields.io/badge/contributions-welcome-informational">
  </p>
</p>

# EncrypC

<p align="center">
	<img src="https://user-images.githubusercontent.com/72680045/102008090-f9f38c80-3d53-11eb-8372-ae41e077a65e.PNG">
</p>
<br>

## Tech Stack Used:
* Python3
* Tkinter for GUI (Inbuilt)
* pycryptodomex for Cryptodome (AES Encryption)

### External Dependencies to be Installed:
* `pycryptodomex` (AES encryption)
```sh
pip install pycryptodomex
```

## Tutorial to Encrypt/Decrypt Files:
1. Open the Application and Click SELECT FILE Button to select your file e.g. "mydoc.pdf" (OR You can add path manually).
2. Enter your Key (This should be alphanumeric letters). Remember this so you can Decrypt the file later. (Else you'll lose your file permanently)
3. Click ENCRYPT Button to encrypt the file. A new encrypted file with ".encr" extention e.g. "mydoc.pdf.encr" will be created in the same directory where the "mydoc.pdf" is.
4. When you want to Decrypt a file you, will select the file with the ".encr" extention and Enter your Key which you chose at the time of Encryption. Click DECRYPT Button to decrypt. The decrypted file will be of the same name as before with the suffix "decrypted" for e.g. "mydoc_decrypted.pdf".
5. Click CLEAR Button to reset the input fields and status bar.

## Important Note:
-	**The Authors will not be responsible for any kind of loss of data so it is essential to have a Backup of Original Data you give as Input to Encrypt/Decrypt in the Software. Under no circumstances shall we be liable or responsible to you or any other person for any damages, loss of any of your useful data by using this Software. Read the [LICENSE](https://github.com/dhhruv/EncrypC/blob/master/LICENSE) for more information.**