
#include <stdio.h>
#include <stdlib.h>

#define N 6

void bfs(int adj[][N], int start)
{
    int visited[N] = {0};
    int queue[N];
    int front = 0, rear = 0;

    visited[start] = 1;
    queue[rear++] = start;

    while (front < rear) {
        int u = queue[front++];
        printf("%c ", 'A' + u);

        for (int v = 0; v < N; ++v) {
            if (adj[u][v] && !visited[v]) {
                visited[v] = 1;
                queue[rear++] = v;
            }
        }
    }
    printf("\n");
}

int main(void)
{
    int adj[N][N] = {{0}};

    adj[0][1] = adj[0][2] = 1; 
    adj[1][0] = adj[1][3] = adj[1][4] = 1; 
    adj[2][0] = adj[2][5] = 1; 
    adj[3][1] = 1; 
    adj[4][1] = adj[4][5] = 1; 
    adj[5][2] = adj[5][4] = 1; 

    bfs(adj, 0); 

    return 0;
}