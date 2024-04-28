def home():
    import socket
    import concurrent.futures
    import os
    from colorama import Fore
    import colorama
    colorama.init()

    banner = Fore.RED + """
     ██╗ ██████╗ ███████╗███████╗ ██████╗ █████╗ ███╗   ██╗
     ██║██╔═══██╗██╔════╝██╔════╝██╔════╝██╔══██╗████╗  ██║
     ██║██║   ██║███████╗███████╗██║     ███████║██╔██╗ ██║
██   ██║██║   ██║╚════██║╚════██║██║     ██╔══██║██║╚██╗██║
╚█████╔╝╚██████╔╝███████║███████║╚██████╗██║  ██║██║ ╚████║
 ╚════╝  ╚═════╝ ╚══════╝╚══════╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═══╝

                                                           """

    if os.name == 'Windows':
            os.system("cls")
    else:
        os.system("clear")

    def scan(port):
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.settimeout(0.1)
                result = s.connect_ex((target, port))
                if result == 0:
                    return port
        except Exception:
            return None

    if __name__ == "__main__":
        print(banner)

        target = input("IP: ")

        open = []

        print("[0] Slow Scan")
        print("[1] Fast Scan (Can increase the usage of your cpu)")

        choice = input("What do you want to do?>>> ")

        if choice == '0':
            with concurrent.futures.ThreadPoolExecutor(max_workers=1000) as executor:
                future_to_port = {executor.submit(scan, port): port for port in range(1, 65536)}
            for future in concurrent.futures.as_completed(future_to_port):
                port = future_to_port[future]
                result = future.result()
                if result is not None:
                    open.append(result)

        elif choice == '1':
            with concurrent.futures.ThreadPoolExecutor(max_workers=10000) as executor:
                future_to_port = {executor.submit(scan, port): port for port in range(1, 65536)}
                for future in concurrent.futures.as_completed(future_to_port):
                    port = future_to_port[future]
                    result = future.result()
                    if result is not None:
                        open.append(result)

        else:
            print("Invalid Choice.")
            home()

        if open:
            print()
            print("Open Ports:")
            print()
            for port in open:
                print(f"Port {port}")
        else:
            print()
            print("No open ports.")

        print()
        input('Press any key to exit...')

home()
