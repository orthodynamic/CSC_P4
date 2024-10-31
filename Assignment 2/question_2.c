#include <stdio.h>
#include <string.h>

void letterCount(char[], int[]);

int main()
{
    char slogan_1[100], slogan_2[100], slogan_3[100];
    int i, j, count, value;
    int count_array_1[127], count_array_2[127], count_array_3[127];

    printf("Enter Slogan 1: ");
    fgets(slogan_1, sizeof(slogan_1), stdin);
    slogan_1[strcspn(slogan_1, "\n")] = 0; 

    printf("Enter Slogan 2: ");
    fgets(slogan_2, sizeof(slogan_2), stdin);
    slogan_2[strcspn(slogan_2, "\n")] = 0;

    printf("Enter Slogan 3: ");
    fgets(slogan_3, sizeof(slogan_3), stdin);
    slogan_3[strcspn(slogan_3, "\n")] = 0;


    letterCount(slogan_1, count_array_1);
    printf("\n");
    letterCount(slogan_2, count_array_2);
    printf("\n");
    letterCount(slogan_3, count_array_3);
    printf("\n");

    return 0;
}

void letterCount(char array_slogan[],int array_count[127])
{
    char search_char;
    int i, hashed_index, count; 
    char charArray[127];
    int unique_count = 0;

    for (i = 0; i < 127; i++) //initialising array
    {   
        array_count[i] = 0;
    }
    

    for (i = 0; i < strlen(array_slogan); i++)   // This loop Stores the character in the array using hashtable
    {   
        count = 0;
        search_char = array_slogan[i];
        hashed_index = search_char;
        
        array_count[hashed_index] ++;
        
        if (array_count[hashed_index] == 1)
        {
            charArray[unique_count++] = search_char;
        }
    }
    
  
    printf("for '%s' : { ", array_slogan); 
    
    for (i = 0; i < unique_count; i++) // This loop deals with the output
    {
        hashed_index = charArray[i];
        
        if (hashed_index != 32)
        {
            if (i == unique_count - 1)
            {
                printf("%c : %d } ", charArray[i], array_count[hashed_index]);
            }
            else
            {
                printf("%c : %d, ", charArray[i], array_count[hashed_index]);
            }
        }    
    }
}
