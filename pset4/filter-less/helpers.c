#include "helpers.h"
#include <math.h>

// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            BYTE average = round((image[i][j].rgbtRed + image[i][j].rgbtGreen + image[i][j].rgbtBlue) / 3.0);
            image[i][j] = (RGBTRIPLE){
                .rgbtRed = average,
                .rgbtGreen = average,
                .rgbtBlue = average,
            };
        }
    }
    return;
}

// Convert image to sepia
void sepia(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            int sepiaRed = round((0.393 * image[i][j].rgbtRed) + (0.769 * image[i][j].rgbtGreen) + (0.189 * image[i][j].rgbtBlue));
            int sepiaGreen =
                round((0.349 * image[i][j].rgbtRed) + (0.686 * image[i][j].rgbtGreen) + (0.168 * image[i][j].rgbtBlue));
            int sepiaBlue = round((0.272 * image[i][j].rgbtRed) + (0.534 * image[i][j].rgbtGreen) + (0.131 * image[i][j].rgbtBlue));
            image[i][j] = (RGBTRIPLE){
                .rgbtRed = (sepiaRed < UINT8_MAX) ? sepiaRed : UINT8_MAX,
                .rgbtGreen = (sepiaGreen < UINT8_MAX) ? sepiaGreen : UINT8_MAX,
                .rgbtBlue = (sepiaBlue < UINT8_MAX) ? sepiaBlue : UINT8_MAX,
            };
        }
    }
    return;
}

// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0; i < height; i++)
    {
        for (int j = 0, half_width = width / 2; j < half_width; j++)
        {
            RGBTRIPLE tmp = image[i][j];
            image[i][j] = image[i][width - j - 1];
            image[i][width - j - 1] = tmp;
        }
    }
    return;
}

// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{
    RGBTRIPLE temp[height][width];

    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            float pixels_to_average = 0;
            int aggregate_red = 0;
            int aggregate_green = 0;
            int aggregate_blue = 0;

            for (int k = -1; k <= 1; k++)
            {
                for (int l = -1; l <= 1; l++)
                {
                    int new_i = i + k;
                    int new_j = j + l;

                    if (new_i >= 0 && new_i < height && new_j >= 0 && new_j < width)
                    {
                        aggregate_red += image[new_i][new_j].rgbtRed;
                        aggregate_green += image[new_i][new_j].rgbtGreen;
                        aggregate_blue += image[new_i][new_j].rgbtBlue;
                        pixels_to_average++;
                    }
                }
            }

            temp[i][j].rgbtRed = round(aggregate_red / pixels_to_average);
            temp[i][j].rgbtGreen = round(aggregate_green / pixels_to_average);
            temp[i][j].rgbtBlue = round(aggregate_blue / pixels_to_average);
        }
    }
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            image[i][j] = temp[i][j];
        }
    }
    return;
}
