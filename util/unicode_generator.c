#include <stdio.h>
#include <string.h>
#include <stdint.h>
#include <stdlib.h>
#include <time.h>

#define NUM 1000

#define FROM_MASK_ONE_BYTE 0x0
#define TO_MASK_ONE_BYTE 0x7F
#define FROM_MASK_TWO_BYTE 0x80
#define TO_MASK_TWO_BYTE 0x7FF
#define FROM_MASK_THREE_BYTE 0x0800
#define TO_MASK_THREE_BYTE 0xFFFF
#define FROM_MASK_FOUR_BYTE 0x10000
#define TO_MASK_FOUR_BYTE 0x1FFFFF

void generate_unicode_onebyte(uint64_t from, uint64_t to, char * filename);
void generate_unicode_twobyte(uint64_t from, uint64_t to, char * filename);
void generate_unicode_threebyte(uint64_t from, uint64_t to, char * filename);
void generate_unicode_fourbyte(uint64_t from, uint64_t to, char * filename);

// run the main method
int main(int argc, char ** argv){

  time_t t; 
  srand((unsigned) time(&t));

  generate_unicode_onebyte(FROM_MASK_ONE_BYTE, TO_MASK_ONE_BYTE, "oneByte");
  generate_unicode_twobyte(FROM_MASK_TWO_BYTE, TO_MASK_TWO_BYTE, "twoByte");
  generate_unicode_threebyte(FROM_MASK_THREE_BYTE, TO_MASK_THREE_BYTE, "threeByte");
  generate_unicode_fourbyte(FROM_MASK_FOUR_BYTE, TO_MASK_FOUR_BYTE, "fourByte");

}

void generate_unicode_onebyte(uint64_t from, uint64_t to, char * filename){
  char fn1[40] = "";
  strcat(fn1, filename);
  strcat(fn1,".unicode");
  FILE * fp = fopen(fn1, "w");

  for(int idx = from; idx <= to; ++idx){
    fputc(idx,fp); 
  }
  fclose(fp);
}

void generate_unicode_twobyte(uint64_t from, uint64_t to, char * filename){
  char fn1[40] = "";
  strcat(fn1, filename);
  strcat(fn1,".unicode");
  FILE * fp = fopen(fn1, "w");
  for(int idx = from; idx <= to; ++idx){
    fputc(idx,fp); 
    int temp = idx;
    int byte1 = (temp >> 6) | 0xC0;
    int byte2 = (temp & 0x003F) | 0x80;
    fputc(byte1, fp);
    fputc(byte2, fp);
  }
  fclose(fp);
}

void generate_unicode_threebyte(uint64_t from, uint64_t to, char * filename){
  char fn1[40] = "";
  strcat(fn1, filename);
  strcat(fn1,".unicode");
  FILE * fp = fopen(fn1, "w");
  for(int idx = from; idx <= to; ++idx){
    //fputc(idx,fp);
    int temp = idx;
    int byte1 = (temp >> 12) | 0xE0;
    int byte2 = ((temp >> 6) & 0x003F) | 0x80;
    int byte3 = (temp & 0x003F) | 0x80;
    fputc(byte1, fp);
    fputc(byte2, fp);
    fputc(byte3, fp); 
  }
  fclose(fp);
}

void generate_unicode_fourbyte(uint64_t from, uint64_t to, char * filename){
  char fn1[40] = "";
  strcat(fn1, filename);
  strcat(fn1,".unicode");
  FILE * fp = fopen(fn1, "w");
  for(int idx = from; idx <= to; ++idx){
    //fputc(idx,fp); 
    int temp = idx;
    int byte1 = (temp >> 18) | 0xF0;
    int byte2 = ((temp >> 12) & 0x003F) | 0x80;
    int byte3 = ((temp >> 6) & 0x003F) | 0x80;
    int byte4 = (temp & 0x003F) | 0x80;
    fputc(byte1, fp);
    fputc(byte2, fp);
    fputc(byte3, fp);
    fputc(byte4, fp);
  }
  fclose(fp);
}

