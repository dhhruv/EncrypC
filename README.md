# EncrypC
File Encryption Application using Python

![encrypc](https://user-images.githubusercontent.com/72680045/99971140-cbbd0580-2dc2-11eb-97ec-e507a9bcbca2.PNG)

## Technologies Used:
* Python3
* Tkinter for GUI (Inbuilt)
* pycryptodomex for Cryptodome (AES Encryption)

### External Dependencies to be Installed:
* `pycryptodomex` (AES encryption)
```sh
pip install pycryptodomex
```

## Tutorial to Encrypt/Decrypt Files:
1. Open the Application and Click SELECT FILE Button and select your file e.g. "mydoc.pdf" (OR You can add path manually).
2. Enter your Key (This should be alphanumeric letters). Remember this so you can Decrypt the file later. (Else you'll lose your file permanently)
3. Click ENCRYPT Button to encrypt the file. A new encrypted file with ".kryp" extention e.g. "mydoc.pdf.kryp" will be created in the same directory where the "mydoc.pdf" is.
4. When you want to Decrypt a file you, will select the file with the ".kryp" extention and Enter your Key which you chose at the time of Encryption. Click DECRYPT Button to decrypt. The decrypted file will be of the same name as before with the suffix "decrypted" for e.g. "mydoc_decrypted.pdf".
5. Click CLEAR Button to reset the input fields and status bar.
6. You can also Click CANCEL Button during Encryption/Decryption to stop the process or if it doesn't respond.

## Special Note:
-	The Software is still in it's Prototype Stage so we request you to ensure that you have a backup of all of your Data on which you're testing to prevent deletion of any of your useful data. Under no circumstances shall we be liable or responsible to you or any other person for any damages, loss of any of your useful data by using this Software. The prototype is basically for testing purposes only.