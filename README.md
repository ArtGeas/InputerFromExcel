# InputerFromExcel

pip install webdriver-manager



Step 2: Add the (Ubuntu) Mozilla team PPA to your list of software sources by running the following command in the same Terminal window:

 sudo add-apt-repository ppa:mozillateam/ppa
 
Step 3: Next, alter the Firefox package priority to ensure the PPA/deb/apt version of Firefox is preferred. This can be done using a slither of code from FosTips (copy and paste it whole, not line by line):

echo '
Package: *
Pin: release o=LP-PPA-mozillateam
Pin-Priority: 1001
' | sudo tee /etc/apt/preferences.d/mozilla-firefox

Step 4: Since you’ll (hopefully) want future Firefox upgrades to be installed automatically, Balint Reczey shares a concise command on his blog that ensures it happens:

echo 'Unattended-Upgrade::Allowed-Origins:: "LP-PPA-mozillateam:${distro_codename}";' | sudo tee /etc/apt/apt.conf.d/51unattended-upgrades-firefox

Step 5: Finally, install Firefox via apt by running this command:

sudo apt install firefox





sudo dpkg -i google-chrome-stable_current_amd64.deb
sudo apt install --fix-broken