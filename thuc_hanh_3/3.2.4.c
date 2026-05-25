// Name: Nguyễn Minh Hoàng
// Student ID: 202418904
// Class: 763965

/* Thực hành 3 - Phần 2 - Bài 4: tìm độ dài chuỗi bằng con trỏ. */

#include <stdio.h>
#include <string.h>

#define DO_DAI_TOI_DA 256

size_t do_dai_chuoi(const char *chuoi) {
    const char *con_tro = chuoi;
    while (*con_tro != '\0') {
        con_tro++;
    }
    return (size_t)(con_tro - chuoi);
}

int main(void) {
    char chuoi[DO_DAI_TOI_DA];

    printf("Nhap chuoi: ");
    if (fgets(chuoi, sizeof(chuoi), stdin) == NULL) {
        printf("Khong doc duoc chuoi.\n");
        return 1;
    }
    chuoi[strcspn(chuoi, "\n")] = '\0';

    printf("Do dai chuoi = %zu\n", do_dai_chuoi(chuoi));
    return 0;
}
