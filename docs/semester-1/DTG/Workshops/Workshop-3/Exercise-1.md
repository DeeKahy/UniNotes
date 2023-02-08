
!!! info 

    In this workshop we will study the MergeSort sorting algorithm.


```c
#include <stdio.h>
#include <stdlib.h>

void Merge(int L[], int start, int end, int mid);
void MergeSort(int L[], int start, int end);
void printList(int L[], int size);

int main(void){
  int L[] = { 5, 3, 8, 1, 6, 10, 7, 2, 4, 9 };
  int L_size = sizeof(L) / sizeof(L[0]);

  printf("Given list \n");
  printList(L, L_size);

  MergeSort(L, 0, L_size - 1);

  printf("The sorted list \n");
  printList(L, L_size);
  return 0;
}

void Merge(int L[], int start, int end, int mid){
  int i, j, k;
  int n1 = mid - start + 1;
  int n2 = end - mid;
  int Left[n1], Right[n2];

  for (i = 0; i < n1; i++)
    Left[i] = L[start + i];
  for (j = 0; j < n2; j++)
    Right[j] = L[mid + 1 + j];

  i = 0;
  j = 0;
  k = start;
  while (i < n1 && j < n2) {
    if (Left[i] <= Right[j]) {
      L[k] = Left[i];
      i++;
    } else {
      L[k] = Right[j];
      j++;
    }
    k++;
  }

  while (i < n1) {
    L[k] = Left[i];
    i++;
    k++;
  }
  while (j < n2) {
    L[k] = Right[j];
    j++;
    k++;
  }
}

void MergeSort(int L[], int start, int end){
  /*Here goes your code as well*/
  if (start < end) {
    int mid = (start + end) / 2;
    MergeSort(L, start, mid);
    MergeSort(L, mid + 1, end);
    Merge(L, start, end, mid);
  }
}

void printList(int L[], int size){
  int i;
  for (i = 0; i < size; i++)
    printf("%d ", L[i]);
  printf("\n");
}

```
And it returns {1,2,3,4,5,6,7,8,9,10}


