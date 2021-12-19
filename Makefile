.DEFAULT_GOAL := all
.PHONY: all tree1 tree2 clean

all: 
	@echo; echo ----------------------
	@echo make all begin
	@echo This is where the meat is
	@echo make all finished
	@echo ----------------------; echo

tree1:
	@echo; echo ----------------------
	@echo make tree1 begin
	@echo
	g++ -o ./bin/tree1 ./code/tree/tree1.cpp
	@echo
	@echo make tree1 finished
	@echo ----------------------; echo

tree2:
	@echo; echo ----------------------
	@echo make tree2 begin
	@echo
	g++ -o ./bin/tree2 ./code/tree/tree2.cpp
	@echo
	@echo make tree2 finished
	@echo ----------------------; echo

clean:
	@echo; echo ----------------------
	@echo make clean begin
	@echo This is where the meat is
	rm .DS_STORE
	@echo make clean finished
	@echo ----------------------; echo
	
