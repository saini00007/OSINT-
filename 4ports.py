#DONE
import asyncio
from concurrent.futures import ProcessPoolExecutor
import nmap
from tqdm import tqdm

def scan_port(host, port):
    nm = nmap.PortScanner()
    nm.scan(host, str(port))
    return port, nm[host]['tcp'][port]['state']

async def scan_ports(host, ports):
    loop = asyncio.get_event_loop()
    with ProcessPoolExecutor() as executor:
        tasks = [
            loop.run_in_executor(executor, scan_port, host, port)
            for port in ports
        ]

        results = []
        for future in tqdm(asyncio.as_completed(tasks), total=len(tasks), desc="Scanning"):
            results.append(await future)

    return {port: state for port, state in results if state == 'open'}

async def main():
    host = '8.8.8.8'
    ports = range(1, 1025)  # Adjust the port range as needed

    open_ports = await scan_ports(host, ports)

    for port, state in open_ports.items():
        print(f"Port {port} is {state}")

if __name__ == "__main__":
    asyncio.run(main())
