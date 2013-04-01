#include <stdio.h>

int main(){
	FILE *fp;
	fp = fopen("2013springnumtoname2.txt", "r");

	int c = fgetc(fp);
	int i = 0;
	while(c != EOF){
		if(c == '\r'){
			i++;
		}else{
			putchar(c);
		}
				

		c = fgetc(fp);
	}

}
