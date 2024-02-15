/*
문제
N개의 수 A1, A2, ..., AN이 입력으로 주어진다. 총 M개의 구간 i, j가 주어졌을 때, i번째 수부터 j번째 수까지 합을 구하는 프로그램을 작성하시오.

입력
첫째 줄에 수의 개수 N이 주어진다. (1 ≤ N ≤ 100,000) 둘째 줄에는 A1, A2, ..., AN이 주어진다. (-1,000 ≤ Ai ≤ 1,000) 셋째 줄에는 구간의 개수 M이 주어진다. (1 ≤ M ≤ 100,000) 넷째 줄부터 M개의 줄에는 각 구간을 나타내는 i와 j가 주어진다. (1 ≤ i ≤ j ≤ N)

출력
총 M개의 줄에 걸쳐 입력으로 주어진 구간의 합을 출력한다.
*/

#include <stdio.h>
#include <stdlib.h>

int main() {
  int N, M;
  scanf("%d", &N);

  long long int *n = (long long int *)malloc(sizeof(long long int) * N);
  long long int *nsum = (long long int *)malloc(sizeof(long long int) * N);

  for (int i = 0; i < N; i++) {
    scanf("%lld", &n[i]);
    if (i == 0) {
      nsum[i] = n[i];
    } else {
      nsum[i] = nsum[i - 1] + n[i];
    }
  }

  scanf("%d", &M);

  int start, end;
  for (int i = 0; i < M; i++) {
    scanf("%d %d", &start, &end);
    if (start == 1) {
      printf("%lld\n", nsum[end - 1]);

    } else {
      printf("%lld\n", nsum[end - 1] - nsum[start - 2]);
    }
  }

  free(nsum);
  free(n);
  return 0;
}