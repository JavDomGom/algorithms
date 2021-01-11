CC=gcc
CFLAGS=-Wall -g
PROGRAM_NAME=quickshort
SRC_FILES=$(PROGRAM_NAME).c
VALGRINDFLAGS=--tool=memcheck --leak-check=full --show-leak-kinds=all -v

build: $(SRC_FILES)
	@echo "`date +'%Y/%m/%d %H:%M:%S'` [$@] Building $(PROGRAM_NAME) binary ..."
	$(CC) $(CFLAGS) -o $(PROGRAM_NAME) $(SRC_FILES)
	@echo "`date +'%Y/%m/%d %H:%M:%S'` [$@] Done!"

valgrind: build
	@echo "`date +'%Y/%m/%d %H:%M:%S'` [$@] Running memory check ..."
	valgrind $(VALGRINDFLAGS) ./$(PROGRAM_NAME) 1 0 2 9 3 8 4 7 5 6 > /dev/null
	@echo "`date +'%Y/%m/%d %H:%M:%S'` [$@] Done!"

clean:
	rm -f $(PROGRAM_NAME)

.PHONY: build clean