#include <stdio.h>
#include <string.h>
#include <stdint.h>
#include <stdlib.h>
#include <time.h>

#define NUM 1000

#define MASK_ONE_BYTE   0xFF
#define MASK_TWO_BYTE   0xFFFF
#define MASK_THREE_BYTE 0xFFFFFF
#define MASK_FOUR_BYTE  0xFFFFFFFF
#define MASK_FIVE_BYTE  0xFFFFFFFFFF
#define MASK_SIX_BYTE   0xFFFFFFFFFFFF
#define MASK_SEVEN_BYTE 0xFFFFFFFFFFFFFF
#define MASK_EIGHT_BYTE 0xFFFFFFFFFFFFFFFF

void generate_random_uint64(uint64_t, char*);

// run the main method
int main(int argc, char ** argv){

  time_t t; 
  srand((unsigned) time(&t));

  // generate uint64's
  generate_random_uint64(MASK_ONE_BYTE, "oneByte");
  generate_random_uint64(MASK_TWO_BYTE, "twoByte");
  generate_random_uint64(MASK_THREE_BYTE, "threeByte");
  generate_random_uint64(MASK_FOUR_BYTE, "fourByte");
  generate_random_uint64(MASK_FIVE_BYTE, "fiveByte");
  generate_random_uint64(MASK_SIX_BYTE, "sixByte");
  generate_random_uint64(MASK_SEVEN_BYTE, "sevenByte");
  generate_random_uint64(MASK_EIGHT_BYTE, "eightByte");

}

// generate random longs to a file
void
generate_random_uint64(uint64_t mask, char * filename){
  char fn1[40] = "";
  char fn2[40] = "";
  strcat(fn1, filename);
  strcat(fn2, filename);
  strcat(fn1,".numbers");
  strcat(fn2, ".json.numbers");
  FILE * fp = fopen(fn1, "w");
  FILE * fp2 = fopen(fn2, "w");
  fprintf(fp2, "%s\n", "{ \"numbers\":{");
  uint64_t randy = 0x0;
  for(int idx = 0; idx < NUM; ++idx){
    randy = 0x0;
    randy = rand();
    randy = randy << 32;
    randy = (randy | rand()) & mask;
    fprintf(fp, "%llu\n", randy);
    fprintf(fp2, "\"i%d\" = %llu\n", idx, randy);
  }
  fprintf(fp2, "%s", "}}\n");
  fclose(fp);
  fclose(fp2);
}
