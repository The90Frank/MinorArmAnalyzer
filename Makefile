PYTHON = python3

.PHONY: install run

install:
	$(PYTHON) -m pip install argparse six capstone
	@echo ""
	@echo "System packages required (install manually):"
	@echo "  apt install mercurial scons swig gcc g++ m4"
	@echo "  apt install gcc-arm-linux-gnueabihf gcc-aarch64-linux-gnu"
	@echo "  apt install binutils-arm-linux-gnueabi libc6-armel-cross"
	@echo "  apt install libgoogle-perftools-dev libncurses5-dev"
	@echo "  apt install libboost-dev zlib1g-dev"
	@echo ""
	@echo "gem5 must be built separately: scons build/ARM/gem5.debug -j4"

run:
	@echo "Usage:"
	@echo "  Compile and simulate: $(PYTHON) aux.py <file.s>"
	@echo "  Visualize trace:      $(PYTHON) dumptohuman.py -f <trace_file>"
