#include "helpers.h"

void colorize(int height, int width, RGBTRIPLE image[height][width])
{
    RGBTRIPLE my_new_color = {
        .rgbtRed = 198,
        .rgbtGreen = 250,
        .rgbtBlue = 76,
    };

    // Change all black pixels to a color of your choosing
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            RGBTRIPLE *pixel = &image[i][j];
            if (pixel->rgbtRed == 0 && pixel->rgbtBlue == 0 && pixel->rgbtGreen == 0)
            {
                *pixel = my_new_color;
            }
        }
    }
}
