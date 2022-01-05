#include <stdio.h>
#include <time.h>
#include <string.h>
int main(int argc, char* argv[])
{
    time_t now;
    char* now_c;
    now = time(NULL);
    now_c = ctime(&now);
    char input[350];
    strcpy(input, argv[1]); /*Vorname*/
    strcat(input, ",");
    strcat(input, argv[2]); /*Nachname*/
    strcat(input, ",");
    strcat(input, argv[3]); /*Thema*/
    strcat(input, ",");
    strcat(input, now_c); /*Zeitstempel*/
    FILE *pf;
    pf = fopen("liste.csv","a");
    fputs(input, pf);
    fclose(pf);
    return 0;
}
