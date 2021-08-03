#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>

unsigned int uang = 0;


void kerjaKeras(){
	puts("\nkamu kerja lembur bagai kuda");
	printf("sedang bekerja...");
	sleep(2);
	printf("\n");
	uang += 50;
}

void kerjaGakKeras(){
	puts("\nkamu kerja mager-mageran");
	uang += 1;
}

void congrats(){
	char flag[32];
	FILE *fptr;
	fptr = fopen("flag.txt", "r");
	fread(&flag, sizeof(char), 32, fptr);
	puts(flag);
	exit(0);
}

void menuBarang(){
	int pilih;
	puts("\nmau beli apa:");
	puts("[1] - kertas A4   - Rp.       100");
	puts("[2] - nasjep      - Rp.     15000");
	puts("[3] - rumah mewah - Rp.1000000000");
	printf("> ");
	scanf("%d", &pilih);

	if(pilih == 1){
		uang -= 100;
	}
	else if(pilih == 2){
		uang -= 15000;
	}
	else if(pilih == 3){
		uang -= 1000000000;
		if((int)uang > 0){
			puts("ecie dah sukses!");
			congrats();
		}
	}
	else{
		puts("kamu gak sukses.");
		exit(0);
	}
}

void beliBarang(){
	if(uang <= 100){
		puts("uangmu <= 100, kamu gak bisa beli apa-apa.");
	}
	else{
		menuBarang();
	}
}

void skuy(){
	int pilih;
	printf("\nuangmu sekarang %d\n", uang);
	puts("tentukan pilihanmu:");
	puts("[1] kerja keras");
	puts("[2] kerja gak keras");
	puts("[3] beli barang");
	printf("> ");
	scanf("%d", &pilih);
	if(pilih == 1){
		kerjaKeras();
	}
	else if(pilih == 2){
		kerjaGakKeras();
	}
	else if(pilih == 3){
		beliBarang();
	}
	else{
		puts("kamu gak sukses.");
		exit(0);
	}
}

int main(){
	setbuf(stdout, NULL);
	while(1){
		skuy();
	}
	
	return 0;
}