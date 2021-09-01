echo "Cloning Repo...."
git clone https://github.com/jinspalakkattu/PublicMusicPlayer.git /PublicMusicPlayer
cd /PublicMusicPlayer
pip3 install -U -r requirements.txt
echo "Starting Bot...."
python3 main.py
