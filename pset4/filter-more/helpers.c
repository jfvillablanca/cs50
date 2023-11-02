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

// Detect edges
int gx_kernel[3][3] = {
    {-1, 0, 1},
    {-2, 0, 2},
    {-1, 0, 1},
};

int gy_kernel[3][3] = {
    {-1, -2, -1},
    {0, 0, 0},
    {1, 2, 1},
};

typedef struct
{
    int red;
    int green;
    int blue;
} g;
void edges(int height, int width, RGBTRIPLE image[height][width])
{
    RGBTRIPLE temp[height][width];

    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            g gx = {
                .red = 0,
                .green = 0,
                .blue = 0,
            };

            g gy = {
                .red = 0,
                .green = 0,
                .blue = 0,
            };

            for (int k = -1; k <= 1; k++)
            {
                for (int l = -1; l <= 1; l++)
                {
                    int new_i = i + k;
                    int new_j = j + l;
                    RGBTRIPLE current_pixel;

                    // Treat all pixels beyond the borders to having zero RGB values
                    if (!(new_i >= 0 && new_i < height && new_j >= 0 && new_j < width))
                    {
                        current_pixel = (RGBTRIPLE){
                            .rgbtRed = 0,
                            .rgbtGreen = 0,
                            .rgbtBlue = 0,
                        };
                    }
                    else
                    {
                        current_pixel = image[new_i][new_j];
                    }

                    gx.red += current_pixel.rgbtRed * gx_kernel[k + 1][l + 1];
                    gx.green += current_pixel.rgbtGreen * gx_kernel[k + 1][l + 1];
                    gx.blue += current_pixel.rgbtBlue * gx_kernel[k + 1][l + 1];

                    gy.red += current_pixel.rgbtRed * gy_kernel[k + 1][l + 1];
                    gy.green += current_pixel.rgbtGreen * gy_kernel[k + 1][l + 1];
                    gy.blue += current_pixel.rgbtBlue * gy_kernel[k + 1][l + 1];
                }
            }

            int edge_red = round(sqrt(pow(gx.red, 2) + pow(gy.red, 2)));
            int edge_green = round(sqrt(pow(gx.green, 2) + pow(gy.green, 2)));
            int edge_blue = round(sqrt(pow(gx.blue, 2) + pow(gy.blue, 2)));
            temp[i][j] = (RGBTRIPLE){
                .rgbtRed = (edge_red < UINT8_MAX) ? edge_red : UINT8_MAX,
                .rgbtGreen = (edge_green < UINT8_MAX) ? edge_green : UINT8_MAX,
                .rgbtBlue = (edge_blue < UINT8_MAX) ? edge_blue : UINT8_MAX,
            };
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
