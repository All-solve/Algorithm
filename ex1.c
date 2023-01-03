#include <stdio.h>
#include <stdlib.h>
#include <time.h>

void main_building(){
int i, j, random = 0, f_time = 1, count = 0;

char arr[4][17];

for(i = 0; i < 4; i++){
for(j = 0; j < 17; j++){
arr[i][j] = 'n';
}
}

srand(time(NULL));

random = rand() % 4;

i = random;

random = rand() % 17;

j = random;

arr[i][j] = 'F';

while (f_time != 0){
f_time = rand() % 10;

if(count == 0){
for(i = 0; i < 3; i++){
for(j = 0; j < 16; j++){
if(arr[i][j] == 'F'){
arr[i + 1][j] = 'f';
arr[i - 1][j] = 'f';
arr[i][j + 1] = 'f';
arr[i][j - 1] = 'f';
}
}
}
}
else if(count != 0){
for(i = 0; i < 3; i++){
for(j = 0; j < 16; j++){
if(arr[i][j] == 'f'){
arr[i + 1][j] = 'f';
arr[i - 1][j] = 'f';
arr[i][j + 1] = 'f';
arr[i][j - 1] = 'f';
}
}
}
}

count++;
}

printf("%d\n", count);

for(i = 0; i < 4; i++){
printf("\n");
printf("%dth floor\n", 4 - i);
for(j = 0; j < 17; j++){
printf("%c ", arr[i][j]);
}
printf("\n");
}
}

void experiment_building(){

}

int main()
{
int n;

printf("화재발생구역은 어디인가요? (1. 본동, 2. 실험동) : ");

scanf("%d", &n);

if(n == 1){
main_building();
}
else if(n == 2){
experiment_building();
}
else printf("1과 2중 하나를 입력해주세요.");

return 0;
}