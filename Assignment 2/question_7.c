#include <stdio.h>
#include <stdlib.h>
#include <time.h>

char block[6][5];

int word_check(char[]);

void display_block(char[]);

int main()
{   
    char id_num[4], choice[6], score = 0;

    printf("Enter you ID: ");
    fgets(id_num, 5, stdin);

    display_block(id_num);

    do
    {
        printf("Enter word to search OR enter END to end program: ");
        scanf("%s", choice);

        if(strcmp(choice, "END") != 0)
        {
            if (word_check(choice) == 1)
            {
                printf("%s is present, Score: %d\n", choice, ++score);
            }
            else
            {
                printf("%s is not present, Score: %d\n", choice, --score);
            }    
        }
        else
        {
            printf("Program ENDED");
        }
    } while (strcmp(choice, "END") != 0);

    return 0;
}

// FUNCTION TO DISPLAY WORD BLOCK

void display_block(char id[])
{
    int i, j, k;
    srand(time(NULL));

    for (i = 0; i < 6; i++) // Populating the block
    {
        for (j = 0; j < 5; j++)
        {   
            block[i][j] = 65 + (rand() % 26); 
        }
        if (i == 5)
        {
            for (k = 0; k < 4; k++)
            {
                 block[i][k] = id[k];
            }
            
        }
        
    }
    
    for (i = 0; i < 6; i++) // Displaying the block
    {   
        printf("-----------------------------------------\n");
        for (j = 0; j < 5; j++)
        {   
            if (j == 4)
            {
                printf("|   %c   |", block[i][j]);
            }
            else
            {
                printf("|   %c   ", block[i][j]);
            }
        }
        printf("\n");
    }
    printf("-----------------------------------------\n");
}

// FUNCTION TO CHECK WORD

int word_check(char word[])
{
    int k, i, j, len, flag, count;

    len = strlen(word);

    for (i = 0; i < 6; i++) // HORIZONTAL CHECK
    {
        for (j = 0; j < 5 - len + 1; j++)
        {
            if (strncmp(&block[i][j], word, len) == 0)
            {
                printf("Found %s horizontally at row %d, starting column %d\n", word, i, j);
                return 1;
            }
            
        }
    }
    for (i = 0; i < 6; i++) // VERTICAL CHECK
    {   
        for (j = 0; j < 6 - len + 1; j++)
        {
            flag = 1; count = 0;
            for (k = j; k < j + len; k++)
            {
                if (word[count++] != block[k][i])
                {
                    flag = 0;
                    break;
                }
            }    
            if (flag == 1)
            {
                return 1;
            }
        }
        
    }
    
    return 0;
}
