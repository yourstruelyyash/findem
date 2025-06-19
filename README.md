# findem! 🔍

**findem!** is a work-in-progress Python recon tool focused on automating subdomain enumeration using `subfinder`.

It’s the first step toward a modular recon engine for red teamers and bug bounty hunters.

## ✅ Current Features

- 📥 Takes a domain from user input
- 🌐 Enumerates subdomains via [Subfinder](https://github.com/projectdiscovery/subfinder)
- 💾 Saves output to file
- 🗣️ Optional verbose output

## 🧪 Usage

python findem.py -f output.txt -v

When prompted:

**Enter domain name: example.com**

CLI Arguments:
Flag	Description
-f, --opfile	Output file to save subdomains (required)
-v, --verbose	Print subdomains to terminal (optional)


📁 Output Example
output.txt
└── blog.example.com
    admin.example.com
    dev.example.com


⚙️ Requirements
Python 3.10 


🛠️ External Dependencies

Make sure these tools are installed and in your $PATH:
subfinder
figlet
lolcat

Install on Debian/Ubuntu/Kali:
sudo apt install figlet lolcat


💡 Planned (Upcoming) Features

--httpx: Check which subdomains are live
--nuclei: Scan live targets for common vulns
--wayback: Pull archived URLs
--screenshot: Auto-screenshot live hosts

⚠️ Disclaimer
This tool is for educational and authorized security testing only.
Always get permission before scanning any target.

🚧 findem! is under active development — I’m building this tool step by step, learning and improving with each version.

👨‍💻 Author
Built with ❤️ by Yashvardhan
