/*
문제
수 N개가 주어졌을 때, i번째 수부터 j번째 수까지 합을 구하는 프로그램을
작성하시오.

입력
첫째 줄에 수의 개수 N과 합을 구해야 하는 횟수 M이 주어진다. 둘째 줄에는 N개의
수가 주어진다. 수는 1,000보다 작거나 같은 자연수이다. 셋째 줄부터 M개의 줄에는
합을 구해야 하는 구간 i와 j가 주어진다.

출력
총 M개의 줄에 입력으로 주어진 i번째 수부터 j번째 수까지 합을 출력한다.

제한
1 ≤ N ≤ 100,000
1 ≤ M ≤ 100,000
1 ≤ i ≤ j ≤ N
*/

#include <stdio.h>
#include <stdlib.h>

int main() {
  int N, M;
  scanf("%d %d", &N, &M);

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