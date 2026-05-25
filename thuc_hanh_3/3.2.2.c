// Name: Nguyễn Minh Hoàng
// Student ID: 202418904
// Class: 763965

/* Thực hành 3 - Phần 2 - Bài 2: tráo đổi hai giá trị bằng con trỏ. */

#include <stdio.h>

void trao_doi(int *so_thu_nhat, int *so_thu_hai) {
    int tam = *so_thu_nhat;
    *so_thu_nhat = *so_thu_hai;
    *so_thu_hai = tam;
}

int main(void) {
    int a;
    int b;

    printf("Nhap so nguyen a: ");
    if (scanf("%d", &a) != 1) {
        printf("Du lieu khong hop le.\n");
        return 1;
    }
    printf("Nhap so nguyen b: ");
    if (scanf("%d", &b) != 1) {
        printf("Du lieu khong hop le.\n");
        return 1;
    }

    printf("Truoc khi trao doi: a = %d, b = %d\n", a, b);
    trao_doi(&a, &b);
    printf("Sau khi trao doi:   a = %d, b = %d\n", a, b);
    return 0;
}
