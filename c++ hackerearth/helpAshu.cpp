#include<bits/stdc++.h>
#define ll long long
#define M 1000000007
#define testfor(T) ll T; cin>>T; while(T--)
using namespace std;
void quickstart()
{
#ifndef ONLINE_JUDGE
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif
	ios_base::sync_with_stdio(0);
}

void buildTreeEven(int *arr, int *tree, int start, int end, int treeIndex) {
	if (start == end) {
		tree[treeIndex] = arr[start] % 2 == 0 ? 1 : 0;
		return;
	}
	int mid = (start + end) / 2;
	buildTreeEven(arr, tree, start, mid, treeIndex * 2);
	buildTreeEven(arr, tree, mid + 1, end, treeIndex * 2 + 1);
	tree[treeIndex] = tree[treeIndex * 2] + tree[treeIndex * 2 + 1];
	return;
}

void buildTreeOdd(int *arr, int *tree, int start, int end, int treeIndex) {
	if (start == end) {
		tree[treeIndex] = arr[start] % 2 == 1 ? 1 : 0;
		return;
	}
	int mid = (start + end) / 2;
	buildTreeOdd(arr, tree, start, mid, treeIndex * 2);
	buildTreeOdd(arr, tree, mid + 1, end, treeIndex * 2 + 1);
	tree[treeIndex] = tree[treeIndex * 2] + tree[treeIndex * 2 + 1];
	return;
}

void updateOdd(int *arr, int *tree, int start, int end, int index, int value, int treeIndex) {
	if (start == end) {
		arr[index] = value;
		tree[treeIndex] = value % 2 == 1 ? 1 : 0;
		return;
	}
	int mid = (start + end) / 2;
	if (mid < index) {
		updateOdd(arr, tree, mid + 1, end, index, value, treeIndex * 2 + 1);
	} else {
		updateOdd(arr, tree, start, mid, index, value, treeIndex * 2);
	}
	tree[treeIndex] = tree[treeIndex * 2] + tree[treeIndex * 2 + 1];
}

void updateEven(int *arr, int *tree, int start, int end, int index, int value, int treeIndex) {
	if (start == end) {
		arr[index] = value;
		tree[treeIndex] = value % 2 == 0 ? 1 : 0;
		return;
	}
	int mid = (start + end) / 2;
	if (mid < index) {
		updateEven(arr, tree, mid + 1, end, index, value, treeIndex * 2 + 1);
	} else {
		updateEven(arr, tree, start, mid, index, value, treeIndex * 2);
	}
	tree[treeIndex] = tree[treeIndex * 2] + tree[treeIndex * 2 + 1];
}

int query(int *tree, int start, int end, int l, int r, int treeIndex) {
	if (start > r || end < l) {
		return 0;
	} else if (start >= l && end <= r) {
		return tree[treeIndex];
	} else {
		int mid = (start + end) / 2;
		int temp1 = query(tree, start, mid, l, r, treeIndex * 2);
		int temp2 = query(tree, mid + 1, end, l, r, treeIndex * 2 + 1);
		return temp1 + temp2;
	}
}

int main()
{
	quickstart();
	int n;
	cin >> n;
	int *arr = new int[n];
	for (int i = 0; i < n; i++) {
		cin >> arr[i];
	}
	int q;
	cin >> q;
	int choice, l, r, index, value;
	int *treeEven = new int[n * 4];
	int *treeOdd = new int[n * 4];
	buildTreeEven(arr, treeEven, 0, n - 1, 1);
	buildTreeOdd(arr, treeOdd, 0, n - 1, 1);

	while (q--) {
		cin >> choice;
		if (choice == 0) {
			cin >> index >> value;
			index -= 1;
			updateEven(arr, treeEven, 0, n - 1, index, value, 1);
			updateOdd(arr, treeOdd, 0, n - 1, index, value, 1);
		} else if (choice == 1) {
			cin >> l >> r;
			l -= 1;
			r -= 1;
			cout << query(treeEven, 0, n - 1, l, r, 1) << endl;
		} else {
			cin >> l >> r;
			l -= 1;
			r -= 1;
			cout << query(treeOdd, 0, n - 1, l, r, 1) << endl;
		}
	}
	return 0;
}
