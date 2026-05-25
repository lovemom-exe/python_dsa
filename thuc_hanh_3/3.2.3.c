// Name: Nguyễn Minh Hoàng
// Student ID: 202418904
// Class: 763965

/* Thực hành 3 - Phần 2 - Bài 3: tính tổng phần tử mảng bằng con trỏ. */

#include <stdio.h>

#define SO_PHAN_TU_TOI_DA 100

long tinh_tong(const int *mang, int so_phan_tu) {
    long tong = 0;
    const int *con_tro = mang;
    const int *ket_thuc = mang + so_phan_tu;

    while (con_tro < ket_thuc) {
        tong += *con_tro;
        con_tro++;
    }
    return tong;
}

int main(void) {
    int mang[SO_PHAN_TU_TOI_DA];
    int n;

    printf("Nhap so phan tu (1..%d): ", SO_PHAN_TU_TOI_DA);
    if (scanf("%d", &n) != 1 || n < 1 || n > SO_PHAN_TU_TOI_DA) {
        printf("So phan tu khong hop le.\n");
        return 1;
    }

    printf("Nhap %d so nguyen: ", n);
    for (int i = 0; i < n; i++) {
        if (scanf("%d", mang + i) != 1) {
            printf("Du lieu khong hop le.\n");
            return 1;
        }
    }

    printf("Tong cac phan tu = %ld\n", tinh_tong(mang, n));
    return 0;
}
