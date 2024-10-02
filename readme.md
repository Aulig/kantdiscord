Just some random features I wanted from a discord bot.

# Features

- Send & play local audio/video files in your current voice channel (most bots can only play online (e.g. Youtube) videos for some reason)
- Skip the currently playing file
- Random commands I wrote while finding out how discord.py works

# Deployment

I'm mostly writing this down so I remember it when I come back to this in the future.

## On gameserver.gratis
- Used FTP to transfer the files on there, using a git repo didn't want to work
- FFMPEG was preinstalled there

## Elsewhere
- `sudo apt install ffmpeg`
- `python -m venv venv`
- `source venv/bin/activate`
- `pip install -r requirements.txt`
- create a config.py file with `TOKEN = "YourDiscordToken"`
- Create a systemd service to autostart your bot:
    - `sudo nano /etc/systemd/system/kantdiscord.service`
    
          [Unit]
          Description=Runs the kant discord bot
          After=network.service
  
          [Service]
          Type=simple
          ExecStart=/home/aulig/kantdiscord/venv/bin/python3 /home/aulig/kantdiscord/bot.py
          WorkingDirectory=/home/aulig/kantdiscord
          User=aulig
          StandardOutput=append:/home/aulig/kantdiscord/systemdexecution.log
          StandardError=append:/home/aulig/kantdiscord/systemdexecution.log
        
          [Install]
          WantedBy=multi-user.target

    - `sudo chmod 644 /etc/systemd/system/kantdiscord.service`
    - `sudo systemctl daemon-reload`
    - `sudo systemctl enable kantdiscord.service`
    - `sudo reboot`
    - Check if it worked: `sudo systemctl status kantdiscord.service`
