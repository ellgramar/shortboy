#ifndef STDINC_H
#define STDINC_H

#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <stdbool.h>
#include <string.h>

// globals
extern uint32_t MEMSIZE = 0xffffff;

extern uint16_t ZFLAG = 0b1000000000000000;
extern uint16_t CFLAG = 0b0100000000000000;
extern uint16_t SFLAG = 0b0010000000000000;
extern uint16_t OFLAG = 0b0001000000000000;
extern uint16_t PFLAG = 0b0000100000000000;
extern uint16_t iFLAG = 0b0000010000000000;

#endif