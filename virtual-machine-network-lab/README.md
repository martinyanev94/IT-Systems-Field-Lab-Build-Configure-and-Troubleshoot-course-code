# Virtual Machine Network Lab

This standard-library Python project models a client, simulated router, and server. It validates the gateway first and then the modeled server path, producing a repeatable JSON connectivity record.

Run the demonstration from the project directory:

```bash
python3 src/main.py
```

Run the tests when pytest is available:

```bash
python3 -m pytest
```

The model is not a live ping tool. A `VERIFIED` result means the supplied topology has consistent modeled interfaces and gateway values. It does not prove a physical cable, operating-system service, or external network is working.
