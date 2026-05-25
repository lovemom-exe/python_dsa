// Name: Nguyễn Minh Hoàng
// Student ID: 202418904
// Class: 763965

/* Thực hành 4 - Phần 2: duyệt mảng bằng con trỏ và in thứ tự đảo ngược. */

#include <stdio.h>

#define SO_PHAN_TU_TOI_DA 100

void in_dao_nguoc(const int *mang, int so_phan_tu) {
    const int *con_tro = mang + so_phan_tu;

    while (con_tro != mang) {
        con_tro--;
        printf("%d ", *con_tro);
    }
    printf("\n");
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

    printf("Mang theo thu tu dao nguoc: ");
    in_dao_nguoc(mang, n);
    return 0;
}
