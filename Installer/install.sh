echo "Installation started"
echo "Installing Dependencies"
pip3 install -r requirements.txt

echo "Installing Tkinter"
sudo apt-get install python3-tk

echo "Installation completed"

#Below steps are for packaging your application
#Execute it if you want to build an executable or a wheel

#pip install pyinstaller
#pyinstaller main.py
#cd dist/main
#./main