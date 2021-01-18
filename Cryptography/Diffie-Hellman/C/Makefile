CC=gcc
CFLAGS=-Wall -g
PROGRAM_NAME=DiffieHellman
SRC_FILES=$(PROGRAM_NAME).c
TST_LIBS=-lcheck -lm -lpthread -lrt -lsubunit -lgmp
TST_DIR=tests
TST_BIN=check_$(PROGRAM_NAME)_tests
TST_FILES=$(addprefix $(TST_DIR)/, *.c)
VALGRINDFLAGS=--tool=memcheck --leak-check=full --show-leak-kinds=all -v

build: $(SRC_FILES)
	@echo "`date +'%Y/%m/%d %H:%M:%S'` [$@] Building $(PROGRAM_NAME) binary ..."
	$(CC) $(CFLAGS) -o $(PROGRAM_NAME) $(SRC_FILES) -lgmp
	@echo "`date +'%Y/%m/%d %H:%M:%S'` [$@] Done!"

build_tst_objects: $(TST_FILES)
	@echo "`date +'%Y/%m/%d %H:%M:%S'` [$@] Building object files for each testing source files ..."
	$(CC) -c $(CFLAGS) $(TST_FILES)
	@echo "`date +'%Y/%m/%d %H:%M:%S'` [$@] Done!"

$(TST_BIN): build_tst_objects
	@echo "`date +'%Y/%m/%d %H:%M:%S'` [$@] Building $(TST_BIN) binary ..."
	$(CC) check_$(PROGRAM_NAME).o $(TST_LIBS) -o $(TST_BIN)
	@echo "`date +'%Y/%m/%d %H:%M:%S'` [$@] Done!"

test: $(TST_BIN)
	@echo "`date +'%Y/%m/%d %H:%M:%S'` [$@] Running unit tests ..."
	./$(TST_BIN)
	@echo "`date +'%Y/%m/%d %H:%M:%S'` [$@] Done!"

valgrind: build
	@echo "`date +'%Y/%m/%d %H:%M:%S'` [$@] Running memory check ..."
	valgrind $(VALGRINDFLAGS) ./$(PROGRAM_NAME) 1 0 2 9 3 8 4 7 5 6 > /dev/null
	@echo "`date +'%Y/%m/%d %H:%M:%S'` [$@] Done!"

clean:
	@echo "`date +'%Y/%m/%d %H:%M:%S'` [$@] Cleaning workdir ..."
	rm -f *.o $(PROGRAM_NAME) check_$(PROGRAM_NAME)_tests
	@echo "`date +'%Y/%m/%d %H:%M:%S'` [$@] Done!"

.PHONY: build clean