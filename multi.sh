if [ -z $UPSTREAM_REPO ]
then
  echo "Cloning main Repository"
  git clone https://github.com/helplessg/multi.git /multi      
else
  echo "Cloning Custom Repo from $UPSTREAM_REPO "
  git clone $UPSTREAM_REPO /multi
fi
cd /multi
pip3 install -U -r requirements.txt
echo "BOT IS STARTING⚡️⚡️⚡️"
python3 loader.py
