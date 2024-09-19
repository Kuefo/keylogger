import psutil

def detect_keylogger(): # Main function
    # List of suspicious process names that could belong to keyloggers
    suspicious_processes = ['keylogger', 'logkeys', 'xinput']

    # Iterate through running processes
    for proc in psutil.process_iter(['pid', 'name']):
        try:
            # Check if process name matches any of the suspicious names
            process_name = proc.info['name'].lower()
            if any(susp_name in process_name for susp_name in suspicious_processes):
                print(f"[!] Suspicious process detected: {process_name} (PID: {proc.info['pid']})")
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass

# Run the detector
if __name__ == "__main__":
    print("[+] Running keylogger detection...")
    detect_keylogger()
    print("[+] Scan complete.")