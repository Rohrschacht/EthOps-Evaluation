#!/usr/bin/env python3

def main(filename: str):
    contract_addresses = []
    with open(filename) as f:
        for line in f:
            if "Contract address:" in line:
                fields = line.split()
                contract_addresses.append(f"\"{fields[-1]}\"")
    print(f"string[] contractAddresses = {{{', '.join(contract_addresses)}}};")

if __name__ == "__main__":
    main("node_output.txt")
