#include <stdio.h>
#include <string.h>

int main()
{
	int type;
  char pass[5];
  char guess[5];
  char guess2[5];
  char j,k;
  
  printf("Enter five digit password: ");
  scanf("%s",pass);
	
  printf("\nEnter the type of your password: ");
  printf("\n1-Just decimal numbers");
  printf("\n2-Just uppercase letters");
  printf("\n3-Just lower case letters");
  printf("\n4-Upper and lower case letters");
  printf("\n5-Letters and numbers\n\n");
  scanf("%d",&type);
	
	if(type==1){
		j='0';
		k='9';
	}
	if(type==2){
		j='A';
		k='Z';
	}
	if(type==3){
		j='a';
		k='z';
	}
	if(type==4){
		j='A';
		k='z';
	}
	if(type==5){
		j='0';
		k='z';
	}
  fflush(stdin);  
  for(guess[0]=j;guess[0]<=k;guess[0]++){
  	for(guess[1]=j;guess[1]<=k;guess[1]++){
	    for(guess[2]=j;guess[2]<=k;guess[2]++){
	    	for(guess[3]=j;guess[3]<=k;guess[3]++){
   		    for(guess[4]=j;guess[4]<=k;guess[4]++){
	    		  printf("\t\t\t\t\t<============= %c%c%c%c%c  =============>\n",guess[0],guess[1],guess[2],guess[3],guess[4]);
			      if( strncmp(guess,pass,5)==0 ){
    	    		printf("\nYour passaword: %c%c%c%c%c",guess[0],guess[1],guess[2],guess[3],guess[4]);
        	  	return(0);
        		}
         	}
        }
      }
    }
  }
	
return(0);
}
