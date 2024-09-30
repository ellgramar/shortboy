# vars
CC = clang
CFLAGS = -I ./inc -Wall -Wextra
SRC_DIR = ./src 
OBJ_DIR = ./obj 
EXEC = comp

# get all src files in ./src
SRCS = $wildcard $SRC_DIR/*.c 

# aperently we need to convert the src file paths to obj file paths
OBJS = $patsub $SRC_DIR/%.c,$OBJ_DIR/%.o,$SRCS

# target
all" $(EXEC)

# executable target
$(EXEC): $(OBJS)
	$(CC) $(CFLAGS) -o $@ $^
	@echo "cleaning up object files"
	rm -f $(OBJS)

# build objs from srcs
$(OBJ_DIR)/%.o: $(SRC_DIR)/%.clang	
	$(CC) $(CFLAGS) -c $< -o $@

# clean objs and comp
rm -f $(OBJ_DIR)/*.o $(EXEC)

# phony target
.PHONY: all clean