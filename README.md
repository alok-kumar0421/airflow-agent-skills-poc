# Airflow Agent Skills PoC

## 🔗 PoC Repository
https://github.com/alok-kumar0421/airflow-agent-skills-poc

This is a small Proof of Concept (PoC) built for the **Airflow Contribution & Verification Agent Skills** GSoC project.

## What this PoC does

The idea here is simple — represent common contributor workflows (like running tests or static checks) as reusable "skills", and execute them differently depending on the environment.

For example:
- On local machine → run normal commands
- Inside Breeze → use Breeze commands

## Why this matters

In Airflow, contributors often switch between local setups and Breeze. This PoC explores how an agent can handle that automatically by choosing the correct command based on context.

## What’s implemented

- Basic skills:
  - Run tests
  - Run static checks
- Context-aware execution:
  - `local`
  - `breeze`
- Simple simulation of how an agent would use these skills
- Designed using a structured skill mapping (extensible for future workflows)
- Easily adaptable to additional contributor tasks beyond tests and checks

## How it works

- `skills.py` contains the core logic (each skill returns a command)
- `main.py` simulates how an agent would call these skills

## How to run

```bash
python main.py
```
## Future Scope

- Add more contributor workflows (e.g., DAG validation, integration tests)
- Integrate dynamic command extraction from Breeze CLI
- Extend to automated execution instead of simulation