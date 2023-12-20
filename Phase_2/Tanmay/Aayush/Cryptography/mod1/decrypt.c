#include <stdio.h>

int main(){
int arr[]={128,322,353,235,336,73,198,332,202,285,57,87,262,221,218,405,335,101,256,227,112,140};
char dec[22];
int i,sus;

for(i=0;i<=22;i++){
    sus=arr[i]%37;
    if(sus<=25){
        printf("%c",'A'+sus);
    }
    else if(sus>=26 && sus<=35){
        printf("%d",sus-26);
    }
    else if(sus==36){
        printf("_");
    }
}




}





