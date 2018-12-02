class MergeSort:
    def CrearSubArreglo(self, A, indIzq, indDer):
        return A[indIzq:indDer + 1]

    def Merge(self, A, p, q, r):
        Izq = self.CrearSubArreglo(A, p, q)
        Der = self.CrearSubArreglo(A, q + 1, r)
        i = 0
        j = 0
        for k in range(p, r + 1):
            if(j >= len(Der)) or (i < len(Izq) and Izq[i] < Der[j]):
                A[k] = Izq[i]
                i = i + 1
            else:
                A[k] = Der[j]
                j = j + 1

    def MergeSort(self, A, p, r):
        if r - p > 0:
            q = int((p + r) / 2)
            self.MergeSort(A, p, q)
            self.MergeSort(A, q + 1, r)
            self.Merge(A, p, q, r)
        return A

    def ordenar(self, A):
        p = 0
        r = len(a) - 1
        q = int((p + r) / 2)
        return self.MergeSort(A, p, r)

a = [78, 67, 34, 35, 89, 56]
print (a)
b = MergeSort()
print (b.ordenar(a))


