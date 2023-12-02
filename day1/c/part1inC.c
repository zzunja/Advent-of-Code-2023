#include <stdio.h>
#include <ctype.h>

//just wipe this shit. start again. u cna proib do it without a 2d array.

int main()
{
    char data[1000][50]; //thjis is just the input
    int line = 0; 
    long long int sum = 0;
    int firstNumber,lastNumber, temp; //remove temp

    //opens the file and sets a buffer for each line of 255 bytes
    FILE *pF = fopen("input.txt", "r");
    char buffer[255];

    //error check
    if(pF == NULL){
        printf("Error opening file.\n");
        return 1;
    }

    //moves data into an 2d array
    while(!feof(pF) && !ferror(pF)) // return true once at the end of the file
    {
        if(fgets(data[line], 1000, pF) != NULL)
        {
            line++;
        }
    }
    fclose(pF); //closes file since we moved it into the data varaible


    for(int i = 0; i < line; i++) //checks every line 
    {
        temp = 0;
        for(int x = 0; x < sizeof(data[i])/sizeof(data[i][0]); x++) //checks every character. do not know how this works
        {
            printf("%c", data[i][x]);
            if(data[i][x] >= '0' && data[i][x] <= '9') //checks if it is a number
                {
                    if(temp == 0)
                    {
                        firstNumber = data[i][x] - '0';
                        temp++;
                    }
                    lastNumber = data[i][x] - '0';
                    //printf("firstNumber: %d lastNumber: %d data: %c\n", firstNumber, lastNumber, data[i][x]);
                }
            
        }
        sum = sum + (firstNumber + lastNumber);
    }



//printf("%c", data[0][0]); im gonna kms ngl wtf all i had to do was change it to c instad of s

    printf("\n%d", sum);
    return 0;
}