# import subprocess

# def get_subdomains(domain_name):
#     try:
#         # Run sublist3r as a subprocess to enumerate subdomains
#         result = subprocess.run(["sublist3r", "-d", domain_name, "-o", "subdomains.txt"], capture_output=True, text=True)
#         if result.returncode == 0:
#             print(f"Subdomains saved in 'subdomains.txt'")
#         else:
#             print("Subdomain enumeration failed")
#             print(result.stderr)
#     except FileNotFoundError:
#         print("Sublist3r is not installed. Please install it using 'pip install sublist3r'")

# # Specify the target domain
# target_domain = "instagram.com"

# # Call the function to enumerate subdomains
# get_subdomains(target_domain)

import subprocess

def get_subdomains(domain_name):
    try:
        # Run sublist3r as a subprocess to enumerate subdomains
        result = subprocess.run(["sublist3r", "-d", domain_name], capture_output=True, text=True)
        
        if result.returncode == 0:
            subdomains = result.stdout.splitlines()
            for subdomain in subdomains:
                print(subdomain)
        else:
            print("Subdomain enumeration failed")
            print(result.stderr)
    except FileNotFoundError:
        print("Sublist3r is not installed. Please install it using 'pip install sublist3r'")

# Specify the target domain
target_domain = "instagram.com"

# Call the function to enumerate subdomains
get_subdomains(target_domain)