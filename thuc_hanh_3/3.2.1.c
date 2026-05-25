// Name: Nguyễn Minh Hoàng
// Student ID: 202418904
// Class: 763965

/* Thực hành 3 - Phần 2 - Bài 1: cộng hai số bằng con trỏ. */

#include <stdio.h>

int cong_hai_so(const int *so_thu_nhat, const int *so_thu_hai) {
    return *so_thu_nhat + *so_thu_hai;
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

    printf("Tong cua %d va %d = %d\n", a, b, cong_hai_so(&a, &b));
    return 0;
}
