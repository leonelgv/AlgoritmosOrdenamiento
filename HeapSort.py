import math

class HeapSort:
    def hIzq(self, i):
        return 2 * i

    def hDer(self, i):
        return 2 * i + 1;

    def intercambia(self, A, x, y):
        tmp = A[x]
        A[x] = A[y]
        A[y] = tmp

    def MaxHeapify(self, A, i, tamanoHeap):
        L = self.hIzq(i)
        R = self.hDer(i)
        #print (A, i, L, R)
        if (L <= tamanoHeap and A[L]>A[i]):
            posMax = L
        else:
            posMax = i

        if (R <= tamanoHeap and A[R] > A[posMax]):
            posMax = R
        if (posMax != i):
            self.intercambia(A, i, posMax)
            self.MaxHeapify(A, posMax, tamanoHeap)

    def construirHeapMaxIni(self, A, tamanoHeap):
        for i in range(math.ceil(tamanoHeap / 2) - 1, 0, -1):
            self.MaxHeapify(A, i, tamanoHeap)

    def OrdenacionHeapSort(self, A, tamanoHeap):
        self.construirHeapMaxIni(A, tamanoHeap)
        for i in range(len(A[1:]), 1, -1):
            print (A, i)
            self.intercambia(A, 1, i)
            tamanoHeap = tamanoHeap - 1
            self.MaxHeapify(A, 1, tamanoHeap)
        return A

    def ordenar(self, A):
        r = len(A) - 1
        return self.OrdenacionHeapSort(A, r)

#a = [9, 21, 4, 40, 10, 35]
a = [78, 67, 34, 35, 89, 56]
print (a)
b = HeapSort()
print (b.ordenar(a))

#x = range(5, -1, -1)
#for n in x:
#    print (a[n])