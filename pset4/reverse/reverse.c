#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include "wav.h"

int check_format(WAVHEADER header);
int get_block_size(WAVHEADER header);

int main(int argc, char *argv[])
{
    // Ensure proper usage
    if (argc != 3)
    {
        printf("Usage: ./reverse input.wav output.wav\n");
        return 1;
    }

    // Open input file for reading
    FILE *input_wav = fopen(argv[1], "r");
    if (input_wav == NULL)
    {
        printf("Could not open %s.\n", argv[1]);
        return 1;
    }

    // Read header
    WAVHEADER wav_header;
    size_t read_bytes = fread(&wav_header, 1, sizeof(WAVHEADER), input_wav);
    if (read_bytes != sizeof(WAVHEADER))
    {
        printf("Error reading header\n");
        return 1;
    }

    // Use check_format to ensure WAV format
    if (check_format(wav_header) != 0)
    {
        return 1;
    }

    // Open output file for writing
    FILE *output_wav = fopen(argv[2], "w");
    if (output_wav == NULL)
    {
        printf("Could not open file.\n");
        return 1;
    }

    // Write header to output file
    size_t written_bytes = fwrite(&wav_header, 1, read_bytes, output_wav);
    if (written_bytes != read_bytes)
    {
        printf("Error writing to file\n");
        return 1;
    }

    // Use get_block_size to calculate size of block
    int block_size = get_block_size(wav_header);

    // Move the pointer to start of the last block
    fseek(input_wav, -block_size, SEEK_END);

    // While input_wav pointer is not equal to the start of the audio data
    // (or alternatively, is not equal to the end of WAVHEADER)
    while (ftell(input_wav) >= (long) sizeof(WAVHEADER))
    {
        BYTE audio_buffer[block_size];
        size_t read_block_bytes = fread(audio_buffer, 1, block_size, input_wav);
        if (read_block_bytes != (size_t) block_size)
        {
            printf("Error reading block\n");
            return 1;
        }
        size_t write_block_bytes = fwrite(audio_buffer, 1, read_block_bytes, output_wav);
        if (read_block_bytes != write_block_bytes)
        {
            printf("Error writing block");
            return 1;
        }
        // Iteratively move the input_wav pointer to the start of the previous block
        // which is 2 blocks away since the pointer moved by 1 block earlier due to fread
        fseek(input_wav, -2 * block_size, SEEK_CUR);
    }

    fclose(input_wav);
    fclose(output_wav);
}

int check_format(WAVHEADER header)
{
    char *wave = "WAVE";
    if (strncmp((const char *) header.format, wave, 4) == 0)
    {
        return 0;
    }
    return 1;
}

int get_block_size(WAVHEADER header)
{
    int bytes_per_sample = header.bitsPerSample / 8;
    int num_channels = header.numChannels;
    return num_channels * bytes_per_sample;
}
