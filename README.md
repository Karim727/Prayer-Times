# Prayer-Times-Command

This is a custom terminal command built using Python that displays the daily Prayer Times for Cairo with some extra options.


### Options:
salah [-h] [-a] [-n] [-l]

### Linux Installation
Copy The python script to a text file and place it in your **Home directory** and then create a symbolic link to it in your /usr/local/bin directory, so that you can run it as a command through your bash terminal. 
```
sudo ln -s ~/salah.py /usr/local/bin/salah
```
##### OR
Put the python script directly into your /usr/local/bin directory and add execution permissions using:
```
sudo mv ~/salah.py /usr/local/bin/salah
sudo chmod +x /usr/local/bin/salah
```
- You can also run the command directly using:
	```
	python3 salah.py
	```
