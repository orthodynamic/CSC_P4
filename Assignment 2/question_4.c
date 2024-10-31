#include <stdio.h>
#include <string.h>

char* BubbleSort(char[]);

int main()
{
    int n, i, j, flag, array_index = 0;
    char current_word[100];
    char array[100][100];  // Set array size to a fixed value as a buffer
    char sorted_word[100], other_word[100];

    printf("Enter the number of transactions: ");
    scanf("%d", &n);

    char transactions[n][100];

    for (i = 0; i < n; i++)
    {
        printf("Enter Transaction %d: ", i+1);
        scanf("%s", transactions[i]);
    }
    
    printf("\nTHE ANAGRAMS:\n");

    for (i = 0; i < n; i++)
    {   
        flag = 0;
        strcpy(current_word, transactions[i]);
        strcpy(sorted_word, current_word);
        strcpy(sorted_word, BubbleSort(sorted_word));// Sort the current word for checking

        // Check if this sorted word has already been added to the array
        for (j = 0; j < array_index; j++)
        {
            if (strcmp(sorted_word, array[j]) == 0)
            {
                flag = 1;
                break;
            }
        }
        
        // If the word is unique, add to array and print the group
        if (flag == 0)
        {
            strcpy(array[array_index++], sorted_word);
            printf("[ ");
            for (j = 0; j < n; j++)
            {
                strcpy(other_word, transactions[j]);
                strcpy(other_word, BubbleSort(other_word));
                if (strcmp(sorted_word, other_word) == 0)
                {
                    printf("%s ", transactions[j]);
                }
            }
            printf("]\n");
        }
    }
    
    return 0;
}

char* BubbleSort(char word[])
{
    int i;
    char temp;
    int swap;
    int top = strlen(word) - 1;

    do
    {
        swap = 0;  // Reset swap at the start of each outer iteration
        for (i = 0; i < top; i++)
        {
            if (word[i] > word[i+1])
            {
                temp = word[i+1];
                word[i+1] = word[i];
                word[i] = temp;
                swap = 1;
            }
        }
        top -= 1;
    } while (swap);
    return word;
}

