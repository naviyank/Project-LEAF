# Set the URL of the LinPEAS release
RELEASE_URL="https://github.com/peass-ng/PEASS-ng/releases/latest/download/linpeas.sh"
# Download LinPEAS script
echo "Downloading LinPEAS..."
curl -L "$RELEASE_URL" -o "linpeas.sh"
# Make LinPEAS script executable
chmod +x linpeas.sh
