# MinorArmAnalyzer

A CPU pipeline analyzer for ARM architecture built on top of the gem5 simulator. It compiles ARM assembly programs, runs them on gem5's MinorCPU model, and produces human-readable cycle-by-cycle execution traces.

## Features

- Compiles ARM assembly files (AArch32 and AArch64) to static binaries
- Runs binaries on gem5 with full debug tracing
- Parses gem5 trace output and maps addresses to disassembled instructions
- Displays cycle-by-cycle pipeline visualization covering: Fetch, Decode, Execute, Memory, Cache, Scoreboard, and Branch Prediction stages
- Includes Draw.io diagrams of the MinorCPU pipeline architecture

## Project structure

```
MinorArmAnalyzer/
├── orchestrator.py     # Main script: compilation, simulation, orchestration
├── dumptohuman.py      # Trace parser and human-readable visualizer
├── config.json         # Pipeline stage label configuration
├── Diagrammi/          # Draw.io diagrams of the MinorCPU pipeline
│   ├── MinorArm.drawio         # Top-level architecture
│   ├── Fetch1/2.drawio         # Fetch stages
│   ├── Decode, Execute         # Decode and execute stages
│   ├── MinorArmIntOp.drawio    # Integer operations
│   ├── MinorArmMulOp.drawio    # Multiplication operations
│   ├── MinorArmDivOp.drawio    # Division operations
│   ├── MinorArmFloatOp.drawio  # Floating-point operations
│   ├── MinorArmBranchOp.drawio # Branch operations
│   └── MinorArmMem1/2, ...     # Memory stages
└── Programmi/          # ARM assembly test programs
    ├── test.s, testfull.s      # Basic and full instruction tests
    ├── testbranch.s/2.s        # Branch instruction tests
    ├── testcond.s              # Conditional instruction tests
    ├── testdiv.s, testmul.s    # Division and multiplication tests
    ├── testldrstr.s            # Load/Store tests
    ├── testmem.s, teststmldm.s # Memory operation tests
    ├── testcachesize.s         # Cache size testing
    ├── testbranchpredictionsize.s # Branch prediction testing
    └── ...
```

## Usage

Install dependencies:
```bash
python3 orchestrator.py --install
```

Compile and simulate an ARM assembly file:
```bash
python3 orchestrator.py <file.s>
```

Visualize execution traces:
```bash
python3 dumptohuman.py <trace_file> [-fs function] [-cs start_cycle] [-ce end_cycle] [-i] [-td 32|64]
```

## Dependencies

- Python 3 with `capstone` library
- gem5 simulator
- ARM cross-compilation toolchain (`arm-linux-gnueabihf-gcc`, `aarch64-linux-gnu-gcc`)

## License

Apache License 2.0 - see [LICENSE](LICENSE) for details.
