# Compiler
CC = clang

# Directories
SRC_DIR = ./src
OBJ_DIR = ./obj
INC_DIR = ./inc

# Output executable
OUTPUT = comp

# Find all .c files in src directory
SRC_FILES := $(wildcard $(SRC_DIR)/*.c)

# Convert each .c file in src directory into corresponding .o file in obj directory
OBJ_FILES := $(patsubst $(SRC_DIR)/%.c,$(OBJ_DIR)/%.o,$(SRC_FILES))

# Compilation flags
CFLAGS = -I$(INC_DIR)

# Default target
all: $(OUTPUT)

# Build the executable by linking the object files
$(OUTPUT): $(OBJ_FILES)
	$(CC) $(OBJ_FILES) -o $(OUTPUT)
	@rm -f $(OBJ_FILES)

# Compile each .c file into a .o file in the obj directory
$(OBJ_DIR)/%.o: $(SRC_DIR)/%.c
	$(CC) $(CFLAGS) -c $< -o $@

# Clean up object files and executable
clean:
	rm -f $(OBJ_FILES) $(OUTPUT)

# Phony targets to avoid conflicts with files named 'all' or 'clean'
.PHONY: all clean