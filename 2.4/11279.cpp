#include <stdio.h>
#include <stdlib.h>
#include <string.h>

class HeapSort {
private:
	int heap[100002];
	int count;
public:
	HeapSort() {
		memset(this->heap, 0, sizeof(int) * 129);
		this->count = 0;
	}

	void insert(int num) {
		this->heap[++count] = num;
		int tmp_state = count;
		while (tmp_state != 1 && heap[tmp_state / 2] < num) {
			heap[tmp_state] = heap[tmp_state / 2];
			tmp_state /= 2;
		}
		this->heap[tmp_state] = num;
	}

	int pop() {
		int value = heap[1];
		int tmp = heap[count--];
		int tmp_p = 1;
		int tmp_c = 2;
		while (tmp_c <= count) {
			if ((tmp_c < count) && heap[tmp_c + 1] > heap[tmp_c]) {
				tmp_c++;
			}
			if (tmp > heap[tmp_c]) break;
			heap[tmp_p] = heap[tmp_c];
			tmp_p = tmp_c;
			tmp_c = 2 * tmp_c;
		}
		heap[tmp_p] = tmp;
		return value;
	}

	void printAll() {
		for (int i = this->count; i >= 1; i--) {
			printf("%d\n", this->pop());
		}
	}
};

int main() {
	HeapSort hs;
	int t;
	int input;
	scanf("%d", &t);

	for (int i = 0; i < t; i++) {
		scanf("%d", &input);
		hs.insert(input);
	}
	hs.printAll();
}