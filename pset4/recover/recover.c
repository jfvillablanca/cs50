#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>

const int BLOCK_SIZE = 512;
typedef uint8_t BYTE;

int main(int argc, char *argv[])
{
    if (argc != 2)
    {
        printf("Usage: ./recover IMAGE\n");
        return 1;
    }

    // Open input file
    FILE *file = fopen(argv[1], "r");
    if (file == NULL)
    {
        printf("Could not open %s.\n", argv[1]);
        return 1;
    }

    char filename[8];
    FILE *img = NULL;

    BYTE buffer[BLOCK_SIZE];
    int jpg_count = 0;
    while (fread(buffer, 1, BLOCK_SIZE, file) == BLOCK_SIZE)
    {
        // If start of new JPEG
        if (buffer[0] == 0xff && buffer[1] == 0xd8 && buffer[2] == 0xff && (buffer[3] & 0xf0) == 0xe0)
        {
            if (jpg_count > 0)
            {
                fclose(img);
            }

            sprintf(filename, "%03i.jpg", jpg_count);
            img = fopen(filename, "w");
            if (img == NULL)
            {
                printf("Could not open %s.\n", filename);
                return 1;
            }
            fwrite(buffer, 1, BLOCK_SIZE, img);
            jpg_count++;
        }
        // Else, proceed writing to the same img file buffer
        else
        {
            if (img != NULL)
            {
                fwrite(buffer, 1, BLOCK_SIZE, img);
            }
        }
    }
    fclose(file);
    if (img != NULL)
    {
        fclose(img);
    }
}
