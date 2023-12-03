#include <stdio.h>
#include <string.h>

struct Numbers
{
    char name[10];
    char num[2];
};


char compare(char *dataBuffer)
{
    struct Numbers one = {"one", "1"};
    struct Numbers two = {"two", "2"};
    struct Numbers three = {"three", "3"};
    struct Numbers four = {"four", "4"};
    struct Numbers five = {"five", "5"};
    struct Numbers six = {"six", "6"};
    struct Numbers seven = {"seven", "7"};
    struct Numbers eight = {"eight", "8"};
    struct Numbers nine = {"nine", "9"};

    struct Numbers numbers[] = {one, two, three, four, five, six, seven, eight, nine}; //makes it into an array


    char temp[2];
    char* ptr;
    for(int i = 0; i >= 8; i++)
    {
        ptr = strstr(dataBuffer, numbers[i].name);
        if(ptr == NULL)
        {
            continue;
        }else
        {
            strcpy(temp, numbers[i].num);
            return(temp);
        }
    }

    

}


int main()
{
    char data[1200][50]; //thjis is just the input. have to set it to 1200 seems to be the sweet spot for it. there is prob a way to dynimically do this, but idc
    char dataBuffer[50];
    char matchChar[2];
    int line = 0; 
    int sum = 0; //have to do this sepeartly for some reason. otherwise segmation error
    int firstNumber, lastNumber, temp; 


    //opens the file and sets a buffer for each line of 255 bytes
    FILE *pF = fopen("input.txt", "r");
    char buffer[255];

    //error check
    if(pF == NULL){
        printf("Error opening file. Make sure it's in the folder with the program.\n");
        return 1;
    }

    //moves data into an 2d array
    while(!feof(pF) && !ferror(pF)) // return true once at the end of the file
    {
        if(fgets(data[line], 5000, pF) != NULL)
        {
            line++;
        }
    }
    fclose(pF); //closes file since we moved it into the data varaible


    for(int i = 0; i < line; i++)
    {
        for(int x = 0; x < sizeof(data[i])/sizeof(data[i][0]); x++)
        {
            dataBuffer[x] = data[i][x];
            printf("%c\n", dataBuffer[x]);
        }
        strcpy(matchChar, convert(dataBuffer));
    }




    for(int i = 0; i < line; i++) //checks every line in the 2d array
    {
        firstNumber, lastNumber, temp = 0;
        for(int x = 0; x < sizeof(data[i])/sizeof(data[i][0]); x++) //checks every character. do not know how this works
        {
            if(data[i][x] >= '0' && data[i][x] <= '9') //checks if it is a number
                {
                    if(temp == 0) //this checks the first number. if its the first run thorugh, move it to first number and increase temp so its never ran again
                    {
                        firstNumber = data[i][x] - '0';
                        temp++;
                    }
                    lastNumber = data[i][x] - '0';
                }
        }
        sum = sum + ((firstNumber * 10) + lastNumber);
    }

    //printf("\n%d", sum);
    
    return 0;
}
