# Makefile

# Recipe(s)
PKG_NAME = vbox-manager
BIN_NAME = vbox-cli
CC =
CXX = 
CFLAGS =

.PHONY := build run install uninstall clean
.DEFAULT_RULES := help

# Rules/Targets
help:
	## Display verbose help message
	@echo -e "build     : Build and Compile source code into binary"
	@echo -e "run       : Build and run locally"
	@echo -e "install   : Install source code/script/binary into system path"
	@echo -e "uninstall : Remove source code/script/binary/files installed into system path"
	@echo -e "clean     : Clean-up all temporary files generated during building process"
	@echo -e "run_all_tests : Run all tests"

build:
	## Build & Compile source code into binary

run: 
	## Build and Run locally
	### Build source code
	@make -s build

	### Run Locally
	@./src/${BIN_NAME} ${CFLAGS}

install:
	## Install source code/script/binary into system path
	install src/${BIN_NAME} /usr/local/bin

uninstall:
	## Remove source code/script/binary/files installed into system path
	rm -f "$$(which $(BIN_NAME))"

clean:
	## Clean-up all temporary files generated during building process

run_all_tests:
	## Run all unit tests
	@./tests/run_all.py
