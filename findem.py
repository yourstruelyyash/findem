import subprocess
import argparse
import shutil
import sys

# ─── BANNER ──────────────────────────────────────────────
if shutil.which("figlet") and shutil.which("lolcat"):
    subprocess.call("figlet -f slant -c 'findem!' | lolcat", shell=True)
else:
    print("[*] findem! - Subdomain Recon Simplified\n")

# ─── ARGUMENT PARSER ─────────────────────────────────────
parser = argparse.ArgumentParser(description="Find subdomains using subfinder and save them to a file.")
parser.add_argument("-f", "--opfile", help="File to save output to", required=True)
parser.add_argument("-v", "--verbose", help="Print subdomains to terminal", action="store_true")
args = parser.parse_args()

# ─── GET DOMAIN INPUT ────────────────────────────────────
domain = input("Enter domain name: ").strip()

# ─── CHECK IF SUBFINDER EXISTS ───────────────────────────
if not shutil.which("subfinder"):
    print("[-] subfinder not found in PATH. Please install it first.")
    sys.exit(1)

# ─── RUN SUBFINDER ───────────────────────────────────────
print(f"[+] Running subfinder on: {domain}")
output = subprocess.getoutput(f"subfinder -d {domain} -silent")

# ─── SAVE TO FILE ────────────────────────────────────────
with open(args.opfile, "w") as f:
    f.write(output)

print(f"[+] Output saved to {args.opfile}")

# ─── VERBOSE OUTPUT ──────────────────────────────────────
if args.verbose:
    print("\n[+] Subdomains found:")
    print(output)
