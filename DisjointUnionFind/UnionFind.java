package DisjointUnionFind;

import java.util.Scanner;

public class UnionFind {
    // Declaring two arrays to hold parent and rank of each node
    private int[] parent;
    private int[] rank;

    UnionFind(int n){
        /*
         *  Constructor
         *  */
        parent = new int[n];
        rank = new int[n];

        //initializing their values
        for (int i = 0; i < n; i++){
            parent[i] = i;
            rank[i] = 0;
        }
    }

    public int find(int node){
        /*
         *  Find function: searches for the parent of the particular node
         *  If node is the parent if itself it is the leader of the tree
         *  If not, uses path compression to find parent
         * */
        if(node == parent[node]) return node;

        return parent[node] = find(parent[node]);
    }

    public void Union(int u, int v){
        /*
         * Union Function: merge the set to which u belongs to and the set
         * to which v belongs.
         *
         * It attaches lower rank trees to high ranks trees while merging,
         * if ranks are equal it increases teh rank of the tree to which
         * other is joined by one
         *
         * */
        u = find(u);
        v = find(v);

        if (u != v){
            if (rank[u] < rank[v]){
                int temp = u;
                u = v;
                v = temp;
            }

            parent[v] = u;

            if (rank[u] == rank[v])
                rank[u]++;
        }
    }

    public boolean isConnected(int u, int v){
        return true;
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        UnionFind unionFind = new UnionFind(n);

        while (scanner.hasNextInt()) {
            int u = scanner.nextInt();
            int v = scanner.nextInt();

            if (unionFind.isConnected(u, v)) continue;
            unionFind.Union(u, v);

            System.out.println(u + " " + v);
        }
    }
}
