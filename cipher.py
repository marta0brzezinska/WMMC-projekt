""""
Implementacja szyfru blokowego zaprojektownego w ramach projektu z przedmiotu WMMC.

Marta Brzezińska
Kinga Kawczyńska
"""
from type_transformations import *

s_box = [
    [27, 157, 79, 88, 120, 130, 61, 102, 165, 77, 199, 95, 140, 216, 7, 138, 58, 178, 100, 57, 78, 39, 41, 255, 17, 126,
     148, 220, 111, 45, 176, 179, 182, 190, 49, 129, 156, 158, 63, 184, 206, 223, 104, 75, 28, 233, 226, 222, 251, 125,
     105, 177, 65, 15, 137, 93, 249, 225, 38, 252, 218, 180, 247, 103, 241, 149, 101, 213, 9, 16, 133, 50, 127, 44, 168,
     232, 30, 248, 236, 141, 1, 239, 2, 145, 244, 29, 139, 90, 59, 23, 175, 253, 219, 152, 215, 37, 36, 62, 164, 33,
     201, 56, 237, 18, 96, 254, 97, 35, 245, 0, 12, 11, 52, 147, 48, 124, 211, 54, 181, 159, 5, 40, 228, 99, 163, 187,
     67, 203, 91, 8, 13, 32, 10, 198, 109, 55, 94, 106, 153, 66, 81, 110, 231, 64, 51, 235, 183, 60, 122, 191, 212, 6,
     116, 118, 74, 185, 80, 117, 107, 46, 186, 4, 246, 250, 166, 169, 86, 171, 238, 229, 217, 234, 195, 114, 3, 172, 72,
     132, 230, 92, 108, 128, 123, 21, 189, 167, 43, 205, 113, 173, 34, 144, 19, 208, 73, 134, 240, 243, 135, 151, 207,
     197, 98, 196, 115, 160, 150, 155, 14, 143, 22, 53, 82, 84, 174, 194, 85, 136, 89, 146, 210, 209, 68, 200, 112, 214,
     170, 221, 31, 24, 83, 161, 26, 70, 202, 188, 204, 227, 242, 193, 69, 20, 121, 131, 42, 154, 76, 47, 71, 192, 162,
     87, 224, 25, 119, 142],
    [234, 68, 152, 34, 190, 22, 26, 97, 35, 172, 162, 189, 169, 89, 49, 77, 127, 163, 145, 210, 201, 2, 212, 142, 122,
     15, 81, 237, 116, 165, 228, 119, 76, 60, 103, 52, 37, 42, 131, 10, 74, 8, 133, 65, 101, 209, 167, 183, 221, 61,
     153, 112, 45, 75, 231, 239, 222, 246, 206, 208, 39, 91, 136, 59, 82, 11, 5, 134, 30, 174, 193, 79, 211, 232, 247,
     29, 186, 233, 67, 124, 255, 157, 218, 205, 12, 197, 203, 62, 241, 105, 121, 227, 115, 220, 177, 31, 90, 117, 150,
     93, 213, 176, 229, 48, 17, 168, 50, 28, 36, 138, 107, 154, 88, 230, 178, 19, 236, 214, 70, 120, 7, 47, 170, 217,
     199, 151, 57, 166, 24, 4, 216, 20, 251, 144, 14, 32, 100, 85, 16, 243, 187, 198, 92, 139, 191, 94, 21, 192, 223,
     235, 83, 114, 242, 250, 113, 125, 224, 0, 25, 182, 110, 54, 248, 238, 73, 96, 95, 254, 71, 141, 148, 188, 130, 156,
     1, 98, 56, 132, 18, 137, 143, 111, 66, 200, 161, 149, 104, 64, 123, 108, 215, 87, 118, 225, 204, 184, 253, 63, 173,
     53, 109, 202, 44, 13, 3, 86, 180, 240, 129, 69, 194, 140, 23, 106, 249, 185, 164, 195, 158, 55, 196, 179, 46, 84,
     80, 40, 38, 58, 128, 245, 51, 181, 102, 175, 252, 6, 33, 72, 27, 160, 126, 226, 207, 219, 41, 159, 155, 9, 244,
     171, 135, 78, 99, 146, 43, 147],
    [160, 35, 244, 104, 180, 110, 159, 103, 161, 165, 229, 29, 254, 25, 54, 95, 73, 23, 112, 206, 127, 28, 218, 184, 87,
     24, 46, 192, 228, 63, 126, 176, 116, 107, 0, 239, 197, 115, 51, 124, 125, 207, 251, 60, 155, 147, 231, 216, 236,
     204, 80, 234, 72, 164, 36, 18, 179, 131, 68, 148, 12, 201, 2, 145, 214, 156, 193, 92, 69, 122, 237, 121, 136, 191,
     59, 157, 210, 162, 200, 11, 248, 212, 17, 255, 243, 49, 77, 89, 27, 222, 183, 166, 209, 203, 144, 93, 85, 37, 75,
     106, 113, 190, 5, 47, 9, 65, 119, 253, 163, 111, 137, 142, 186, 230, 181, 16, 117, 4, 173, 178, 57, 146, 43, 102,
     205, 105, 91, 187, 10, 135, 232, 129, 79, 194, 132, 31, 208, 1, 252, 38, 169, 39, 21, 50, 211, 224, 13, 141, 62,
     101, 196, 109, 149, 56, 94, 26, 247, 41, 74, 185, 249, 15, 213, 120, 250, 108, 97, 128, 202, 66, 139, 140, 64, 52,
     71, 177, 182, 100, 3, 242, 233, 143, 76, 199, 83, 19, 246, 221, 6, 138, 215, 48, 8, 32, 44, 130, 86, 134, 118, 189,
     154, 240, 171, 220, 235, 61, 195, 153, 99, 175, 227, 22, 241, 40, 14, 225, 88, 170, 82, 30, 34, 198, 158, 114, 90,
     53, 55, 81, 20, 245, 188, 217, 42, 150, 226, 172, 70, 133, 98, 174, 152, 67, 84, 167, 58, 7, 123, 96, 168, 78, 238,
     45, 151, 219, 223, 33],
    [243, 100, 197, 78, 205, 11, 15, 215, 133, 80, 61, 174, 226, 168, 221, 224, 248, 135, 223, 17, 125, 29, 35, 84, 13,
     161, 209, 216, 160, 58, 149, 18, 63, 115, 120, 69, 214, 107, 225, 60, 141, 79, 128, 46, 181, 152, 1, 159, 242, 98,
     47, 43, 207, 245, 190, 12, 184, 72, 28, 157, 244, 182, 94, 191, 129, 113, 33, 178, 219, 99, 230, 165, 180, 74, 233,
     3, 105, 37, 183, 227, 203, 234, 145, 91, 83, 156, 123, 199, 236, 81, 51, 247, 4, 102, 73, 76, 44, 163, 171, 108,
     172, 70, 5, 146, 88, 132, 9, 196, 106, 82, 53, 118, 71, 158, 90, 220, 201, 67, 42, 142, 6, 117, 62, 127, 85, 148,
     188, 228, 130, 235, 255, 124, 239, 147, 176, 54, 250, 126, 164, 212, 240, 232, 39, 249, 95, 36, 48, 136, 75, 109,
     30, 64, 38, 169, 140, 177, 119, 16, 114, 210, 25, 14, 218, 198, 139, 7, 179, 238, 32, 19, 251, 189, 211, 104, 144,
     49, 40, 167, 2, 8, 206, 111, 59, 112, 237, 151, 31, 175, 52, 143, 166, 154, 246, 103, 45, 254, 173, 92, 241, 252,
     50, 195, 193, 187, 138, 204, 134, 68, 55, 97, 10, 26, 231, 96, 131, 150, 23, 41, 57, 217, 22, 186, 21, 34, 153,
     155, 137, 89, 208, 27, 213, 77, 93, 202, 110, 229, 162, 0, 87, 170, 222, 253, 185, 66, 121, 192, 200, 56, 101, 86,
     116, 194, 24, 122, 20, 65],
    [164, 12, 221, 173, 162, 53, 232, 195, 66, 135, 43, 243, 110, 246, 78, 92, 20, 155, 165, 222, 181, 113, 58, 250, 30,
     255, 112, 116, 26, 99, 56, 81, 41, 120, 80, 157, 184, 182, 242, 115, 117, 183, 194, 138, 241, 31, 237, 124, 82,
     215, 28, 127, 186, 153, 75, 201, 140, 245, 7, 67, 68, 137, 223, 19, 180, 46, 147, 211, 154, 196, 213, 74, 34, 139,
     219, 109, 84, 178, 108, 39, 49, 73, 11, 244, 36, 65, 158, 70, 144, 42, 23, 6, 168, 175, 205, 240, 131, 227, 202,
     177, 174, 102, 18, 217, 85, 199, 163, 253, 29, 61, 247, 126, 214, 57, 216, 151, 171, 148, 62, 54, 59, 169, 88, 3,
     136, 114, 94, 129, 130, 119, 252, 156, 4, 79, 190, 161, 32, 204, 249, 191, 150, 210, 89, 118, 234, 48, 9, 37, 248,
     166, 40, 123, 45, 1, 188, 167, 187, 125, 233, 122, 51, 159, 134, 35, 212, 22, 21, 132, 218, 152, 160, 38, 193, 128,
     47, 230, 228, 179, 206, 251, 60, 200, 64, 107, 17, 27, 238, 197, 76, 225, 97, 86, 87, 101, 185, 25, 100, 103, 208,
     224, 2, 254, 33, 145, 121, 90, 95, 55, 231, 24, 77, 96, 133, 226, 14, 69, 104, 16, 50, 149, 91, 203, 0, 13, 111,
     105, 143, 235, 106, 15, 220, 189, 8, 63, 239, 141, 172, 44, 176, 198, 142, 192, 10, 229, 98, 83, 209, 207, 146, 52,
     170, 72, 5, 93, 236, 71],
    [39, 21, 41, 223, 194, 108, 219, 216, 92, 244, 150, 187, 120, 198, 10, 170, 146, 106, 153, 171, 143, 118, 66, 165,
     76, 222, 241, 91, 180, 72, 246, 152, 68, 81, 1, 245, 28, 204, 24, 224, 26, 230, 84, 238, 47, 250, 193, 27, 199,
     243, 114, 97, 103, 32, 188, 37, 48, 63, 237, 29, 202, 44, 166, 55, 240, 102, 79, 220, 248, 77, 253, 49, 71, 93, 54,
     99, 251, 173, 136, 167, 117, 119, 203, 208, 177, 232, 33, 183, 130, 14, 206, 144, 42, 60, 217, 160, 20, 168, 239,
     94, 254, 154, 18, 195, 184, 110, 5, 227, 122, 134, 73, 205, 53, 52, 12, 90, 98, 51, 242, 197, 56, 16, 234, 23, 70,
     185, 133, 124, 45, 4, 138, 176, 121, 116, 218, 213, 221, 145, 236, 115, 211, 22, 86, 192, 35, 107, 212, 111, 58,
     209, 0, 62, 65, 11, 181, 164, 155, 36, 142, 9, 149, 255, 127, 129, 225, 101, 15, 74, 156, 182, 50, 34, 61, 128,
     159, 6, 40, 67, 214, 109, 228, 17, 43, 126, 112, 59, 19, 2, 161, 57, 233, 25, 210, 141, 247, 8, 163, 226, 113, 125,
     196, 80, 235, 178, 7, 179, 137, 201, 172, 30, 174, 82, 186, 249, 13, 189, 75, 140, 252, 215, 83, 87, 100, 207, 38,
     123, 104, 169, 131, 191, 132, 89, 151, 78, 139, 147, 46, 200, 96, 85, 31, 3, 162, 231, 190, 69, 148, 157, 175, 158,
     105, 229, 88, 135, 64, 95],
    [232, 170, 224, 21, 33, 17, 70, 73, 241, 72, 129, 135, 248, 203, 213, 188, 159, 102, 109, 207, 138, 52, 184, 246,
     249, 233, 128, 106, 9, 57, 110, 181, 141, 243, 199, 31, 119, 204, 193, 174, 139, 77, 186, 165, 94, 137, 8, 168,
     160, 206, 49, 211, 185, 133, 227, 150, 42, 247, 20, 99, 191, 45, 53, 13, 235, 56, 19, 10, 197, 205, 67, 250, 130,
     172, 200, 116, 95, 194, 3, 63, 156, 103, 79, 238, 122, 196, 229, 36, 180, 6, 25, 177, 223, 214, 140, 163, 230, 146,
     132, 88, 29, 75, 22, 15, 237, 11, 12, 164, 40, 208, 155, 167, 89, 234, 91, 219, 44, 145, 231, 96, 98, 221, 202, 27,
     82, 187, 210, 39, 93, 114, 225, 37, 228, 161, 173, 121, 66, 244, 251, 59, 41, 74, 4, 68, 107, 125, 216, 81, 76, 46,
     101, 154, 108, 242, 104, 123, 209, 178, 166, 189, 183, 195, 24, 175, 71, 222, 148, 50, 217, 253, 171, 115, 105,
     240, 55, 30, 62, 14, 131, 134, 212, 124, 5, 136, 111, 100, 182, 201, 245, 47, 252, 18, 90, 78, 2, 157, 143, 120,
     179, 226, 28, 112, 83, 254, 26, 92, 220, 147, 38, 192, 97, 215, 51, 151, 127, 60, 1, 87, 255, 149, 158, 86, 85, 84,
     239, 153, 162, 34, 169, 236, 126, 117, 118, 48, 7, 61, 64, 190, 54, 35, 32, 142, 58, 152, 80, 218, 0, 69, 23, 176,
     65, 144, 113, 198, 43, 16],
    [159, 194, 161, 237, 92, 45, 30, 69, 248, 89, 57, 71, 176, 4, 210, 33, 18, 36, 65, 224, 205, 219, 207, 77, 56, 82,
     94, 11, 51, 6, 220, 131, 8, 73, 170, 19, 158, 97, 132, 111, 150, 183, 246, 20, 253, 74, 162, 126, 233, 154, 255,
     169, 145, 104, 189, 215, 79, 102, 42, 60, 230, 197, 203, 254, 85, 222, 24, 63, 99, 54, 218, 251, 179, 101, 40, 163,
     168, 228, 64, 140, 62, 29, 70, 152, 191, 28, 123, 155, 22, 174, 130, 148, 239, 41, 213, 26, 46, 39, 87, 3, 81, 216,
     5, 226, 108, 86, 49, 201, 34, 103, 114, 76, 118, 61, 245, 234, 156, 66, 15, 231, 116, 43, 187, 172, 13, 1, 115, 10,
     149, 223, 164, 151, 109, 238, 211, 72, 52, 196, 214, 35, 31, 91, 252, 212, 206, 202, 129, 138, 171, 199, 84, 137,
     173, 146, 12, 160, 232, 249, 182, 17, 142, 198, 67, 27, 105, 141, 153, 250, 113, 23, 55, 75, 96, 125, 117, 165,
     107, 127, 144, 244, 133, 240, 236, 25, 221, 241, 14, 38, 88, 21, 2, 181, 204, 147, 135, 48, 208, 139, 80, 100, 78,
     185, 47, 68, 32, 83, 110, 227, 167, 195, 53, 235, 136, 90, 175, 157, 225, 178, 180, 121, 9, 134, 106, 58, 242, 186,
     184, 37, 247, 177, 50, 98, 229, 122, 209, 16, 119, 217, 7, 112, 190, 200, 243, 0, 95, 44, 188, 59, 166, 120, 193,
     143, 124, 93, 128, 192]
]

inv_s_box = [
    [109, 80, 82, 174, 161, 120, 151, 14, 129, 68, 132, 111, 110, 130, 208, 53, 69, 24, 103, 192, 241, 183, 210, 89,
     229, 253, 232, 0, 44, 85, 76, 228, 131, 99, 190, 107, 96, 95, 58, 21, 121, 22, 244, 186, 73, 29, 159, 247, 114, 34,
     71, 144, 112, 211, 117, 135, 101, 19, 16, 88, 147, 6, 97, 38, 143, 52, 139, 126, 222, 240, 233, 248, 176, 194, 154,
     43, 246, 9, 20, 2, 156, 140, 212, 230, 213, 216, 166, 251, 3, 218, 87, 128, 179, 55, 136, 11, 104, 106, 202, 123,
     18, 66, 7, 63, 42, 50, 137, 158, 180, 134, 141, 28, 224, 188, 173, 204, 152, 157, 153, 254, 4, 242, 148, 182, 115,
     49, 25, 72, 181, 35, 5, 243, 177, 70, 195, 198, 217, 54, 15, 86, 12, 79, 255, 209, 191, 83, 219, 113, 26, 65, 206,
     199, 93, 138, 245, 207, 36, 1, 37, 119, 205, 231, 250, 124, 98, 8, 164, 185, 74, 165, 226, 167, 175, 189, 214, 90,
     30, 51, 17, 31, 61, 118, 32, 146, 39, 155, 160, 125, 235, 184, 33, 149, 249, 239, 215, 172, 203, 201, 133, 10, 223,
     100, 234, 127, 236, 187, 40, 200, 193, 221, 220, 116, 150, 67, 225, 94, 13, 170, 60, 92, 27, 227, 47, 41, 252, 57,
     46, 237, 122, 169, 178, 142, 75, 45, 171, 145, 78, 102, 168, 81, 196, 64, 238, 197, 84, 108, 162, 62, 77, 56, 163,
     48, 59, 91, 105, 23],
    [157, 174, 21, 204, 129, 66, 235, 120, 41, 247, 39, 65, 84, 203, 134, 25, 138, 104, 178, 115, 131, 146, 5, 212, 128,
     158, 6, 238, 107, 75, 68, 95, 135, 236, 3, 8, 108, 36, 226, 60, 225, 244, 37, 254, 202, 52, 222, 121, 103, 14, 106,
     230, 35, 199, 161, 219, 176, 126, 227, 63, 33, 49, 87, 197, 187, 43, 182, 78, 1, 209, 118, 168, 237, 164, 40, 53,
     32, 15, 251, 71, 224, 26, 64, 150, 223, 137, 205, 191, 112, 13, 96, 61, 142, 99, 145, 166, 165, 7, 175, 252, 136,
     44, 232, 34, 186, 89, 213, 110, 189, 200, 160, 181, 51, 154, 151, 92, 28, 97, 192, 31, 119, 90, 24, 188, 79, 155,
     240, 16, 228, 208, 172, 38, 177, 42, 67, 250, 62, 179, 109, 143, 211, 169, 23, 180, 133, 18, 253, 255, 170, 185,
     98, 125, 2, 50, 111, 246, 173, 81, 218, 245, 239, 184, 10, 17, 216, 29, 127, 46, 105, 12, 122, 249, 9, 198, 69,
     233, 101, 94, 114, 221, 206, 231, 159, 47, 195, 215, 76, 140, 171, 11, 4, 144, 147, 70, 210, 217, 220, 85, 141,
     124, 183, 20, 201, 86, 194, 83, 58, 242, 59, 45, 19, 72, 22, 100, 117, 190, 130, 123, 82, 243, 93, 48, 56, 148,
     156, 193, 241, 91, 30, 102, 113, 54, 73, 77, 0, 149, 116, 27, 163, 55, 207, 88, 152, 139, 248, 229, 57, 74, 162,
     214, 153, 132, 234, 196, 167, 80],
    [34, 137, 62, 178, 117, 102, 188, 245, 192, 104, 128, 79, 60, 146, 214, 161, 115, 82, 55, 185, 228, 142, 211, 17,
     25, 13, 155, 88, 21, 11, 219, 135, 193, 255, 220, 1, 54, 97, 139, 141, 213, 157, 232, 122, 194, 251, 26, 103, 191,
     85, 143, 38, 173, 225, 14, 226, 153, 120, 244, 74, 43, 205, 148, 29, 172, 105, 169, 241, 58, 68, 236, 174, 52, 16,
     158, 98, 182, 86, 249, 132, 50, 227, 218, 184, 242, 96, 196, 24, 216, 87, 224, 126, 67, 95, 154, 15, 247, 166, 238,
     208, 177, 149, 123, 7, 3, 125, 99, 33, 165, 151, 5, 109, 18, 100, 223, 37, 32, 116, 198, 106, 163, 71, 69, 246, 39,
     40, 30, 20, 167, 131, 195, 57, 134, 237, 197, 129, 72, 110, 189, 170, 171, 147, 111, 181, 94, 63, 121, 45, 59, 152,
     233, 252, 240, 207, 200, 44, 65, 75, 222, 6, 0, 8, 77, 108, 53, 9, 91, 243, 248, 140, 217, 202, 235, 118, 239, 209,
     31, 175, 119, 56, 4, 114, 176, 90, 23, 159, 112, 127, 230, 199, 101, 73, 27, 66, 133, 206, 150, 36, 221, 183, 78,
     61, 168, 93, 49, 124, 19, 41, 136, 92, 76, 144, 81, 162, 64, 190, 47, 231, 22, 253, 203, 187, 89, 254, 145, 215,
     234, 210, 28, 10, 113, 46, 130, 180, 51, 204, 48, 70, 250, 35, 201, 212, 179, 84, 2, 229, 186, 156, 80, 160, 164,
     42, 138, 107, 12, 83],
    [237, 46, 178, 75, 92, 102, 120, 165, 179, 106, 210, 5, 55, 24, 161, 6, 157, 19, 31, 169, 254, 222, 220, 216, 252,
     160, 211, 229, 58, 21, 150, 186, 168, 66, 223, 22, 145, 77, 152, 142, 176, 217, 118, 51, 96, 194, 43, 50, 146, 175,
     200, 90, 188, 110, 135, 208, 247, 218, 29, 182, 39, 10, 122, 32, 151, 255, 243, 117, 207, 35, 101, 112, 57, 94, 73,
     148, 95, 231, 3, 41, 9, 89, 109, 84, 23, 124, 249, 238, 104, 227, 114, 83, 197, 232, 62, 144, 213, 209, 49, 69, 1,
     248, 93, 193, 173, 76, 108, 37, 99, 149, 234, 181, 183, 65, 158, 33, 250, 121, 111, 156, 34, 244, 253, 86, 131, 20,
     137, 123, 42, 64, 128, 214, 105, 8, 206, 17, 147, 226, 204, 164, 154, 40, 119, 189, 174, 82, 103, 133, 125, 30,
     215, 185, 45, 224, 191, 225, 85, 59, 113, 47, 28, 25, 236, 97, 138, 71, 190, 177, 13, 153, 239, 98, 100, 196, 11,
     187, 134, 155, 67, 166, 72, 44, 61, 78, 56, 242, 221, 203, 126, 171, 54, 63, 245, 202, 251, 201, 107, 2, 163, 87,
     246, 116, 233, 80, 205, 4, 180, 52, 228, 26, 159, 172, 139, 230, 36, 7, 27, 219, 162, 68, 115, 14, 240, 18, 15, 38,
     12, 79, 127, 235, 70, 212, 141, 74, 81, 129, 88, 184, 167, 132, 140, 198, 48, 0, 60, 53, 192, 91, 16, 143, 136,
     170, 199, 241, 195, 130],
    [222, 153, 200, 123, 132, 252, 91, 58, 232, 146, 242, 82, 1, 223, 214, 229, 217, 184, 102, 63, 16, 166, 165, 90,
     209, 195, 28, 185, 50, 108, 24, 45, 136, 202, 72, 163, 84, 147, 171, 79, 150, 32, 89, 10, 237, 152, 65, 174, 145,
     80, 218, 160, 249, 5, 119, 207, 30, 113, 22, 120, 180, 109, 118, 233, 182, 85, 8, 59, 60, 215, 87, 255, 251, 81,
     71, 54, 188, 210, 14, 133, 34, 31, 48, 245, 76, 104, 191, 192, 122, 142, 205, 220, 15, 253, 126, 206, 211, 190,
     244, 29, 196, 193, 101, 197, 216, 225, 228, 183, 78, 75, 12, 224, 26, 21, 125, 39, 27, 40, 143, 129, 33, 204, 159,
     151, 47, 157, 111, 51, 173, 127, 128, 96, 167, 212, 162, 9, 124, 61, 43, 73, 56, 235, 240, 226, 88, 203, 248, 66,
     117, 219, 140, 115, 169, 53, 68, 17, 131, 35, 86, 161, 170, 135, 4, 106, 0, 18, 149, 155, 92, 121, 250, 116, 236,
     3, 100, 93, 238, 99, 77, 177, 64, 20, 37, 41, 36, 194, 52, 156, 154, 231, 134, 139, 241, 172, 42, 7, 69, 187, 239,
     105, 181, 55, 98, 221, 137, 94, 178, 247, 198, 246, 141, 67, 164, 70, 112, 49, 114, 103, 168, 74, 230, 2, 19, 62,
     199, 189, 213, 97, 176, 243, 175, 208, 6, 158, 144, 227, 254, 46, 186, 234, 95, 44, 38, 11, 83, 57, 13, 110, 148,
     138, 23, 179, 130, 107, 201, 25],
    [150, 34, 187, 241, 129, 106, 175, 204, 195, 159, 14, 153, 114, 214, 89, 166, 121, 181, 102, 186, 96, 1, 141, 123,
     38, 191, 40, 47, 36, 59, 209, 240, 53, 86, 171, 144, 157, 55, 224, 0, 176, 2, 92, 182, 61, 128, 236, 44, 56, 71,
     170, 117, 113, 112, 74, 63, 120, 189, 148, 185, 93, 172, 151, 57, 254, 152, 22, 177, 32, 245, 124, 72, 29, 110,
     167, 216, 24, 69, 233, 66, 201, 33, 211, 220, 42, 239, 142, 221, 252, 231, 115, 27, 8, 73, 99, 255, 238, 51, 116,
     75, 222, 165, 65, 52, 226, 250, 17, 145, 5, 179, 105, 147, 184, 198, 50, 139, 133, 80, 21, 81, 12, 132, 108, 225,
     127, 199, 183, 162, 173, 163, 88, 228, 230, 126, 109, 253, 78, 206, 130, 234, 217, 193, 158, 20, 91, 137, 16, 235,
     246, 160, 10, 232, 31, 18, 101, 156, 168, 247, 249, 174, 95, 188, 242, 196, 155, 23, 62, 79, 97, 227, 15, 19, 208,
     77, 210, 248, 131, 84, 203, 205, 28, 154, 169, 87, 104, 125, 212, 11, 54, 215, 244, 229, 143, 46, 4, 103, 200, 119,
     13, 48, 237, 207, 60, 82, 37, 111, 90, 223, 83, 149, 192, 140, 146, 135, 178, 219, 7, 94, 134, 6, 67, 136, 25, 3,
     39, 164, 197, 107, 180, 251, 41, 243, 85, 190, 122, 202, 138, 58, 43, 98, 64, 26, 118, 49, 9, 35, 30, 194, 68, 213,
     45, 76, 218, 70, 100, 161],
    [246, 216, 194, 78, 142, 182, 89, 234, 46, 28, 67, 105, 106, 63, 177, 103, 255, 5, 191, 66, 58, 3, 102, 248, 162,
     90, 204, 123, 200, 100, 175, 35, 240, 4, 227, 239, 87, 131, 208, 127, 108, 140, 56, 254, 116, 61, 149, 189, 233,
     50, 167, 212, 21, 62, 238, 174, 65, 29, 242, 139, 215, 235, 176, 79, 236, 250, 136, 70, 143, 247, 6, 164, 9, 7,
     141, 101, 148, 41, 193, 82, 244, 147, 124, 202, 223, 222, 221, 217, 99, 112, 192, 114, 205, 128, 44, 76, 119, 210,
     120, 59, 185, 150, 17, 81, 154, 172, 27, 144, 152, 18, 30, 184, 201, 252, 129, 171, 75, 231, 232, 36, 197, 135, 84,
     155, 181, 145, 230, 214, 26, 10, 72, 178, 98, 53, 179, 11, 183, 45, 20, 40, 94, 32, 241, 196, 251, 117, 97, 207,
     166, 219, 55, 213, 243, 225, 151, 110, 80, 195, 220, 16, 48, 133, 226, 95, 107, 43, 158, 111, 47, 228, 1, 170, 73,
     134, 39, 163, 249, 91, 157, 198, 88, 31, 186, 160, 22, 52, 42, 125, 15, 159, 237, 60, 209, 38, 77, 161, 85, 68,
     253, 34, 74, 187, 122, 13, 37, 69, 49, 19, 109, 156, 126, 51, 180, 14, 93, 211, 146, 168, 245, 115, 206, 121, 165,
     92, 2, 130, 199, 54, 132, 86, 96, 118, 0, 25, 113, 64, 229, 104, 83, 224, 173, 8, 153, 33, 137, 188, 23, 57, 12,
     24, 71, 138, 190, 169, 203, 218],
    [243, 125, 190, 99, 13, 102, 29, 238, 32, 220, 127, 27, 154, 124, 186, 118, 235, 159, 16, 35, 43, 189, 88, 169, 66,
     183, 95, 163, 85, 81, 6, 140, 204, 15, 108, 139, 17, 227, 187, 97, 74, 93, 58, 121, 245, 5, 96, 202, 195, 106, 230,
     28, 136, 210, 69, 170, 24, 10, 223, 247, 59, 113, 80, 67, 78, 18, 117, 162, 203, 7, 82, 11, 135, 33, 45, 171, 111,
     23, 200, 56, 198, 100, 25, 205, 150, 64, 105, 98, 188, 9, 213, 141, 4, 253, 26, 244, 172, 37, 231, 68, 199, 73, 57,
     109, 53, 164, 222, 176, 104, 132, 206, 39, 239, 168, 110, 126, 120, 174, 112, 236, 249, 219, 233, 86, 252, 173, 47,
     177, 254, 146, 90, 31, 38, 180, 221, 194, 212, 151, 147, 197, 79, 165, 160, 251, 178, 52, 153, 193, 91, 128, 40,
     131, 83, 166, 49, 87, 116, 215, 36, 0, 155, 2, 46, 75, 130, 175, 248, 208, 76, 51, 34, 148, 123, 152, 89, 214, 12,
     229, 217, 72, 218, 191, 158, 41, 226, 201, 225, 122, 246, 54, 240, 84, 255, 250, 1, 209, 137, 61, 161, 149, 241,
     107, 145, 62, 192, 20, 144, 22, 196, 234, 14, 134, 143, 94, 138, 55, 101, 237, 70, 21, 30, 184, 65, 129, 19, 216,
     103, 207, 77, 232, 60, 119, 156, 48, 115, 211, 182, 3, 133, 92, 181, 185, 224, 242, 179, 114, 42, 228, 8, 157, 167,
     71, 142, 44, 63, 50]
]

P = [8, 15, 22, 29, 36, 43, 50, 57,
     1, 16, 23, 30, 37, 44, 51, 58,
     2, 9, 24, 31, 38, 45, 52, 59,
     3, 10, 17, 32, 39, 46, 53, 60,
     4, 11, 18, 25, 40, 47, 54, 61,
     5, 12, 19, 26, 33, 48, 55, 62,
     6, 13, 20, 27, 34, 41, 56, 63,
     7, 14, 21, 28, 35, 42, 49, 64]

inv_P = [9, 17, 25, 33, 41, 49, 57, 1,
         18, 26, 34, 42, 50, 58, 2, 10,
         27, 35, 43, 51, 59, 3, 11, 19,
         36, 44, 52, 60, 4, 12, 20, 28,
         45, 53, 61, 5, 13, 21, 29, 37,
         54, 62, 6, 14, 22, 30, 38, 46,
         63, 7, 15, 23, 31, 39, 47, 55,
         8, 16, 24, 32, 40, 48, 56, 64]


def S_function(input, sbox):
    """
    Splits an int value into 8-bit blocks, transforms them using given s-boxes and converts back to an int value.

    :param input: int value to be transformed
    :param sbox: either s-boxes or inverted s-boxes
    :return: transformed int value
    """
    input_tab = int_to_blocks(input, 8, 8)
    for i in range(len(input_tab)):
        input_tab[i] = sbox[i][input_tab[i]]
    result = blocks_to_int(input_tab, 8)
    return result


def P_function(input, P_tab):
    """
    Converts an int value to a list of bits, permutates using given table and converts back to an int value.

    :param input: int value to be permutated
    :param P_tab: either table P or inverted table P
    :return: transformed int value
    """
    input_tab = int_to_list(input)
    output_tab = list(map(lambda x: input_tab[x - 1], P_tab))
    output = list_to_int(output_tab)
    return output


def E_function(input):
    """
    Converts 8-bit block to a 64-bit subkey.

    :param input: 8-bit int value
    :return: 64-bit int value
    """
    return pow(input, 10, pow(2, 64))


def key_schedule(key):
    """
    Creates 9 64-bit subkeys from a 72-bit key.

    :param key: int value of the key
    :return: list of subkeys
    """
    subkeys = []
    blocks = int_to_blocks(key, 9, 8)

    for block in blocks.reverse():
        subkeys.append(E_function(block))

    return subkeys


def encrypt(plaintext, key):
    """
    Encrypts given plaintext using designed block cipher and a given key.

    :param plaintext: int value to be encrypted
    :param key: int value of the key to be used
    :return: int value representing ciphertext
    """
    result = plaintext
    if result.bit_length() > 64:
        raise ValueError('plaintext too large')

    for i in range(7):
        result ^= key_schedule(key)[i]
        result = S_function(result, s_box)
        result = P_function(result, P)

    result ^= key_schedule(key)[7]
    result = S_function(result, s_box)
    result ^= key_schedule(key)[8]

    return result


def decrypt(ciphertext, key):
    """
    Decrpyts given ciphertext using designed block cipher and a given key.

    :param ciphertext: int value to be decrypted
    :param key: int value of the key to be used
    :return: int value representing plaintext
    """
    result = ciphertext
    if result.bit_length() > 64:
        raise ValueError('ciphertext too large')
    result ^= key_schedule(key)[8]
    result = S_function(result, inv_s_box)
    result ^= key_schedule(key)[7]

    for i in range(7):
        result = P_function(result, inv_P)
        result = S_function(result, inv_s_box)
        result ^= key_schedule(key)[6 - i]

    return result