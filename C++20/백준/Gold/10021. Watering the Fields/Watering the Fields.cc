#include <vector>
#include <algorithm>
#include <iostream>

struct Edge {
    long cost;
    int a;
    int b;
};

int find(int parents[], int x) {
    if (parents[x] == x) return x;
    parents[x] = find(parents, parents[x]);
    return parents[x];
}

void union_arr(int parents[], int a, int b) {
    const int a_p = find(parents, a);
    const int b_p = find(parents, b);
    if (a_p > b_p) parents[a_p] = b_p;
    else if (a_p < b_p) parents[b_p] = a_p;
}

bool cmp(const Edge& a, const Edge& b) {
    return a.cost < b.cost;
}

int main() {
    int n, c;
    std::cin >> n >> c;

    std::pair<int, int> nodes[n];

    for (int i = 0; i < n; i++) {
        std::cin >> nodes[i].first >> nodes[i].second;
    }

    std::vector<Edge> edges;

    for (int i = 0; i < n; i++) {
        for (int j = i + 1; j < n; j++) {
            const long x_values = nodes[i].first - nodes[j].first;
            const long y_values = nodes[i].second - nodes[j].second;
            const long cost = x_values * x_values + y_values * y_values;

            if (cost >= c) edges.push_back({cost, i, j});
        }
    }

    std::sort(edges.begin(), edges.end(), cmp);

    int parents[2000];
    for (int i = 0; i < n; i++) parents[i] = i;

    int cnt = 0;
    long result = 0l;

    for (const Edge& edge : edges) {
        if (find(parents, edge.a) != find(parents, edge.b)) {
            union_arr(parents, edge.a, edge.b);
            result += edge.cost;
            cnt++;
        }
        if (cnt == n - 1) break;
    }

    if (cnt != n - 1) {
        std::cout << -1;
    } else {
        std::cout << result;
    }
    
    return 0;
}
