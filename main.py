# main.py
from skills import run_tests, run_static_checks

def simulate_agent():
    print("=== Agent Skills PoC ===")

    # simulate local execution
    print("\n[Local Context]")
    print("Run Tests:", run_tests("local"))
    print("Static Checks:", run_static_checks("local"))

    # simulate breeze execution
    print("\n[Breeze Context]")
    print("Run Tests:", run_tests("breeze"))
    print("Static Checks:", run_static_checks("breeze"))

if __name__ == "__main__":
    simulate_agent()