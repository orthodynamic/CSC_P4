#include <stdio.h>
#include <string.h>

void word_compression(char[]);

int main()
{   
    int n, j, k;

    printf("How many words do you want to compress?: ");
    scanf("%d", &n);

    char word_list[n][127];

    for (j = 0; j < n; j++)
    {
        printf("words %d: ", j+1);
        scanf("%s", word_list[j]);    
    }

    for (k = 0; k < n; k++)
    {
        word_compression(word_list[k]);
        printf("\n");
    }
    
    
    return 0;
}

void word_compression(char word[])
{
    char uniqueCharacters[127];
    char search_char, unique_count = 0;
    int hashed_index, x, i;
    int letterCount[127];

    for (x = 0; x < 127; x++)
    {
        letterCount[x] = 0;
    }
    

    for (i = 0; i < strlen(word); i++)
    {
        search_char = word[i];
        hashed_index = search_char;
        letterCount[hashed_index]++;

        if (letterCount[hashed_index] == 1)  
        {
            uniqueCharacters[unique_count++] = search_char;
        }
    }

    printf("compressed word: ");
    for ( i = 0; i < unique_count; i++)
    {
        printf("%c", uniqueCharacters[i]);
    }
}
