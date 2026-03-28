
from skills import run_skill

def simulate_agent():
    print("=== Agent Skills PoC ===\n")

    print("[Local Context]")
    print("Run Tests:", run_skill("run_tests","local"))
    print("Static Checks:", run_skill("static_checks", "local"))

    print("\n[Breeze Context]")
    print("Run Tests:", run_skill("run_tests","breeze"))
    print("Static Checks:", run_skill("static_checks", "breeze"))


if __name__ == "__main__":
    simulate_agent()