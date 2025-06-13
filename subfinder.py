import subprocess
import re
from urllib.parse import urlparse

# Tách domain nếu user nhập vào URL
def extract_domain(input):
    parsed = urlparse(input)
    if parsed.scheme:
        return parsed.hostname
    return input

# Kiểm tra domain có hợp lệ hay không
def check_valid_domain(domain):
    pattern = re.compile(r"^(?!\-)(?:[a-zA-Z0-9\-]{1,63}\.)+(?:[a-zA-Z]{2,})$")
    return pattern.match(domain) is not None

def run_subfinder(domain):
    try:
        result = subprocess.run(
            ["subfinder", "-d", domain, "-silent"],
            capture_output=True,
            text=True,
            check=True
        )
        if result.stdout.strip():
            print("Các subdomain tìm được:")
            print(result.stdout)
        else:
            print("Không tìm thấy bất cứ subdomain nào")
    except subprocess.CalledProcessError as e:
        print("Lỗi khi chạy subfinder:", e)
        print("Thông báo lỗi:", e.stderr)

if __name__ == "__main__":
    input_str = input("Nhập domain: ")
    domain = extract_domain(input_str)
    if check_valid_domain(domain):
        run_subfinder(domain)
    else:
        print("Vui lòng nhập domain hợp lệ. \t\t\t Ví dụ: http://example.com, example.com, example,...")