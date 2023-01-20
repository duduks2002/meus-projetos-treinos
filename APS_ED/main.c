#include<stdio.h>
#include<conio.h>
#include<stdlib.h>
#include <time.h>

//quick
void QuickSort(int v[],int tam){
    int j = tam,k;
    if (tam <= 1)
        return;
    else{
        int x = v[0];
        int a = 1;
        int b = tam - 1;
        do{
            while ((a < tam) && (v[a] <= x))
                a++;
            while (v[b] > x)
                b--;
            if (a < b){
                int temp = v[a];
                v[a] = v[b];
                v[b] = temp;
                a++;
                b--;
            }
            //for (k = 0; k < j; k++)
            //    printf("%d ",v[k]);
            printf("\n");
        } while (a <= b);
        v[0] = v[b];
        v[b] = x;
        QuickSort(v,b);
        QuickSort(&v[a], tam - a);
       // for (k=0; k < j; k++)
        //    printf("%d ", v[k]);
        printf("\n");
    }
}
//bubble
void bubbleSort(int v[],int tam) {
    int i, j = tam,k;
    int troca;
    do{
        tam--;
        troca = 0;
        for (i=0;i<tam;i++) {
            if (v[i]>v[i+1]){
                int aux = 0;
                aux = v[i];
                v[i]= v[i+1];
                v[i+1]=aux;
                troca=1;

                printf("\n");
            }
        }
    }while(troca);
    for (k=0;k<j;k++){
        printf("%d ",v[k]);
    }
}
//selection
void selectionSort(int Vet[],int n){

    int Menor, aux;

    for(int i=0;i<n-1;i++){
        Menor=i;
        for(int j=i+1 ; j<n ; j++){
            if(Vet[Menor] > Vet[j])
                Menor=j;
        }
        if(i!=Menor){
            aux=Vet[i];
            Vet[i]=Vet[Menor];
            Vet[Menor]=aux;
        }
    }
}
//insertion
void insertionSort(int vet[],int tamanho){
    int i,j,aux;
    for(j=1;j<tamanho;j++){
        aux=vet[j];
        i=j-1;
        while ((i>=0)&&(vet[i]>aux)){
            vet[i+1]=vet[i];
            i--;
        }
        vet[i+1]=aux;
    }
}

int main(){

    long inicio, fim;

    FILE *file;
    file = fopen("numeros\\aleatorio100uni.txt","r");
    int dados;
    int tamanho=100;

    int VetorBB[tamanho];
    int VetorQK[tamanho];
    int VetorSC[tamanho];
    int VetorIR[tamanho];

    printf("Deseja usar qual tipo de valor? \n\n");
    printf("1- Valores fixos\n");
    printf("2- Valores aleatorios\n");
    int esc;
    scanf("%d",&esc);

    if(esc==1){
        for (int i=0;i<tamanho;i++){
            fscanf(file,"%d",&dados);
            VetorBB[i]=dados;
            VetorQK[i]=dados;
            VetorSC[i]=dados;
            VetorIR[i]=dados;
        }
    }else
        if(esc==2){
            for (int i=0;i<tamanho;i++){
                VetorBB[i]=rand();
                VetorQK[i]=rand();
                VetorSC[i]=rand();
                VetorIR[i]=rand();
            }
        }
    printf("\n\n");

    printf("Qual metodo deseja usar?\n\n");
    printf("1- BubbleSort\n");
    printf("2- QuickSort\n");
    printf("3- SelectionSort\n");
    printf("4- InsertionSort\n");
    int opt;
    scanf("%d",&opt);

    if (opt == 1){
        printf("===================================\n");
        printf("Ordenacao com BubbleSort: \n");
        printf("===================================\n");
        printf("Vetor original: \n");
        for(int i=0;i<tamanho;i++){
            printf("%d - ",VetorBB[i]);
        }
        printf("\n\n");
        printf("-----------------------------------\n");
        printf("Ordenando...\n");
        printf("-----------------------------------\n");

        bubbleSort(VetorBB,tamanho);

        printf("\n\n\n");

    }else
        if(opt == 2){
            printf("===================================\n");
            printf("Ordenacao com QuickSort: \n");
            printf("===================================\n");
            printf("Vetor original: \n");
            for(int i=0;i<tamanho;i++){
                printf("%d - ",VetorQK[i]);
            }
            printf("\n\n");
            printf("-----------------------------------\n");
            printf("Ordenando...\n");
            printf("-----------------------------------\n");

            QuickSort(VetorQK,tamanho);


            for(int i=0;i<tamanho;i++){
                printf("%d ",VetorQK[i]);
            }
            printf("\n\n\n");


        }else
            if(opt == 3){
                printf("===================================\n");
                printf("Ordenacao com SelectionSort: \n");
                printf("===================================\n");
                printf("Vetor original: \n");
                for(int i=0;i<tamanho;i++){
                    printf("%d - ",VetorSC[i]);
                }
                printf("\n\n");
                printf("-----------------------------------\n");
                printf("Ordenando...\n");
                printf("-----------------------------------\n");

                selectionSort(VetorSC,tamanho);

                printf("\n\n\n");
                for(int i=0;i<tamanho;i++){
                    printf("%d ",VetorSC[i]);
                }
                printf("\n\n\n");


            }else
                if(opt == 4){
                    printf("===================================\n");
                    printf("Ordenacao com InsertionSort: \n");
                    printf("===================================\n");
                    printf("Vetor original: \n");
                    for(int i=0;i<tamanho;i++){
                        printf("%d - ",VetorIR[i]);
                    }
                    printf("\n\n");
                    printf("-----------------------------------\n");
                    printf("Ordenando...\n");
                    printf("-----------------------------------\n");
                    inicio = clock();
                    selectionSort(VetorIR,tamanho);
                    fim = clock();
                    printf("\n\n\n");
                    for(int i=0;i<tamanho;i++){
                        printf("%d ",VetorIR[i]);
                    }
                    printf("\n\n\n");
                    printf("\nTempo: %d\n", ((fim - inicio) / (CLOCKS_PER_SEC / 1000)));
                }
    printf("DESEJA CONTINUAR? 1-SIM 2-NAO\n\n");
    int r;
    scanf("%d",&r);
        if(r==1){
            return main();
        }

}


